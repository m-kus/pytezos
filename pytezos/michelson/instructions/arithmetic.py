from typing import List, Union, Tuple, Type, Callable, cast

from pytezos.michelson.interpreter.stack import MichelsonStack
from pytezos.michelson.types import BoolType, IntType, NatType, TimestampType, MutezType, OptionType, PairType
from pytezos.michelson.instructions.base import MichelsonInstruction, dispatch_types, format_stdout
from pytezos.context.base import NodeContext


class AbsInstruction(MichelsonInstruction, prim='ABS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a = cast(IntType, stack.pop1())
        a.assert_equal_types(IntType)
        res = NatType.from_value(abs(int(a)))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))
        return cls()


class AddInstruction(MichelsonInstruction, prim='ADD'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a, b = cast(Tuple[Union[IntType, NatType, MutezType, TimestampType], ...], stack.pop2())
        res_type, = dispatch_types(a, b, mapping={
            (NatType, NatType): (NatType,),
            (NatType, IntType): (IntType,),
            (IntType, NatType): (IntType,),
            (IntType, IntType): (IntType,),
            (TimestampType, IntType): (TimestampType,),
            (IntType, TimestampType): (TimestampType,),
            (MutezType, MutezType): (MutezType,)
        })  # type: Union[Type[IntType], Type[NatType], Type[TimestampType], Type[MutezType]]
        res = res_type.from_value(int(a) + int(b))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a, b], [res]))
        return cls()


class CompareInstruction(MichelsonInstruction, prim='COMPARE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a, b = stack.pop2()
        a.assert_equal_types(type(b))
        res = IntType.from_value(a.__cmp__(b))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a, b], [res]))
        return cls()


class EdivInstruction(MichelsonInstruction, prim='EDIV'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a, b = cast(Tuple[Union[IntType, NatType, MutezType, TimestampType], ...], stack.pop2())
        q_type, r_type = dispatch_types(a, b, mapping={
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
            res = OptionType.from_some(PairType.from_comb_leaves(items))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a, b], [res]))
        return cls()


def execute_zero_compare(prim: str, stack: MichelsonStack, stdout: List[str], compare: Callable[[int], bool]):
    a = cast(IntType, stack.pop1())
    a.assert_equal_types(IntType)
    res = BoolType(compare(int(a)))
    stack.push(res)
    stdout.append(format_stdout(prim, [a], [res]))


class EqInstruction(MichelsonInstruction, prim='EQ'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x == 0)
        return cls()


class GeInstruction(MichelsonInstruction, prim='GE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x >= 0)
        return cls()


class GtInstruction(MichelsonInstruction, prim='GT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x > 0)
        return cls()


class LeInstruction(MichelsonInstruction, prim='LE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x <= 0)
        return cls()


class LtInstruction(MichelsonInstruction, prim='LT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x < 0)
        return cls()


class NeqInstruction(MichelsonInstruction, prim='NEQ'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_zero_compare(cls.prim, stack, stdout, lambda x: x != 0)
        return cls()


class IntInstruction(MichelsonInstruction, prim='INT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a = cast(NatType, stack.pop1())
        a.assert_equal_types(NatType)
        res = IntType.from_value(int(a))
        stack.push(res)
        stdout.append(f'{cls.prim} / {repr(a)} => {repr(res)}')
        return cls()


class IsNatInstruction(MichelsonInstruction, prim='ISNAT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a = cast(IntType, stack.pop1())
        a.assert_equal_types(IntType)
        if int(a) >= 0:
            res = OptionType.from_some(NatType.from_value(int(a)))
        else:
            res = OptionType.none(NatType)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))
        return cls()


def execute_shift(prim: str, stack: MichelsonStack, stdout: List[str], shift: Callable[[int, int], int]):
    a, b = cast(Tuple[NatType, NatType], stack.pop2())
    a.assert_equal_types(NatType)
    b.assert_equal_types(NatType)
    assert int(b) < 257, f'shift overflow {int(b)}, should not exceed 256'
    res = NatType.from_value(shift(int(a), int(b)))
    stack.push(res)
    stdout.append(format_stdout(prim, [a, b], [res]))


class LslInstruction(MichelsonInstruction, prim='LSL'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_shift(cls.prim, stack, stdout, lambda x: x[0] << x[1])
        return cls()


class LsrInstruction(MichelsonInstruction, prim='LSR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_shift(cls.prim, stack, stdout, lambda x: x[0] >> x[1])
        return cls()


class MulInstruction(MichelsonInstruction, prim='MUL'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a, b = cast(Tuple[Union[IntType, NatType, MutezType], ...], stack.pop2())
        res_type, = dispatch_types(a, b, mapping={
            (NatType, NatType): (NatType,),
            (NatType, IntType): (IntType,),
            (IntType, NatType): (IntType,),
            (IntType, IntType): (IntType,),
            (MutezType, NatType): (MutezType,),
            (NatType, MutezType): (MutezType,)
        })  # type: Union[Type[IntType], Type[NatType], Type[TimestampType], Type[MutezType]]
        res = res_type.from_value(int(a) * int(b))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a, b], [res]))
        return cls()


class NegInstruction(MichelsonInstruction, prim='NEG'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a = cast(Union[IntType, NatType], stack.pop1())
        _ = dispatch_types(a, mapping={
            (IntType,): (IntType,),
            (NatType,): (IntType,)
        })
        res = IntType.from_value(-int(a))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))
        return cls()


class SubInstruction(MichelsonInstruction, prim='SUB'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a, b = cast(Tuple[Union[IntType, NatType, MutezType, TimestampType], ...], stack.pop2())
        res_type = dispatch_types(a, b, mapping={
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
        stdout.append(format_stdout(cls.prim, [a, b], [res]))
        return cls()


def execute_boolean_add(prim: str, stack: MichelsonStack, stdout: List[str], add: Callable):
    a, b = cast(Tuple[Union[BoolType, NatType], ...], stack.pop2())
    res_type, convert = dispatch_types(a, b, mapping={
        (BoolType, BoolType): (BoolType, bool),
        (NatType, NatType): (NatType, int)
    })
    val = add(convert(a), convert(b))
    res = res_type.from_value(val)
    stack.push(res)
    stdout.append(format_stdout(prim, [a, b], [res]))


class OrInstruction(MichelsonInstruction, prim='OR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_boolean_add(cls.prim, stack, stdout, lambda x: x[0] | x[1])
        return cls()


class XorInstruction(MichelsonInstruction, prim='XOR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_boolean_add(cls.prim, stack, stdout, lambda x: x[0] ^ x[1])
        return cls()


class AndInstruction(MichelsonInstruction, prim='AND'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a, b = cast(Tuple[Union[BoolType, NatType, IntType], ...], stack.pop2())
        res_type, convert = dispatch_types(a, b, mapping={
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
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a = cast(Union[IntType, NatType, BoolType], stack.pop1())
        res_type, convert = dispatch_types(a, mapping={
            (NatType,): (IntType, lambda x: ~int(x)),
            (IntType,): (IntType, lambda x: ~int(x)),
            (BoolType,): (BoolType, lambda x: not bool(x))
        })
        res = res_type.from_value(convert(a))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))
        return cls()
