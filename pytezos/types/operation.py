from pytezos.types.base import MichelsonType


class OperationType(MichelsonType, prim='operation'):

    def assert_value_defined(self):
        pass

    def parse_micheline_value(self, val_expr):
        assert False, 'forbidden'

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        assert False, 'forbidden'

    def parse_python_object(self, py_obj):
        pass

    def to_python_object(self, lazy_diff=False):
        pass
