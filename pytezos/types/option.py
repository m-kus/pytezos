from pytezos.types.base import MichelsonType, parse_micheline_value


class OptionType(MichelsonType, prim='option', args_len=1):

    def assert_value_defined(self):
        if isinstance(self.value, type(self.args[0])):
            pass
        elif self.value is None:
            pass
        else:
            assert False, f'expected None or {type(self.args[0]).__name__}, got {type(self.value).__name__}'

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_value(val_expr, {
            ('Some', 1): lambda x: self.args[0].parse_micheline_value(x[0]),
            ('None', 0): lambda x: None
        })
        return self.spawn(value)

    def to_micheline_value(self, mode='readable'):
        self.assert_value_defined()
        if isinstance(self.value, MichelsonType):
            arg = self.value.to_micheline_value(mode=mode)
            return {'prim': 'Some', 'args': [arg]}
        else:
            return {'prim': 'None'}

    def parse_python_object(self, py_obj):
        if py_obj is None:
            value = None
        else:
            value = self.args[0].parse_python_object(py_obj)
        return self.spawn(value)

    def to_python_object(self):
        self.assert_value_defined()
        if isinstance(self.value, MichelsonType):
            return self.value.to_python_object()
        else:
            return None

    def __cmp__(self, other):
        self.assert_value_defined()
        self.assert_equal_types(other)
        assert self.is_comparable(), f'not a comparable type'