from typing import Callable, List, Tuple, Type, Union, cast

from py_ecc import optimized_bls12_381 as bls12_381

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.instructions.base import MichelsonInstruction, dispatch_types, format_stdout
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import (BLS12_381_FrType, BLS12_381_G1Type, BLS12_381_G2Type, IntType, MutezType, NatType, OptionType,
                                     PairType, TimestampType)


class AbsInstruction(MichelsonInstruction, prim='ABS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a = cast(IntType, stack.pop1())
        a.assert_type_equal(IntType)
        res = NatType.from_value(abs(int(a)))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))  # type: ignore
        return cls(stack_items_added=1)


class AddInstruction(MichelsonInstruction, prim='ADD'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a, b = cast(Tuple[Union[IntType, NatType, MutezType, TimestampType,
                                BLS12_381_G1Type, BLS12_381_G2Type, BLS12_381_FrType], ...],
                    stack.pop2())
        res_type, = dispatch_types(type(a), type(b), mapping={
            (NatType, NatType): (NatType,),
            (NatType, IntType): (IntType,),
            (IntType, NatType): (IntType,),
            (IntType, IntType): (IntType,),
            (TimestampType, IntType): (TimestampType,),
            (IntType, TimestampType): (TimestampType,),
            (MutezType, MutezType): (MutezType,),
            (BLS12_381_FrType, BLS12_381_FrType): (BLS12_381_FrType,),
            (BLS12_381_G1Type, BLS12_381_G1Type): (BLS12_381_G1Type,),
            (BLS12_381_G2Type, BLS12_381_G2Type): (BLS12_381_G2Type,)
        })
        res_type = cast(Union[Type[IntType], Type[NatType], Type[TimestampType], Type[MutezType],
                              Type[BLS12_381_G1Type], Type[BLS12_381_G2Type], Type[BLS12_381_FrType]],
                        res_type)
        if issubclass(res_type, IntType):
            res = res_type.from_value(int(a) + int(b))  # type: ignore
        else:
            res = res_type.from_point(bls12_381.add(a.to_point(), b.to_point()))  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a, b], [res]))  # type: ignore
        return cls(stack_items_added=1)


class EdivInstruction(MichelsonInstruction, prim='EDIV'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a, b = cast(Tuple[Union[IntType, NatType, MutezType, TimestampType], ...], stack.pop2())
        q_type, r_type = dispatch_types(type(a), type(b), mapping={  # type: ignore
            (NatType, NatType): (NatType, NatType),
            (NatType, IntType): (IntType, NatType),
            (IntType, NatType): (IntType, NatType),
            (IntType, IntType): (IntType, NatType),
            (MutezType, NatType): (MutezType, MutezType),
            (MutezType, MutezType): (NatType, MutezType)
        })  # type: Union[Type[IntType], Type[NatType], Type[TimestampType], Type[MutezType]]
        if int(b) == 0:
            res = OptionType.none(PairType.create_type(args=[q_type, r_type]))
        else:
            q, r = divmod(int(a), int(b))
            if r < 0:
                r += abs(int(b))
                q += 1
            items = [q_type.from_value(q), r_type.from_value(r)]
            res = OptionType.from_some(PairType.from_comb(items))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a, b], [res]))  # type: ignore
        return cls(stack_items_added=1)


def execute_shift(prim: str, stack: MichelsonStack, stdout: List[str], shift: Callable[[Tuple[int, int]], int]):
    a, b = cast(Tuple[NatType, NatType], stack.pop2())
    a.assert_type_equal(NatType)
    b.assert_type_equal(NatType)
    assert int(b) < 257, f'shift overflow {int(b)}, should not exceed 256'
    c = shift((int(a), int(b)))
    res = NatType.from_value(c)
    stack.push(res)
    stdout.append(format_stdout(prim, [a, b], [res]))


class LslInstruction(MichelsonInstruction, prim='LSL'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_shift(cls.prim, stack, stdout, lambda x: x[0] << x[1])  # type: ignore
        return cls(stack_items_added=1)


class LsrInstruction(MichelsonInstruction, prim='LSR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        execute_shift(cls.prim, stack, stdout, lambda x: x[0] >> x[1])  # type: ignore
        return cls(stack_items_added=1)


class MulInstruction(MichelsonInstruction, prim='MUL'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a, b = cast(
            Tuple[Union[IntType, NatType, MutezType, BLS12_381_FrType, BLS12_381_G1Type, BLS12_381_G2Type], ...],
            stack.pop2())
        res_type, = dispatch_types(type(a), type(b), mapping={
            (NatType, NatType): (NatType,),
            (NatType, IntType): (IntType,),
            (IntType, NatType): (IntType,),
            (IntType, IntType): (IntType,),
            (MutezType, NatType): (MutezType,),
            (NatType, MutezType): (MutezType,),
            (NatType, BLS12_381_FrType): (BLS12_381_FrType,),
            (IntType, BLS12_381_FrType): (BLS12_381_FrType,),
            (BLS12_381_FrType, NatType): (BLS12_381_FrType,),
            (BLS12_381_FrType, IntType): (BLS12_381_FrType,),
            (BLS12_381_FrType, BLS12_381_FrType): (BLS12_381_FrType,),
            (BLS12_381_G1Type, BLS12_381_FrType): (BLS12_381_G1Type,),
            (BLS12_381_G2Type, BLS12_381_FrType): (BLS12_381_G2Type,),
        })
        res_type = cast(Union[Type[IntType], Type[NatType], Type[TimestampType], Type[MutezType],
                              Type[BLS12_381_FrType], Type[BLS12_381_G1Type], Type[BLS12_381_G2Type]], res_type)
        if issubclass(res_type, IntType):
            res = res_type.from_value(int(a) * int(b))  # type: ignore
        else:
            res = res_type.from_point(bls12_381.multiply(a.to_point(), int(b)))  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a, b], [res]))  # type: ignore
        return cls(stack_items_added=1)


class NegInstruction(MichelsonInstruction, prim='NEG'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a = cast(Union[IntType, NatType, BLS12_381_FrType, BLS12_381_G1Type, BLS12_381_G2Type], stack.pop1())
        res_type, = dispatch_types(type(a), mapping={
            (IntType,): (IntType,),
            (NatType,): (IntType,),
            (BLS12_381_FrType,): (BLS12_381_FrType,),
            (BLS12_381_G1Type,): (BLS12_381_G1Type,),
            (BLS12_381_G2Type,): (BLS12_381_G2Type,)
        })
        if issubclass(res_type, IntType):
            res = IntType.from_value(-int(a))  # type: ignore
        else:
            res = res_type.from_point(bls12_381.neg(a.to_point()))  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))  # type: ignore
        return cls(stack_items_added=1)


class SubInstruction(MichelsonInstruction, prim='SUB'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a, b = cast(Tuple[Union[IntType, NatType, MutezType, TimestampType], ...], stack.pop2())
        res_type, = dispatch_types(type(a), type(b), mapping={  # type: ignore
            (NatType, NatType): (IntType,),
            (NatType, IntType): (IntType,),
            (IntType, NatType): (IntType,),
            (IntType, IntType): (IntType,),
            (TimestampType, IntType): (TimestampType,),
            (TimestampType, TimestampType): (IntType,),
            (MutezType, MutezType): (MutezType,)
        })  # type: Union[Type[IntType], Type[NatType], Type[TimestampType], Type[MutezType]]
        res = res_type.from_value(int(a) - int(b))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a, b], [res]))  # type: ignore
        return cls(stack_items_added=1)


class IntInstruction(MichelsonInstruction, prim='INT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a = cast(Union[NatType, BLS12_381_FrType], stack.pop1())
        a.assert_type_in(NatType, BLS12_381_FrType)
        res = IntType.from_value(int(a))
        stack.push(res)
        stdout.append(f'{cls.prim} / {repr(a)} => {repr(res)}')
        return cls(stack_items_added=1)


class IsNatInstruction(MichelsonInstruction, prim='ISNAT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        a = cast(IntType, stack.pop1())
        a.assert_type_equal(IntType)
        if int(a) >= 0:
            res = OptionType.from_some(NatType.from_value(int(a)))
        else:
            res = OptionType.none(NatType)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))  # type: ignore
        return cls(stack_items_added=1)
