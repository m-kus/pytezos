from decimal import Decimal

from pytezos.encoding import forge_timestamp, parse_contract, is_address, forge_contract, parse_public_key, \
    is_public_key, forge_public_key, parse_address, is_pkh, forge_address, parse_signature, forge_base58, is_sig, is_kt
from pytezos.micheline.formatter import format_timestamp, micheline_to_michelson
from pytezos.types.core import NatType, IntType, StringType
from pytezos.types.base import MichelsonType, parse_micheline_literal
from pytezos.micheline.parser import michelson_to_micheline


class TimestampType(IntType, prim='timestamp'):

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_literal(val_expr, {
            'int': int,
            'string': forge_timestamp
        })
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        if mode == 'optimized':
            return {'int': str(self.value)}
        elif mode == 'readable':
            return {'string': format_timestamp(self.value)}
        else:
            assert False, f'unsupported mode {mode}'

    def parse_python_object(self, py_obj):
        if isinstance(py_obj, int):
            value = py_obj
        elif isinstance(py_obj, str):
            value = forge_timestamp(py_obj)
        else:
            assert False, f'unexpected value type {py_obj}'
        return self.spawn(value)

    def to_python_object(self, lazy_diff=False):
        self.assert_value_defined()
        return self.value


class MutezType(NatType, prim='mutez'):

    def parse_python_object(self, py_obj):
        if isinstance(py_obj, int):
            value = py_obj
        elif isinstance(py_obj, Decimal):
            value = int(py_obj * (10 ** 6))
        elif isinstance(py_obj, str):
            value = int(Decimal(py_obj) * (10 ** 6))
        else:
            assert False, f'unexpected value type {py_obj}'
        assert value >= 0, f'expected natural number, got {value}'
        return self.spawn(value)


class AddressType(StringType, prim='address'):

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_literal(val_expr, {
            'bytes': lambda x: parse_contract(bytes.fromhex(x)),
            'string': lambda x: x
        })
        assert is_address(value), f'expected tz/KT address, got {value}'
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        if mode == 'optimized':
            return {'int': forge_contract(self.value)}  # because address can also have an entrypoint
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def parse_python_object(self, py_obj):
        assert is_address(py_obj), f'expected tz/KT address, got {py_obj}'
        return self.spawn(py_obj)

    def to_python_object(self, lazy_diff=False):
        self.assert_value_defined()
        return str(self.value)

    def __cmp__(self, other):
        self.assert_value_defined()
        self.assert_equal_types(other)
        if is_pkh(self.value) and is_kt(other.value):
            return -1
        elif is_kt(self.value) and is_pkh(other.value):
            return 1
        else:
            return str(self).__cmp__(str(other))


class KeyType(StringType, prim='key'):

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_literal(val_expr, {
            'bytes': lambda x: parse_public_key(bytes.fromhex(x)),
            'string': lambda x: x
        })
        assert is_public_key(value), f'expected ed/sp/p2 public key, got {value}'
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        if mode == 'optimized':
            return {'int': forge_public_key(self.value)}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def parse_python_object(self, py_obj):
        assert is_public_key(py_obj), f'expected ed/sp/p2 public key, got {py_obj}'
        return self.spawn(py_obj)

    def to_python_object(self, lazy_diff=False):
        self.assert_value_defined()
        return self.value


class KeyHashType(StringType, prim='key_hash'):

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_literal(val_expr, {
            'bytes': lambda x: parse_address(bytes.fromhex(x)),
            'string': lambda x: x
        })
        assert is_pkh(value), f'expected tz1/tz2/tz3 key hash, got {value}'
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        if mode == 'optimized':
            return {'int': forge_address(self.value, tz_only=True)}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def parse_python_object(self, py_obj):
        assert is_pkh(py_obj), f'expected tz1/tz2/tz3 key hash, got {py_obj}'
        return self.spawn(py_obj)

    def to_python_object(self, lazy_diff=False):
        self.assert_value_defined()
        return self.value


class SignatureType(StringType, prim='signature'):

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_literal(val_expr, {
            'bytes': lambda x: parse_signature(bytes.fromhex(x)),
            'string': lambda x: x
        })
        assert is_sig(value), f'expected signature, got {value}'
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        if mode == 'optimized':
            return {'int': forge_base58(self.value)}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def parse_python_object(self, py_obj):
        assert is_sig(py_obj), f'expected signature, got {py_obj}'
        return self.spawn(py_obj)

    def to_python_object(self, lazy_diff=False):
        self.assert_value_defined()
        return self.value


class ChainIdType(StringType, prim='chain_id'):

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_literal(val_expr, {
            'bytes': lambda x: parse_signature(bytes.fromhex(x)),
            'string': lambda x: x
        })
        assert is_sig(value), f'expected signature, got {value}'
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        if mode == 'optimized':
            return {'int': forge_base58(self.value)}
        elif mode == 'readable':
            return {'string': self.value}
        else:
            assert False, f'unsupported mode {mode}'

    def parse_python_object(self, py_obj):
        assert is_sig(py_obj), f'expected signature, got {py_obj}'
        return self.spawn(py_obj)

    def to_python_object(self, lazy_diff=False):
        self.assert_value_defined()
        return self.value


class NeverType(MichelsonType, prim='never'):

    def assert_value_defined(self):
        assert False, f'forbidden'

    def parse_micheline_value(self, val_expr):
        assert False, f'forbidden'

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        assert False, f'forbidden'

    def parse_python_object(self, py_obj):
        assert False, f'forbidden'

    def to_python_object(self, lazy_diff=False):
        assert False, f'forbidden'


class ContractType(AddressType, prim='contract', args_len=1):

    @property
    def param_type(self):
        return self.type_args[0]

    def generate_pydoc(self, definitions: list, inferred_name=None):
        param_expr = micheline_to_michelson(self.param_type.get_micheline_type())
        if self.param_type.type_args:
            name = self.field_name or self.type_name or inferred_name or f'{self.prim}_{len(definitions)}'
            param_name = f'{name}_param'
            definitions.insert(0, (param_name, param_expr))
            return f'contract (${param_name})'
        else:
            return f'contract ({param_expr})'


class LambdaType(MichelsonType, prim='lambda', args_len=2):

    @property
    def param_type(self):
        return self.type_args[0]

    @property
    def return_type(self):
        return self.type_args[1]

    def assert_value_defined(self):
        assert isinstance(self.value, list), f'value is undefined'

    def parse_micheline_value(self, val_expr):
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'
        return self.spawn(val_expr)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        return self.value

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, str), f'expected string, got {type(py_obj).__name__}'
        value = michelson_to_micheline(py_obj)
        return self.spawn(value)

    def to_python_object(self, lazy_diff=False):
        self.assert_value_defined()
        return micheline_to_michelson(self.value)

    def generate_pydoc(self, definitions: list, inferred_name=None):
        name = self.field_name or self.type_name or inferred_name or f'{self.prim}_{len(definitions)}'
        expr = {}
        for i, suffix in enumerate(['return', 'param']):
            arg_expr = micheline_to_michelson(self.type_args[i].get_micheline_type())
            if self.type_args[i].type_args:
                arg_name = f'{name}_{suffix}'
                definitions.insert(0, (arg_name, arg_expr))
                expr[suffix] = f'${arg_name}'
            else:
                expr[suffix] = arg_expr
        return f'lambda ({expr["param"]} -> {expr["return"]})'

    def __repr__(self):
        self.assert_value_defined()
        return micheline_to_michelson(self.value)
