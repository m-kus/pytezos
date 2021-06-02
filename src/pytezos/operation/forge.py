from typing import Any, Dict

from pytezos.michelson.forge import (
    forge_address,
    forge_array,
    forge_base58,
    forge_bool,
    forge_int,
    forge_int16,
    forge_int32,
    forge_micheline,
    forge_nat,
    forge_public_key,
    forge_script,
)
from pytezos.rpc.kind import operation_tags

reserved_entrypoints = {
    'default': b'\x00',
    'root': b'\x01',
    'do': b'\x02',
    'set_delegate': b'\x03',
    'remove_delegate': b'\x04',
}


def has_parameters(content: Dict[str, Any]) -> bool:
    if content.get('parameters'):
        if content['parameters']['entrypoint'] == 'default' and content['parameters']['value'] == {'prim': 'Unit'}:
            return False
        return True
    return False


def forge_entrypoint(entrypoint) -> bytes:
    """Encode Michelson contract entrypoint into the byte form.

    :param entrypoint: string
    """
    if entrypoint in reserved_entrypoints:
        return reserved_entrypoints[entrypoint]
    else:
        return b'\xff' + forge_array(entrypoint.encode(), len_bytes=1)


def forge_operation(content: Dict[str, Any]) -> bytes:
    """Forge operation content (locally).

    :param content: {.., "kind": "transaction", ...}
    """
    encode_content = {
        'failing_noop': forge_failing_noop,
        'activate_account': forge_activate_account,
        'reveal': forge_reveal,
        'transaction': forge_transaction,
        'origination': forge_origination,
        'delegation': forge_delegation,
        'endorsement': forge_endorsement,
        'endorsement_with_slot': forge_endorsement_with_slot,
    }
    encode_proc = encode_content.get(content['kind'])
    if not encode_proc:
        raise NotImplementedError(content['kind'])

    return encode_proc(content)


def forge_operation_group(operation_group: Dict[str, Any]) -> bytes:
    """Forge operation group (locally).

    :param operation_group: {"branch": "B...", "contents": [], ...}
    """
    res = forge_base58(operation_group['branch'])
    res += b''.join(map(forge_operation, operation_group['contents']))
    return res


def forge_activate_account(content: Dict[str, Any]) -> bytes:
    res = forge_nat(operation_tags[content['kind']])
    res += forge_base58(content['pkh'])
    res += bytes.fromhex(content['secret'])
    return res


def forge_reveal(content: Dict[str, Any]) -> bytes:
    res = forge_nat(operation_tags[content['kind']])
    res += forge_address(content['source'], tz_only=True)
    res += forge_nat(int(content['fee']))
    res += forge_nat(int(content['counter']))
    res += forge_nat(int(content['gas_limit']))
    res += forge_nat(int(content['storage_limit']))
    res += forge_public_key(content['public_key'])
    return res


def forge_transaction(content: Dict[str, Any]) -> bytes:
    res = forge_nat(operation_tags[content['kind']])
    res += forge_address(content['source'], tz_only=True)
    res += forge_nat(int(content['fee']))
    res += forge_nat(int(content['counter']))
    res += forge_nat(int(content['gas_limit']))
    res += forge_nat(int(content['storage_limit']))
    res += forge_nat(int(content['amount']))
    res += forge_address(content['destination'])

    if has_parameters(content):
        res += forge_bool(True)
        res += forge_entrypoint(content['parameters']['entrypoint'])
        res += forge_array(forge_micheline(content['parameters']['value']))
    else:
        res += forge_bool(False)

    return res


def forge_origination(content: Dict[str, Any]) -> bytes:
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


def forge_delegation(content: Dict[str, Any]) -> bytes:
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


def forge_endorsement(content: Dict[str, Any]) -> bytes:
    res = forge_nat(operation_tags[content['kind']])
    res += forge_int32(int(content['level']))
    return res


def forge_inline_endorsement(content: Dict[str, Any]) -> bytes:
    res = forge_base58(content['branch'])
    res += forge_nat(operation_tags[content['operations']['kind']])
    res += forge_int32(int(content['operations']['level']))
    res += forge_base58(content['signature'])
    return res


def forge_endorsement_with_slot(content: Dict[str, Any]) -> bytes:
    res = forge_nat(operation_tags[content['kind']])
    res += forge_array(forge_inline_endorsement(content['endorsement']))
    res += forge_int16(content['slot'])
    return res


def forge_failing_noop(content: Dict[str, Any]) -> bytes:
    res = forge_nat(operation_tags[content['kind']])
    res += forge_array(content['arbitrary'].encode())
    return res
