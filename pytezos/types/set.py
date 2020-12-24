from typing import Generator, List

from pytezos.types.base import MichelsonType


class SetType(MichelsonType, prim='set', args_len=1):

    def assert_value_defined(self):
        assert isinstance(self.value, list), f'expected list, got {type(self.value).__name__}'

    def assert_item_defined(self, item):
        assert isinstance(item, type(self.type_args[0])), \
            f'invalid element type: expected {type(self.type_args[0]).__name__}, got {type(item).__name__}'

    def __len__(self):
        self.assert_value_defined()
        return len(self.value)

    def __iter__(self) -> Generator[MichelsonType, None, None]:
        self.assert_value_defined()
        for item in self.value:
            self.assert_item_defined(item)
            yield item

    def contains(self, item: MichelsonType) -> bool:
        self.assert_value_defined()
        self.assert_item_defined(item)
        return item in self.value

    def add(self, item: MichelsonType) -> MichelsonType:
        self.assert_value_defined()
        self.assert_item_defined(item)
        if item in self.value:
            return self
        else:
            return self.spawn(list(sorted([item] + self.value)))

    def remove(self, item: MichelsonType) -> MichelsonType:
        self.assert_value_defined()
        self.assert_item_defined(item)
        if item in self.value:
            return self.spawn(list(filter(lambda x: x != item, self.value)))
        else:
            return self

    def parse_micheline_value(self, val_expr):
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'
        value = list(map(self.type_args[0].parse_micheline_value, val_expr))
        assert len(set(value)) == len(value), f'duplicate elements found'
        assert value == list(sorted(value)), f'set values are unsorted'
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return list(map(lambda x: x.to_micheline_value(mode=mode, lazy_diff=lazy_diff), self))

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, set), f'expected set, got {type(py_obj).__name__}'
        value = list(map(self.type_args[0].parse_python_object, py_obj))
        value = list(sorted(value))
        return self.spawn(value)

    def to_python_object(self, lazy_diff=False):
        return list(map(lambda x: x.to_python_object(lazy_diff=lazy_diff), self))

    def generate_pydoc(self, definitions: list, inferred_name=None):
        name = self.field_name or self.type_name or inferred_name
        arg_doc = self.type_args[0].generate_pydoc(definitions, inferred_name=f'{name}_item' if name else None)
        return f'{{ {arg_doc}, ... }}'

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        value = [item.merge_lazy_diff(lazy_diff) for item in self]
        return self.spawn(value)

    def aggregate_lazy_diff(self, lazy_diff: List[dict]):
        for item in self:
            item.aggregate_lazy_diff(lazy_diff)

    def __contains__(self, py_obj):
        key = self.type_args[0].parse_python_object(py_obj)
        return self.contains(key)
