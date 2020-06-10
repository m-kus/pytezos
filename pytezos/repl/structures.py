from pytezos.michelson.pack import pack
from pytezos.repl.control import instruction
from pytezos.repl.context import Context
from pytezos.repl.types import assert_stack_type, Option, Pair, String, Bytes, List, BigMap, Map, Set, Or, Bool, Nat, \
    Unit, StackItem, dispatch_type_map
from pytezos.michelson.pack import unpack


@instruction(['CAR', 'CDR'])
def do_car(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Pair)
    idx = {'CAR': 0, 'CDR': 1}
    res = top.get_element(idx[prim])
    ctx.push(res, annots=annots)


@instruction('CONCAT')
def do_concat(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, [String, Bytes, List])
    if type(top) in [String, Bytes]:
        second = ctx.pop1()
        val_type = dispatch_type_map(top, second, {
            (String, String): str,
            (Bytes, Bytes): bytes
        })
        res = type(top)(val_type(top) + val_type(second))
    elif type(top) == List:
        res_type = top.val_type()
        val_type, sep = {
            String: (str, ''),
            Bytes: (bytes, b'')
        }[res_type]
        res = res_type(sep.join(map(val_type, top)))
    else:
        assert False
    ctx.push(res, annots=annots)


@instruction('CONS')
def do_cons(ctx: Context, prim, args, annots):
    val, container = ctx.pop2()
    assert_stack_type(container, List)
    res = container.prepend(val)
    ctx.push(res, annots=annots)


@instruction('EMPTY_BIG_MAP', args_len=2)
def do_empty_big_map(ctx: Context, prim, args, annots):
    res = ctx.big_maps.empty(k_type_expr=args[0], v_type_expr=args[1])
    ctx.push(res, annots=annots)


@instruction('EMPTY_MAP', args_len=2)
def do_empty_map(ctx: Context, prim, args, annots):
    res = Map.empty(k_type_expr=args[0], v_type_expr=args[1])
    ctx.push(res, annots=annots)


@instruction('EMPTY_SET', args_len=1)
def do_empty_set(ctx: Context, prim, args, annots):
    res = Set.empty(k_type_expr=args[0])
    ctx.push(res, annots=annots)


@instruction('GET')
def do_get(ctx: Context, prim, args, annots):
    key, container = ctx.pop2()
    assert_stack_type(container, [Map, BigMap])

    if type(container) == Map:
        val = container.find(key)
    else:
        val = ctx.big_maps.find(container, key)

    if val is not None:
        res = Option.some(val)
    else:
        res = Option.none(container.val_type_expr())

    ctx.push(res, annots=annots)


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
