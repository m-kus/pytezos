from hashlib import sha256, sha512

from pytezos import crypto as crypto
from pytezos.repl.control import instruction
from pytezos.repl.context import Context
from pytezos.repl.types import assert_stack_type, Int, Nat, Timestamp, Mutez, Option, Pair, Bool, Bytes, Key, \
    Signature, KeyHash, dispatch_type_map


@instruction('ABS')
def do_abs(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Int)
    res = Nat(abs(int(top)))
    ctx.push(res, annots=annots)


@instruction('ADD')
def do_add(ctx: Context, prim, args, annots):
    a, b = ctx.pop2()
    res_type = dispatch_type_map(a, b, {
        (Nat, Nat): Nat,
        (Nat, Int): Int,
        (Int, Nat): Int,
        (Int, Int): Int,
        (Timestamp, Int): Timestamp,
        (Int, Timestamp): Timestamp,
        (Mutez, Mutez): Mutez
    })
    res = res_type(int(a) + int(b))
    ctx.push(res, annots=annots)


@instruction('COMPARE')
def do_compare(ctx: Context, prim, args, annots):
    a, b = ctx.pop2()
    res = Int(a.__cmp__(b))
    ctx.push(res, annots=annots)


@instruction('EDIV')
def do_ediv(ctx: Context, prim, args, annots):
    a, b = ctx.pop2()
    q_type, r_type = dispatch_type_map(a, b, {
        (Nat, Nat): (Nat, Nat),
        (Nat, Int): (Int, Nat),
        (Int, Nat): (Int, Nat),
        (Int, Int): (Int, Nat),
        (Mutez, Nat): (Mutez, Mutez),
        (Mutez, Mutez): (Nat, Mutez)
    })
    if int(b) == 0:
        res = Option.none(Pair.new(q_type(), r_type()).type_expr)
    else:
        q, r = divmod(int(a), int(b))
        if r < 0:
            r += abs(int(b))
            q += 1
        res = Option.some(Pair.new(q_type(q), r_type(r)))
    ctx.push(res, annots=annots)


@instruction(['EQ', 'GE', 'GT', 'LE', 'LT', 'NEQ'])
def do_eq(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Int)
    handlers = {
        'EQ': lambda x: x == 0,
        'GE': lambda x: x >= 0,
        'GT': lambda x: x > 0,
        'LE': lambda x: x <= 0,
        'LT': lambda x: x < 0,
        'NEQ': lambda x: x != 0
    }
    res = Bool(handlers[prim](int(top)))
    ctx.push(res, annots=annots)


@instruction('INT')
def do_int(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Nat)
    res = Int(int(top))
    ctx.push(res, annots=annots)


@instruction('ISNAT')
def do_is_nat(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Int)
    if int(top) >= 0:
        res = Option.some(Nat(int(top)))
    else:
        res = Option.none(Nat().type_expr)
    ctx.push(res, annots=annots)


@instruction(['LSL', 'LSR'])
def do_lsl(ctx: Context, prim, args, annots):
    a, b = ctx.pop2()
    assert_stack_type(a, Nat)
    assert_stack_type(b, Nat)
    assert int(b) < 257, f'shift overflow {int(b)}, should not exceed 256'
    handlers = {
        'LSL': lambda x: x[0] << x[1],
        'LSR': lambda x: x[0] >> x[1]
    }
    res = Nat(handlers[prim]((int(a), int(b))))
    ctx.push(res, annots=annots)


@instruction('MUL')
def do_mul(ctx: Context, prim, args, annots):
    a, b = ctx.pop2()
    res_type = dispatch_type_map(a, b, {
        (Nat, Nat): Nat,
        (Nat, Int): Int,
        (Int, Nat): Int,
        (Int, Int): Int,
        (Mutez, Nat): Mutez,
        (Nat, Mutez): Mutez
    })
    res = res_type(int(a) * int(b))
    ctx.push(res, annots=annots)


@instruction('NEG')
def do_neg(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, [Int, Nat])
    res = Int(-int(top))
    ctx.push(res, annots=annots)


@instruction('SUB')
def do_sub(ctx: Context, prim, args, annots):
    a, b = ctx.pop2()
    res_type = dispatch_type_map(a, b, {
        (Nat, Nat): Int,
        (Nat, Int): Int,
        (Int, Nat): Int,
        (Int, Int): Int,
        (Timestamp, Int): Timestamp,
        (Timestamp, Timestamp): Int,
        (Mutez, Mutez): Mutez
    })
    res = res_type(int(a) - int(b))
    ctx.push(res, annots=annots)


@instruction(['OR', 'XOR'])
def do_or_xor(ctx: Context, prim, args, annots):
    a, b = ctx.pop2()
    val_type, res_type = dispatch_type_map(a, b, {
        (Bool, Bool): (bool, Bool),
        (Nat, Nat): (int, Nat),
    })
    handlers = {
        'OR': lambda x: x[0] | x[1],
        'XOR': lambda x: x[0] ^ x[1]
    }
    res = res_type(handlers[prim]((val_type(a), val_type(b))))
    ctx.push(res, annots=annots)


@instruction('AND')
def do_and(ctx: Context, prim, args, annots):
    a, b = ctx.pop2()
    val_type, res_type = dispatch_type_map(a, b, {
        (Bool, Bool): (bool, Bool),
        (Nat, Nat): (int, Nat),
        (Int, Nat): (int, Nat),
        (Nat, Int): (int, Nat)
    })
    res = res_type(val_type(a) & val_type(b))
    ctx.push(res, annots=annots)


@instruction('NOT')
def do_not(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, [Nat, Int, Bool])
    if type(top) in [Nat, Int]:
        res = Int(~int(top))
    elif type(top) == Bool:
        res = Bool(not bool(top))
    else:
        assert False
    ctx.push(res, annots=annots)


@instruction('BLAKE2B')
def do_blake2b(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Bytes)
    res = Bytes(crypto.blake2b_32(bytes(top)).digest())
    ctx.push(res, annots=annots)


@instruction('CHECK_SIGNATURE')
def do_check_sig(ctx: Context, prim, args, annots):
    pk, sig, msg = ctx.pop3()
    assert_stack_type(pk, Key)
    assert_stack_type(sig, Signature)
    assert_stack_type(msg, Bytes)
    key = crypto.Key.from_encoded_key(str(pk))
    try:
        key.verify(signature=str(sig), message=bytes(msg))
    except:
        res = Bool(False)
    else:
        res = Bool(True)
    ctx.push(res, annots=annots)


@instruction('HASH_KEY')
def do_hash_key(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Key)
    key = crypto.Key.from_encoded_key(str(top))
    res = KeyHash.new(key.public_key_hash())
    ctx.push(res, annots=annots)


@instruction(['SHA256', 'SHA512'])
def do_sha(ctx: Context, prim, args, annots):
    top = ctx.pop1()
    assert_stack_type(top, Bytes)
    handlers = {
        'SHA256': lambda x: sha256(x).digest(),
        'SHA512': lambda x: sha512(x).digest(),
    }
    res = Bytes(handlers[prim](bytes(top)))
    ctx.push(res, annots=annots)
