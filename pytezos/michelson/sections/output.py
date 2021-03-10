from typing import List
from typing import Type

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline


class OutputSection(Micheline, prim='output', args_len=1):

    @staticmethod
    def match(output_expr) -> Type['OutputSection']:
        cls = Micheline.match(output_expr)
        if not issubclass(cls, OutputSection):
            cls = OutputSection.create_type(args=[cls])
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_output_expr(cls.as_micheline_expr())
        stdout.append('output: updated')
