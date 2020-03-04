from os.path import isfile

from pytezos import Contract, pytezos
from pytezos.encoding import is_kt
from pytezos.michelson.converter import micheline_to_michelson
from pytezos.repl.control import instruction, do_interpret
from pytezos.repl.context import Context
from pytezos.repl.parser import get_int, get_string, get_bool, parse_prim_expr, get_entry_expr, assert_expr_equal
from pytezos.repl.types import Pair, Mutez, Address, ChainID, Timestamp, assert_stack_type, List

helpers_prim = ['DUMP', 'PRINT', 'DROP_ALL', 'EXPAND', 'RUN', 'PATCH',
                'INCLUDE', 'DEBUG', 'BIG_MAP_DIFF', 'BEGIN', 'COMMIT']
patch_prim = ['AMOUNT', 'BALANCE', 'CHAIN_ID', 'SENDER', 'SOURCE', 'NOW']


@instruction('DUMP', args_len=1)
def do_dump(ctx: Context, prim, args, annots):
    return ctx.dump(count=get_int(args[0]))


@instruction('DUMP')
def do_dump(ctx: Context, prim, args, annots):
    return ctx.dump(count=len(ctx))


@instruction('PRINT', args_len=1)
def do_print(ctx: Context, prim, args, annots):
    ctx.printf(template=f' {get_string(args[0])};')


@instruction('DEBUG', args_len=1)
def do_debug(ctx: Context, prim, args, annots):
    ctx.debug = get_bool(args[0])


@instruction('DROP_ALL')
def do_drop_all(ctx: Context, prim, args, annots):
    ctx.drop_all()


@instruction('EXPAND', args_len=1)
def do_expand(ctx: Context, prim, args, annots):
    return micheline_to_michelson(args[0])


@instruction('BEGIN', args_len=2)
def do_begin(ctx: Context, prim, args, annots):
    p_type_expr = ctx.get('parameter')
    assert p_type_expr, f'parameter type is not initialized'

    entrypoint = next((a for a in annots if a[0] == '%'), '%default')
    ctx.printf(f' use {entrypoint};')

    p_type_expr = get_entry_expr(p_type_expr, entrypoint)
    parameter = ctx.big_maps.pre_alloc(args[0], p_type_expr, copy=True)

    s_type_expr = ctx.get('storage')
    assert s_type_expr, f'storage type is not initialized'
    storage = ctx.big_maps.pre_alloc(args[1], s_type_expr)

    ctx.drop_all()
    run_input = Pair.new(parameter, storage)
    ctx.push(run_input, annots=annots)


@instruction('COMMIT')
def do_commit(ctx: Context, prim, args, annots):
    debug, ctx.debug = ctx.debug, False

    output = ctx.pop1()
    assert_stack_type(output, Pair)

    operations = output.get_element(0)
    assert_stack_type(operations, List)

    s_type_expr = ctx.get('storage')
    assert s_type_expr, f'storage type is not initialized'
    storage = output.get_element(1)
    assert_expr_equal(s_type_expr, storage.type_expr)

    storage, big_map_diff = ctx.big_maps.diff(storage)
    ctx.big_maps.commit(big_map_diff)

    res = Pair.new(operations, storage)
    ctx.push(res)
    ctx.debug = debug
    return operations, storage, big_map_diff


@instruction('RUN', args_len=2)
def do_run(ctx: Context, prim, args, annots):
    do_begin(ctx, prim, args, annots)

    code = ctx.get('code')
    assert code, f'code is not initialized'

    do_interpret(ctx, code)
    return do_commit(ctx, prim, args=[], annots=[])


@instruction('PATCH', args_len=2)
def do_patch(ctx: Context, prim, args, annots):
    key, _ = parse_prim_expr(args[0])
    assert key in patch_prim, f'expected one of {", ".join(patch_prim)}, got {args[0]}'
    if key in ['AMOUNT', 'BALANCE']:
        res = Mutez(get_int(args[1]))
    elif key == 'NOW':
        res = Timestamp(get_int(args[1]))
    elif key in ['SOURCE', 'SENDER', 'ADDRESS']:
        res = Address.new(get_string(args[1]))
    elif key == 'CHAIN_ID':
        res = ChainID(get_string(args[1]))
    else:
        assert False
    ctx.set(key, res)


@instruction('PATCH', args_len=1)
def do_unset(ctx: Context, prim, args, annots):
    key, _ = parse_prim_expr(args[0])
    assert key in patch_prim, f'expected one of {", ".join(patch_prim)}, got {args[0]}'
    ctx.unset(key)


@instruction('INCLUDE', args_len=1)
def do_include(ctx: Context, prim, args, annots):
    path = get_string(args[0])

    if isfile(path):
        code = Contract.from_file(path).code
    else:
        parts = path.split('%')
        address, network = parts[0], parts[1] if len(parts) > 1 else 'mainnet'
        assert is_kt(address), f'expected filename or KT address (with network), got {path}'
        code = pytezos.using(network).contract(address).contract.code

    do_interpret(ctx, code)


@instruction('BIG_MAP_DIFF')
def do_big_map_diff(ctx: Context, prim, args, annots):
    top = ctx.peek()
    _, big_map_diff = ctx.big_maps.diff(top)
    return big_map_diff
