from typing import List
from typing import Type

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline


class InputSection(Micheline, prim='input', args_len=1):

    @staticmethod
    def match(input_expr) -> Type['InputSection']:
        cls = Micheline.match(input_expr)
        if not issubclass(cls, InputSection):
            cls = InputSection.create_type(args=[cls])
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_input_expr(cls.as_micheline_expr())
        stdout.append('input: updated')
