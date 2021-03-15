from copy import copy
from typing import Generator, List, Type

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline, MichelineSequence
from pytezos.michelson.types.base import MichelsonType


class SetType(MichelsonType, prim='set', args_len=1):

    def __init__(self, items: List[MichelsonType]):
        super(SetType, self).__init__()
        self.items = items

    def __repr__(self):
        return f'{{{", ".join(map(repr, self.items))}}}'

    def __len__(self):
        return len(self.items)

    def __iter__(self) -> Generator[MichelsonType, None, None]:
        yield from iter(self.items)

    def __eq__(self, other) -> bool:
        if not isinstance(other, SetType):
            return False
        return self.items == other.items

    @staticmethod
    def empty(item_type: Type[MichelsonType]) -> 'SetType':
        cls = SetType.create_type(args=[item_type])
        return cls(items=[])  # type: ignore

    @staticmethod
    def from_items(items: List[MichelsonType]) -> 'SetType':
        assert len(items) > 0, 'cannot instantiate from empty list'
        item_type = items[0].get_anon_type()
        for item in items[1:]:
            item_type.assert_type_equal(type(item))
        cls = SetType.create_type(args=[item_type])
        cls.check_constraints(items)  # type: ignore
        return cls(items)  # type: ignore

    @classmethod
    def check_constraints(cls, items: List[MichelsonType]):
        assert len(set(items)) == len(items), f'duplicate elements found'
        assert items == list(sorted(items)), f'set elements are not sorted'

    @classmethod
    def dummy(cls, context: AbstractContext):
        return cls([])

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'SetType':
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'
        items = list(map(cls.args[0].from_micheline_value, val_expr))
        cls.check_constraints(items)
        return cls(items)

    @classmethod
    def from_python_object(cls, py_obj) -> 'SetType':
        if isinstance(py_obj, list):
            py_set = set(py_obj)
            assert len(py_set) == len(py_obj), f'found duplicates'
        else:
            assert isinstance(py_obj, set), f'expected set or list, got {type(py_obj).__name__}'
            py_set = py_obj
        items = list(map(cls.args[0].from_python_object, py_set))
        items = list(sorted(items))
        return cls(items)

    def to_literal(self) -> Type[Micheline]:
        return MichelineSequence.create_type(args=[item.to_literal() for item in self.items])

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return list(map(lambda x: x.to_micheline_value(mode=mode, lazy_diff=lazy_diff), self))

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        assert not comparable, f'{self.prim} is not comparable'
        return list(map(lambda x: x.to_python_object(try_unpack=try_unpack,
                                                     lazy_diff=lazy_diff,
                                                     comparable=True), self))

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None, comparable=False):
        name = cls.field_name or cls.type_name or inferred_name
        arg_doc = cls.args[0].generate_pydoc(definitions,
                                             inferred_name=f'{name}_item' if name else None,
                                             comparable=True)
        return f'{{ {arg_doc}, … }}'

    def contains(self, item: MichelsonType) -> bool:
        self.args[0].assert_type_equal(type(item))
        return item in self.items

    def add(self, item: MichelsonType) -> 'SetType':
        if self.contains(item):
            return copy(self)
        else:
            items = [item] + self.items
            return type(self)(list(sorted(items)))

    def remove(self, item: MichelsonType) -> 'SetType':
        if self.contains(item):
            items = list(filter(lambda x: x != item, self.items))
            return type(self)(items)
        else:
            return copy(self)

    def __contains__(self, py_obj):
        key = self.args[0].from_python_object(py_obj)
        return self.contains(key)
