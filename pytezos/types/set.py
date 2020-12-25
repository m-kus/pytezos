from typing import Generator, List
from copy import copy

from pytezos.types.base import MichelsonType, LazyStorage


class SetType(MichelsonType, prim='set', args_len=1):

    def __init__(self, items: List[MichelsonType]):
        super(SetType, self).__init__()
        self.items = items

    def __len__(self):
        return len(self.items)

    def __iter__(self) -> Generator[MichelsonType, None, None]:
        yield from iter(self.items)

    @classmethod
    def from_micheline_value(cls, val_expr):
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'
        items = list(map(cls.type_args[0].from_micheline_value, val_expr))
        assert len(set(items)) == len(items), f'duplicate elements found'
        assert items == list(sorted(items)), f'set values are unsorted'
        return cls(items)

    @classmethod
    def from_python_object(cls, py_obj):
        assert isinstance(py_obj, set), f'expected set, got {type(py_obj).__name__}'
        items = list(map(cls.type_args[0].from_python_object, py_obj))
        items = list(sorted(items))
        return cls(items)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return list(map(lambda x: x.to_micheline_value(mode=mode, lazy_diff=lazy_diff), self))

    def to_python_object(self, lazy_diff=False):
        return list(map(lambda x: x.to_python_object(lazy_diff=lazy_diff), self))

    def generate_pydoc(self, definitions: list, inferred_name=None):
        name = self.field_name or self.type_name or inferred_name
        arg_doc = self.type_args[0].generate_pydoc(definitions, inferred_name=f'{name}_item' if name else None)
        return f'{{ {arg_doc}, ... }}'

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        return copy(self)  # Big_map is not comparable

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        pass  # Big_map is not comparable

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action: str):
        pass  # Big_map is not comparable

    def contains(self, item: MichelsonType) -> bool:
        assert isinstance(item, self.type_args[0]), f'expected {self.type_args[0].__name__}, got {type(item).__name__}'
        return item in self.items

    def add(self, item: MichelsonType) -> MichelsonType:
        if self.contains(item):
            return copy(self)
        else:
            items = [item] + self.items
            return type(self)(list(sorted(items)))

    def remove(self, item: MichelsonType) -> MichelsonType:
        if self.contains(item):
            items = list(filter(lambda x: x != item, self.items))
            return type(self)(items)
        else:
            return copy(self)

    def __contains__(self, py_obj):
        key = self.type_args[0].from_python_object(py_obj)
        return self.contains(key)
