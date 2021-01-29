from typing import Type, List

from pytezos.michelson.micheline import MichelsonPrimitive
from pytezos.michelson.types.base import MichelsonType
from pytezos.context.base import NodeContext
from pytezos.michelson.interpreter.stack import MichelsonStack


class StorageSection(MichelsonPrimitive, prim='storage', args_len=1):

    def __init__(self, item: MichelsonType):
        super(MichelsonPrimitive, self).__init__()
        self.item = item

    def __repr__(self):
        return repr(self.item)

    @staticmethod
    def match(type_expr) -> Type['StorageSection']:
        cls = MichelsonPrimitive.match(type_expr)
        if not issubclass(cls, StorageSection):
            cls = StorageSection.create_type(args=[cls])
        return cls

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        context.set_storage_expr(cls.as_micheline_expr())

    @classmethod
    def generate_pydoc(cls) -> str:
        definitions = []
        res = cls.args[0].generate_pydoc(definitions, cls.prim)
        if res != f'${cls.prim}':
            definitions.insert(0, (cls.prim, res))
        return '\n'.join(f'${var}:\n\t{doc}\n' for var, doc in definitions)

    @classmethod
    def dummy(cls, context: NodeContext):
        return cls(cls.args[0].dummy(context))

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'StorageSection':
        item = cls.args[0].from_micheline_value(val_expr)
        return cls(item)

    @classmethod
    def from_python_object(cls, py_obj) -> 'StorageSection':
        item = cls.args[0].from_python_object(py_obj)
        return cls(item)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return self.item.to_micheline_value(mode=mode, lazy_diff=lazy_diff)

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.item.to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff)

    def attach_context(self, context: NodeContext):
        self.item.attach_context(context)

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'StorageSection':
        item = self.item.merge_lazy_diff(lazy_diff)
        return type(self)(item)

    def aggregate_lazy_diff(self, mode='readable') -> List[dict]:
        lazy_diff = list()
        self.item.aggregate_lazy_diff(lazy_diff, mode=mode)
        return lazy_diff
