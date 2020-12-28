from typing import List, Type, cast

from pytezos.types.base import MichelsonType, LazyStorage


class SectionType(MichelsonType):

    def __init__(self, item: MichelsonType):
        super(SectionType, self).__init__()
        self.item = item

    def __repr__(self):
        return repr(self.item)

    @staticmethod
    def match(type_expr) -> Type['SectionType']:
        return cast(Type['SectionType'], MichelsonType.match(type_expr))

    @classmethod
    def generate_pydoc(cls, definitions=None, inferred_name=None):
        definitions = []
        res = cls.type_args[0].generate_pydoc(definitions, inferred_name or cls.prim)
        if res != f'${cls.prim}':
            definitions.insert(0, (cls.prim, res))
        return '\n'.join(f'${var}:\n\t{doc}\n' for var, doc in definitions)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'MichelsonType':
        item = cls.type_args[0].from_micheline_value(val_expr)
        return cls(item)

    @classmethod
    def from_python_object(cls, py_obj) -> 'MichelsonType':
        item = cls.type_args[0].from_python_object(py_obj)
        return cls(item)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return {'prim': self.prim, 'args': [self.item.to_micheline_value(mode=mode, lazy_diff=lazy_diff)]}

    def to_python_object(self, lazy_diff=False):
        return self.item.to_python_object(lazy_diff=lazy_diff)

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        item = self.item.merge_lazy_diff(lazy_diff)
        return type(self)(item)

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action: str):
        self.item.attach_lazy_storage(lazy_storage, action=action)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        self.item.aggregate_lazy_diff(lazy_diff, mode=mode)

    def __getitem__(self, key):
        assert hasattr(self.item, '__getitem__'), f'index access is not implemented for {self.item.prim}'
        return self.item[key]


class ParameterType(SectionType, prim='parameter', args_len=1):

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action='copy'):
        super(ParameterType, self).attach_lazy_storage(lazy_storage, action)


class StorageType(SectionType, prim='storage', args_len=1):

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action='remove'):
        super(StorageType, self).attach_lazy_storage(lazy_storage, action)
