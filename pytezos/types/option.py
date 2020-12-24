from typing import List

from pytezos.types.base import MichelsonType, parse_micheline_value


class OptionType(MichelsonType, prim='option', args_len=1):

    def assert_value_defined(self):
        assert self.value is None or isinstance(self.value, type(self.type_args[0])), \
            f'expected None or {type(self.type_args[0]).__name__}, got {type(self.value).__name__}'

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_value(val_expr, {
            ('Some', 1): lambda x: self.type_args[0].parse_micheline_value(x[0]),
            ('None', 0): lambda x: None
        })
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        if isinstance(self.value, MichelsonType):
            arg = self.value.to_micheline_value(mode=mode, lazy_diff=lazy_diff)
            return {'prim': 'Some', 'args': [arg]}
        else:
            return {'prim': 'None'}

    def parse_python_object(self, py_obj):
        if py_obj is None:
            value = None
        else:
            value = self.type_args[0].parse_python_object(py_obj)
        return self.spawn(value)

    def to_python_object(self, lazy_diff=False):
        self.assert_value_defined()
        if isinstance(self.value, MichelsonType):
            return self.value.to_python_object(lazy_diff=lazy_diff)
        else:
            return None

    def __cmp__(self, other):
        self.assert_value_defined()
        self.assert_equal_types(other)
        assert self.is_comparable(), f'not a comparable type'

    def generate_pydoc(self, definitions: list, inferred_name=None):
        name = self.field_name or self.type_name or inferred_name
        arg_doc = self.type_args[0].generate_pydoc(definitions, inferred_name=name)
        return f'{arg_doc} || None'

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        self.assert_value_defined()
        if self.value is None:
            value = None
        else:
            value = self.value.merge_lazy_diff(lazy_diff)
        return self.spawn(value)

    def aggregate_lazy_diff(self, lazy_diff: List[dict]):
        self.assert_value_defined()
        if self.value is not None:
            self.value.aggregate_lazy_diff(lazy_diff)
