from pytezos.types.base import MichelsonType


class ParameterType(MichelsonType, prim='parameter', args_len=1):

    def assert_value_defined(self):
        assert isinstance(self.value, MichelsonType)

    def parse_micheline_value(self, val_expr):
        value = self.args[0].parse_micheline_value(val_expr)
        return self.spawn(value)

    def to_micheline_value(self, mode='readable'):
        self.assert_value_defined()
        return {'prim': 'parameter', 'args': [self.value.to_micheline_value(mode=mode)]}

    def parse_python_object(self, py_obj):
        value = self.args[0].parse_python_object(py_obj)
        return self.spawn(value)

    def to_python_object(self):
        self.assert_value_defined()
        return self.value.to_python_object()


class StorageType(MichelsonType, prim='storage', args_len=1):

    def assert_value_defined(self):
        assert isinstance(self.value, MichelsonType)

    def parse_micheline_value(self, val_expr):
        value = self.args[0].parse_micheline_value(val_expr)
        return self.spawn(value)

    def to_micheline_value(self, mode='readable'):
        self.assert_value_defined()
        return {'prim': 'storage', 'args': [self.value.to_micheline_value(mode=mode)]}

    def parse_python_object(self, py_obj):
        value = self.args[0].parse_python_object(py_obj)
        return self.spawn(value)

    def to_python_object(self):
        self.assert_value_defined()
        return self.value.to_python_object()
