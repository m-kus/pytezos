from datetime import datetime

from pytezos import pytezos
from pytezos.repl.control import instruction
from pytezos.repl.context import Context
from pytezos.repl.types import assert_stack_type, Mutez, ChainID, Address, Contract, Option, assert_equal_types, \
    KeyHash, Timestamp, expr_equal, Operation
from pytezos.repl.parser import get_entry_expr

INITIAL_BALANCE = 257000000
MAINNET_CHAIN_ID = 'NetXdQprcVkpaWU'
UNIT_TYPE_EXPR = {'prim': 'unit'}


def get_network_by_chain_id(chain_id: ChainID):
    networks = {
        MAINNET_CHAIN_ID: 'mainnet'
    }
    key = str(chain_id)
    assert key in networks, f'unknown chain_id {key}'
    return networks[key]


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
    ctx.push(res, annots=annots)


@instruction('SELF')
def do_self(ctx: Context, prim, args, annots):
    p_type_expr = ctx.get('parameter')
    assert p_type_expr, f'parameter type is not initialized'

    entry_annot = next((a for a in annots if a[0] == '%'), '%default')
    ctx.printf(f' use {entry_annot};')

    p_type_expr = get_entry_expr(p_type_expr, entry_annot)
    res = Contract.new(ctx.dummy_gen.self + entry_annot, type_expr=p_type_expr)
    ctx.push(res, annots=['@self'])


@instruction('SENDER')
def do_sender(ctx: Context, prim, args, annots):
    res = ctx.get('SENDER')
    assert res, f'SENDER is not initialized'
    ctx.push(res, annots=['@sender'])


@instruction('SOURCE')
def do_source(ctx: Context, prim, args, annots):
    res = ctx.get('SOURCE')
    assert res, f'SOURCE is not initialized'
    ctx.push(res, annots=['@source'])


@instruction('NOW')
def do_now(ctx: Context, prim, args, annots):
    res = ctx.get('NOW')
    if not res:
        chain_id = ctx.get('CHAIN_ID')
        if chain_id:
            now = pytezos.using(get_network_by_chain_id(chain_id)).now()
        else:
            now = int(datetime.utcnow().timestamp())
        res = Timestamp(now)
    ctx.push(res, annots=['@now'])


def check_contract(ctx: Context, address, entry_annot, type_expr):
    chain_id = ctx.get('CHAIN_ID')
    if not chain_id:
        ctx.printf(' skip check;')
        return True

    network = get_network_by_chain_id(chain_id)

    try:
        ci = pytezos.using(network).contract(address)
        actual = get_entry_expr(ci.contract.parameter.code, entry_annot)
        if expr_equal(type_expr, actual):
            return True
        else:
            ctx.printf(' entry type mismatch;')
    except Exception:
        ctx.printf(' not found;')

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

    content = {
        'kind': 'origination',
        'source': ctx.dummy_gen.self,
        'balance': str(int(amount)),
        'script': {
            'storage': storage.val_expr,
            'code': code
        }
    }

    if not delegate.is_none():
        content['delegate'] = str(delegate.get_some())

    originated_address = Address.new(ctx.dummy_gen.get_fresh_address())
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
