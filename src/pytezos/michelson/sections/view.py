from typing import Any
from typing import List
from typing import Optional
from typing import Type
from typing import Union
from typing import cast

from pytezos.context.abstract import AbstractContext
from pytezos.michelson.micheline import Micheline
from pytezos.michelson.micheline import MichelineLiteral
from pytezos.michelson.micheline import MichelsonRuntimeError
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

    @staticmethod
    def check_code(code: Type['Micheline'], lambda_: bool) -> None:
        if code.prim == 'SELF':
            raise MichelsonRuntimeError('view', f'{code.prim} is not allowed in views')
        if code.prim in ('CREATE_CONTRACT', 'SET_DELEGATE', 'TRANSFER_TOKENS') and not lambda_:
            raise MichelsonRuntimeError('view', f'{code.prim} is not allowed in views')

        lambda_ |= code.prim in ('LAMBDA', 'lambda')
        for arg in getattr(code, 'args', ()):
            ViewSection.check_code(arg, lambda_)

    @classmethod
    def create_type(
        cls,
        args: List[Union[Type['Micheline'], Any]],
        annots: Optional[list] = None,
        **kwargs,
    ) -> Type['ViewSection']:
        view_name = cast(Type[MichelineLiteral], args[0])
        if not issubclass(view_name, MichelineLiteral):
            raise MichelsonRuntimeError('view', 'Expected view name as first argument', view_name)
        name = view_name.get_string()
        if len(name) >= 32:
            # TODO: also check for denied symbols
            raise MichelsonRuntimeError('view', f'Too long view name {view_name}')

        # NOTE: Check for opcodes forbidden in views
        cls.check_code(args[3], lambda_=False)

        res = type(cls.__name__, (cls,), dict(args=args, name=name, **kwargs))
        return cast(Type['ViewSection'], res)

    @classmethod
    def generate_pydoc(cls) -> str:
        definitions = []  # type: ignore
        return cls.args[1].generate_pydoc(definitions, cls.prim)
