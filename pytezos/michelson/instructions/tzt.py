
from typing import List
from typing import Type

from pytezos.context.abstract import AbstractContext
from pytezos.logging import logger
from pytezos.michelson.instructions.base import MichelsonInstruction
from pytezos.michelson.instructions.base import format_stdout
from pytezos.michelson.micheline import MichelineLiteral
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types.base import MichelsonType


class StackEltInstruction(MichelsonInstruction, prim='Stack_elt', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        raise RuntimeError('Stack_elt primitive is used only in TZT tests and cannot be executed directly')

    @classmethod
    def push(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res_type: MichelsonType
        literal: Type[MichelineLiteral]
        res_type, literal = cls.args  # type: ignore
        if not res_type.is_pushable():
            raise Exception(f'{res_type.prim} contains non-pushable arguments')
        res = res_type.from_literal(literal)

        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore

    @classmethod
    def pull(cls, stack: MichelsonStack, stdout: List[str]):
        res_type: MichelsonType
        literal: Type[MichelineLiteral]
        res_type, literal = cls.args  # type: ignore
        res = res_type.from_literal(literal)

        expected_res = stack.pop1()

        if res != expected_res:
            logger.debug('expected: %s(%s)', expected_res.__class__.__name__, expected_res.__dict__)
            logger.debug('actual: %s(%s)', res.__class__.__name__, res.__dict__)
            raise Exception('Stack content is not equal to expected')

        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
