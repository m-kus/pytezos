from typing import List, Type

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline


class CodeSection(Micheline, prim='code', args_len=1):

    @staticmethod
    def match(code_expr) -> Type['CodeSection']:
        cls = Micheline.match(code_expr)
        if not issubclass(cls, CodeSection):
            cls = CodeSection.create_type(args=[cls])
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_code_expr(cls.as_micheline_expr())
        stdout.append(f'code: updated')
