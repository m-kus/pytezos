from datetime import datetime

from pytezos.interop import Interop
from pytezos.repl.control import instruction
from pytezos.repl.context import Context
from pytezos.repl.types import assert_stack_type, Mutez, ChainID, Address, Contract, Option, assert_equal_types, \
    KeyHash, Timestamp, expr_equal, Operation
from pytezos.repl.parser import get_entry_expr

INITIAL_BALANCE = 257000000
MAINNET_CHAIN_ID = 'NetXdQprcVkpaWU'
UNIT_TYPE_EXPR = {'prim': 'unit'}


@instruction('parameter', args_len=1)
def do_parameter(ctx: Context, prim, args, annots):
    ctx.set('parameter', args[0])


@instruction('storage', args_len=1)
def do_parameter(ctx: Context, prim, args, annots):
    ctx.set('storage', args[0])


@instruction('code', args_len=1)
def do_parameter(ctx: Context, prim, args, annots):
    ctx.set('code', args[0])


@instruction('AMOUNT')
def do_amount(ctx: Context, prim, args, annots):
    res = ctx.get('AMOUNT', Mutez(0))
    ctx.push(res, annots=['@amount'])


def get_balance(ctx: Context):
    res = ctx.get('BALANCE')
    if res is None:
        res = Mutez(INITIAL_BALANCE)
        ctx.set('BALANCE', res)
    return res


@instruction('BALANCE')
def do_balance(ctx: Context, prim, args, annots):
    res = get_balance(ctx)
    ctx.push(res, annots=['@balance'])


@instruction('CHAIN_ID')
def do_chain_id(ctx: Context, prim, args, annots):
    res = ctx.get('CHAIN_ID', ChainID(MAINNET_CHAIN_ID))
    ctx.push(res, annots=[f'@{ctx.get("NETWORK", "mainnet")}'])


@instruction('SELF')
def do_self(ctx: Context, prim, args, annots):
    p_type_expr = ctx.get('parameter')
    assert p_type_expr, f'parameter type is not initialized'

    entry_annot = next((a for a in annots if a[0] == '%'), '%default')
    ctx.print(f'use {entry_annot}')

    p_type_expr, _ = get_entry_expr(p_type_expr, entry_annot)
    res = Contract.new(ctx.dummy_gen.self + entry_annot, type_expr=p_type_expr)
    ctx.push(res, annots=['@self'])


@instruction('SENDER')
def do_sender(ctx: Context, prim, args, annots):
    res = ctx.get('SENDER')
    assert res is not None, f'SENDER is not initialized'
    ctx.push(res, annots=['@sender'])


@instruction('SOURCE')
def do_source(ctx: Context, prim, args, annots):
    res = ctx.get('SOURCE')
    assert res is not None, f'SOURCE is not initialized'
    ctx.push(res, annots=['@source'])


@instruction('NOW')
def do_now(ctx: Context, prim, args, annots):
    res = ctx.get('NOW')
    if res is None:
        network = ctx.get('NETWORK')
        if network:
            interop = Interop().using(network)
            constants = interop.shell.block.context.constants()  # cached
            ts = interop.shell.head.header()['timestamp']
            dt = datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ')
            first_delay = constants['time_between_blocks'][0]
            return int((dt - datetime(1970, 1, 1)).total_seconds()) + int(first_delay)
        else:
            now = int(datetime.utcnow().timestamp())
        res = Timestamp(now)
    ctx.push(res, annots=['@now'])


def check_contract(ctx: Context, address, entry_annot, type_expr):
    network = ctx.get('NETWORK')
    if not network:
        ctx.print('skip check')
        return True
    try:
        script = Interop().using(network).shell.contracts[address].script()
        p_type_expr = next(s for s in script['code'] if s['prim'] == 'parameter')
        actual, _ = get_entry_expr(p_type_expr, entry_annot)
        if expr_equal(type_expr, actual):
            return True
        else:
            ctx.print('entry type mismatch')
    except Exception:
        ctx.print('not found')

    return False


@instruction('ADDRESS')
def do_address(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Contract)
    res = Address.new(top.get_address())
    if top.name:
        annots.append(f'@{top.name}.address')
    ctx.push(res, annots=annots)


@instruction('CONTRACT', args_len=1)
def do_contract(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Address)

    entry_annot = next((a for a in annots if a[0] == '%'), '%default')
    contract = Contract.new(str(top) + entry_annot, type_expr=args[0])

    if check_contract(ctx, address=str(top), entry_annot=entry_annot, type_expr=args[0]):
        res = Option.some(contract)
    else:
        res = Option.none(contract.type_expr)

    if top.name:
        annots.append(f'@{top.name}.contract')
    ctx.push(res, annots=[a for a in annots if a[0] != '%'])


@instruction('IMPLICIT_ACCOUNT')
def do_implicit_account(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, KeyHash)
    res = Contract.new(str(top), type_expr=UNIT_TYPE_EXPR)
    ctx.push(res, annots=annots)


def decrease_balance(ctx: Context, amount: Mutez):
    balance = get_balance(ctx)
    if int(balance) > 0:
        assert int(amount) <= int(balance), f'needed {int(amount)} utz, got only {int(balance)} utz'
        ctx.set('BALANCE', Mutez(int(balance) - int(amount)))


@instruction('CREATE_CONTRACT', args_len=1)
def do_create_contract(ctx: Context, prim, args, annots):
    assert len(args[0]) == 3, 'expected { parameter ; storage ; code }'
    parameter_type, storage_type, code = args[0]
    delegate, amount, storage = ctx.pop3()

    assert_stack_type(amount, Mutez)
    decrease_balance(ctx, amount)

    assert_stack_type(delegate, Option)
    assert_equal_types(storage_type, storage.type_expr)

    originated_address = Address.new(ctx.dummy_gen.get_fresh_address())
    content = {
        'kind': 'origination',
        'source': ctx.dummy_gen.self,
        'balance': str(int(amount)),
        'script': {
            'storage': storage.val_expr,
            'code': code
        },
        'originated_contract': str(originated_address)
    }

    if not delegate.is_none():
        content['delegate'] = str(delegate.get_some())

    orig = Operation.new(content)
    ctx.push(originated_address)
    ctx.push(orig)


@instruction('SET_DELEGATE')
def do_set_delegate(ctx: Context, prim, args, annots):
    delegate = ctx.pop1()
    assert_stack_type(delegate, Option)

    content = {
        'kind': 'delegation',
        'source': ctx.dummy_gen.self,
        'delegate': None if delegate.is_none() else str(delegate.get_some())
    }
    res = Operation.new(content)
    ctx.push(res)


@instruction('TRANSFER_TOKENS')
def do_transfer_tokens(ctx: Context, prim, args, annots):
    param, amount, dest = ctx.pop3()

    assert_stack_type(amount, Mutez)
    decrease_balance(ctx, amount)

    assert_stack_type(dest, Contract)
    dest.assert_param_type(param)

    content = {
        'kind': 'transaction',
        'source': ctx.dummy_gen.self,
        'amount': str(int(amount)),
        'destination': dest.get_address(),
        'parameters': {
            'entrypoint': dest.get_entrypoint(),
            'value': param.val_expr
        }
    }
    res = Operation.new(content)
    ctx.push(res)
