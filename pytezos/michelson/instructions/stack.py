from copy import deepcopy
from typing import List, Any, Type, cast

from pytezos.michelson.types import MichelsonType
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.micheline import parse_micheline_literal
from pytezos.michelson.stack import MichelsonStack


class PushInstruction(MichelsonInstruction, prim='PUSH', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        res_type, val_expr = cls.args  # type: Type[MichelsonType], Any
        res = res_type.from_micheline_value(val_expr)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class DropnInstruction(MichelsonInstruction, prim='DROP', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        count = parse_micheline_literal(cls.args[0], {'int': int})
        dropped = stack.pop(count)
        stdout.append(format_stdout(cls.prim, dropped, []))
        return cls()


class DropInstruction(MichelsonInstruction, prim='DROP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        dropped = stack.pop1()
        stdout.append(format_stdout(cls.prim, [dropped], []))
        return cls()


class DupnInstruction(MichelsonInstruction, prim='DUP', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        depth = parse_micheline_literal(cls.args[0], {'int': int})
        stack.protect(depth)
        res = deepcopy(stack.peek())
        stack.restore(depth)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class DupInstruction(MichelsonInstruction, prim='DUP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        res = deepcopy(stack.peek())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class SwapInstruction(MichelsonInstruction, prim='SWAP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        a, b = stack.pop2()
        stack.push(a)
        stack.push(b)
        stdout.append(format_stdout(cls.prim, [a, b], [b, a]))
        return cls()


class DigInstruction(MichelsonInstruction, prim='DIG', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        depth = parse_micheline_literal(cls.args[0], {'int': int})
        stack.protect(depth)
        res = stack.pop1()
        stack.restore(depth)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [f'<{depth}>', res], [res]))
        return cls()


class DugInstruction(MichelsonInstruction, prim='DUG', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        depth = parse_micheline_literal(cls.args[0], {'int': int})
        res = stack.pop1()
        stack.protect(depth)
        stack.push(res)
        stack.restore(depth)
        stdout.append(format_stdout(cls.prim, [res], [f'<{depth}>', res]))
        return cls()


class CastIntruction(MichelsonInstruction, prim='CAST', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        top = stack.pop1()
        cast_type = cast(Type[MichelsonType], cls.args[0])
        res = cast_type.from_micheline_value(top.to_micheline_value())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [top], [res]))
        return cls()


class RenameInstruction(MichelsonInstruction, prim='RENAME', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        return cls()
