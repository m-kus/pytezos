from typing import Tuple
from os.path import join

from pytezos.micheline.formatter import micheline_to_michelson


class Unit(object):

    def __repr__(self):
        return 'Unit'

    def __eq__(self, other):
        return isinstance(other, Unit)


class Pair(tuple):
    pass


class MichelsonRuntimeError(ValueError):

    def __init__(self, message, trace, data):
        super(MichelsonRuntimeError, self).__init__(f'{message}: {" -> ".join(trace)}')
        self.message = message
        self.trace = trace
        self.data = data

    @classmethod
    def init(cls, message, prim, data=None):
        return cls(message, trace=[prim], data=data)

    @classmethod
    def wrap(cls, error: 'MichelsonRuntimeError', prim):
        return cls(error.message, trace=[prim] + error.trace, data=error.data)


class MichelsonTypeCheckError(MichelsonRuntimeError):
    pass


def expr_equal(a, b):
    if type(a) != type(b):
        return False
    elif isinstance(a, dict):
        if a.get('prim'):
            if a['prim'] != b['prim']:
                return False
            elif not expr_equal(a.get('args', []), b.get('args', [])):
                return False
            else:
                a_type_annots = get_type_annots(a)
                b_type_anonts = get_type_annots(b)
                if a_type_annots and b_type_anonts:
                    return a_type_annots == b_type_anonts
                else:
                    return True
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


def get_type_annots(type_expr: dict) -> list:
    return list(filter(lambda x: x.startswith(':'), type_expr.get('annots', [])))


def assert_type(value, exp_type):
    assert isinstance(value, exp_type), f'expected {exp_type.__name__}, got {type(value).__name__}'


def remove_field_annots(type_expr):
    return dict(
        prim=type_expr['prim'],
        args=type_expr.get('args', []),
        annots=list(filter(lambda x: not x.startswith('%'),
                           type_expr.get('annots', [])))
    )


def extend_annots(type_expr, annots):
    assert isinstance(annots, list), f'expected list, got {annots}'
    return dict(prim=type_expr['prim'],
                args=type_expr.get('args', []),
                annots=type_expr.get('annots', []) + annots)


def assert_single_var_annot(annots):
    if isinstance(annots, list):
        assert len(list(filter(lambda x: x.startswith('@'), annots))) <= 1, \
            f'multiple variable annotations are not allowed'


def assert_single_type_annot(annots):
    if isinstance(annots, list):
        assert len(list(filter(lambda x: x.startswith(':'), annots))) <= 1, \
            f'multiple type annotations are not allowed'


def assert_no_field_annots(annots):
    if isinstance(annots, list):
        assert all(map(lambda x: not x.startswith('%'), annots)), \
            f'field annotations are not allowed here'


def parse_prim_expr(expr) -> tuple:
    assert isinstance(expr, dict), f'expected dict, got {type(expr).__name__}'
    assert 'prim' in expr, f'prim field is absent'
    return expr['prim'], expr.get('args', []), expr.get('annots', [])


def get_prim_args(val_expr, prim, args_len: int):
    p, args, _ = parse_prim_expr(val_expr)
    assert p == prim, f'expected {prim}, got {p}'
    assert len(args) == args_len, f'expected {args_len} args, got {len(args)}'
    return args


def parse_type(type_expr) -> Tuple[str, list, list]:
    prim, args, annots = parse_prim_expr(type_expr)
    assert_single_type_annot(annots)
    if prim in ['list', 'set', 'map', 'big_map', 'option', 'contract', 'lambda']:
        for arg_expr in args:
            assert isinstance(arg_expr, dict), f'expected dict, got {type(arg_expr).__name__}'
            assert_no_field_annots(arg_expr.get('annots', []))

    return prim, args, annots


def is_comparable(type_expr):
    prim, args, _ = parse_type(type_expr)
    comparable_types = {
        'string', 'int', 'bytes', 'nat', 'bool',
        'address', 'key_hash', 'mutez', 'timestamp'
    }
    if prim in comparable_types:
        return True
    elif prim == 'pair':
        left, _, _ = parse_type(args[0])
        return left != 'pair' and all(map(is_comparable, args))
    else:
        return False


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


def is_big_map_val(type_expr):
    prim, args, _ = parse_type(type_expr)
    if prim in ['big_map', 'operation']:
        return False
    return all(map(is_big_map_val, args))


def assert_big_map_val(type_expr):
    assert is_big_map_val(type_expr), f'cannot be a big map value: {micheline_to_michelson(type_expr)}'


def assert_pushable(type_expr):
    assert is_pushable(type_expr), f'type is not pushable: {micheline_to_michelson(type_expr)}'


def assert_comparable(type_expr):
    assert is_comparable(type_expr), f'type is not comparable: {micheline_to_michelson(type_expr)}'


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


def get_name(type_expr, prefixes, default=None):
    annots = type_expr.get('annots', [])
    assert isinstance(annots, list), f'expected list, got {annots}'
    for prefix in prefixes:
        name = next(filter(lambda x: x.startswith(prefix), annots), None)
        if name is not None:
            return name[1:]
    return default


def parse_core_expr(expr) -> tuple:
    assert isinstance(expr, dict), f'expected dict, got {type(expr)}'
    core_type, value = next((k, v) for k, v in expr.items() if k[0] != '_' and k != 'annots')
    return core_type, expr[core_type]


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


def restore_entry_expr(val_expr, type_expr, field_annot):
    _, entry_path = get_entry_expr(type_expr, field_annot)
    for idx in reversed(entry_path):
        val_expr = {'prim': 'Left' if idx == '0' else 'Right',
                    'args': [val_expr]}
    return val_expr


def dispatch_prim_map(val_expr, mapping: dict):
    p, args = parse_prim_expr(val_expr)
    expected = ' or '.join(map(lambda x: f'{x[0]} ({x[1]} args)', mapping.items()))
    assert (p, len(args)) in mapping, f'expected {expected}, got {p} ({len(args)} args)'
    res = mapping[(p, len(args))]
    if callable(res):
        return res(args)
    else:
        return res


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


def parse_comb(expr, size, type_path='/') -> list:
    res = []

    def is_pair(ex):
        return isinstance(ex, dict) \
               and ex.get('prim', '').lower() == 'pair' \
               and len(ex.get('args', [])) == 2

    assert is_pair(expr), f'expected 2-pair, got {expr}'
    left, right = expr['args']
    assert not is_pair(left), f'left argument must not be a pair ({type_path})'
    res.append((left, join(type_path, '0')))

    if size == 2:
        assert not is_pair(right), f'terminal leaf must not be a pair ({type_path})'
        res.append((right, join(type_path, '1')))
    else:
        res.extend(parse_comb(right, size - 1, join(type_path, '1')))

    return res

