from typing import List, cast, Any, Type

from pytezos.michelson.instructions.base import format_stdout, MichelsonInstruction
from pytezos.michelson.micheline import parse_micheline_literal
from pytezos.michelson.interpreter.stack import MichelsonStack
from pytezos.michelson.types import PairType, OrType
from pytezos.context.base import NodeContext


def execute_cxr(prim: str, stack: MichelsonStack, stdout: List[str], idx: int):
    pair = cast(PairType, stack.pop1())
    assert isinstance(pair, PairType), f'expected pair, got {pair.prim}'
    res = pair[idx]
    stack.push(res)
    stdout.append(format_stdout(prim, [pair], [res]))


class CarInstruction(MichelsonInstruction, prim='CAR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_cxr(cls.prim, stack, stdout, 0)
        return cls()


class CdrInstruction(MichelsonInstruction, prim='CDR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_cxr(cls.prim, stack, stdout, 1)
        return cls()


class GetnInstruction(MichelsonInstruction, prim='GET', args_len=1):

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['GetnInstruction']:
        res = type(cls.__name__, (cls,), dict(args=[parse_micheline_literal(args[0], {'int': int})], **kwargs))
        return cast(Type['GetnInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        pair = cast(PairType, stack.pop1())
        assert isinstance(pair, PairType), f'expected pair, got {pair.prim}'
        if cls.args[0] % 2 == 0:
            res = pair.get_sub_comb(cls.args[0])
        else:
            res = pair.get_comb_leaf(cls.args[0])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [pair], [res]))
        return cls()


class LeftInstruction(MichelsonInstruction, prim='LEFT', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        left = stack.pop1()
        res = OrType.from_left(left, cls.args[1])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left], [res]))
        return cls()


class RightInstruction(MichelsonInstruction, prim='RIGHT', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        right = stack.pop1()
        res = OrType.from_right(right, cls.args[1])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [right], [res]))
        return cls()


class PairInstruction(MichelsonInstruction, prim='PAIR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        left, right = stack.pop2()
        res = PairType.from_items([left, right])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left, right], [res]))
        return cls()


class UnpairInstruction(MichelsonInstruction, prim='UNPAIR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        pair = cast(PairType, stack.pop1())
        assert isinstance(pair, PairType), f'expected pair, got {pair.prim}'
        left, right = tuple(iter(pair))
        stack.push(right)
        stack.push(left)
        stdout.append(format_stdout(cls.prim, [pair], [left, right]))
        return cls()


class UnpairnInstruction(MichelsonInstruction, prim='UNPAIR', args_len=1):

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['UpdatenInstruction']:
        n = parse_micheline_literal(args[0], {'int': int})
        assert n >= 2, f'invalid n == {n}'
        res = type(cls.__name__, (cls,), dict(args=[n], **kwargs))
        return cast(Type['UpdatenInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        pair = cast(PairType, stack.pop1())
        assert isinstance(pair, PairType), f'expected pair, got {pair.prim}'
        left, right = tuple(iter(pair))
        stack.push(right)
        stack.push(left)
        stdout.append(format_stdout(cls.prim, [pair], [left, right]))
        return cls()


class UpdatenInstruction(MichelsonInstruction, prim='UPDATE', args_len=1):

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['UpdatenInstruction']:
        res = type(cls.__name__, (cls,), dict(args=[parse_micheline_literal(args[0], {'int': int})], **kwargs))
        return cast(Type['UpdatenInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        pass
