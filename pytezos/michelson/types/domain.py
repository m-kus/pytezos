from decimal import Decimal

from pytezos.crypto.encoding import is_address, is_public_key, is_pkh, \
    is_sig, \
    is_kt, is_chain_id
from pytezos.michelson.forge import forge_public_key, unforge_public_key, unforge_chain_id, unforge_signature, forge_address, \
    unforge_address, unforge_contract, forge_base58, forge_timestamp, forge_contract
from pytezos.michelson.format import format_timestamp, micheline_to_michelson
from pytezos.michelson.types.core import NatType, IntType, StringType
from pytezos.michelson.types.base import MichelsonType, parse_micheline_literal
from pytezos.michelson.parse import michelson_to_micheline


class TimestampType(IntType, prim='timestamp'):

    @classmethod
    def from_value(cls, value: int) -> 'TimestampType':
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'TimestampType':
        value = parse_micheline_literal(val_expr, {
            'int': int,
            'string': forge_timestamp
        })
        return cls.from_value(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'TimestampType':
        if isinstance(py_obj, int):
            value = py_obj
        elif isinstance(py_obj, str):
            value = forge_timestamp(py_obj)
        else:
            assert False, f'unexpected value type {py_obj}'
        return cls.from_value(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if mode == 'optimized':
            return {'int': str(self.value)}
        elif mode == 'readable':
            return {'string': format_timestamp(self.value)}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.value


class MutezType(NatType, prim='mutez'):

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

    def __lt__(self, other: 'AddressType') -> bool:
        if is_pkh(self.value) and is_kt(other.value):
            return True
        elif is_kt(self.value) and is_pkh(other.value):
            return False
        else:
            return self.value < other.value

    @classmethod
    def dummy(cls) -> 'AddressType':
        return cls(unforge_address(b'\x00' * 22))

    @classmethod
    def from_value(cls, value: str) -> 'AddressType':
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
        if mode == 'optimized':
            return {'bytes': forge_contract(self.value).hex()}  # because address can also have an entrypoint
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.value


class KeyType(StringType, prim='key'):

    @classmethod
    def dummy(cls) -> 'KeyType':
        return cls(unforge_public_key(b'\x00' * 33))

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
        if mode == 'optimized':
            return {'bytes': forge_public_key(self.value).hex()}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.value


class KeyHashType(StringType, prim='key_hash'):

    @classmethod
    def dummy(cls) -> 'KeyHashType':
        return cls(unforge_address(b'\x00' * 21))

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
        if mode == 'optimized':
            return {'bytes': forge_address(self.value, tz_only=True).hex()}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.value


class SignatureType(StringType, prim='signature'):

    @classmethod
    def dummy(cls) -> 'SignatureType':
        return cls(unforge_signature(b'\x00' * 64))

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
        if mode == 'optimized':
            return {'bytes': forge_base58(self.value).hex()}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.value


class ChainIdType(StringType, prim='chain_id'):

    @classmethod
    def dummy(cls) -> 'ChainIdType':
        return cls(unforge_chain_id(b'\x00' * 4))

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
        if mode == 'optimized':
            return {'bytes': forge_base58(self.value).hex()}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.value


class ContractType(AddressType, prim='contract', args_len=1):

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None):
        param_expr = micheline_to_michelson(cls.type_args[0].get_micheline_type())
        if cls.type_args[0].type_args:
            name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
            param_name = f'{name}_param'
            definitions.insert(0, (param_name, param_expr))
            return f'contract (${param_name})'
        else:
            return f'contract ({param_expr})'


class LambdaType(MichelsonType, prim='lambda', args_len=2):

    def __init__(self, value: list):
        super(LambdaType, self).__init__()
        self.value = value

    def __repr__(self):
        return micheline_to_michelson(self.value)

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None):
        name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
        expr = {}
        for i, suffix in enumerate(['return', 'param']):
            arg_expr = micheline_to_michelson(cls.type_args[i].get_micheline_type())
            if cls.type_args[i].type_args:
                arg_name = f'{name}_{suffix}'
                definitions.insert(0, (arg_name, arg_expr))
                expr[suffix] = f'${arg_name}'
            else:
                expr[suffix] = arg_expr
        return f'lambda ({expr["param"]} -> {expr["return"]})'

    @classmethod
    def dummy(cls) -> 'LambdaType':
        return cls([])

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'LambdaType':
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'
        return cls(val_expr)

    @classmethod
    def from_python_object(cls, py_obj) -> 'LambdaType':
        assert isinstance(py_obj, str), f'expected string, got {type(py_obj).__name__}'
        value = michelson_to_micheline(py_obj)
        return cls(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        # TODO: optimized mode -> harcoded values in the code
        return self.value

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return micheline_to_michelson(self.value)
