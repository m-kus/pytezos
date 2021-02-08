from typing import List, Callable, cast, Tuple, Union

from pytezos.context.abstract import AbstractContext
from pytezos.michelson.instructions.base import dispatch_types, format_stdout, MichelsonInstruction
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import BoolType, NatType, IntType


def execute_boolean_add(prim: str, stack: MichelsonStack, stdout: List[str], add: Callable):
    a, b = cast(Tuple[Union[BoolType, NatType], ...], stack.pop2())
    res_type, convert = dispatch_types(type(a), type(b), mapping={
        (BoolType, BoolType): (BoolType, bool),
        (NatType, NatType): (NatType, int)
    })
    val = add((convert(a), convert(b)))
    res = res_type.from_value(val)
    stack.push(res)
    stdout.append(format_stdout(prim, [a, b], [res]))


class OrInstruction(MichelsonInstruction, prim='OR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_boolean_add(cls.prim, stack, stdout, lambda x: x[0] | x[1])
        return cls()


class XorInstruction(MichelsonInstruction, prim='XOR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_boolean_add(cls.prim, stack, stdout, lambda x: x[0] ^ x[1])
        return cls()


class AndInstruction(MichelsonInstruction, prim='AND'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a, b = cast(Tuple[Union[BoolType, NatType, IntType], ...], stack.pop2())
        res_type, convert = dispatch_types(type(a), type(b), mapping={
            (BoolType, BoolType): (BoolType, bool),
            (NatType, NatType): (NatType, int),
            (NatType, IntType): (NatType, int),
            (IntType, NatType): (NatType, int),
        })
        res = res_type.from_value(convert(a) & convert(b))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a, b], [res]))
        return cls()


class NotInstruction(MichelsonInstruction, prim='NOT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a = cast(Union[IntType, NatType, BoolType], stack.pop1())
        res_type, convert = dispatch_types(type(a), mapping={
            (NatType,): (IntType, lambda x: ~int(x)),
            (IntType,): (IntType, lambda x: ~int(x)),
            (BoolType,): (BoolType, lambda x: not bool(x))
        })
        res = res_type.from_value(convert(a))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))
        return cls()