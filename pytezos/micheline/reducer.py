import functools
from decimal import Decimal
from os.path import join

import pytezos.encoding as encoding
from pytezos.micheline.schema import resolve_type_path
from pytezos.micheline.formatter import micheline_to_michelson
from pytezos.micheline.types import assert_big_map_val, assert_comparable, assert_type, parse_type, parse_prim_expr,\
    get_prim_args, get_string, get_int, get_bytes, dispatch_prim_map, dispatch_core_map, MichelsonTypeCheckError, \
    Unit, Pair, parse_comb

parsers = {}


def primitive(prim, args_len=0):
    def register_primitive(func):
        parsers[prim] = (args_len, func)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return register_primitive


def val_selector(val_expr, type_expr, val, type_path):
    prim = type_expr['prim']
    if prim == 'pair':
        return tuple(val)
    elif prim == 'option':
        return tuple(val) if val is not None else None
    elif prim == 'or':
        return val[0]
    elif prim == 'set':
        return set(val)
    elif prim == 'map':
        return dict(val)
    elif prim == 'big_map' and isinstance(val_expr, list):
        return dict(val)
    else:
        return val


def parse_expression(val_expr, type_expr, selector=val_selector, type_path='0'):
    """ Run an extensible parser for Micheline expressions.
    This function will just do the type checking for you,
    if you want to build a response you'd need to define a selector.

    :param val_expr: value expression (Micheline)
    :param type_expr: corresponding type expression (Micheline)
    :param selector: function selector(val_expr, type_expr, val, type_path). \
    Default selector (val_selector) converts Micheline to Python objects
    :param type_path: starting binary path (default is '0')
    """
    prim, args, _ = parse_type(type_expr)
    if prim not in parsers:
        raise MichelsonTypeCheckError.init('unknown primitive', prim)

    args_len, func = parsers[prim]
    if 0 < args_len != len(args):
        raise MichelsonTypeCheckError.init(f'expected {args_len} arg(s), got {len(args)}', prim)

    try:
        res = func(val_expr, type_expr, selector, type_path)
    except AssertionError as e:
        raise MichelsonTypeCheckError.init(str(e), prim)
    except MichelsonTypeCheckError as e:
        raise MichelsonTypeCheckError.wrap(e, prim)
    else:
        return res


@primitive('string')
def parse_string(val_expr, type_expr, selector, type_path):
    return selector(val_expr, type_expr, get_string(val_expr), type_path)


@primitive('int')
def parse_int(val_expr, type_expr, selector, type_path):
    return selector(val_expr, type_expr, get_int(val_expr), type_path)


@primitive('bytes')
def parse_bytes(val_expr, type_expr, selector, type_path):
    return selector(val_expr, type_expr, get_bytes(val_expr), type_path)


@primitive('nat')
def parse_nat(val_expr, type_expr, selector, type_path):
    val = get_int(val_expr)
    assert val >= 0, f'nat cannot be negative ({val})'
    return selector(val_expr, type_expr, val, type_path)


@primitive('bool')
def parse_bool(val_expr, type_expr, selector, type_path):
    val = dispatch_prim_map(val_expr, {
        ('False', 0): False,
        ('True', 0): True
    })
    return selector(val_expr, type_expr, val, type_path)


@primitive('unit')
def parse_unit(val_expr, type_expr, selector, type_path):
    _ = get_prim_args(val_expr, prim='Unit', args_len=0)
    return selector(val_expr, type_expr, Unit(), type_path)


@primitive('list', args_len=1)
def parse_list(val_expr, type_expr, selector, type_path):
    assert_type(val_expr, list)
    val = [parse_expression(item, type_expr['args'][0], selector, join(type_path, 'l')) for item in val_expr]
    return selector(val_expr, type_expr, val, type_path)


@primitive('pair', args_len=-1)
def parse_pair(val_expr, type_expr, selector, type_path):
    _, type_args, _ = parse_prim_expr(type_expr)
    assert len(type_args) >= 2, f'pair type must have at least 2 args, got {len(type_args)}'

    if isinstance(val_expr, dict):
        prim, val_args, _ = parse_prim_expr(val_expr)
        assert prim == 'Pair', f'expected Pair, got {prim}'
    elif isinstance(val_expr, list):
        val_args = val_expr
    else:
        assert False, f'unexpected pair value: {val_expr}'
    assert len(val_args) >= 2, f'pair value must have at least 2 args, got {len(val_args)}'

    # TODO: свести к одному виду?

    if len(type_args) == len(val_args):
        val = [parse_expression(val_args[i], type_args[i], selector, join(type_path, str(i)))
               for i in range(len(type_args))]

    elif len(type_args) < len(val_args):
        comb_type = parse_comb(type_expr, len(val_expr), type_path)
        val = [parse_expression(val_args[i], comb_type[i][0], selector, comb_type[i][1])
               for i in range(len(comb_type))]
    else:
        assert isinstance(val_expr, dict), f'Pair is expected'
        comb_val = parse_comb(val_expr, len(type_expr), type_path)
        val = [parse_expression(comb_val[i][0], type_args[i], selector, comb_val[i][1])
               for i in range(len(comb_val))]

    return selector(val_expr, type_expr, val, type_path)


@primitive('option', args_len=1)
def parse_option(val_expr, type_expr, selector, type_path):
    val = dispatch_prim_map(val_expr, {
        ('None', 0): None,
        ('Some', 1): lambda x: [parse_expression(x[0], type_expr['args'][0], selector, join(type_path, 'o'))]
    })
    return selector(val_expr, type_expr, val, type_path)


@primitive('or', args_len=2)
def parse_or(val_expr, type_expr, selector, type_path):
    val = dispatch_prim_map(val_expr, {
        ('Left', 1): lambda x: [parse_expression(x[0], type_expr['args'][0], selector, join(type_path, '0'))],
        ('Right', 1): lambda x: [parse_expression(x[0], type_expr['args'][1], selector, join(type_path, '1'))]
    })
    return selector(val_expr, type_expr, val, type_path)


@primitive('set', args_len=1)
def parse_set(val_expr, type_expr, selector, type_path):
    assert_type(val_expr, list)
    assert_comparable(type_expr['args'][0])
    val = [parse_expression(item, type_expr['args'][0], selector, join(type_path, 's')) for item in val_expr]
    return selector(val_expr, type_expr, val, type_path)


def parse_elt(val_expr, type_expr, selector, type_path):
    elt_args = get_prim_args(val_expr, prim='Elt', args_len=2)
    return [parse_expression(elt_args[i], type_expr['args'][i], selector, join(type_path, p))
            for i, p in enumerate('kv')]


@primitive('map', args_len=2)
def parse_map(val_expr, type_expr, selector, type_path):
    assert_type(val_expr, list)
    assert_comparable(type_expr['args'][0])
    val = [parse_elt(item, type_expr, selector, type_path) for item in val_expr]
    return selector(val_expr, type_expr, val, type_path)


@primitive('big_map', args_len=2)
def parse_big_map(val_expr, type_expr, selector, type_path):
    assert_comparable(type_expr['args'][0])
    assert_big_map_val(type_expr['args'][1])
    if isinstance(val_expr, list):
        return parse_map(val_expr, type_expr, selector, type_path)
    else:
        val = get_int(val_expr)
        return selector(val_expr, type_expr, val, type_path)


@primitive('timestamp')
def parse_timestamp(val_expr, type_expr, selector, type_path):
    val = dispatch_core_map(val_expr, {'int': int, 'string': encoding.forge_timestamp})
    return selector(val_expr, type_expr, val, type_path)


@primitive('mutez')
def parse_mutez(val_expr, type_expr, selector, type_path):
    return parse_nat(val_expr, type_expr, selector, type_path)


@primitive('address')
def parse_address(val_expr, type_expr, selector, type_path):
    val = dispatch_core_map(val_expr, {
        'bytes': lambda x: encoding.parse_contract(bytes.fromhex(x)),
        'string': lambda x: x
    })
    return selector(val_expr, type_expr, val, type_path)


@primitive('contract', args_len=1)
def parse_contract(val_expr, type_expr, selector, type_path):
    val = dispatch_core_map(val_expr, {
        'bytes': lambda x: encoding.parse_contract(bytes.fromhex(x)),
        'string': lambda x: x
    })
    return selector(val_expr, type_expr, val, type_path)


@primitive('operation')
def parse_operation(val_expr, type_expr, selector, type_path):
    return selector(val_expr, type_expr, get_string(val_expr), type_path)


@primitive('key')
def parse_key(val_expr, type_expr, selector, type_path):
    val = dispatch_core_map(val_expr, {
        'bytes': lambda x: encoding.parse_public_key(bytes.fromhex(x)),
        'string': lambda x: x
    })
    return selector(val_expr, type_expr, val, type_path)


@primitive('key_hash')
def parse_key_hash(val_expr, type_expr, selector, type_path):
    return parse_address(val_expr, type_expr, selector, type_path)


@primitive('signature')
def parse_signature(val_expr, type_expr, selector, type_path):
    val = dispatch_core_map(val_expr, {
        'bytes': lambda x: encoding.parse_signature(bytes.fromhex(x)),
        'string': lambda x: x
    })
    return selector(val_expr, type_expr, val, type_path)


@primitive('chain_id')
def parse_chain_id(val_expr, type_expr, selector, type_path):
    val = dispatch_core_map(val_expr, {
        'bytes': lambda x: encoding.parse_chain_id(bytes.fromhex(x)),
        'string': lambda x: x
    })
    return selector(val_expr, type_expr, val, type_path)


@primitive('lambda', args_len=2)
def parse_lambda(val_expr, type_expr, selector, type_path):
    assert_type(val_expr, list)
    return selector(val_expr, type_expr, val_expr, type_path)


def micheline_to_pyobject(val_expr, type_expr, schema: dict, root_path='/'):
    """

    :param val_expr:
    :param type_expr:
    :param schema:
    :param root_path:
    :return:
    """
    def flatten_pair(args) -> Pair:
        res = list()
        for arg in args:
            if isinstance(arg, Pair):
                res.extend(flatten_pair(arg))
            else:
                res.append(arg)
        return Pair(res)

    def selector(val_node, type_node, val, type_path):
        prim = schema[type_path]['prim']
        names = schema[type_path].get('names', [])
        if prim == 'map':
            return dict(val)
        elif prim == 'big_map':
            return dict(val) if isinstance(val_node, list) else val
        elif prim == 'option':
            return val[0] if val is not None else None
        elif prim == 'pair':
            return flatten_pair(val)
        elif prim == 'tuple':
            if names:
                return dict(zip(names, flatten_pair(val)))
            else:
                return tuple(flatten_pair(val))
        elif prim in ['or', 'union', 'enum']:
            arg_path = join(type_path, {'Left': '0', 'Right': '1'}[val_node['prim']])
            if schema[arg_path]['prim'] == 'option':
                arg_path = join(arg_path, 'o')
            is_leaf = schema[arg_path]['prim'] != 'or'
            res = {schema[arg_path].get('name'): val[0]} if is_leaf else val[0]
            return next(iter(res)) if prim == 'enum' else res
        elif prim == 'unit':
            return Unit
        elif prim == 'lambda':
            return micheline_to_michelson(val)
        elif prim == 'timestamp':
            return dispatch_core_map(val_node, {'string': str, 'int': int})
        elif prim == 'bytes':
            return val.hex()
        elif prim == 'mutez':
            return Decimal(val) / 10 ** 6
        else:
            return val

    return parse_expression(val_expr, resolve_type_path(type_expr, schema, root_path), selector, root_path)
