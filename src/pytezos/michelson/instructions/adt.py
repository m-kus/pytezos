from typing import List, Tuple, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import MichelsonType, OrType, PairType


def execute_cxr(prim: str, stack: MichelsonStack, stdout: List[str], idx: int):
    pair = cast(PairType, stack.pop1())
    pair.assert_type_in(PairType)
    res = pair.items[idx]
    stack.push(res)
    stdout.append(format_stdout(prim, [pair], [res]))


class CarInstruction(MichelsonInstruction, prim='CAR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_cxr(cls.prim, stack, stdout, 0)  # type: ignore
        return cls(stack_items_added=1)


class CdrInstruction(MichelsonInstruction, prim='CDR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_cxr(cls.prim, stack, stdout, 1)  # type: ignore
        return cls(stack_items_added=1)


class GetnInstruction(MichelsonInstruction, prim='GET', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        pair = cast(PairType, stack.pop1())
        pair.assert_type_in(PairType)
        index = cls.args[0].get_int()  # type: ignore
        res = pair.access_comb(index)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [pair], [res], index))  # type: ignore
        return cls(stack_items_added=1)


class UpdatenInstruction(MichelsonInstruction, prim='UPDATE', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        element, pair = cast(Tuple[MichelsonType, PairType], stack.pop2())
        pair.assert_type_in(PairType)
        index = cls.args[0].get_int()  # type: ignore
        res = pair.update_comb(index, element)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [element, pair], [res], index))  # type: ignore
        return cls(stack_items_added=1)


class LeftInstruction(MichelsonInstruction, prim='LEFT', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        left = stack.pop1()
        res = OrType.from_left(left, cls.args[0])  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left], [res]))  # type: ignore
        return cls()


class RightInstruction(MichelsonInstruction, prim='RIGHT', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        right = stack.pop1()
        res = OrType.from_right(right, cls.args[0])  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [right], [res]))  # type: ignore
        return cls(stack_items_added=1)


class PairInstruction(MichelsonInstruction, prim='PAIR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        left, right = stack.pop2()
        res = PairType.from_comb([left, right])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [left, right], [res]))  # type: ignore
        return cls(stack_items_added=1)


class UnpairInstruction(MichelsonInstruction, prim='UNPAIR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        pair = cast(PairType, stack.pop1())
        pair.assert_type_in(PairType)
        left, right = tuple(iter(pair))
        stack.push(right)
        stack.push(left)
        stdout.append(format_stdout(cls.prim, [pair], [left, right]))  # type: ignore
        return cls(stack_items_added=2)


class PairnInstruction(MichelsonInstruction, prim='PAIR', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        count = cls.args[0].get_int()  # type: ignore
        assert count >= 2, f'invalid argument, must be >= 2'
        leaves = stack.pop(count=count)
        res = PairType.from_comb(leaves)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, leaves, [res], count))  # type: ignore
        return cls(stack_items_added=1)


class UnpairnInstruction(MichelsonInstruction, prim='UNPAIR', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        count = cls.args[0].get_int()  # type: ignore
        assert count >= 2, f'invalid argument, must be >= 2'
        pair = cast(PairType, stack.pop1())
        pair.assert_type_in(PairType)
        leaves = list(pair.iter_comb())
        assert len(leaves) == count, f'expected {count} leaves, got {len(leaves)}'
        for leaf in reversed(leaves):
            stack.push(leaf)
        stdout.append(format_stdout(cls.prim, [pair], leaves, count))  # type: ignore
        return cls(stack_items_added=len(leaves))
