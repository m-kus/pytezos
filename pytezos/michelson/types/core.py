from pytezos.michelson.types.base import MichelsonType, unit
from pytezos.michelson.micheline import parse_micheline_value, parse_micheline_literal, blind_unpack as blind_unpack
from pytezos.context.execution import ExecutionContext

Unit = unit()


class StringType(MichelsonType, prim='string'):

    def __init__(self, value: str = ''):
        super(StringType, self).__init__()
        self.value = value

    def __lt__(self, other: 'StringType'):
        return self.value < other.value

    def __eq__(self, other: 'StringType'):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return self.value

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
    def dummy(cls, context: ExecutionContext) -> 'StringType':
        return cls()

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'StringType':
        value = parse_micheline_literal(val_expr, {'string': str})
        return cls.from_value(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'StringType':
        return cls.from_value(py_obj)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'string': self.value}

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.value

    def __getitem__(self, item):
        assert isinstance(item, tuple)
        start, stop = item
        assert len(self.value) > 0, f'string is empty'
        assert stop <= len(self.value), f'out of bounds {stop} <= {len(self.value)}'
        return StringType(self.value[start:stop])


class IntType(MichelsonType, prim='int'):

    def __init__(self, value: int = 0):
        super(IntType, self).__init__()
        self.value = value

    def __lt__(self, other: 'IntType'):
        return self.value < other.value

    def __eq__(self, other: 'IntType'):
        return self.value == other.value

    def __cmp__(self, other: 'IntType'):
        if self.value == other.value:
            return 0
        elif self.value < other.value:
            return -1
        else:
            return 1

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    @classmethod
    def dummy(cls, context: ExecutionContext) -> 'IntType':
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

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'int': str(self.value)}

    def to_python_object(self, try_unpack=False, lazy_diff=False):
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

    def __lt__(self, other: 'BytesType'):
        return self.value < other.value

    def __eq__(self, other: 'BytesType'):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return self.value.hex()

    def __bytes__(self):
        return self.value

    def __len__(self):
        return len(self.value)

    @classmethod
    def dummy(cls, context: ExecutionContext) -> 'BytesType':
        return cls()

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

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'bytes': self.value.hex()}

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        if try_unpack:
            return blind_unpack(self.value)
        return self.value

    def __getitem__(self, item):
        assert isinstance(item, tuple)
        start, stop = item
        assert stop <= len(self.value), f'index out of bounds'
        return BytesType(self.value[start:stop])


class BoolType(MichelsonType, prim='bool'):

    def __init__(self, value: bool):
        super(BoolType, self).__init__()
        self.value = value

    def __lt__(self, other: 'BoolType'):
        return self.value < other.value

    def __eq__(self, other: 'BoolType'):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return str(self.value)

    def __bool__(self):
        return self.value

    @classmethod
    def dummy(cls, context: ExecutionContext) -> 'BoolType':
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

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'prim': 'True' if self.value else 'False'}

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.value


class UnitType(MichelsonType, prim='unit'):

    def __init__(self):
        super(UnitType, self).__init__()

    def __lt__(self, other: 'UnitType'):
        return False

    def __eq__(self, other: 'UnitType'):
        return True

    def __hash__(self):
        return hash(Unit)

    def __repr__(self):
        return 'Unit'

    @classmethod
    def dummy(cls, context: ExecutionContext) -> 'UnitType':
        return cls()

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'UnitType':
        parse_micheline_value(val_expr, {('Unit', 0): lambda x: x})
        return cls()

    @classmethod
    def from_python_object(cls, py_obj) -> 'UnitType':
        assert py_obj is None or isinstance(py_obj, unit), f'expected None or Unit, got {type(py_obj).__name__}'
        return cls()

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'prim': 'Unit'}

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return unit()


class NeverType(MichelsonType, prim='never'):
    pass
