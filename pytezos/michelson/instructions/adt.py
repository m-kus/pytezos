from typing import List, cast, Any, Type, Tuple

from pytezos.michelson.instructions.base import format_stdout, MichelsonInstruction
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import PairType, OrType, MichelsonType
from pytezos.context.abstract import AbstractContext


def execute_cxr(prim: str, stack: MichelsonStack, stdout: List[str], idx: int):
    pair = cast(PairType, stack.pop1())
    pair.assert_type_in(PairType)
    res = pair.items[idx]
    stack.push(res)
    stdout.append(format_stdout(prim, [pair], [res]))


class CarInstruction(MichelsonInstruction, prim='CAR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_cxr(cls.prim, stack, stdout, 0)
        return cls()


class CdrInstruction(MichelsonInstruction, prim='CDR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_cxr(cls.prim, stack, stdout, 1)
        return cls()


class GetnInstruction(MichelsonInstruction, prim='GET', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        pair = cast(PairType, stack.pop1())
        pair.assert_type_in(PairType)
        index = cls.args[0].get_int()
        res = pair.access_comb(index)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [pair], [res], index))
        return cls()


class UpdatenInstruction(MichelsonInstruction, prim='UPDATE', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        element, pair = cast(Tuple[MichelsonType, PairType], stack.pop2())
        pair.assert_type_in(PairType)
        index = cls.args[0].get_int()
        res = pair.update_comb(index, element)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [element, pair], [res], index))
        return cls()


class LeftInstruction(MichelsonInstruction, prim='LEFT', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        left = stack.pop1()
        res = OrType.from_left(left, cls.args[0])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left], [res]))
        return cls()


class RightInstruction(MichelsonInstruction, prim='RIGHT', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        right = stack.pop1()
        res = OrType.from_right(right, cls.args[0])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [right], [res]))
        return cls()


class PairInstruction(MichelsonInstruction, prim='PAIR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        left, right = stack.pop2()
        res = PairType.from_comb([left, right])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left, right], [res]))
        return cls()


class UnpairInstruction(MichelsonInstruction, prim='UNPAIR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        pair = cast(PairType, stack.pop1())
        pair.assert_type_in(PairType)
        left, right = tuple(iter(pair))
        stack.push(right)
        stack.push(left)
        stdout.append(format_stdout(cls.prim, [pair], [left, right]))
        return cls()


class PairnInstruction(MichelsonInstruction, prim='PAIR', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        count = cls.args[0].get_int()
        assert count >= 2, f'invalid argument, must be >= 2'
        leaves = stack.pop(count=count)
        res = PairType.from_comb(leaves)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, leaves, [res], count))
        return cls()


class UnpairnInstruction(MichelsonInstruction, prim='UNPAIR', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        count = cls.args[0].get_int()
        assert count >= 2, f'invalid argument, must be >= 2'
        pair = cast(PairType, stack.pop1())
        pair.assert_type_in(PairType)
        leaves = list(pair.iter_comb())
        assert len(leaves) == count, f'expected {count} leaves, got {len(leaves)}'
        for leaf in reversed(leaves):
            stack.push(leaf)
        stdout.append(format_stdout(cls.prim, [pair], leaves, count))
        return cls()
