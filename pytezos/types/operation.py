from pytezos.types.base import MichelsonType


class OperationType(MichelsonType, prim='operation'):

    def __init__(self, value):
        super(OperationType, self).__init__()
        self.value = value

    @classmethod
    def from_micheline_value(cls, val_expr):
        assert False, 'forbidden'

    @classmethod
    def from_python_object(cls, py_obj) -> 'OperationType':
        pass

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        assert False, 'forbidden'

    def to_python_object(self, lazy_diff=False):
        pass
