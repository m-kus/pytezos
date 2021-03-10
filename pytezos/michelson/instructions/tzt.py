
from pytezos.michelson.types.core import IntType, NatType
from pytezos.context.abstract import AbstractContext
from typing import List
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.instructions.base import MichelsonInstruction


class StackEltInstruction(MichelsonInstruction, prim='Stack_elt', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res_type, literal = cls.args
        assert res_type.is_pushable(), f'{res_type.prim} contains non-pushable arguments'
        res = res_type.from_literal(literal)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls()
