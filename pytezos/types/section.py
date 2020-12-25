from typing import List

from pytezos.types.base import MichelsonType, LazyStorage


class ParameterType(MichelsonType, prim='parameter', args_len=1):

    def assert_value_defined(self):
        assert isinstance(self.value, MichelsonType)

    def parse_micheline_value(self, val_expr):
        value = self.type_args[0].parse_micheline_value(val_expr)
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        return {'prim': self.prim, 'args': [self.value.to_micheline_value(mode=mode, lazy_diff=lazy_diff)]}

    def parse_python_object(self, py_obj):
        value = self.type_args[0].parse_python_object(py_obj)
        return self.spawn(value)

    def to_python_object(self, lazy_diff=False):
        self.assert_value_defined()
        return self.value.to_python_object(lazy_diff=lazy_diff)

    def generate_pydoc(self, definitions=None, inferred_name=None):
        definitions = []
        res = self.type_args[0].generate_pydoc(definitions, inferred_name or self.prim)
        if res != f'${self.prim}':
            definitions.insert(0, (self.prim, res))
        return '\n'.join(f'${var}:\n\t{doc}\n' for var, doc in definitions)

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        value = self.value.merge_lazy_diff(lazy_diff)
        return self.spawn(value)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        self.assert_value_defined()
        self.value.aggregate_lazy_diff(lazy_diff, mode=mode)

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action='copy'):
        self.assert_value_defined()
        self.value.attach_lazy_storage(lazy_storage, action=action)

    def __getitem__(self, item):
        self.assert_value_defined()
        return self.value[item]


class StorageType(ParameterType, prim='storage', args_len=1):

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action='remove'):
        self.assert_value_defined()
        self.value.attach_lazy_storage(lazy_storage, action=action)
