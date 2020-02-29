from pytezos.crypto import blake2b_32
from pytezos.encoding import forge_base58, forge_address, forge_public_key, forge_contract, forge_timestamp, \
    base58_encode
from pytezos.michelson.forge import forge_micheline, unforge_micheline
from pytezos.repl.parser import parse_prim_expr


def prepack_micheline(val_expr, type_expr):
    def try_pack(val_node, type_node):
        type_prim, type_args = parse_prim_expr(type_node)
        is_string = isinstance(val_node, dict) and val_node.get('string')

        if type_prim in ['set', 'list']:
            val_node = [try_pack(i, type_args[0]) for i in val_node]
        elif type_prim in ['map', 'big_map']:
            val_node = [{'prim': 'Elt', 'args': [try_pack(elt['args'][i], type_args[i]) for i in [0, 1]]}
                        for elt in val_node]
        elif type_prim == 'pair':
            val_node['args'] = [try_pack(val_node['args'][i], type_args[i]) for i in [0, 1]]
        elif type_prim == 'option':
            if val_node['prim'] == 'Some':
                val_node['args'] = [try_pack(val_node['args'][0], type_args[0])]
        elif type_prim == 'or':
            type_idx = 0 if val_node['prim'] == 'Left' else 1
            val_node['args'] = [try_pack(val_node['args'][0], type_args[type_idx])]
        elif type_prim == 'lambda':
            pass  # TODO: PUSH, SELF, CONTRACT
        elif type_prim == 'chain_id' and is_string:
            return {'bytes': forge_base58(val_node['string']).hex()}
        elif type_prim == 'signature' and is_string:
            return {'bytes': forge_base58(val_node['string']).hex()}
        elif type_prim == 'key_hash' and is_string:
            return {'bytes': forge_address(val_node['string'], tz_only=True).hex()}
        elif type_prim == 'key' and is_string:
            return {'bytes': forge_public_key(val_node['string']).hex()}
        elif type_prim == 'address' and is_string:
            return {'bytes': forge_address(val_node['string']).hex()}
        elif type_prim == 'contract' and is_string:
            return {'bytes': forge_contract(val_node['string']).hex()}
        elif type_prim == 'timestamp' and is_string:
            return {'int': forge_timestamp(val_node['string'])}

        return val_node

    return try_pack(val_expr, type_expr)


def pack(val_expr, type_expr):
    data = prepack_micheline(val_expr, type_expr)
    return b'\x05' + forge_micheline(data)


def get_key_hash(val_expr, type_expr):
    data = blake2b_32(pack(val_expr, type_expr)).digest()
    return base58_encode(data, b'expr').decode()


def unpack(data: bytes, type_expr):
    assert data.startswith(b'\x05'), f'packed data should start with 05'
    parsed = unforge_micheline(data[1:])
    return parsed
