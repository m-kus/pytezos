from typing import List, Any, Type, cast

from pytezos.michelson.types import MichelsonType
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.micheline import parse_micheline_literal
from pytezos.michelson.stack import MichelsonStack
from pytezos.context.execution import ExecutionContext


class PushInstruction(MichelsonInstruction, prim='PUSH', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        res_type, val_expr = cls.args  # type: Type[MichelsonType], Any
        assert res_type.is_pushable(), f'{res_type.prim} contains non-pushable arguments'
        res = res_type.from_micheline_value(val_expr)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class DropnInstruction(MichelsonInstruction, prim='DROP', args_len=1):

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['DropnInstruction']:
        res = type(cls.__name__, (cls,), dict(args=[parse_micheline_literal(args[0], {'int': int})], **kwargs))
        return cast(Type['DropnInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        dropped = stack.pop(count=cls.args[0])
        stdout.append(format_stdout(cls.prim, dropped, []))
        return cls()


class DropInstruction(MichelsonInstruction, prim='DROP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        dropped = stack.pop1()
        stdout.append(format_stdout(cls.prim, [dropped], []))
        return cls()


class DupnInstruction(MichelsonInstruction, prim='DUP', args_len=1):

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['DupnInstruction']:
        res = type(cls.__name__, (cls,), dict(args=[parse_micheline_literal(args[0], {'int': int})], **kwargs))
        return cast(Type['DupnInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        stack.protect(count=cls.args[0])
        res = stack.peek().duplicate()
        stack.restore(count=cls.args[0])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class DupInstruction(MichelsonInstruction, prim='DUP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        res = stack.peek().duplicate()
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class SwapInstruction(MichelsonInstruction, prim='SWAP'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        a, b = stack.pop2()
        stack.push(a)
        stack.push(b)
        stdout.append(format_stdout(cls.prim, [a, b], [b, a]))
        return cls()


class DigInstruction(MichelsonInstruction, prim='DIG', args_len=1):

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['DigInstruction']:
        res = type(cls.__name__, (cls,), dict(args=[parse_micheline_literal(args[0], {'int': int})], **kwargs))
        return cast(Type['DigInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        stack.protect(count=cls.args[0])
        res = stack.pop1()
        stack.restore(count=cls.args[0])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [f'<{cls.args[0]}>', res], [res]))
        return cls()


class DugInstruction(MichelsonInstruction, prim='DUG', args_len=1):

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['DugInstruction']:
        res = type(cls.__name__, (cls,), dict(args=[parse_micheline_literal(args[0], {'int': int})], **kwargs))
        return cast(Type['DugInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        res = stack.pop1()
        stack.protect(count=cls.args[0])
        stack.push(res)
        stack.restore(count=cls.args[0])
        stdout.append(format_stdout(cls.prim, [res], [f'<{cls.args[0]}>', res]))
        return cls()


class CastIntruction(MichelsonInstruction, prim='CAST', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        top = stack.pop1()
        cast_type = cast(Type[MichelsonType], cls.args[0])
        res = cast_type.from_micheline_value(top.to_micheline_value())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [top], [res]))
        return cls()


class RenameInstruction(MichelsonInstruction, prim='RENAME', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        return cls()
