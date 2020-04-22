from os.path import isfile

from pytezos import Contract
from pytezos.interop import Interop
from pytezos.encoding import is_kt
from pytezos.repl.control import instruction, do_interpret
from pytezos.repl.context import Context
from pytezos.repl.parser import get_int, get_string, get_bool, parse_prim_expr, restore_entry_expr, assert_expr_equal
from pytezos.repl.types import Pair, Mutez, Address, ChainID, Timestamp, assert_stack_type, List, Operation

networks = ['mainnet', 'zeronet', 'babylonnet', 'carthagenet']
helpers_prim = ['DUMP', 'PRINT', 'DROP_ALL', 'EXPAND', 'RUN', 'PATCH', 'INCLUDE',
                'DEBUG', 'BIG_MAP_DIFF', 'BEGIN', 'COMMIT', 'RESET', 'STORAGE']
patch_prim = ['AMOUNT', 'BALANCE', 'CHAIN_ID', 'SENDER', 'SOURCE', 'NOW']


def is_prim(val_expr, prim):
    return isinstance(val_expr, dict) and val_expr.get('prim') == prim


@instruction('DUMP', args_len=1)
def do_dump(ctx: Context, prim, args, annots):
    res = ctx.dump(count=get_int(args[0]))
    if res:
        return {'kind': 'stack', 'stack': res}
    else:
        return {'kind': 'message', 'value': 'stack is empty'}


@instruction('DUMP')
def do_dump_all(ctx: Context, prim, args, annots):
    return do_dump(ctx, prim, args=[{'int': str(len(ctx))}], annots=annots)


@instruction('PRINT', args_len=1)
def do_print(ctx: Context, prim, args, annots):
    ctx.printf(template=get_string(args[0]))


@instruction('DEBUG', args_len=1)
def do_debug(ctx: Context, prim, args, annots):
    ctx.debug = get_bool(args[0])


@instruction('DROP_ALL')
def do_drop_all(ctx: Context, prim, args, annots):
    ctx.drop_all()


@instruction('EXPAND', args_len=1)
def do_expand(ctx: Context, prim, args, annots):
    return {'kind': 'code', 'code': args[0]}


@instruction('BEGIN', args_len=2)
def do_begin(ctx: Context, prim, args, annots):
    p_type_expr = ctx.get('parameter')
    assert p_type_expr, f'parameter type is not initialized'

    entrypoint = next((a for a in annots if a[0] == '%'), '%default')
    ctx.print(f'use {entrypoint}')

    network = ctx.get('NETWORK')
    if network:
        ctx.print(f'use {network}')

    p_val_expr = restore_entry_expr(val_expr=args[0], type_expr=p_type_expr, field_annot=entrypoint)
    parameter = ctx.big_maps.pre_alloc(p_val_expr, p_type_expr, copy=True, network=network)

    s_type_expr = ctx.get('storage')
    assert s_type_expr, f'storage type is not initialized'
    s_val_expr = ctx.get('STORAGE') if is_prim(args[1], 'STORAGE') else args[1]
    storage = ctx.big_maps.pre_alloc(s_val_expr, s_type_expr, network=network)

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
    assert operations.val_type() == Operation, f'expected list of operations'

    s_type_expr = ctx.get('storage')
    assert s_type_expr, f'storage type is not initialized'
    storage = output.get_element(1)
    assert_expr_equal(s_type_expr, storage.type_expr)

    storage, big_map_diff = ctx.big_maps.diff(storage)
    ctx.big_maps.commit(big_map_diff)

    res = Pair.new(operations, storage)
    ctx.push(res)
    ctx.debug = debug
    return {'kind': 'output',
            'operations': operations,
            'storage': storage,
            'big_map_diff': big_map_diff}


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
    elif key in ['SOURCE', 'SENDER']:
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
        parts = path.split(':')
        network = parts[0] if len(parts) > 1 else ctx.get('NETWORK', 'mainnet')
        address = parts[1] if len(parts) > 1 else parts[0]
        assert is_kt(address), f'expected filename or KT address (with network), got {path}'
        script = Interop().using(network).shell.contracts[address].script()
        code = script['code']
        ctx.set('STORAGE', script['storage'])

    do_interpret(ctx, code)


@instruction('BIG_MAP_DIFF')
def do_big_map_diff(ctx: Context, prim, args, annots):
    top = ctx.peek()
    _, big_map_diff = ctx.big_maps.diff(top)
    return {'kind': 'big_map_diff', 'big_map_diff': big_map_diff}


@instruction('RESET')
def do_reset_none(ctx: Context, prim, args, annots):
    ctx.unset('NETWORK')
    ctx.unset('CHAIN_ID')
    ctx.big_maps.reset()
    ctx.drop_all()


@instruction('RESET', args_len=1)
def do_reset(ctx: Context, prim, args, annots):
    network = get_string(args[0])
    assert network in networks, f'expected on of {", ".join(networks)}, got {network}'
    ctx.set('NETWORK', network)
    chain_id = ChainID(Interop().using(network).shell.chains.main.chain_id())
    ctx.set('CHAIN_ID', chain_id)
    ctx.big_maps.reset()
    ctx.drop_all()
