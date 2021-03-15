
from typing import List, Type, cast

from pytezos.context.abstract import AbstractContext
from pytezos.logging import logger
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.micheline import MichelineLiteral, MichelineSequence
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.types.big_map import BigMapType


class StackEltInstruction(MichelsonInstruction, prim='Stack_elt', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        raise RuntimeError('`Stack_elt` primitive is used only in TZT tests and cannot be executed directly')

    @classmethod
    def push(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res_type: MichelsonType
        literal: Type[MichelineLiteral]
        res_type, literal = cls.args  # type: ignore
        if res_type.prim == 'big_map':
            if isinstance(literal.literal, int):
                res = context.tzt_big_maps[literal.literal]  # type: ignore
            else:
                res = res_type.from_literal(literal)
                res.attach_context(context)
        elif res_type.is_pushable():
            res = res_type.from_literal(literal)
        else:
            raise Exception(f'`{res_type.prim}` is neither pushable nor big_map')

        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore

    @classmethod
    def pull(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res_type: MichelsonType
        literal: Type[MichelineLiteral]
        res_type, literal = cls.args  # type: ignore
        res = res_type.from_literal(literal)
        if res_type.is_pushable():
            expected_res = stack.pop1()
        elif res_type.prim == 'big_map':
            if issubclass(literal, MichelineSequence):
                expected_res = stack.pop1()
            else:
                expected_res = stack.pop1()
                # NOTE: We care about validity of the pointer, not it's contents
                res = expected_res
        else:
            raise Exception(f'`{res_type.prim}` is neither pushable nor big_map')

        if res != expected_res:
            logger.debug('expected: %s(%s)', expected_res.__class__.__name__, expected_res.__dict__)
            logger.debug('actual: %s(%s)', res.__class__.__name__, res.__dict__)
            raise Exception('Stack content is not equal to expected')

        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore


class BigMapInstruction(MichelsonInstruction, prim='Big_map', args_len=4):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        raise RuntimeError('`Big_map` primitive is used only in TZT tests and cannot be executed directly')

    @classmethod
    def add(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res_type: MichelsonType
        key_type: Type[MichelsonType]
        value_type: Type[MichelsonType]
        literal: Type[MichelineLiteral]
        res_type, key_type, value_type, literal = cls.args  # type: ignore

        big_map = BigMapType.empty(key_type, value_type)
        big_map.ptr = cast(int, res_type.literal)
        big_map.attach_context(context)
        for arg in literal.args:
            _, big_map = big_map.update(  # type: ignore
                key=key_type.from_literal(arg.args[0]),
                val=value_type.from_literal(arg.args[1]),
            )
        context.tzt_big_maps[big_map.ptr] = big_map  # type: ignore

        stdout.append(format_stdout(cls.prim, [], [literal]))  # type: ignore
