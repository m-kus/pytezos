from pytezos.types.base import MichelsonType


class PairType(MichelsonType, prim='pair', args_len=None):

    def assert_value_defined(self):
        assert isinstance(self.value, list), f'value is undefined'

    def parse_micheline_value(self, val_expr):
        pass

    def to_micheline_value(self, mode='optimized'):
        pass

    def parse_python_object(self, py_obj):
        pass

    def to_python_object(self):
        pass
