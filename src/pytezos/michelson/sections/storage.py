from typing import List, Type

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline, MichelsonRuntimeError
from pytezos.michelson.types import *


class StorageSection(Micheline, prim='storage', args_len=1):
    args: List[Type[MichelsonType]]  # type: ignore

    def __init__(self, item: MichelsonType):
        super().__init__()
        self.item = item

    def __repr__(self):
        return repr(self.item)

    @staticmethod
    def match(type_expr) -> Type['StorageSection']:
        try:
            cls = Micheline.match(type_expr)
            if not issubclass(cls, StorageSection):
                cls = StorageSection.create_type(args=[cls])
            assert cls.args[0].field_name is None, f'argument type cannot be annotated: %{cls.args[0].field_name}'  # type: ignore
        except Exception as e:
            raise MichelsonRuntimeError('storage', *e.args) from e
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_storage_expr(cls.as_micheline_expr())
        stdout.append('storage: updated')

    @classmethod
    def generate_pydoc(cls) -> str:
        definitions = []  # type: ignore
        res = cls.args[0].generate_pydoc(definitions, cls.prim)
        if res != f'${cls.prim}':
            definitions.insert(0, (cls.prim, res))
        return '\n'.join(f'${var}:\n\t{doc}\n' for var, doc in definitions)

    @classmethod
    def dummy(cls, context: AbstractContext):
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

    def attach_context(self, context: AbstractContext):
        self.item.attach_context(context)

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'StorageSection':
        item = self.item.merge_lazy_diff(lazy_diff)
        return type(self)(item)

    def aggregate_lazy_diff(self, mode='readable') -> List[dict]:
        lazy_diff = []  # type: ignore
        self.item.aggregate_lazy_diff(lazy_diff, mode=mode)
        return lazy_diff
