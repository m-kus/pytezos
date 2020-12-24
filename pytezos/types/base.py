from typing import Tuple, Dict, Callable, List
from pprint import pformat

type_mappings = {
    'nat': 'int  /* Natural number */',
    'unit': 'Unit || None /* Void */',
    'bytes': 'string  /* Hex string */ ||\n\tbytes  /* Python byte string */',
    'timestamp': 'int  /* Unix time in seconds */ ||\n\tstring  /* Formatted datetime `%Y-%m-%dT%H:%M:%SZ` */',
    'mutez': 'int  /* Amount in `utz` (10^-6) */ ||\n\tDecimal  /* Amount in `tz` */',
    'contract': 'string  /* Base58 encoded `KT` address with optional entrypoint */',
    'address': 'string  /* Base58 encoded `tz` or `KT` address */',
    'key': 'string  /* Base58 encoded public key */',
    'key_hash': 'string  /* Base58 encoded public key hash */',
    'signature': 'string  /* Base58 encoded signature */',
    'lambda': 'string  /* Michelson source code */',
    'chain_id': 'string  /* Base58 encoded chain ID */'
}


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

    def __init__(self, value=undefined(), field_name=None, type_name=None, var_name=None, type_args=None):
        self.value = value
        self.field_name = field_name
        self.type_name = type_name
        self.var_name = var_name
        self.type_args = type_args or []  # type: List[MichelsonType]

    @classmethod
    def __init_subclass__(cls, prim='', args_len=0, **kwargs):
        super().__init_subclass__(**kwargs)
        if prim:
            cls.type_classes[prim] = (cls, args_len)
            cls.prim = prim

    def spawn(self, value):
        return type(self)(value=value,  # NOTE: can be mutated, but not in practice
                          field_name=self.field_name,
                          type_name=self.type_name,
                          type_args=self.type_args)  # NOTE: can be mutated, but not in practice

    def rename(self, var_name):
        return type(self)(value=self.value,  # NOTE: can be mutated, but not in practice
                          field_name=self.field_name,
                          type_name=self.type_name,
                          var_name=var_name,
                          type_args=self.type_args)  # NOTE: can be mutated, but not in practice

    @classmethod
    def construct_type(cls, field_name, type_name, type_args: List['MichelsonType']):
        return cls(value=undefined(), field_name=field_name, type_name=type_name, type_args=type_args)

    def get_type(self):
        return type(self)(value=undefined(),
                          field_name=self.field_name,
                          type_name=self.type_name,
                          type_args=[arg.get_type() for arg in self.type_args])

    @staticmethod
    def from_micheline_type(type_expr):
        prim, type_args, field_name, type_name = parse_micheline_type(type_expr)
        assert prim in MichelsonType.type_classes, f'unknown primitive {prim}'
        cls, args_len = MichelsonType.type_classes[prim]
        assert args_len is None or len(type_args) == args_len, f'{prim}: expected {args_len} args, got {len(type_args)}'
        args = list(map(MichelsonType.from_micheline_type, type_args))   # type: List[MichelsonType]

        if prim in ['list', 'set', 'map', 'big_map', 'option', 'contract', 'lambda', 'parameter', 'storage']:
            for arg in args:
                assert arg.field_name is None, f'{prim} argument type cannot be annotated: %{arg.field_name}'
        if prim in ['set', 'map', 'big_map']:
            assert args[0].is_comparable(), f'{prim} key type has to be comparable (cannot be {args[0].prim})'
        if prim == 'big_map':
            assert args[0].is_big_map_friendly(), f'impossible big_map value type'

        return cls.construct_type(field_name=field_name, type_name=type_name, args=args)

    def get_micheline_type(self) -> dict:
        annots = []
        if self.field_name is not None:
            annots.append(f'%{self.field_name}')
        if self.type_name is not None:
            annots.append(f':{self.type_name}')
        type_args = [arg.get_micheline_type() for arg in self.type_args]
        expr = dict(prim=self.prim, annots=annots, args=type_args)
        return {k: v for k, v in expr.items() if v}

    def parse_micheline_value(self, val_expr) -> 'MichelsonType':
        raise NotImplementedError

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        raise NotImplementedError

    def parse_python_object(self, py_obj) -> 'MichelsonType':
        raise NotImplementedError

    def to_python_object(self, lazy_diff=False):
        raise NotImplementedError

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        return self.spawn(value=self.value)

    def aggregate_lazy_diff(self, lazy_diff: List[dict]):
        assert self.prim not in ['big_map', 'sapling_state'], f'must be explicitly defined for lazy types'

    def generate_pydoc(self, definitions: List[Tuple[str, str]], inferred_name=None) -> str:
        assert len(self.type_args) == 0, f'defined for simple types only'
        if self.prim in type_mappings:
            if all(x != self.prim for x, _ in definitions):
                definitions.append((self.prim, type_mappings[self.prim]))
        return self.prim

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
        return all(map(lambda x: x.is_comparable(), self.type_args))

    def is_passable(self):
        if self.prim in ['operation']:
            return False
        return all(map(lambda x: x.is_passable(), self.type_args))

    def is_storable(self):
        if self.prim in ['contract', 'operation']:
            return False
        return all(map(lambda x: x.is_storable(), self.type_args))

    def is_pushable(self):
        if self.prim in ['big_map', 'contract', 'operation', 'sapling_state', 'ticket']:
            return False
        return all(map(lambda x: x.is_pushable(), self.type_args))

    def is_packable(self):
        if self.prim in ['big_map', 'operation', 'sapling_state', 'ticket']:
            return False
        return all(map(lambda x: x.is_packable(), self.type_args))

    def is_duplicable(self):
        if self.prim in ['ticket']:
            return False
        return all(map(lambda x: x.is_duplicable(), self.type_args))

    def is_big_map_friendly(self):
        if self.prim in ['big_map', 'operation', 'sapling_state']:
            return False
        return all(map(lambda x: x.is_big_map_friendly(), self.type_args))
