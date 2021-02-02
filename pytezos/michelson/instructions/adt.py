from typing import List, cast, Any, Type, Tuple

from pytezos.michelson.instructions.base import format_stdout, MichelsonInstruction
from pytezos.michelson.micheline import parse_micheline_literal
from pytezos.michelson.interpreter.stack import MichelsonStack
from pytezos.michelson.types import PairType, OrType, MichelsonType
from pytezos.context.execution import ExecutionContext


def execute_cxr(prim: str, stack: MichelsonStack, stdout: List[str], idx: int):
    pair = cast(PairType, stack.pop1())
    assert isinstance(pair, PairType), f'expected pair, got {pair.prim}'
    res = pair[idx]
    stack.push(res)
    stdout.append(format_stdout(prim, [pair], [res]))


class CarInstruction(MichelsonInstruction, prim='CAR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        execute_cxr(cls.prim, stack, stdout, 0)
        return cls()


class CdrInstruction(MichelsonInstruction, prim='CDR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        execute_cxr(cls.prim, stack, stdout, 1)
        return cls()


class GetnInstruction(MichelsonInstruction, prim='GET', args_len=1):
    index: int

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['GetnInstruction']:
        index = parse_micheline_literal(args[0], {'int': int})
        res = type(cls.__name__, (cls,), dict(args=args, index=index, **kwargs))
        return cast(Type['GetnInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        pair = cast(PairType, stack.pop1())
        assert isinstance(pair, PairType), f'expected pair, got {pair.prim}'
        if cls.index % 2 == 0:
            res = pair.get_sub_comb(cls.index)
        else:
            res = pair.get_comb_leaf(cls.index)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [pair], [res]))
        return cls()


class UpdatenInstruction(MichelsonInstruction, prim='UPDATE', args_len=1):
    index: int

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['UpdatenInstruction']:
        index = parse_micheline_literal(args[0], {'int': int})
        res = type(cls.__name__, (cls,), dict(args=args, index=index, **kwargs))
        return cast(Type['UpdatenInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        element, pair = cast(Tuple[MichelsonType, PairType], stack.pop2())
        assert isinstance(pair, PairType), f'expected pair, got {pair.prim}'
        if cls.index % 2 == 0:
            assert isinstance(element, PairType), f'expected pair, got {pair.prim}'
            res = pair.update_sub_comb(cls.index, element)
        else:
            res = pair.update_comb_leaf(cls.index, element)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [element, pair], [res]))
        return cls()


class LeftInstruction(MichelsonInstruction, prim='LEFT', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        left = stack.pop1()
        res = OrType.from_left(left, cls.args[1])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left], [res]))
        return cls()


class RightInstruction(MichelsonInstruction, prim='RIGHT', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        right = stack.pop1()
        res = OrType.from_right(right, cls.args[1])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [right], [res]))
        return cls()


class PairInstruction(MichelsonInstruction, prim='PAIR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        left, right = stack.pop2()
        res = PairType.from_comb_leaves([left, right])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left, right], [res]))
        return cls()


class UnpairInstruction(MichelsonInstruction, prim='UNPAIR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        pair = cast(PairType, stack.pop1())
        assert isinstance(pair, PairType), f'expected pair, got {pair.prim}'
        left, right = tuple(iter(pair))
        stack.push(right)
        stack.push(left)
        stdout.append(format_stdout(cls.prim, [pair], [left, right]))
        return cls()


class PairnInstruction(MichelsonInstruction, prim='PAIR', args_len=1):
    count: int

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['PairnInstruction']:
        count = parse_micheline_literal(args[0], {'int': int})
        assert count >= 2, f'invalid n == {count}'
        res = type(cls.__name__, (cls,), dict(args=args, count=count, **kwargs))
        return cast(Type['PairnInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        leaves = stack.pop(count=cls.count)
        res = PairType.from_comb_leaves(leaves)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, leaves, [res]))
        return cls()


class UnpairnInstruction(MichelsonInstruction, prim='UNPAIR', args_len=1):
    count: int

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['UpdatenInstruction']:
        count = parse_micheline_literal(args[0], {'int': int})
        assert count >= 2, f'invalid n == {count}'
        res = type(cls.__name__, (cls,), dict(args=args, count=count, **kwargs))
        return cast(Type['UpdatenInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: ExecutionContext):
        pair = cast(PairType, stack.pop1())
        assert isinstance(pair, PairType), f'expected pair, got {pair.prim}'
        leaves = list(pair.iter_comb_leaves())
        assert len(leaves) == cls.count, f'expected {cls.count} leaves, got {len(leaves)}'
        for leaf in reversed(leaves):
            stack.push(leaf)
        stdout.append(format_stdout(cls.prim, [pair], leaves))
        return cls()
