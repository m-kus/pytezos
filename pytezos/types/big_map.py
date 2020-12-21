from pytezos.types.base import parse_micheline_literal
from pytezos.types.map import MapType


class BigMapType(MapType, prim='big_map', args_len=2):

    def assert_value_defined(self):
        if isinstance(self.value, int):
            pass
        else:
            super(BigMapType, self).assert_value_defined()

    def parse_micheline_value(self, val_expr):
        if isinstance(val_expr, dict):
            value = parse_micheline_literal(val_expr, {'int': int})
            return self.spawn(value)
        else:
            return super(BigMapType, self).parse_micheline_value(val_expr)

    def to_micheline_value(self, mode='readable'):
        if isinstance(self.value, int):
            return {'int': str(self.value)}
        else:
            return super(BigMapType, self).to_micheline_value(mode=mode)

    def parse_python_object(self, py_obj):
        if isinstance(py_obj, int):
            return self.spawn(py_obj)
        else:
            return super(BigMapType, self).parse_python_object(py_obj)

    def to_python_object(self):
        if isinstance(self.value, int):
            return self.value
        else:
            return super(BigMapType, self).to_python_object()

