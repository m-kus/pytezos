from pytezos.encoding import forge_address, forge_bool, forge_nat, forge_array, forge_public_key, \
    forge_base58
from pytezos.michelson.forge import forge_entrypoint, forge_micheline, forge_script

operation_tags = {
    'endorsement': 0,
    'proposal': 5,
    'ballot': 6,
    'seed_nonce_revelation': 1,
    'double_endorsement_evidence': 2,
    'double_baking_evidence': 3,
    'activate_account': 4,
    'reveal': 107,
    'transaction': 108,
    'origination': 109,
    'delegation': 110
}


def forge_operation(content) -> bytes:
    """ Forge operation content (locally).

    :param content: {.., "kind": "transaction", ...}
    """
    encode_content = {
        'activate_account': forge_activate_account,
        'reveal': forge_reveal,
        'transaction': forge_transaction,
        'origination': forge_origination,
        'delegation': forge_delegation
    }
    encode_proc = encode_content.get(content['kind'])
    if not encode_proc:
        raise NotImplementedError(content['kind'])

    return encode_proc(content)


def forge_operation_group(operation_group):
    """ Forge operation group (locally).

    :param operation_group: {"branch": "B...", "contents": [], ...}
    """
    res = forge_base58(operation_group['branch'])
    res += b''.join(map(forge_operation, operation_group['contents']))
    return res


def forge_activate_account(content: dict):
    res = forge_nat(operation_tags[content['kind']])
    res += forge_base58(content['pkh'])
    res += bytes.fromhex(content['secret'])
    return res


def forge_reveal(content):
    res = forge_nat(operation_tags[content['kind']])
    res += forge_address(content['source'], tz_only=True)
    res += forge_nat(int(content['fee']))
    res += forge_nat(int(content['counter']))
    res += forge_nat(int(content['gas_limit']))
    res += forge_nat(int(content['storage_limit']))
    res += forge_public_key(content['public_key'])
    return res


def forge_transaction(content):
    res = forge_nat(operation_tags[content['kind']])
    res += forge_address(content['source'], tz_only=True)
    res += forge_nat(int(content['fee']))
    res += forge_nat(int(content['counter']))
    res += forge_nat(int(content['gas_limit']))
    res += forge_nat(int(content['storage_limit']))
    res += forge_nat(int(content['amount']))
    res += forge_address(content['destination'])

    if content.get('parameters'):
        res += forge_bool(True)
        res += forge_entrypoint(content['parameters']['entrypoint'])
        res += forge_array(forge_micheline(content['parameters']['value']))
    else:
        res += forge_bool(False)

    return res


def forge_origination(content):
    res = forge_nat(operation_tags[content['kind']])
    res += forge_address(content['source'], tz_only=True)
    res += forge_nat(int(content['fee']))
    res += forge_nat(int(content['counter']))
    res += forge_nat(int(content['gas_limit']))
    res += forge_nat(int(content['storage_limit']))
    res += forge_nat(int(content['balance']))

    if content.get('delegate'):
        res += forge_bool(True)
        res += forge_address(content['delegate'], tz_only=True)
    else:
        res += forge_bool(False)

    res += forge_script(content['script'])

    return res


def forge_delegation(content):
    res = forge_nat(operation_tags[content['kind']])
    res += forge_address(content['source'], tz_only=True)
    res += forge_nat(int(content['fee']))
    res += forge_nat(int(content['counter']))
    res += forge_nat(int(content['gas_limit']))
    res += forge_nat(int(content['storage_limit']))

    if content.get('delegate'):
        res += forge_bool(True)
        res += forge_address(content['delegate'], tz_only=True)
    else:
        res += forge_bool(False)

    return res
