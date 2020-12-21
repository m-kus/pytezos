from pytezos.types.base import MichelsonType


class ListType(MichelsonType, prim='list', args_len=1):

    def assert_value_defined(self):
        assert isinstance(self.value, list), f'value is undefined'
        for element in self.value:
            assert isinstance(element, type(self.args[0])),  \
                f'invalid element type: expected {type(self.args[0]).__name__}, got {type(element).__name__}'

    def parse_micheline_value(self, val_expr):
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'
        value = list(map(self.args[0].parse_micheline_value, val_expr))
        return self.spawn(value)

    def to_micheline_value(self, mode='readable'):
        self.assert_value_defined()
        return list(map(lambda x: x.to_micheline_value(mode=mode), self.value))

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, list), f'expected list, got {type(py_obj).__name__}'
        value = list(map(self.args[0].parse_python_object, py_obj))
        return self.spawn(value)

    def to_python_object(self):
        self.assert_value_defined()
        return list(map(lambda x: x.to_python_object(), self.value))