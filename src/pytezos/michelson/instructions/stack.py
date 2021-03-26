from typing import List

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.instructions.base import MichelsonInstruction, Wildcard, format_stdout
from pytezos.michelson.stack import MichelsonStack


class PushInstruction(MichelsonInstruction, prim='PUSH', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res_type, literal = cls.args  # type: Type[MichelsonType], Type[Micheline]  # type: ignore
        assert res_type.is_pushable(), f'{res_type.prim} contains non-pushable arguments'
        res = res_type.from_literal(literal)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class DropnInstruction(MichelsonInstruction, prim='DROP', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        count = cls.args[0].get_int()  # type: ignore
        dropped = stack.pop(count=count)
        stdout.append(format_stdout(cls.prim, dropped, [], count))  # type: ignore
        return cls()


class DropInstruction(MichelsonInstruction, prim='DROP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        dropped = stack.pop1()
        stdout.append(format_stdout(cls.prim, [dropped], []))  # type: ignore
        return cls()


class DupnInstruction(MichelsonInstruction, prim='DUP', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        depth = cls.args[0].get_int() - 1  # type: ignore
        stack.protect(count=depth)
        res = stack.peek().duplicate()
        stack.restore(count=depth)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [*Wildcard.n(depth), res], [res, *Wildcard.n(depth), res], depth))  # type: ignore
        return cls(stack_items_added=1)


class DupInstruction(MichelsonInstruction, prim='DUP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res = stack.peek().duplicate()
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [res], [res, res]))  # type: ignore
        return cls(stack_items_added=1)


class SwapInstruction(MichelsonInstruction, prim='SWAP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a, b = stack.pop2()
        stack.push(a)
        stack.push(b)
        stdout.append(format_stdout(cls.prim, [a, b], [b, a]))  # type: ignore
        return cls(stack_items_added=2)


class DigInstruction(MichelsonInstruction, prim='DIG', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        depth = cls.args[0].get_int()  # type: ignore
        stack.protect(count=depth)
        res = stack.pop1()
        stack.restore(count=depth)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [*Wildcard.n(depth), res], [res, *Wildcard.n(depth)], depth))  # type: ignore
        return cls(stack_items_added=1)


class DugInstruction(MichelsonInstruction, prim='DUG', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        depth = cls.args[0].get_int()  # type: ignore
        res = stack.pop1()
        stack.protect(count=depth)
        stack.push(res)
        stack.restore(count=depth)
        stdout.append(format_stdout(cls.prim, [res, *Wildcard.n(depth)], [*Wildcard.n(depth), res], depth))  # type: ignore
        return cls(stack_items_added=1)


class CastIntruction(MichelsonInstruction, prim='CAST', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res = stack.pop1()
        # TODO: will become obsolete in the next protocol? (because annots are no longer part of the type)
        # cast_type = cast(Type[MichelsonType], cls.args[0])
        # res = cast_type.from_micheline_value(top.to_micheline_value())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [res], [res]))  # type: ignore
        return cls(stack_items_added=1)


class RenameInstruction(MichelsonInstruction, prim='RENAME'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        return cls()
