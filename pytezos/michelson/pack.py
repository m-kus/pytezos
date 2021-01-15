from pytezos.crypto.encoding import base58_encode
from pytezos.crypto.key import blake2b_32
from pytezos.michelson.forge import unforge_micheline, unforge_public_key, unforge_chain_id, unforge_signature, \
    unforge_address
from pytezos.michelson.format import micheline_to_michelson


def micheline_value_to_python_object(val_expr):
    if isinstance(val_expr, dict):
        if len(val_expr) == 1:
            prim = next(iter(val_expr))
            if prim == 'string':
                return val_expr[prim]
            elif prim == 'int':
                return int(val_expr[prim])
            elif prim == 'bytes':
                return blind_unpack(bytes.fromhex(val_expr[prim]))
            elif prim == 'bool':
                return True if val_expr[prim] == 'True' else False
        elif val_expr.get('prim'):
            prim = val_expr['prim']
            if prim == 'Pair':
                return tuple(micheline_value_to_python_object(x) for x in val_expr['args'])
    return micheline_to_michelson(val_expr)


def blind_unpack(data: bytes):
    try:
        return unforge_chain_id(data)
    except ValueError:
        pass
    try:
        return unforge_address(data)
    except (ValueError, KeyError):
        pass
    try:
        return unforge_public_key(data)
    except (ValueError, KeyError):
        pass
    try:
        return unforge_signature(data)
    except ValueError:
        pass

    if len(data) > 0 and data.startswith(b'\x05'):
        try:
            res = unforge_micheline(data[1:])
            return micheline_value_to_python_object(res)
        except (ValueError, AssertionError):
            pass

    try:
        return data.decode()
    except ValueError:
        pass

    return data


def get_key_hash(packed_key: bytes) -> str:
    data = blake2b_32(packed_key).digest()
    return base58_encode(data, b'expr').decode()
