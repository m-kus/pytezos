from typing import List, Tuple, Union, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import BigMapType, BoolType, ListType, MapType, MichelsonType, OptionType, SetType


class ConsInstruction(MichelsonInstruction, prim='CONS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        elt, lst = cast(Tuple[MichelsonType, ListType], stack.pop2())
        lst.assert_type_in(ListType)
        res = lst.prepend(elt)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [elt, lst], [res]))  # type: ignore
        return cls(stack_items_added=1)


class NilInstruction(MichelsonInstruction, prim='NIL', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res = ListType.empty(cls.args[0])  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class EmptyBigMapInstruction(MichelsonInstruction, prim='EMPTY_BIG_MAP', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res = BigMapType.empty(key_type=cls.args[0], val_type=cls.args[1])  # type: ignore
        res.attach_context(context)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class EmptyMapInstruction(MichelsonInstruction, prim='EMPTY_MAP', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res = MapType.empty(key_type=cls.args[0], val_type=cls.args[1])  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class EmptySetInstruction(MichelsonInstruction, prim='EMPTY_SET', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res = SetType.empty(item_type=cls.args[0])  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class GetInstruction(MichelsonInstruction, prim='GET'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        key, src = cast(Tuple[MichelsonType, Union[MapType, BigMapType]], stack.pop2())
        src.assert_type_in(MapType, BigMapType)
        val = src.get(key, dup=True)
        if val is None:
            res = OptionType.none(src.args[0])
        else:
            res = OptionType.from_some(val)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [key, src], [res]))  # type: ignore
        return cls(stack_items_added=1)


class GetAndUpdateInstruction(MichelsonInstruction, prim='GET_AND_UPDATE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        key, val, src = cast(Tuple[MichelsonType, OptionType, Union[MapType, BigMapType]], stack.pop3())
        src.assert_type_in(MapType, BigMapType)
        prev_val, dst = src.update(key, None if val.is_none() else val.get_some())
        res = OptionType.none(src.args[1]) if prev_val is None else OptionType.from_some(prev_val)
        stack.push(dst)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [key, val, src], [res, dst]))  # type: ignore
        return cls(stack_items_added=2)


class UpdateInstruction(MichelsonInstruction, prim='UPDATE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        key, val, src = cast(Tuple[MichelsonType, Union[OptionType, BoolType], Union[MapType, BigMapType, SetType]],
                             stack.pop3())
        val.assert_type_in(OptionType, BoolType)
        if isinstance(val, BoolType):
            src.assert_type_in(SetType)
            dst = src.add(key) if bool(val) else src.remove(key)  # type: ignore
        else:
            src.assert_type_in(MapType, BigMapType)
            _, dst = src.update(key, None if val.is_none() else val.get_some())  # type: ignore
        stack.push(dst)
        stdout.append(format_stdout(cls.prim, [key, val, src], [dst]))  # type: ignore
        return cls(stack_items_added=1)


class MemInstruction(MichelsonInstruction, prim='MEM'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        key, src = cast(Tuple[MichelsonType, Union[SetType, MapType, BigMapType]], stack.pop2())
        src.assert_type_in(MapType, BigMapType, SetType)
        res = BoolType.from_value(src.contains(key))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [key, src], [res]))  # type: ignore
        return cls(stack_items_added=1)


class NoneInstruction(MichelsonInstruction, prim='NONE', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res = OptionType.none(cls.args[0])  # type: ignore
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))  # type: ignore
        return cls(stack_items_added=1)


class SomeInstruction(MichelsonInstruction, prim='SOME'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        some = stack.pop1()
        res = OptionType.from_some(some)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [some], [res]))  # type: ignore
        return cls(stack_items_added=1)
