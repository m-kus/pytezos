from typing import Type, cast, List

from pytezos.michelson.types.base import MichelsonType
from pytezos.context.base import NodeContext


class StorageType(MichelsonType, prim='storage', args_len=1):

    def __init__(self, item: MichelsonType):
        super(MichelsonType, self).__init__()
        self.item = item

    def __repr__(self):
        return repr(self.item)

    @staticmethod
    def match(type_expr) -> Type['StorageType']:
        return cast(Type['StorageType'], MichelsonType.match(type_expr))

    @classmethod
    def generate_pydoc(cls, definitions=None, inferred_name=None):
        definitions = []
        res = cls.args[0].generate_pydoc(definitions, inferred_name or cls.prim)
        if res != f'${cls.prim}':
            definitions.insert(0, (cls.prim, res))
        return '\n'.join(f'${var}:\n\t{doc}\n' for var, doc in definitions)

    @classmethod
    def dummy(cls):
        return cls(cls.args[0].dummy())

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'StorageType':
        item = cls.args[0].from_micheline_value(val_expr)
        return cls(item)

    @classmethod
    def from_python_object(cls, py_obj) -> 'StorageType':
        item = cls.args[0].from_python_object(py_obj)
        return cls(item)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return self.item.to_micheline_value(mode=mode, lazy_diff=lazy_diff)

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.item.to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff)

    def attach_context(self, context: NodeContext):
        super(StorageType, self).attach_context(context)

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'StorageType':
        item = self.item.merge_lazy_diff(lazy_diff)
        return type(self)(item)

    def aggregate_lazy_diff(self, lazy_diff: List[dict] = (), mode='readable'):
        lazy_diff = list()
        self.item.aggregate_lazy_diff(lazy_diff, mode=mode)
        return lazy_diff

    def __getitem__(self, key):
        assert hasattr(self.item, '__getitem__'), f'index access is not implemented for {self.item.prim}'
        return self.item[key]
