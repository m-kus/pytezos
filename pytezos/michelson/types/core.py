from typing import Type

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline, MichelineLiteral, blind_unpack, parse_micheline_literal, parse_micheline_value
from pytezos.michelson.types.base import MichelsonType


class unit(object):

    def __repr__(self):
        return 'Unit'

    def __eq__(self, other):
        return isinstance(other, unit)

    def __lt__(self, other):
        return False


Unit = unit()


class TrueLiteral(Micheline, prim='True'):
    pass


class FalseLiteral(Micheline, prim='False'):
    pass


class UnitLiteral(Micheline, prim='Unit'):
    pass


class StringType(MichelsonType, prim='string'):

    def __init__(self, value: str = ''):
        super(StringType, self).__init__()
        self.value = value

    def __lt__(self, other: 'StringType'):  # type: ignore
        return self.value < other.value

    def __eq__(self, other: 'StringType'):  # type: ignore
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f'\'{self.value}\''

    def __str__(self):
        return self.value

    def __len__(self):
        return len(self.value)

    @classmethod
    def from_value(cls, value: str) -> 'StringType':
        assert isinstance(value, str), f'expected string, got {type(value).__name__}'
        assert len(value) == len(value.encode()), f'unicode symbols are not allowed: {value}'
        return cls(value)

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'StringType':
        return cls()

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'StringType':
        value = parse_micheline_literal(val_expr, {'string': str})
        return cls.from_value(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'StringType':
        return cls.from_value(py_obj)

    def to_literal(self) -> Type[Micheline]:
        return MichelineLiteral.create(self.value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'string': self.value}

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        return self.value

    def __getitem__(self, item):
        assert isinstance(item, slice), f'expected start:end, got {item}'
        assert len(self.value) > 0, f'string is empty'
        assert item.stop <= len(self.value), f'out of bounds {item.stop} <= {len(self.value)}'
        return StringType(self.value[item.start:item.stop])


class IntType(MichelsonType, prim='int'):

    def __init__(self, value: int = 0):
        super(IntType, self).__init__()
        self.value = value

    def __lt__(self, other: 'IntType'):  # type: ignore
        return self.value < other.value

    def __eq__(self, other: 'IntType'):  # type: ignore
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'IntType':
        return cls()

    @classmethod
    def from_value(cls, value: int) -> 'IntType':
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'IntType':
        value = parse_micheline_literal(val_expr, {'int': int})
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'IntType':
        assert isinstance(py_obj, int), f'expected integer, got {type(py_obj).__name__}'
        return cls(py_obj)

    def to_literal(self) -> Type[Micheline]:
        return MichelineLiteral.create(self.value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'int': str(self.value)}

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        return self.value


class NatType(IntType, prim='nat'):

    @classmethod
    def from_value(cls, value: int) -> 'NatType':
        assert value >= 0, f'expected natural number, got {value}'
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'NatType':
        value = parse_micheline_literal(val_expr, {'int': int})
        return cls.from_value(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'NatType':
        assert isinstance(py_obj, int), f'expected integer, got {type(py_obj).__name__}'
        return cls.from_value(py_obj)


class BytesType(MichelsonType, prim='bytes'):

    def __init__(self, value: bytes = b''):
        super(BytesType, self).__init__()
        self.value = value

    def __lt__(self, other: 'BytesType'):  # type: ignore
        return self.value < other.value

    def __eq__(self, other: 'BytesType'):  # type: ignore
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f'0x{self.value.hex()}'

    def __bytes__(self):
        return self.value

    def __len__(self):
        return len(self.value)

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'BytesType':
        return cls()

    @classmethod
    def from_value(cls, value: bytes):
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'BytesType':
        value = parse_micheline_literal(val_expr, {'bytes': bytes.fromhex})
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'BytesType':
        if isinstance(py_obj, bytes):
            value = py_obj
        elif isinstance(py_obj, str):
            if py_obj.startswith('0x'):
                py_obj = py_obj[2:]
            value = bytes.fromhex(py_obj)
        else:
            assert False, f'unexpected value type {py_obj}'
        return cls(value)

    def to_literal(self) -> Type[Micheline]:
        return MichelineLiteral.create(self.value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'bytes': self.value.hex()}

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        if try_unpack:
            return blind_unpack(self.value)
        return self.value

    def __getitem__(self, item):
        assert isinstance(item, slice), f'expected start:stop, got {item}'
        assert item.stop <= len(self.value), f'index out of bounds'
        return BytesType(self.value[item.start:item.stop])


class BoolType(MichelsonType, prim='bool'):

    def __init__(self, value: bool):
        super(BoolType, self).__init__()
        self.value = value

    def __lt__(self, other: 'BoolType'):  # type: ignore
        return self.value < other.value

    def __eq__(self, other: 'BoolType'):  # type: ignore
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return str(self.value)

    def __bool__(self):
        return self.value

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'BoolType':
        return cls(False)

    @classmethod
    def from_value(cls, value: bool):
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'BoolType':
        value = parse_micheline_value(val_expr, {
            ('False', 0): lambda x: False,
            ('True', 0): lambda x: True
        })
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'BoolType':
        assert isinstance(py_obj, bool), f'expected boolean, got {type(py_obj).__name__}'
        return cls(py_obj)

    def to_literal(self) -> Type[Micheline]:
        return TrueLiteral if self.value else FalseLiteral

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'prim': 'True' if self.value else 'False'}

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        return self.value


class UnitType(MichelsonType, prim='unit'):

    def __init__(self):
        super(UnitType, self).__init__()

    def __lt__(self, other: 'UnitType'):  # type: ignore
        return False

    def __eq__(self, other: 'UnitType'):  # type: ignore
        return True

    def __hash__(self):
        return hash(Unit)

    def __repr__(self):
        return 'Unit'

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'UnitType':
        return cls()

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'UnitType':
        parse_micheline_value(val_expr, {('Unit', 0): lambda x: x})
        return cls()

    @classmethod
    def from_python_object(cls, py_obj) -> 'UnitType':
        assert py_obj is None or isinstance(py_obj, unit), f'expected None or Unit, got {type(py_obj).__name__}'
        return cls()

    def to_literal(self) -> Type[Micheline]:
        return UnitLiteral

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'prim': 'Unit'}

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        return unit()


class NeverType(MichelsonType, prim='never'):

    def __lt__(self, other: 'NeverType'):  # type: ignore
        return False

    def __eq__(self, other: 'NeverType'):  # type: ignore
        return True
