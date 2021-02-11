from typing import List, Type, cast

from pytezos.michelson.micheline import Micheline
from pytezos.michelson.types import MichelsonType
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout, Wildcard
from pytezos.michelson.stack import MichelsonStack
from pytezos.context.abstract import AbstractContext
from pytezos.michelson.format import micheline_to_michelson


class PushInstruction(MichelsonInstruction, prim='PUSH', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res_type, literal = cls.args  # type: Type[MichelsonType], Type[Micheline]
        assert res_type.is_pushable(), f'{res_type.prim} contains non-pushable arguments'
        res = res_type.from_literal(literal)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class DropnInstruction(MichelsonInstruction, prim='DROP', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        count = cls.args[0].get_int()
        dropped = stack.pop(count=count)
        stdout.append(format_stdout(cls.prim, dropped, [], count))
        return cls()


class DropInstruction(MichelsonInstruction, prim='DROP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        dropped = stack.pop1()
        stdout.append(format_stdout(cls.prim, [dropped], []))
        return cls()


class DupnInstruction(MichelsonInstruction, prim='DUP', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        depth = cls.args[0].get_int() - 1
        stack.protect(count=depth)
        res = stack.peek().duplicate()
        stack.restore(count=depth)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [*Wildcard.n(depth), res], [res, *Wildcard.n(depth), res], depth))
        return cls()


class DupInstruction(MichelsonInstruction, prim='DUP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res = stack.peek().duplicate()
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [res], [res, res]))
        return cls()


class SwapInstruction(MichelsonInstruction, prim='SWAP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a, b = stack.pop2()
        stack.push(a)
        stack.push(b)
        stdout.append(format_stdout(cls.prim, [a, b], [b, a]))
        return cls()


class DigInstruction(MichelsonInstruction, prim='DIG', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        depth = cls.args[0].get_int()
        stack.protect(count=depth)
        res = stack.pop1()
        stack.restore(count=depth)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [*Wildcard.n(depth), res], [res, *Wildcard.n(depth)], depth))
        return cls()


class DugInstruction(MichelsonInstruction, prim='DUG', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        depth = cls.args[0].get_int()
        res = stack.pop1()
        stack.protect(count=depth)
        stack.push(res)
        stack.restore(count=depth)
        stdout.append(format_stdout(cls.prim, [res, *Wildcard.n(depth)], [*Wildcard.n(depth), res], depth))
        return cls()


class CastIntruction(MichelsonInstruction, prim='CAST', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        top = stack.pop1()
        cast_type = cast(Type[MichelsonType], cls.args[0])
        res = cast_type.from_micheline_value(top.to_micheline_value())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [top], [res]))
        return cls()


class RenameInstruction(MichelsonInstruction, prim='RENAME'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        return cls()
