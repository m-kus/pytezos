from os.path import join
from pytezos.encoding import parse_address, parse_public_key, parse_signature, parse_chain_id


def dummy_micheline(schema: dict, root_path='/'):
    """

    :param schema:
    :param root_path:
    :return: Micheline value expression
    """

    def encode_node(type_path):
        prim = schema[type_path]['prim']
        if prim == 'option':
            return dict(prim='None')
        elif prim in ['pair', 'tuple']:
            args_len = schema[type_path]['args_len']
            return dict(
                prim='Pair',
                args=list(map(lambda x: encode_node(join(type_path, x)), range(args_len)))
            )
        elif prim in ['or', 'union', 'enum']:
            return dict(
                prim='Left',
                args=[encode_node(join(type_path, '0'))]
            )
        elif prim in ['map', 'big_map', 'set', 'list']:
            return []
        elif prim in ['int', 'nat', 'mutez', 'timestamp']:
            return {'int': '0'}
        elif prim in ['string', 'bytes']:
            return {'string': ''}
        elif prim == 'bool':
            return {'prim': 'False'}
        elif prim == 'unit':
            return {'prim': 'Unit'}
        elif prim == 'address':
            return {'string': parse_address(b'\x00' * 22)}
        elif prim == 'key':
            return {'string': parse_public_key(b'\x00' * 33)}
        elif prim == 'key_hash':
            return {'string': parse_address(b'\x00' * 21)}
        elif prim == 'signature':
            return {'string': parse_signature(b'\x00' * 64)}
        elif prim == 'chain_id':
            return {'string': parse_chain_id(b'\x00' * 4)}
        else:
            raise ValueError(f'Cannot create dummy value for `{prim}` at `{type_path}`')

    return encode_node(root_path)
