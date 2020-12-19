from pytezos.types.base import MichelsonType, parse_micheline_literal, parse_micheline_value, unit

Unit = unit()


class StringType(MichelsonType, prim='string'):

    def assert_value_defined(self):
        assert isinstance(self.value, str), f'value is undefined'

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_literal(val_expr, {'string': str})
        assert len(value) == len(value.encode()), f'unicode symbols are not allowed: {val_expr}'
        return self.spawn(value)

    def to_micheline_value(self, mode='optimized'):
        self.assert_value_defined()
        return {'string': self.value}

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, str), f'expected string, got {type(py_obj).__name__}'
        assert len(py_obj) == len(py_obj.encode()), f'unicode symbols are not allowed: {py_obj}'
        return self.spawn(py_obj)

    def to_python_object(self):
        self.assert_value_defined()
        return self.value


class IntType(MichelsonType, prim='int'):

    def assert_value_defined(self):
        assert isinstance(self.value, int), f'value is undefined'

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_literal(val_expr, {'int': int})
        return self.spawn(value)

    def to_micheline_value(self, mode='optimized'):
        self.assert_value_defined()
        return {'int': str(self.value)}

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, int), f'expected integer, got {type(py_obj).__name__}'
        return self.spawn(py_obj)

    def to_python_object(self):
        self.assert_value_defined()
        return self.value


class NatType(IntType, prim='nat'):

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_literal(val_expr, {'int': int})
        assert value >= 0, f'expected natural number, got {value}'
        return self.spawn(value)

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, int), f'expected integer, got {type(py_obj).__name__}'
        assert py_obj >= 0, f'expected natural number, got {py_obj}'
        return self.spawn(py_obj)


class BytesType(MichelsonType, prim='bytes'):

    def assert_value_defined(self):
        assert isinstance(self.value, bytes), f'value is undefined'

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_literal(val_expr, {'bytes': bytes.fromhex})
        return self.spawn(value)

    def to_micheline_value(self, mode='optimized'):
        self.assert_value_defined()
        return {'bytes': self.value.hex()}

    def parse_python_object(self, py_obj):
        if isinstance(py_obj, bytes):
            value = py_obj
        elif isinstance(py_obj, str):
            if py_obj.startswith('0x'):
                py_obj = py_obj[2:]
            value = bytes.fromhex(py_obj)
        else:
            assert False, f'unexpected value type {py_obj}'
        return self.spawn(value)

    def to_python_object(self):
        self.assert_value_defined()
        return self.value


class BoolType(MichelsonType, prim='bool'):

    def assert_value_defined(self):
        assert isinstance(self.value, bool), f'value is undefined'

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_value(val_expr, {
            ('False', 0): lambda x: False,
            ('True', 0): lambda x: True
        })
        return self.spawn(value)

    def to_micheline_value(self, mode='optimized'):
        self.assert_value_defined()
        return {'prim': 'True' if self.value else 'False'}

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, bool), f'expected boolean, got {type(py_obj).__name__}'
        return self.spawn(py_obj)

    def to_python_object(self):
        self.assert_value_defined()
        return self.value


class UnitType(MichelsonType, prim='unit'):

    def assert_value_defined(self):
        assert isinstance(self.value, unit), f'value is undefined'

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_value(val_expr, {('Unit', 0): lambda x: unit()})
        return self.spawn(value)

    def to_micheline_value(self, mode='optimized'):
        self.assert_value_defined()
        return {'prim': 'Unit'}

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, unit), f'expected Unit, got {type(py_obj).__name__}'
        return self.spawn(py_obj)

    def to_python_object(self):
        self.assert_value_defined()
        return self.value

    def __cmp__(self, other):
        self.assert_value_defined()
        self.assert_equal_types(other)
        return 0
