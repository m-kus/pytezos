from typing import Any, List, Optional, Type, Union, cast

from pytezos.context.abstract import AbstractContext
from pytezos.michelson.micheline import Micheline, MichelineLiteral, MichelsonRuntimeError
from pytezos.michelson.types.base import MichelsonType


class ViewSection(Micheline, prim='view', args_len=4):
    """
    Syntax: view {name} {arg_type} {ret_type} {code}
    """
    args: List[Type[MichelsonType]]  # type: ignore
    name: str

    def __init__(self, item: MichelsonType):
        super().__init__()
        self.item = item

    def __repr__(self):
        return repr(self.item)

    @staticmethod
    def match(type_expr) -> Type['ViewSection']:
        try:
            cls = Micheline.match(type_expr)
            if not issubclass(cls, ViewSection):
                cls = ViewSection.create_type(args=[cls])
        except Exception as e:
            raise MichelsonRuntimeError('view', *e.args) from e
        return cls

    @classmethod
    def create_type(cls,
                    args: List[Union[Type['Micheline'], Any]],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['ViewSection']:
        view_name = cast(Type[MichelineLiteral], args[0])
        if not issubclass(view_name, MichelineLiteral):
            raise MichelsonRuntimeError('view', 'Expected view name as first argument', view_name)
        name = view_name.get_string()
        if len(name) >= 32:
            # TODO: also check for denied symbols
            raise MichelsonRuntimeError('view', f'Too long view name {view_name}')

        res = type(cls.__name__, (cls,), dict(args=args, name=name, **kwargs))
        return cast(Type['ViewSection'], res)

    @classmethod
    def generate_pydoc(cls) -> str:
        definitions = []  # type: ignore
        return cls.args[1].generate_pydoc(definitions, cls.prim)
