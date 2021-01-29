from typing import List, Type

from pytezos.michelson.micheline import MichelsonPrimitive
from pytezos.context.base import NodeContext
from pytezos.michelson.interpreter.stack import MichelsonStack


class CodeSection(MichelsonPrimitive, prim='code', args_len=1):

    @staticmethod
    def match(code_expr) -> Type['CodeSection']:
        cls = MichelsonPrimitive.match(code_expr)
        if not issubclass(cls, CodeSection):
            cls = CodeSection.create_type(args=[cls])
        return cls

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        context.set_code_expr(cls.as_micheline_expr())
