from typing import List, Optional

from pytezos.types.base import MichelsonType, parse_micheline_value, LazyStorage


class OptionType(MichelsonType, prim='option', args_len=1):

    def __init__(self, item: Optional[MichelsonType]):
        super(OptionType, self).__init__()
        self.item = item

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

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if self.item is None:
            return {'prim': 'None'}
        else:
            arg = self.item.to_micheline_value(mode=mode, lazy_diff=lazy_diff)
            return {'prim': 'Some', 'args': [arg]}

    def to_python_object(self, lazy_diff=False):
        if self.item is None:
            return None
        else:
            return self.item.to_python_object(lazy_diff=lazy_diff)

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        if self.item is None:
            item = None
        else:
            item = self.item.merge_lazy_diff(lazy_diff)
        return type(self)(item)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        if self.item is not None:
            self.item.aggregate_lazy_diff(lazy_diff)

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action: str):
        if self.item is not None:
            self.item.attach_lazy_storage(lazy_storage, action=action)

    def __cmp__(self, other: 'OptionType'):
        raise NotImplementedError  # TODO
