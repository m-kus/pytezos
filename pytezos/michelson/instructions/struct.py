from typing import List, cast, Tuple, Union

from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.types import MichelsonType, BoolType, ListType, OptionType, \
    MapType, SetType, BigMapType
from pytezos.michelson.interpreter.stack import MichelsonStack
from pytezos.context.base import NodeContext


class ConsInstruction(MichelsonInstruction, prim='CONS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        elt, lst = cast(Tuple[MichelsonType, ListType], stack.pop2())
        assert isinstance(lst, ListType), f'expected list, got {lst.prim}'
        res = lst.prepend(elt)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [elt, lst], [res]))
        return cls()


class NilInstruction(MichelsonInstruction, prim='NIL', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        res = ListType.empty(cls.args[0])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class EmptyBigMapInstruction(MichelsonInstruction, prim='EMPTY_BIG_MAP', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        res = BigMapType.empty(key_type=cls.args[0], val_type=cls.args[1])
        res.attach_context(context)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class EmptyMapInstruction(MichelsonInstruction, prim='EMPTY_MAP', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        res = MapType.empty(key_type=cls.args[0], val_type=cls.args[1])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class EmptySetInstruction(MichelsonInstruction, prim='EMPTY_SET', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        res = SetType.empty(item_type=cls.args[0])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class GetInstruction(MichelsonInstruction, prim='GET'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        key, src = cast(Tuple[MichelsonType, Union[MapType, BigMapType]], stack.pop2())
        assert type(src) in [MapType, BigMapType], f'unexpected {cls.prim}'
        val = src.get(key, dup=True)
        if val is None:
            res = OptionType.none(src.args[0])
        else:
            res = OptionType.from_some(val)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [key, src], [res]))
        return cls()


class GetAndUpdateInstruction(MichelsonInstruction, prim='GET_AND_UPDATE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        key, val, src = cast(Tuple[MichelsonType, OptionType, Union[MapType, BigMapType]], stack.pop3())
        assert type(src) in [MapType, BigMapType], f'unexpected {cls.prim}'
        prev_val, dst = src.update(key, None if val.is_none() else val.get_some())
        res = OptionType.none(src.args[1]) if prev_val is None else OptionType.from_some(prev_val)
        stack.push(dst)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [key, val, src], [res, dst]))
        return cls()


class UpdateInstruction(MichelsonInstruction, prim='UPDATE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        key, val, src = cast(Tuple[MichelsonType, OptionType, Union[MapType, BigMapType]], stack.pop3())
        assert type(src) in [MapType, BigMapType], f'unexpected {cls.prim}'
        _, dst = src.update(key, None if val.is_none() else val.get_some())
        stack.push(dst)
        stdout.append(format_stdout(cls.prim, [key, val, src], [dst]))
        return cls()


class MemInstruction(MichelsonInstruction, prim='MEM'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        key, src = cast(Tuple[MichelsonType, Union[SetType, MapType, BigMapType]], stack.pop2())
        assert type(src) in [SetType, MapType, BigMapType], f'unexpected {src.prim}'
        res = BoolType.from_value(src.contains(key))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [key, src], [res]))
        return cls()


class NoneInstruction(MichelsonInstruction, prim='NONE', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        res = OptionType.none(cls.args[0])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class SomeInstruction(MichelsonInstruction, prim='SOME'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        some = stack.pop1()
        res = OptionType.from_some(some)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [some], [res]))
        return cls()
