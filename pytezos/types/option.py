from typing import List, Optional, Type

from pytezos.types.base import MichelsonType, parse_micheline_value, LazyStorage


class OptionType(MichelsonType, prim='option', args_len=1):

    def __init__(self, item: Optional[MichelsonType]):
        super(OptionType, self).__init__()
        self.item = item

    def __lt__(self, other: 'OptionType') -> bool:
        if other.item is None:
            return False
        elif self.item is None:
            return True
        else:
            return self.item < other.item

    def __eq__(self, other: 'OptionType') -> bool:
        return self.item == other.item

    def __repr__(self):
        return f'{repr(self.item)}!' if self.item else 'None'

    @staticmethod
    def none(some_type: Type[MichelsonType]) -> 'OptionType':
        cls = OptionType.construct_type(type_args=[some_type])
        return cls(None)

    @staticmethod
    def from_some(item: MichelsonType) -> 'OptionType':
        cls = OptionType.construct_type(type_args=[type(item)])
        return cls(item)

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None):
        name = cls.field_name or cls.type_name or inferred_name
        arg_doc = cls.type_args[0].generate_pydoc(definitions, inferred_name=name)
        return f'{arg_doc} || None'

    @classmethod
    def from_micheline_value(cls, val_expr):
        item = parse_micheline_value(val_expr, {
            ('Some', 1): lambda x: cls.type_args[0].from_micheline_value(x[0]),
            ('None', 0): lambda x: None
        })
        return cls(item)

    @classmethod
    def from_python_object(cls, py_obj):
        if py_obj is None:
            item = None
        else:
            item = cls.type_args[0].from_python_object(py_obj)
        return cls(item)

    def is_none(self) -> bool:
        return self.item is None

    def get_some(self) -> MichelsonType:
        assert not self.is_none()
        return self.item

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if self.is_none():
            return {'prim': 'None'}
        else:
            arg = self.item.to_micheline_value(mode=mode, lazy_diff=lazy_diff)
            return {'prim': 'Some', 'args': [arg]}

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        if self.is_none():
            return None
        else:
            return self.item.to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff)

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        if self.is_none():
            item = None
        else:
            item = self.item.merge_lazy_diff(lazy_diff)
        return type(self)(item)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        if not self.is_none():
            self.item.aggregate_lazy_diff(lazy_diff)

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action: str):
        if not self.is_none():
            self.item.attach_lazy_storage(lazy_storage, action=action)
