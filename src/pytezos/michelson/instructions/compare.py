from typing import Callable, List, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import BoolType, IntType


def compare(a, b) -> int:
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1


class CompareInstruction(MichelsonInstruction, prim='COMPARE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a, b = stack.pop2()
        a.assert_type_equal(type(b))
        res = IntType.from_value(compare(a, b))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a, b], [res]))  # type: ignore
        return cls(stack_items_added=1)


def execute_zero_compare(prim: str, stack: MichelsonStack, stdout: List[str], compare: Callable[[int], bool]):
    a = cast(IntType, stack.pop1())
    a.assert_type_equal(IntType)
    res = BoolType(compare(int(a)))
    stack.push(res)
    stdout.append(format_stdout(prim, [a], [res]))


class EqInstruction(MichelsonInstruction, prim='EQ'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x == 0)  # type: ignore
        return cls(stack_items_added=1)


class GeInstruction(MichelsonInstruction, prim='GE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x >= 0)  # type: ignore
        return cls(stack_items_added=1)


class GtInstruction(MichelsonInstruction, prim='GT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x > 0)  # type: ignore
        return cls(stack_items_added=1)


class LeInstruction(MichelsonInstruction, prim='LE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x <= 0)  # type: ignore
        return cls(stack_items_added=1)


class LtInstruction(MichelsonInstruction, prim='LT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x < 0)  # type: ignore
        return cls(stack_items_added=1)


class NeqInstruction(MichelsonInstruction, prim='NEQ'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x != 0)  # type: ignore
        return cls(stack_items_added=1)
