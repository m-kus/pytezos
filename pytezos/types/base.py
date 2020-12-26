from copy import copy
from typing import Tuple, Dict, Callable, List, Optional, Type, cast

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


class LazyStorage:

    def register_big_map(self, ptr: int, action: str):
        raise NotImplementedError

    def get_tmp_big_map_id(self) -> int:
        raise NotImplementedError

    def get_big_map_diff(self) -> Tuple[int, str]:
        raise NotImplementedError

    def get_big_map_value(self, key_hash: str):
        raise NotImplementedError


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
    prim: str = ''
    field_name: Optional[str] = None
    type_name: Optional[str] = None
    type_args: List[Type['MichelsonType']] = []
    type_classes: Dict[str, Tuple[Type['MichelsonType'], int]] = {}

    def __init__(self, var_name: Optional[str] = None):
        self.var_name = var_name

    def __lt__(self, other: 'MichelsonType'):  # for sorting
        assert not self.is_comparable(), f'must be implemented for comparable types'

    def __eq__(self, other: 'MichelsonType'):  # for contains
        assert not self.is_comparable(), f'must be implemented for comparable types'

    @classmethod
    def __init_subclass__(cls, prim='', args_len=0, **kwargs):
        super().__init_subclass__(**kwargs)
        if prim:
            cls.type_classes[prim] = (cls, args_len)
            cls.prim = prim

    @staticmethod
    def match(type_expr) -> Type['MichelsonType']:
        prim, type_args, field_name, type_name = parse_micheline_type(type_expr)
        assert prim in MichelsonType.type_classes, f'unknown primitive {prim}'
        cls, args_len = MichelsonType.type_classes[prim]
        assert args_len is None or len(type_args) == args_len, f'{prim}: expected {args_len} args, got {len(type_args)}'
        args = [MichelsonType.match(arg) for arg in type_args]
        return cls.construct_type(type_args=args, field_name=field_name, type_name=type_name)

    @classmethod
    def construct_type(cls, type_args: List[Type['MichelsonType']],
                       field_name: Optional[str] = None, type_name: Optional[str] = None) -> Type['MichelsonType']:
        if cls.prim in ['list', 'set', 'map', 'big_map', 'option', 'contract', 'lambda', 'parameter', 'storage']:
            for arg in type_args:
                assert arg.field_name is None, f'{cls.prim} argument type cannot be annotated: %{arg.field_name}'
        if cls.prim in ['set', 'map', 'big_map']:
            assert type_args[0].is_comparable(), f'{cls.prim} key type has to be comparable (not {type_args[0].prim})'
        if cls.prim == 'big_map':
            assert type_args[0].is_big_map_friendly(), f'impossible big_map value type'
        res = type(cls.__name__, (cls,), dict(field_name=field_name, type_name=type_name, type_args=type_args))
        return cast(Type['MichelsonType'], res)

    @classmethod
    def assert_equal_types(cls, other: Type['MichelsonType']):
        assert cls.prim == other.prim, f'primitive: "{cls.prim}" vs "{other.prim}"'
        if cls.type_name and other.type_name:
            assert cls.type_name == other.type_name, f'type annotations: "{cls.type_name}" vs "{other.type_name}"'
        if cls.field_name and other.field_name:
            assert cls.field_name == other.field_name, f'field annotations: "{cls.field_name}" vs "{other.field_name}"'
        assert len(cls.type_args) == len(other.type_args), f'args len: {len(cls.type_args)} vs {len(other.type_args)}'
        for i, arg in enumerate(other.type_args):
            assert cls.type_args[i].assert_equal_types(arg)

    @classmethod
    def get_micheline_type(cls) -> dict:
        annots = []
        if cls.field_name is not None:
            annots.append(f'%{cls.field_name}')
        if cls.type_name is not None:
            annots.append(f':{cls.type_name}')
        type_args = [arg.get_micheline_type() for arg in cls.type_args]
        expr = dict(prim=cls.prim, annots=annots, args=type_args)
        return {k: v for k, v in expr.items() if v}

    @classmethod
    def generate_pydoc(cls, definitions: List[Tuple[str, str]], inferred_name=None) -> str:
        assert len(cls.type_args) == 0, f'defined for simple types only'
        if cls.prim in type_mappings:
            if all(x != cls.prim for x, _ in definitions):
                definitions.append((cls.prim, type_mappings[cls.prim]))
        return cls.prim

    @classmethod
    def is_comparable(cls):
        if cls.prim in ['bls12_381_fr', 'bls12_381_g1', 'bls12_381_g2', 'sapling_state', 'sapling_transaction',
                        'big_map', 'contract', 'lambda', 'list', 'map', 'set', 'operation', 'ticket']:
            return False
        return all(map(lambda x: x.is_comparable(), cls.type_args))

    @classmethod
    def is_passable(cls):
        if cls.prim in ['operation']:
            return False
        return all(map(lambda x: x.is_passable(), cls.type_args))

    @classmethod
    def is_storable(cls):
        if cls.prim in ['contract', 'operation']:
            return False
        return all(map(lambda x: x.is_storable(), cls.type_args))

    @classmethod
    def is_pushable(cls):
        if cls.prim in ['big_map', 'contract', 'operation', 'sapling_state', 'ticket']:
            return False
        return all(map(lambda x: x.is_pushable(), cls.type_args))

    @classmethod
    def is_packable(cls):
        if cls.prim in ['big_map', 'operation', 'sapling_state', 'ticket']:
            return False
        return all(map(lambda x: x.is_packable(), cls.type_args))

    @classmethod
    def is_duplicable(cls):
        if cls.prim in ['ticket']:
            return False
        return all(map(lambda x: x.is_duplicable(), cls.type_args))

    @classmethod
    def is_big_map_friendly(cls):
        if cls.prim in ['big_map', 'operation', 'sapling_state']:
            return False
        return all(map(lambda x: x.is_big_map_friendly(), cls.type_args))

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'MichelsonType':
        raise NotImplementedError

    @classmethod
    def from_python_object(cls, py_obj) -> 'MichelsonType':
        raise NotImplementedError

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        raise NotImplementedError

    def to_python_object(self, lazy_diff=False):
        raise NotImplementedError

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        assert len(self.type_args) == 0 or self.prim in ['contract', 'lambda'], f'defined for simple types only'
        return copy(self)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        assert len(self.type_args) == 0 or self.prim in ['contract', 'lambda'], f'defined for simple types only'

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action: str):  # NOTE: mutation
        assert len(self.type_args) == 0 or self.prim in ['contract', 'lambda'], f'defined for simple types only'

