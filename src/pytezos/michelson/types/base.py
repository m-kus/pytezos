from copy import copy, deepcopy
from typing import Any, List, Optional, Tuple, Type, Union, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.forge import forge_micheline, unforge_micheline
from pytezos.michelson.micheline import Micheline

type_mappings = {
    'nat': 'int  /* Natural number */',
    'unit': 'None || Unit /* `from pytezos import Unit` for resolving None ambiguity */',
    'bytes': 'str  /* Hex string */ ||\n\tbytes  /* Python byte string */',
    'timestamp': 'int  /* Unix time in seconds */ ||\n\tstring  /* Formatted datetime `%Y-%m-%dT%H:%M:%SZ` */',
    'mutez': 'int  /* Amount in `utz` (10^-6) */ ||\n\tDecimal  /* Amount in `tz` */',
    'contract': 'str  /* Base58 encoded `KT` address with optional entrypoint */'
                ' ||\n\tNone  /* when you need to avoid type checking */'
                ' ||\n\tUndefined  /* `from pytezos import Undefined` for resolving None ambiguity  */',
    'address': 'str  /* Base58 encoded `tz` or `KT` address */',
    'key': 'str  /* Base58 encoded public key */',
    'key_hash': 'str  /* Base58 encoded public key hash */',
    'signature': 'str  /* Base58 encoded signature */',
    'lambda': 'str  /* Michelson source code */',
    'chain_id': 'str  /* Base58 encoded chain ID */',
    'ticket': '/* no literal form, tickets can only be created by another contract */',
    'operation': '/* no literal form, operations can only be spawned by another contract or lambda */'
}


class undefined:

    def __repr__(self):
        return '_'

    def __eq__(self, other):
        return isinstance(other, undefined)

    def __lt__(self, other):
        return False

    def __hash__(self):
        return hash(None)


Undefined = undefined()


def parse_name(annots: List[str], prefix: str) -> Optional[str]:
    if annots is None:
        return None
    sub_annots = [x[1:] for x in annots if x.startswith(prefix)]
    assert len(sub_annots) <= 1, f'multiple "{prefix}" annotations are not allowed: {sub_annots}'
    return sub_annots[0] if sub_annots else None


class MichelsonType(Micheline):
    field_name: Optional[str] = None
    type_name: Optional[str] = None
    args: List[Union[Type['MichelsonType'], Any]] = []

    # NOTE: for sorting
    def __lt__(self, other: 'MichelsonType'):
        assert not self.is_comparable(), f'must be implemented for comparable types'

    # NOTE: for contains
    def __eq__(self, other: 'MichelsonType'):  # type: ignore
        assert not self.is_comparable(), f'must be implemented for comparable types'

    def __getitem__(self, key):
        assert False, f'forbidden'

    @staticmethod
    def match(expr) -> Type['MichelsonType']:
        return cast(Type['MichelsonType'], Micheline.match(expr))

    @classmethod
    def create_type(cls,
                    args: List[Type['Micheline']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonType']:
        type_args = [arg for arg in args if issubclass(arg, MichelsonType)]
        if cls.prim in ['list', 'set', 'map', 'big_map', 'option', 'contract', 'lambda']:
            for arg in type_args:
                assert arg.field_name is None, f'{cls.prim} argument type cannot be annotated: %{arg.field_name}'
        if cls.prim in ['set', 'map', 'big_map', 'ticket']:
            assert type_args[0].is_comparable(), f'{cls.prim} key type has to be comparable (not {type_args[0].prim})'
        if cls.prim == 'big_map':
            assert type_args[0].is_big_map_friendly(), f'impossible big_map value type'
        res = type(cls.__name__, (cls,), dict(field_name=parse_name(annots, '%'),  # type: ignore
                                              type_name=parse_name(annots, ':'),  # type: ignore
                                              args=args,
                                              **kwargs))
        return cast(Type['MichelsonType'], res)

    @classmethod
    def get_anon_type(cls) -> Type['MichelsonType']:
        return cls.create_type(args=cls.args)

    @classmethod
    def as_micheline_expr(cls) -> dict:
        annots = []
        if cls.type_name is not None:
            annots.append(f':{cls.type_name}')
        if cls.field_name is not None:
            annots.append(f'%{cls.field_name}')
        args = [arg.as_micheline_expr() for arg in cls.args]
        expr = dict(prim=cls.prim, annots=annots, args=args)
        return {k: v for k, v in expr.items() if v}

    @classmethod
    def generate_pydoc(cls, definitions: List[Tuple[str, str]], inferred_name=None, comparable=False) -> str:
        assert len(cls.args) == 0 \
            or cls.prim in ['contract', 'lambda', 'ticket', 'sapling_state', 'sapling_transaction'], \
            'defined for simple types only'
        if cls.prim in type_mappings:
            if all(x != cls.prim for x, _ in definitions):
                definitions.append((cls.prim, type_mappings[cls.prim]))
        return cls.prim  # type: ignore

    @classmethod
    def is_comparable(cls):
        if cls.prim in ['bls12_381_fr', 'bls12_381_g1', 'bls12_381_g2', 'sapling_state', 'sapling_transaction',
                        'big_map', 'contract', 'lambda', 'list', 'map', 'set', 'operation', 'ticket']:
            return False
        return all(map(lambda x: x.is_comparable(), cls.args))

    @classmethod
    def is_passable(cls):
        if cls.prim in ['operation']:
            return False
        elif cls.prim == 'lambda':
            return True
        return all(map(lambda x: x.is_passable(), cls.args))

    @classmethod
    def is_storable(cls):
        if cls.prim in ['contract', 'operation']:
            return False
        elif cls.prim == 'lambda':
            return True
        return all(map(lambda x: x.is_storable(), cls.args))

    @classmethod
    def is_pushable(cls):
        if cls.prim in ['big_map', 'operation', 'sapling_state', 'ticket']:
            return False
        elif cls.prim == 'lambda':
            return True
        return all(map(lambda x: x.is_pushable(), cls.args))

    @classmethod
    def is_packable(cls):
        if cls.prim in ['big_map', 'operation', 'sapling_state', 'ticket']:
            return False
        elif cls.prim == 'lambda':
            return True
        return all(map(lambda x: x.is_packable(), cls.args))

    @classmethod
    def is_duplicable(cls):
        if cls.prim in ['ticket']:
            return False
        elif cls.prim == 'lambda':
            return True
        return all(map(lambda x: x.is_duplicable(), cls.args))

    @classmethod
    def is_big_map_friendly(cls):
        if cls.prim in ['big_map', 'operation', 'sapling_state']:
            return False
        elif cls.prim == 'lambda':
            return True
        return all(map(lambda x: x.is_big_map_friendly(), cls.args))

    @classmethod
    def unpack(cls, data: bytes) -> 'MichelsonType':
        assert cls.is_packable(), f'{cls.prim} cannot be packed'
        assert data.startswith(b'\x05'), f'packed data should start with 05'
        val_expr = unforge_micheline(data[1:])
        return cls.from_micheline_value(val_expr)

    @classmethod
    def from_literal(cls, literal: Type[Micheline]) -> 'MichelsonType':
        expr = literal.as_micheline_expr()
        return cls.from_micheline_value(expr)

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'MichelsonType':
        raise NotImplementedError

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'MichelsonType':
        raise NotImplementedError

    @classmethod
    def from_python_object(cls, py_obj) -> 'MichelsonType':
        raise NotImplementedError

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        raise NotImplementedError

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        raise NotImplementedError

    def to_literal(self) -> Type[Micheline]:
        raise NotImplementedError

    def attach_context(self, context: AbstractContext, big_map_copy=False):  # NOTE: mutation
        assert len(self.args) == 0 or self.prim in ['contract', 'lambda', 'ticket', 'set']

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        assert len(self.args) == 0 or self.prim in ['contract', 'lambda', 'ticket', 'set']
        return copy(self)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable') -> 'MichelsonType':
        assert len(self.args) == 0 or self.prim in ['contract', 'lambda', 'ticket', 'set']
        return copy(self)

    def forge(self, mode='readable') -> bytes:
        val_expr = self.to_micheline_value(mode=mode)
        return forge_micheline(val_expr)

    def pack(self, legacy=False) -> bytes:
        assert self.is_packable(), f'{self.prim} cannot be packed'
        data = self.forge(mode='legacy_optimized' if legacy else 'optimized')
        return b'\x05' + data

    def duplicate(self):
        assert self.is_duplicable(), f'{self.prim} is not duplicable'
        return deepcopy(self)


def generate_pydoc(ty: Type[MichelsonType], title=None):
    definitions = []  # type: ignore
    top_def = ty.generate_pydoc(definitions, inferred_name=title)
    if not top_def.startswith('$'):
        definitions.insert(0, (title or ty.field_name or ty.type_name or 'element', top_def))
    return '\n'.join(map(lambda x: f'${x[0]}:\n\t{x[1]}\n', definitions))
