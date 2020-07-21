import functools
from typing import Tuple, Callable

from pytezos.michelson.formatter import micheline_to_michelson
import pytezos.encoding as encoding

parsers = {}


def primitive(prim, args_len=0):
    def register_primitive(func):
        parsers[prim] = (args_len, func)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return register_primitive


class Unit(object):

    def __repr__(self):
        return 'Unit'

    def __eq__(self, other):
        return isinstance(other, Unit)


class MichelsonRuntimeError(ValueError):

    def __init__(self, message, trace):
        super(MichelsonRuntimeError, self).__init__(f'{message}: {" -> ".join(trace)}')
        self.message = message
        self.trace = trace

    @classmethod
    def init(cls, message, prim):
        return cls(message, trace=[prim])

    @classmethod
    def wrap(cls, error: 'MichelsonRuntimeError', prim):
        return cls(error.message, trace=[prim] + error.trace)


class MichelsonTypeCheckError(MichelsonRuntimeError):
    pass


def assert_no_field_annots(annots):
    if isinstance(annots, list):
        assert all(map(lambda x: not x.startswith('%'), annots)), \
            f'field annotations are not allowed here'


def assert_single_type_annot(annots):
    if isinstance(annots, list):
        assert len(list(filter(lambda x: x.startswith(':'), annots))) <= 1, \
            f'multiple type annotations are not allowed'


def assert_single_var_annot(annots):
    if isinstance(annots, list):
        assert len(list(filter(lambda x: x.startswith('@'), annots))) <= 1, \
            f'multiple variable annotations are not allowed'


def assert_type(value, exp_type):
    assert isinstance(value, exp_type), f'expected {exp_type.__name__}, got {type(value).__name__}'


def parse_prim_expr(expr) -> tuple:
    assert isinstance(expr, dict), f'expected dict, got {type(expr).__name__}'
    assert 'prim' in expr, f'prim field is absent'
    return expr['prim'], expr.get('args', [])


def get_prim_args(val_expr, prim, args_len: int):
    p, args = parse_prim_expr(val_expr)
    assert p == prim, f'expected {prim}, got {p}'
    assert len(args) == args_len, f'expected {args_len} args, got {len(args)}'
    return args


def dispatch_prim_map(val_expr, mapping: dict):
    p, args = parse_prim_expr(val_expr)
    expected = ' or '.join(map(lambda x: f'{x[0]} ({x[1]} args)', mapping.items()))
    assert (p, len(args)) in mapping, f'expected {expected}, got {p} ({len(args)} args)'
    res = mapping[(p, len(args))]
    if callable(res):
        return res(args)
    else:
        return res


def parse_core_expr(expr) -> tuple:
    assert isinstance(expr, dict), f'expected dict, got {type(expr)}'
    core_type, value = next((k, v) for k, v in expr.items() if k[0] != '_' and k != 'annots')
    return core_type, expr[core_type]


def dispatch_core_map(val_expr, mapping: dict):
    act_type, val = parse_core_expr(val_expr)
    expected = ' or '.join(map(lambda x: f'`{x}`', mapping))
    assert act_type in mapping, f'expected {expected}, got {act_type}'
    res = mapping[act_type]
    if callable(res):
        try:
            return res(val)
        except ValueError as e:
            raise MichelsonTypeCheckError.init(str(e), act_type)
    else:
        return res


def get_core_val(val_expr, core_type):
    act_type, value = parse_core_expr(val_expr)
    assert core_type == act_type, f'expected {core_type}, got {act_type}'
    return value


def get_string(val_expr):
    return get_core_val(val_expr, core_type='string')


def get_int(val_expr):
    return int(get_core_val(val_expr, core_type='int'))


def get_bool(val_expr):
    return dispatch_prim_map(val_expr, {('True', 0): True, ('False', 0): False})


def get_bytes(val_expr):
    return bytes.fromhex(get_core_val(val_expr, core_type='bytes'))


def get_entry_expr(type_expr, field_annot):
    def _get(node, path):
        assert_type(node, dict)
        if field_annot in node.get('annots', []):
            return node, path

        for i, arg in enumerate(node.get('args', [])):
            res = _get(arg, path + str(i))
            if res:
                return res

    entry = _get(type_expr, '')
    if not entry and field_annot == '%default':
        entry_type, entry_path = type_expr, ''
    else:
        entry_type, entry_path = entry

    assert entry_type, f'entrypoint `{field_annot[1:]}` was not found'
    return entry_type, entry_path


def restore_entry_expr(val_expr, type_expr, field_annot):
    _, entry_path = get_entry_expr(type_expr, field_annot)
    for idx in reversed(entry_path):
        val_expr = {'prim': 'Left' if idx == '0' else 'Right',
                    'args': [val_expr]}
    return val_expr


def expr_equal(a, b):
    if type(a) != type(b):
        return False
    elif isinstance(a, dict):
        if a.get('prim'):
            if a['prim'] != b['prim']:
                return False
            else:
                return expr_equal(a.get('args', []), b.get('args', []))
        else:
            return a == b
    elif isinstance(a, list):
        if len(a) != len(b):
            return False
        else:
            return all(map(lambda i: expr_equal(a[i], b[i]), range(len(a))))
    else:
        assert False, (a, b)


def assert_expr_equal(expected, actual):
    assert expr_equal(expected, actual), \
        f'expected {micheline_to_michelson(expected)}, got {micheline_to_michelson(actual)}'


def is_comparable(type_expr):
    prim, args, _ = parse_type(type_expr)
    comparable_types = {
        'string', 'int', 'bytes', 'nat', 'bool',
        'address', 'key_hash', 'mutez', 'timestamp'
    }
    if prim in comparable_types:
        return True
    elif prim == 'pair':
        left, _ = parse_prim_expr(args[0])
        return left != 'pair' and all(map(is_comparable, args))
    else:
        return False


def assert_comparable(type_expr):
    assert is_comparable(type_expr), f'type is not comparable: {micheline_to_michelson(type_expr)}'


def is_pushable(type_expr):
    prim, args, _ = parse_type(type_expr)
    if prim in ['big_map', 'contract', 'operation']:
        return False
    elif prim == 'lambda':
        return True
    elif args:
        return all(map(is_pushable, args))
    else:
        return True


def assert_pushable(type_expr):
    assert is_pushable(type_expr), f'type is not pushable: {micheline_to_michelson(type_expr)}'


def is_big_map_val(type_expr):
    prim, args, _ = parse_type(type_expr)
    if prim in ['big_map', 'operation']:
        return False
    return all(map(is_big_map_val, args))


def assert_big_map_val(type_expr):
    assert is_big_map_val(type_expr), f'cannot be a big map value: {micheline_to_michelson(type_expr)}'


def parse_type(type_expr) -> Tuple[str, list, Callable]:
    prim, args = parse_prim_expr(type_expr)
    if prim not in parsers:
        raise MichelsonRuntimeError.init('unknown primitive', prim)

    args_len, func = parsers[prim]
    if len(args) != args_len:
        raise MichelsonRuntimeError.init(f'expected {args_len} arg(s), got {len(args)}', prim)

    assert_single_type_annot(type_expr.get('annots'))
    if prim in ['list', 'set', 'map', 'big_map', 'option', 'contract', 'lambda']:
        for arg in args:
            assert_no_field_annots(arg.get('annots'))

    return prim, args, func


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
    prim, _, func = parse_type(type_expr)
    try:
        res = func(val_expr, type_expr, selector, type_path)
    except AssertionError as e:
        raise MichelsonTypeCheckError.init(str(e), prim)
    except MichelsonRuntimeError as e:
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
    val = [parse_expression(item, type_expr['args'][0], selector, type_path + '0') for item in val_expr]
    return selector(val_expr, type_expr, val, type_path)


@primitive('pair', args_len=2)
def parse_pair(val_expr, type_expr, selector, type_path):
    args = get_prim_args(val_expr, prim='Pair', args_len=2)
    val = [parse_expression(args[i], type_expr['args'][i], selector, type_path + str(i)) for i in [0, 1]]
    return selector(val_expr, type_expr, val, type_path)


@primitive('option', args_len=1)
def parse_option(val_expr, type_expr, selector, type_path):
    val = dispatch_prim_map(val_expr, {
        ('None', 0): None,
        ('Some', 1): lambda x: [parse_expression(x[0], type_expr['args'][0], selector, type_path + '0')]
    })
    return selector(val_expr, type_expr, val, type_path)


@primitive('or', args_len=2)
def parse_or(val_expr, type_expr, selector, type_path):
    val = dispatch_prim_map(val_expr, {
        ('Left', 1): lambda x: [parse_expression(x[0], type_expr['args'][0], selector, type_path + '0')],
        ('Right', 1): lambda x: [parse_expression(x[0], type_expr['args'][1], selector, type_path + '1')]
    })
    return selector(val_expr, type_expr, val, type_path)


@primitive('set', args_len=1)
def parse_set(val_expr, type_expr, selector, type_path):
    assert_type(val_expr, list)
    assert_comparable(type_expr['args'][0])
    val = [parse_expression(item, type_expr['args'][0], selector, type_path + '0') for item in val_expr]
    return selector(val_expr, type_expr, val, type_path)


def parse_elt(val_expr, type_expr, selector, type_path):
    elt_args = get_prim_args(val_expr, prim='Elt', args_len=2)
    return [parse_expression(elt_args[i], type_expr['args'][i], selector, type_path + str(i)) for i in [0, 1]]


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
        'bytes': lambda x: encoding.parse_address(bytes.fromhex(x)),
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
