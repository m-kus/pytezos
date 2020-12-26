from pytezos.types.base import MichelsonType, parse_micheline_literal, parse_micheline_value, unit

Unit = unit()


class StringType(MichelsonType, prim='string'):

    def __init__(self, value: str = ''):
        super(StringType, self).__init__()
        self.value = value

    def __lt__(self, other: 'StringType'):
        return self.value < other.value

    def __eq__(self, other: 'StringType'):
        return self.value == other.value

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value

    @classmethod
    def from_value(cls, value: str):
        assert isinstance(value, str), f'expected string, got {type(value).__name__}'
        assert len(value) == len(value.encode()), f'unicode symbols are not allowed: {value}'
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'StringType':
        value = parse_micheline_literal(val_expr, {'string': str})
        return cls.from_value(value)

    @classmethod
    def from_python_object(cls, py_obj):
        return cls.from_value(py_obj)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'string': self.value}

    def to_python_object(self, lazy_diff=False):
        return self.value


class IntType(MichelsonType, prim='int'):

    def __init__(self, value: int = 0):
        super(IntType, self).__init__()
        self.value = value

    def __lt__(self, other: 'IntType'):
        return self.value < other.value

    def __eq__(self, other: 'IntType'):
        return self.value == other.value

    def __repr__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    @classmethod
    def from_micheline_value(cls, val_expr):
        value = parse_micheline_literal(val_expr, {'int': int})
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj):
        assert isinstance(py_obj, int), f'expected integer, got {type(py_obj).__name__}'
        return cls(py_obj)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'int': str(self.value)}

    def to_python_object(self, lazy_diff=False):
        return self.value


class NatType(IntType, prim='nat'):

    @classmethod
    def from_value(cls, value: int):
        assert value >= 0, f'expected natural number, got {value}'
        return cls(value)

    @classmethod
    def from_micheline_value(cls, val_expr):
        value = parse_micheline_literal(val_expr, {'int': int})
        return cls.from_value(value)

    @classmethod
    def from_python_object(cls, py_obj):
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

    def __repr__(self):
        return self.value.hex()

    def __bytes__(self):
        return self.value

    @classmethod
    def from_micheline_value(cls, val_expr):
        value = parse_micheline_literal(val_expr, {'bytes': bytes.fromhex})
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj):
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

    def to_python_object(self, lazy_diff=False):
        return self.value


class BoolType(MichelsonType, prim='bool'):

    def __init__(self, value: bool):
        super(BoolType, self).__init__()
        self.value = value

    def __lt__(self, other: 'BoolType'):
        return self.value < other.value

    def __eq__(self, other: 'BoolType'):
        return self.value == other.value

    def __repr__(self):
        return str(self.value)

    def __bool__(self):
        return self.value

    @classmethod
    def from_micheline_value(cls, val_expr):
        value = parse_micheline_value(val_expr, {
            ('False', 0): lambda x: False,
            ('True', 0): lambda x: True
        })
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj):
        assert isinstance(py_obj, bool), f'expected boolean, got {type(py_obj).__name__}'
        return cls(py_obj)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'prim': 'True' if self.value else 'False'}

    def to_python_object(self, lazy_diff=False):
        return self.value


class UnitType(MichelsonType, prim='unit'):

    def __init__(self):
        super(UnitType, self).__init__()

    def __lt__(self, other: 'UnitType'):
        return False

    def __eq__(self, other: 'UnitType'):
        return True

    def __repr__(self):
        return 'Unit'

    @classmethod
    def parse_micheline_value(cls, val_expr):
        parse_micheline_value(val_expr, {('Unit', 0): lambda x: x})
        return cls()

    @classmethod
    def from_python_object(cls, py_obj):
        assert py_obj is None or isinstance(py_obj, unit), f'expected None or Unit, got {type(py_obj).__name__}'
        return cls()

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'prim': 'Unit'}

    def to_python_object(self, lazy_diff=False):
        return unit()


class NeverType(MichelsonType, prim='never'):
    pass
