from typing import Tuple, Generator, List

from pytezos.types.base import MichelsonType


class ListType(MichelsonType, prim='list', args_len=1):

    def assert_value_defined(self):
        assert isinstance(self.value, list), f'expected list, got {type(self.value).__name__}'

    def assert_item_defined(self, item):
        assert isinstance(item, type(self.type_args[0])), \
            f'invalid element type: expected {type(self.type_args[0]).__name__}, got {type(item).__name__}'
        item.assert_value_defined()

    def __len__(self):
        self.assert_value_defined()
        return len(self.value)

    def __iter__(self) -> Generator[MichelsonType, None, None]:
        self.assert_value_defined()
        for item in self.value:
            self.assert_item_defined(item)
            yield item

    def split_head(self) -> Tuple[MichelsonType, 'ListType']:
        assert len(self) > 0, f'cannot split empty list'
        head = self.value[0]
        tail = self.spawn(self.value[1:])
        self.assert_item_defined(head)
        return head, tail

    def prepend(self, item: MichelsonType) -> 'ListType':
        self.assert_value_defined()
        self.assert_item_defined(item)
        return self.spawn([item] + self.value)

    def parse_micheline_value(self, val_expr: list) -> 'ListType':
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'
        value = list(map(self.type_args[0].parse_micheline_value, val_expr))
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return list(map(lambda x: x.to_micheline_value(mode=mode, lazy_diff=lazy_diff), self))

    def parse_python_object(self, py_obj) -> 'ListType':
        assert isinstance(py_obj, list), f'expected list, got {type(py_obj).__name__}'
        value = list(map(self.type_args[0].parse_python_object, py_obj))
        return self.spawn(value)

    def to_python_object(self, lazy_diff=False):
        return list(map(lambda x: x.to_python_object(lazy_diff=lazy_diff), self))

    def generate_pydoc(self, definitions: List[Tuple[str, str]], inferred_name=None):
        name = self.field_name or self.type_name or inferred_name
        arg_doc = self.type_args[0].generate_pydoc(definitions, inferred_name=f'{name}_item' if name else None)
        return f'[ {arg_doc}, ... ]'

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        value = [item.merge_lazy_diff(lazy_diff) for item in self]
        return self.spawn(value)

    def aggregate_lazy_diff(self, lazy_diff: List[dict]):
        for item in self:
            item.aggregate_lazy_diff(lazy_diff)

    def __getitem__(self, idx: int) -> MichelsonType:
        self.assert_value_defined()
        if isinstance(idx, int):
            assert idx < len(self.value), f'index out of bounds: {idx} >= {len(self.value)}'
            item = self.value[idx]
            self.assert_item_defined(item)
            return item
        else:
            assert False, f'expected int, got {type(idx).__name__}'
