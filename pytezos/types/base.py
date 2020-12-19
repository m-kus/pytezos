from typing import Tuple, Dict, Callable, List
from pprint import pformat
from copy import deepcopy


class undefined:
    pass


class unit(object):

    def __repr__(self):
        return 'Unit'

    def __eq__(self, other):
        return isinstance(other, unit)


def parse_micheline_type(type_expr) -> Tuple[str, list, str, str]:
    assert isinstance(type_expr, dict), f'expected dict, got {type(type_expr).__name__} (type_expr)'
    prim = type_expr.get('prim')
    assert prim is not None, f'prim field is absent'
    args = type_expr.get('args', [])
    assert isinstance(args, list), f'expected list, got {type(args).__name__} (args)'
    annots = type_expr.get('annots', [])
    assert isinstance(args, list), f'expected list of, got {type(args).__name__} (annots)'

    def parse_name(prefix) -> str:
        sub_annots = [x[1:] for x in annots if x.startswith(prefix)]
        assert len(sub_annots) <= 1, f'multiple "{prefix}" annotations are not allowed: {sub_annots}'
        return sub_annots[0] if sub_annots else None

    return prim, args, parse_name('%'), parse_name(':')


def parse_micheline_value(val_expr, handlers: Dict[Tuple[str, int], Callable]):
    assert isinstance(val_expr, dict), f'expected dict, got {type(val_expr).__name__}'
    prim, args = val_expr.get('prim'), val_expr.get('args', [])
    expected = ' or '.join(map(lambda x: f'{x[0]} ({x[1]} args)', handlers.items()))
    assert (prim, len(args)) in handlers, f'expected {expected}, got {prim} ({len(args)} args)'
    handler = handlers[(prim, len(args))]
    return handler(args)


def parse_micheline_literal(val_expr, handlers: Dict[str, Callable]):
    assert isinstance(val_expr, dict), f'expected dict, got {type(val_expr).__name__}'
    core_type, value = next((k, v) for k, v in val_expr.items() if k[0] != '_' and k != 'annots')
    expected = ' or '.join(map(lambda x: f'`{x}`', handlers))
    assert core_type in handlers, f'expected one of {expected}, got {core_type}'
    handler = handlers[core_type]
    return handler(value)


class MichelsonType:
    prim = None
    type_classes = {}

    def __init__(self, value, field_name=None, type_name=None, variable_name=None, args=None):
        self.value = value
        self.field_name = field_name
        self.type_name = type_name
        self.variable_name = variable_name
        self.args = args or []  # type: List[MichelsonType]

    @classmethod
    def __init_subclass__(cls, prim='', args_len=0, **kwargs):
        super().__init_subclass__(**kwargs)
        if prim:
            cls.type_classes[prim] = (cls, args_len)
            cls.prim = prim

    def spawn(self, value):
        return type(self)(value=value,
                          field_name=self.field_name,
                          type_name=self.type_name,
                          args=deepcopy(self.args))

    @staticmethod
    def from_micheline_type(type_expr):
        prim, type_args, field_name, type_name = parse_micheline_type(type_expr)
        assert prim in MichelsonType.type_classes, f'unknown primitive {prim}'
        cls, args_len = MichelsonType.type_classes[prim]
        assert args_len is None or len(type_args) == args_len, f'{prim}: expected {args_len} args, got {len(type_args)}'
        args = list(map(MichelsonType.from_micheline_type, type_args))   # type: List[MichelsonType]

        if prim in ['list', 'set', 'map', 'big_map', 'option', 'contract', 'lambda']:
            for arg in args:
                assert arg.field_name is None, f'{prim} argument type cannot be annotated: %{arg.field_name}'
        if prim in ['set', 'map', 'big_map']:
            assert args[0].is_comparable(), f'{prim} key type has to be comparable (cannot be {args[0].prim})'
        if prim == 'big_map':
            assert args[0].is_big_map_friendly(), f'impossible big_map value type'

        return cls(value=undefined(), field_name=field_name, type_name=type_name, args=args)

    def get_micheline_type(self) -> dict:
        annots = []
        if self.field_name is not None:
            annots.append(f'%{self.field_name}')
        if self.type_name is not None:
            annots.append(f':{self.type_name}')
        type_args = [arg.get_micheline_type() for arg in self.args]
        expr = dict(prim=self.prim, annots=annots, args=type_args)
        return {k: v for k, v in expr.items() if v}

    def parse_micheline_value(self, val_expr):
        raise NotImplementedError

    def to_micheline_value(self, mode):
        raise NotImplementedError

    def parse_python_object(self, py_obj):
        raise NotImplementedError

    def to_python_object(self):
        raise NotImplementedError

    def __int__(self):
        assert isinstance(self.value, int), f'expected int, got {type(self.value).__name__}'
        return self.value

    def __str__(self):
        assert isinstance(self.value, str), f'expected string, got {type(self.value).__name__}'
        return self.value

    def __bytes__(self):
        assert isinstance(self.value, bytes), f'expected bytes, got {type(self.value).__name__}'
        return self.value

    def __bool__(self):
        assert isinstance(self.value, bool), f'expected bool, got {type(self.value).__name__}'
        return self.value

    def __repr__(self):
        return pformat(self.value, indent=2, compact=True)

    def assert_value_defined(self):
        raise NotImplementedError

    def assert_equal_types(self, other):
        assert isinstance(other, type(self)), \
            f'cannot compare different types: {type(self).__name__} vs {type(other).__name__}'
        assert isinstance(other.value, type(self.value)), \
            f'cannot compare different types: {type(self.value).__name__} vs {type(other.value).__name__}'

    def __cmp__(self, other):
        self.assert_value_defined()
        self.assert_equal_types(other)
        assert self.is_comparable(), f'not a comparable type'
        assert type(self.value) in [str, int, bytes, bool],  \
            f'can only compare simple types, not {type(self.value).__name__}'
        return self.value.__cmp__(other.value)

    def is_defined(self):
        try:
            self.assert_value_defined()
        except AssertionError:
            return False
        else:
            return True

    def is_comparable(self):
        if self.prim in ['bls12_381_fr', 'bls12_381_g1', 'bls12_381_g2', 'sapling_state', 'sapling_transaction',
                         'big_map', 'contract', 'lambda', 'list', 'map', 'set', 'operation', 'ticket']:
            return False
        return all(map(lambda x: x.is_comparable(), self.args))

    def is_passable(self):
        if self.prim in ['operation']:
            return False
        return all(map(lambda x: x.is_passable(), self.args))

    def is_storable(self):
        if self.prim in ['contract', 'operation']:
            return False
        return all(map(lambda x: x.is_storable(), self.args))

    def is_pushable(self):
        if self.prim in ['big_map', 'contract', 'operation', 'sapling_state', 'ticket']:
            return False
        return all(map(lambda x: x.is_pushable(), self.args))

    def is_packable(self):
        if self.prim in ['big_map', 'operation', 'sapling_state', 'ticket']:
            return False
        return all(map(lambda x: x.is_packable(), self.args))

    def is_duplicable(self):
        if self.prim in ['ticket']:
            return False
        return all(map(lambda x: x.is_duplicable(), self.args))

    def is_big_map_friendly(self):
        if self.prim in ['big_map', 'operation', 'sapling_state']:
            return False
        return all(map(lambda x: x.is_big_map_friendly(), self.args))
