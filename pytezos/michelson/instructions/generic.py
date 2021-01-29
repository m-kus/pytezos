from typing import List, cast, Union, Tuple

from pytezos.michelson.instructions.base import MichelsonInstruction, dispatch_types, format_stdout
from pytezos.michelson.interpreter.stack import MichelsonStack
from pytezos.michelson.types import StringType, BytesType, ListType, SetType, MapType, NatType, OptionType, UnitType
from pytezos.context.base import NodeContext


class ConcatInstruction(MichelsonInstruction, prim='CONCAT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a = cast(Union[StringType, BytesType, ListType], stack.pop1())
        if type(a) in [StringType, BytesType]:
            b = cast(Union[StringType, BytesType], stack.pop1())
            res_type, convert = dispatch_types(a, b, mapping={
                (StringType, StringType): (StringType, str),
                (BytesType, BytesType): (BytesType, bytes)
            })
            res = res_type.from_value(convert(a) + convert(b))
            stdout.append(format_stdout(cls.prim, [a, b], [res]))
        else:
            assert isinstance(a, ListType), f'unexpected {a.prim}'
            res_type, convert, delim = dispatch_types(a.args[0], mapping={
                (StringType,): (StringType, str, ''),
                (BytesType,): (BytesType, bytes, b'')
            })
            res = res_type.from_value(delim.join(map(convert, a)))
            stdout.append(format_stdout(cls.prim, [a], [res]))
        stack.push(res)
        return cls()


class PackInstruction(MichelsonInstruction, prim='PACK'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a = stack.pop1()
        res = BytesType.unpack(a.pack())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))
        return cls()


class UnpackInstruction(MichelsonInstruction, prim='UNPACK', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a = cast(BytesType, stack.pop1())
        a.assert_equal_types(BytesType)
        try:
            some = cls.args[0].unpack(bytes(a))
            res = OptionType.from_some(some)
        except Exception as e:
            stdout.append(f'{cls.prim}: {e}')
            res = OptionType.none(cls.args[0])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))
        return cls()


class SizeInstruction(MichelsonInstruction, prim='SIZE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        src = cast(Union[StringType, BytesType, ListType, SetType, MapType], stack.pop1())
        assert type(src) in [StringType, BytesType, ListType, SetType, MapType], f'unexpected {src.prim}'
        res = NatType.from_value(len(src))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [src], [res]))
        return cls()


class SliceInstruction(MichelsonInstruction, prim='SLICE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        offset, length, s = cast(Tuple[NatType, NatType, Union[StringType, BytesType]], stack.pop3())
        offset.assert_equal_types(NatType)
        length.assert_equal_types(NatType)
        assert type(s) in [StringType, BytesType], f'unexpected {s.prim}'
        start, stop = int(offset), int(offset) + int(length)
        if 0 < stop <= len(s):
            res = OptionType.from_some(s[start:stop])
        else:
            res = OptionType.none(type(s))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [offset, length, s], [res]))
        return cls()


class UnitInstruction(MichelsonInstruction, prim='UNIT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        res = UnitType()
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()
