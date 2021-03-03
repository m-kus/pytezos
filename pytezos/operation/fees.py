from pytezos.operation.forge import forge_operation

hard_gas_limit_per_operation = 1040000
hard_storage_limit_per_operation = 60000
minimal_fees = 100
minimal_nanotez_per_byte = 1
minimal_nanotez_per_gas_unit = .1


def calculate_fee(content: dict, consumed_gas: int, extra_size: int, reserve=10) -> int:
    """ Calculate minimal required operation fee.

    :param content: operation content {..., "kind": "transaction", ... }
    :param consumed_gas: amount of gas consumed during the simulation (dry-run)
    :param extra_size: size of the additional operation data (branch, etc)
    :param reserve: safe reserve, just in case
    """
    size = len(forge_operation(content)) + extra_size
    fee = minimal_fees \
        + minimal_nanotez_per_byte * size \
        + int(minimal_nanotez_per_gas_unit * consumed_gas)
    return fee + reserve


def default_fee(content) -> int:
    """ Take hard gas limit instead of precise amount (no simulation) and calculate fee.

    :param content: operation content {..., "kind": "transaction", ... }
    """
    return calculate_fee(
        content=content,
        consumed_gas=default_gas_limit(content),
        extra_size=32 + 64 + 3 * 3  # branch, signature, fee:gas_limit:storage_limit mutez values (+3 bytes)
    )


def default_gas_limit(content) -> int:
    """ Get default gas limit by operation kind.

    :param content: operation content {..., "kind": "transaction", ... }
    """
    values = {
        'reveal': 1000,
        'delegation': 1000,
        'origination': hard_gas_limit_per_operation,
        'transaction': hard_gas_limit_per_operation if content.get('destination', '').startswith('KT') else 1427
    }
    return values.get(content['kind'])  # type: ignore


def default_storage_limit(content):
    """ Get default storage limit by operation kind.

    :param content: operation content {..., "kind": "transaction", ... }
    """
    values = {
        'reveal': 0,
        'delegation': 0,
        'origination': hard_storage_limit_per_operation,
        'transaction': hard_storage_limit_per_operation if content.get('destination', '').startswith('KT') else 257
    }
    return values.get(content['kind'])
