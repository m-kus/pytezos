from datetime import datetime
import secrets

from pytezos import pytezos
from pytezos.encoding import parse_address
from pytezos.repl.control import instruction
from pytezos.repl.context import Context
from pytezos.repl.types import assert_stack_type, Mutez, ChainID, Address, Contract, Option, assert_equal_types, \
    KeyHash, Timestamp, expr_equal, Operation
from pytezos.repl.parser import get_entry_expr

MAINNET_CHAIN_ID = 'NetXdQprcVkpaWU'
UNIT_TYPE_EXPR = {'prim': 'unit'}
SELF_ADDRESS = 'KT1VG2WtYdSWz5E7chTeAdDPZNy2MpP8pTfL'


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
    ctx.push(res, annots=annots)


@instruction('BALANCE')
def do_balance(ctx: Context, prim, args, annots):
    res = ctx.get('BALANCE', Mutez(0))
    ctx.push(res, annots=annots)


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
    res = Contract.new(SELF_ADDRESS + entry_annot, type_expr=p_type_expr)
    ctx.push(res, annots=[a for a in annots if a[0] != '%'])


@instruction('SENDER')
def do_sender(ctx: Context, prim, args, annots):
    res = ctx.get('SENDER')
    assert res, f'SENDER is not initialized'
    ctx.push(res, annots=annots)


@instruction('SOURCE')
def do_source(ctx: Context, prim, args, annots):
    res = ctx.get('SOURCE')
    assert res, f'SOURCE is not initialized'
    ctx.push(res, annots=annots)


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
    ctx.push(res, annots=annots)


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

    ctx.push(res, annots=[a for a in annots if a[0] != '%'])


@instruction('IMPLICIT_ACCOUNT')
def do_implicit_account(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, KeyHash)
    res = Contract.new(str(top), type_expr=UNIT_TYPE_EXPR)
    ctx.push(res, annots=annots)


def decrease_balance(ctx: Context, amount: Mutez):
    balance = ctx.get('BALANCE', Mutez(0))
    assert int(amount) <= int(balance), f'needed {int(amount)} utz, got only {int(balance)} utz'
    ctx.set('BALANCE', Mutez(int(balance) - int(amount)))


def generate_address():
    return parse_address(b''.join([b'\x01', secrets.token_bytes(20), b'\x00']))


@instruction('CREATE_CONTRACT', args_len=3)
def do_create_contract(ctx: Context, prim, args, annots):
    delegate, amount, storage = ctx.pop3()

    assert_stack_type(amount, Mutez)
    decrease_balance(ctx, amount)

    assert_stack_type(delegate, Option)
    assert_equal_types(args[0], storage.type_expr)

    content = {
        'kind': 'origination',
        'source': SELF_ADDRESS,
        'balance': str(int(amount)),
        'script': {
            'storage': storage.val_expr,
            'code': args[2]
        }
    }

    if not delegate.is_none():
        content['delegate'] = str(delegate.get_some())

    contract = Contract.new(generate_address(), type_expr=args[1])
    orig = Operation.new(content)
    ctx.push(contract)
    ctx.push(orig)


@instruction('SET_DELEGATE')
def do_set_delegate(ctx: Context, prim, args, annots):
    delegate = ctx.pop1()
    assert_stack_type(delegate, Option)

    content = {
        'kind': 'delegation',
        'source': SELF_ADDRESS,
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
        'source': SELF_ADDRESS,
        'amount': str(int(amount)),
        'destination': dest.get_address(),
        'parameters': {
            'entrypoint': dest.get_entrypoint(),
            'value': param.val_expr
        }
    }
    res = Operation.new(content)
    ctx.push(res)
