from decimal import Decimal
from typing import Type, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.context.abstract import get_originated_address
from pytezos.crypto.encoding import base58_decode, is_address, is_chain_id, is_kt, is_pkh, is_public_key, is_sig
from pytezos.michelson.forge import (forge_address, forge_base58, forge_contract, forge_public_key, optimize_timestamp, unforge_address,
                                     unforge_chain_id, unforge_contract, unforge_public_key, unforge_signature)
from pytezos.michelson.format import format_timestamp, micheline_to_michelson
from pytezos.michelson.micheline import Micheline, parse_micheline_literal
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.types.base import Undefined
from pytezos.michelson.types.core import IntType, MichelsonType, NatType, StringType


class TimestampType(IntType, prim='timestamp'):  # type: ignore

    @classmethod
    def from_value(cls, value: int) -> 'TimestampType':
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'TimestampType':
        value = parse_micheline_literal(val_expr, {
            'int': int,
            'string': optimize_timestamp
        })
        return cls.from_value(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'TimestampType':
        if isinstance(py_obj, int):
            value = py_obj
        elif isinstance(py_obj, str):
            value = optimize_timestamp(py_obj)
        else:
            assert False, f'unexpected value type {py_obj}'
        return cls.from_value(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if mode in ['optimized', 'legacy_optimized']:
            return {'int': str(self.value)}
        elif mode == 'readable':
            return {'string': format_timestamp(self.value)}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        return self.value


class MutezType(NatType, prim='mutez'):

    def __repr__(self):
        return str(Decimal(self.value) / 10 ** 6)

    @classmethod
    def from_value(cls, value: int) -> 'MutezType':
        assert value >= 0, f'expected natural number, got {value}'
        assert value.bit_length() <= 63, f'mutez overflow, got {value.bit_length()} bits, should not exceed 63'
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'MutezType':
        if isinstance(py_obj, int):
            value = py_obj
        elif isinstance(py_obj, Decimal):
            value = int(py_obj * (10 ** 6))
        elif isinstance(py_obj, str):
            value = int(Decimal(py_obj) * (10 ** 6))
        else:
            assert False, f'unexpected value type {py_obj}'
        return cls.from_value(value)


class AddressType(StringType, prim='address'):

    def __repr__(self):
        return f'{self.value[:6]}…{self.value[-3:]}'

    def __lt__(self, other: 'AddressType') -> bool:  # type: ignore
        if is_pkh(self.value) and is_kt(other.value):
            return True
        elif is_kt(self.value) and is_pkh(other.value):
            return False
        else:
            return self.value < other.value

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'AddressType':
        return cls.from_value(context.get_dummy_address())

    @classmethod
    def from_value(cls, value: str) -> 'AddressType':
        if value.endswith('%default'):
            value = value.split('%')[0]
        assert is_address(value), f'expected tz/KT address, got {value}'
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'AddressType':
        value = parse_micheline_literal(val_expr, {
            'bytes': lambda x: unforge_contract(bytes.fromhex(x)),
            'string': lambda x: x
        })
        return cls.from_value(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'AddressType':
        return cls.from_value(py_obj)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if mode in ['optimized', 'legacy_optimized']:
            return {'bytes': forge_contract(self.value).hex()}  # because address can also have an entrypoint
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        return self.value


class KeyType(StringType, prim='key'):

    @property
    def raw(self) -> bytes:
        return base58_decode(self.value.encode())

    @property
    def prefix(self) -> str:
        return self.value[:4]

    def __lt__(self, other: 'KeyType') -> bool:  # type: ignore
        """
        Keys are ordered as follows: edpk < sppk < p2pk
        All keys are in compressed form in Tezos (flag | X) where flag specifies if Y is odd or even
        https://crypto.stackexchange.com/questions/70754/ec-key-compression
        For secp256r1 (aka p256) we need to cut the first byte (for unknown reason)
        """
        curves = {
            'edpk': (0, 0),
            'sppk': (1, 0),
            'p2pk': (2, 1)
        }
        res = curves[self.prefix][0] - curves[other.prefix][0]
        if res < 0:
            return True
        elif res > 0:
            return False
        else:
            offset = curves[self.prefix][1]
            return self.raw[offset:] < other.raw[offset:]

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'KeyType':
        return cls.from_value(context.get_dummy_public_key())

    @classmethod
    def from_value(cls, value: str) -> 'KeyType':
        assert is_public_key(value), f'expected ed/sp/p2 public key, got {value}'
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'KeyType':
        value = parse_micheline_literal(val_expr, {
            'bytes': lambda x: unforge_public_key(bytes.fromhex(x)),
            'string': lambda x: x
        })
        return cls.from_value(value)

    @classmethod
    def parse_python_object(cls, py_obj) -> 'KeyType':
        return cls.from_value(py_obj)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if mode in ['optimized', 'legacy_optimized']:
            return {'bytes': forge_public_key(self.value).hex()}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        return self.value


class KeyHashType(StringType, prim='key_hash'):

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'KeyHashType':
        return cls.from_value(context.get_dummy_key_hash())

    @classmethod
    def from_value(cls, value: str) -> 'KeyHashType':
        assert is_pkh(value), f'expected tz1/tz2/tz3 key hash, got {value}'
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'KeyHashType':
        value = parse_micheline_literal(val_expr, {
            'bytes': lambda x: unforge_address(bytes.fromhex(x)),
            'string': lambda x: x
        })
        return cls.from_value(value)

    @classmethod
    def parse_python_object(cls, py_obj):
        return cls.from_value(py_obj)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if mode in ['optimized', 'legacy_optimized']:
            return {'bytes': forge_address(self.value, tz_only=True).hex()}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        return self.value


class SignatureType(StringType, prim='signature'):

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'SignatureType':
        return cls.from_value(context.get_dummy_signature())

    @classmethod
    def from_value(cls, value: str) -> 'SignatureType':
        assert is_sig(value), f'expected signature, got {value}'
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'SignatureType':
        value = parse_micheline_literal(val_expr, {
            'bytes': lambda x: unforge_signature(bytes.fromhex(x)),
            'string': lambda x: x
        })
        return cls.from_value(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'SignatureType':
        return cls.from_value(py_obj)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if mode in ['optimized', 'legacy_optimized']:
            return {'bytes': forge_base58(self.value).hex()}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        return self.value


class ChainIdType(StringType, prim='chain_id'):

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'ChainIdType':
        return cls.from_value(context.get_dummy_chain_id())

    @classmethod
    def from_value(cls, value: str) -> 'ChainIdType':
        assert is_chain_id(value), f'expected chain id, got {value}'
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'ChainIdType':
        value = parse_micheline_literal(val_expr, {
            'bytes': lambda x: unforge_chain_id(bytes.fromhex(x)),
            'string': lambda x: x
        })
        return cls.from_value(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'ChainIdType':
        return cls.from_value(py_obj)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if mode in ['optimized', 'legacy_optimized']:
            return {'bytes': forge_base58(self.value).hex()}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        return self.value


class ContractType(AddressType, prim='contract', args_len=1):

    def __repr__(self):
        address, entrypoint = self.get_address(), self.get_entrypoint()
        return f'{address[:6]}…{address[-3:]}%{entrypoint}'

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None, comparable=False):
        super(ContractType, cls).generate_pydoc(definitions)
        param_expr = micheline_to_michelson(cls.args[0].as_micheline_expr())
        if cls.args[0].args:
            name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
            param_name = f'{name}_param'
            definitions.insert(0, (param_name, param_expr))
            return f'contract (${param_name})'
        else:
            return f'contract ({param_expr})'

    @classmethod
    def from_python_object(cls, py_obj) -> 'ContractType':
        if py_obj is None or py_obj is Undefined:
            py_obj = get_originated_address(0)
        res = super(ContractType, cls).from_python_object(py_obj)
        return cast(ContractType, res)

    def get_address(self) -> str:
        return self.value.split('%')[0]

    def get_entrypoint(self) -> str:
        res = self.value.split('%')
        return res[1] if len(res) == 2 else 'default'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        assert not comparable, f'{self.prim} is not comparable'
        return super(ContractType, self).to_python_object()


class LambdaType(MichelsonType, prim='lambda', args_len=2):  # type: ignore

    def __init__(self, value: Type[Micheline]):
        super(LambdaType, self).__init__()
        self.value = value

    def __repr__(self):
        return 'Lambda'

    def __eq__(self, other) -> bool:
        if not isinstance(other, LambdaType):
            return False
        # FIXME: That seems ugly
        return self.value.as_micheline_expr() == other.value.as_micheline_expr()

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None, comparable=False):
        super(LambdaType, cls).generate_pydoc(definitions)
        name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
        expr = {}
        for i, suffix in enumerate(['return', 'param']):
            arg_expr = micheline_to_michelson(cls.args[i].as_micheline_expr())
            if cls.args[i].args:
                arg_name = f'{name}_{suffix}'
                definitions.insert(0, (arg_name, arg_expr))
                expr[suffix] = f'${arg_name}'
            else:
                expr[suffix] = arg_expr
        return f'lambda ({expr["param"]} -> {expr["return"]})'

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'LambdaType':
        return cls(Micheline.match(context.get_dummy_lambda()))

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'LambdaType':
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'
        return cls(Micheline.match(val_expr))

    @classmethod
    def from_python_object(cls, py_obj) -> 'LambdaType':
        assert isinstance(py_obj, str), f'expected string, got {type(py_obj).__name__}'
        value = michelson_to_micheline(py_obj)
        return cls.from_micheline_value(value)

    def to_literal(self) -> Type[Micheline]:
        return self.value

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        # TODO: optimized mode -> harcoded values in the code
        return self.value.as_micheline_expr()

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        assert not comparable, f'{self.prim} is not comparable'
        return micheline_to_michelson(self.to_micheline_value())
