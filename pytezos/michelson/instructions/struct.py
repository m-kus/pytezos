from typing import List, cast, Tuple, Union

from pytezos.michelson.instructions.stack import PushInstruction
from pytezos.michelson.micheline import parse_micheline_literal
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout, dispatch_types
from pytezos.michelson.types import MichelsonType, LambdaType, PairType, BoolType, ListType, OrType, OptionType, \
    MapType, SetType, StringType, BytesType, BigMapType
from pytezos.michelson.stack import MichelsonStack


def execute_cxr(prim: str, stack: MichelsonStack, stdout: List[str], idx: int):
    pair = cast(PairType, stack.pop1())
    assert isinstance(pair, PairType), f'expected pair, got {pair.prim}'
    res = pair[idx]
    stack.push(res)
    stdout.append(format_stdout(prim, [pair], [res]))


class CarInstruction(MichelsonInstruction, prim='CAR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        execute_cxr(cls.prim, stack, stdout, 0)
        return cls()


class CdrInstruction(MichelsonInstruction, prim='CDR'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        execute_cxr(cls.prim, stack, stdout, 1)
        return cls()


class ConcatInstruction(MichelsonInstruction, prim='CONCAT'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
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


class ConsInstruction(MichelsonInstruction, prim='CONS'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        elt, lst = cast(Tuple[MichelsonType, ListType], stack.pop2())
        assert isinstance(lst, ListType), f'expected list, got {lst.prim}'
        res = lst.prepend(elt)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [elt, lst], [res]))
        return cls()


class EmptyBigMapInstruction(MichelsonInstruction, prim='EMPTY_BIG_MAP', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        res = BigMapType.empty(key_type=cls.args[0], val_type=cls.args[1])
        res.attach_context(cls.context)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class EmptyMapInstruction(MichelsonInstruction, prim='EMPTY_MAP', args_len=2):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        res = MapType.empty(key_type=cls.args[0], val_type=cls.args[1])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class EmptySetInstruction(MichelsonInstruction, prim='EMPTY_SET', args_len=1):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        res = SetType.empty(item_type=cls.args[0])
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class GetInstruction(MichelsonInstruction, prim='GET'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        key, src = cast(Tuple[MichelsonType, Union[MapType, BigMapType]], stack.pop2())
        assert type(src) in  [MapType, BigMapType], f'unexpected {cls.prim}'
        val = src.get(key)
        if val is None:
            res = OptionType.none(src.args[0])
        else:
            res = OptionType.from_some(val)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [key, src], [res]))
        return cls()


class GetnInstruction(MichelsonInstruction, prim='GET', args_len=1):
    pass


@instruction(['LEFT', 'RIGHT'], args_len=1)
def do_left(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    if prim == 'LEFT':
        res = Or.left(r_type_expr=args[0], item=top)
    else:
        res = Or.right(l_type_expr=args[0], item=top)
    ctx.push(res, annots=annots)


@instruction('MEM')
def do_mem(ctx: Context, prim, args, annots):
    key, container = ctx.pop2()
    assert_stack_type(container, [Set, Map, BigMap])
    if type(container) == BigMap:
        res = Bool(ctx.big_maps.contains(container, key))
    else:
        res = Bool(key in container)
    ctx.push(res, annots=annots)


@instruction('NIL', args_len=1)
def do_nil(ctx: Context, prim, args, annots):
    nil = List.empty(args[0])
    ctx.push(nil, annots=annots)


@instruction('NONE', args_len=1)
def do_none(ctx: Context, prim, args, annots):
    none = Option.none(args[0])
    ctx.push(none, annots=annots)


@instruction('PACK')
def do_pack(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    res = Bytes(pack(top.val_expr, top.type_expr))
    ctx.push(res, annots=annots)


@instruction('PAIR')
def do_pair(ctx: Context, prim, args, annots):
    left, right = ctx.pop2()
    res = Pair.new(left, right)
    ctx.push(res, annots=annots)


@instruction('SIZE')
def do_size(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, [String, Bytes, List, Set, Map])
    res = Nat(len(top))
    ctx.push(res, annots=annots)


@instruction('SLICE')
def do_slice(ctx: Context, prim, args, annots):
    offset, length, s = ctx.pop3()
    assert_stack_type(s, [String, Bytes])
    offset, length = int(offset), int(length)
    if len(s) > 0 and offset + length <= len(s):
        res = Option.some(s[offset:offset+length])
    else:
        res = Option.none(type(s)().type_expr)
    ctx.push(res, annots=annots)


@instruction('SOME')
def do_some(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    res = Option.some(top)
    ctx.push(res, annots=annots)


@instruction('UNIT')
def do_unit(ctx: Context, prim, args, annots):
    ctx.push(Unit(), annots=annots)


@instruction('UNPACK', args_len=1)
def do_unpack(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Bytes)
    try:
        val_expr = unpack(data=bytes(top), type_expr=args[0])
        item = StackItem.parse(val_expr=val_expr, type_expr=args[0])
        res = Option.some(item)
    except Exception as e:
        ctx.print(f'failed: {e}')
        res = Option.none(args[0])
    ctx.push(res, annots=annots)


@instruction('UPDATE')
def do_update(ctx: Context, prim, args, annots):
    key, val, container = ctx.pop3()
    assert_stack_type(container, [Set, Map, BigMap])

    if type(container) == Set:
        assert_stack_type(val, Bool)
        if val:
            res = container.add(key)
        else:
            res = container.remove(key)
    else:
        assert_stack_type(val, Option)
        if val.is_none():
            res = container.remove(key)
        else:
            res = container.update(key, val.get_some())

    ctx.push(res, annots=annots)
