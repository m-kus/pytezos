from typing import List, Type

from pytezos.michelson.micheline import MichelsonPrimitive
from pytezos.context.execution import ExecutionContext


class CodeSection(MichelsonPrimitive, prim='code', args_len=1):

    @staticmethod
    def match(code_expr) -> Type['CodeSection']:
        cls = MichelsonPrimitive.match(code_expr)
        if not issubclass(cls, CodeSection):
            cls = CodeSection.create_type(args=[cls])
        return cls

    @classmethod
    def execute(cls, stack, stdout: List[str], context: ExecutionContext):
        context.set_code_expr(cls.as_micheline_expr())
        stdout.append(f'code: updated')
