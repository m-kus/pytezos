from typing import Any, Dict, Optional

from pytezos.operation.forge import forge_operation

# NOTE: Correct for PtEdo2Zk
DEFAULT_CONSTANTS = dict(
    hard_gas_limit_per_operation=1040000,
    hard_storage_limit_per_operation=60000,
)
DEFAULT_TRANSACTION_GAS_LIMIT = 1427
DEFAULT_TRANSACTION_STORAGE_LIMIT = 257
MINIMAL_FEES = 100
MINIMAL_MUTEZ_PER_BYTE = 1
MINIMAL_MUTEZ_PER_GAS_UNIT = 0.1


def calculate_fee(
    content: Dict[str, Any],
    consumed_gas: int,
    extra_size: int,
    reserve=10,
) -> int:
    """Calculate minimal required operation fee.

    :param content: operation content {..., "kind": "transaction", ... }
    :param consumed_gas: amount of gas consumed during the simulation (dry-run)
    :param extra_size: size of the additional operation data (branch, etc)
    :param reserve: safe reserve, just in case
    """
    size = len(forge_operation(content)) + extra_size
    fee = MINIMAL_FEES + MINIMAL_MUTEZ_PER_BYTE * size + int(MINIMAL_MUTEZ_PER_GAS_UNIT * consumed_gas)
    return fee + reserve


def default_fee(
    content: Dict[str, Any],
) -> int:
    """Take hard gas limit instead of precise amount (no simulation) and calculate fee.

    :param content: operation content {..., "kind": "transaction", ... }
    """
    return calculate_fee(
        content=content,
        consumed_gas=default_gas_limit(content),
        extra_size=32 + 64 + 3 * 3,  # branch, signature, fee:gas_limit:storage_limit mutez values (+3 bytes)
    )


def default_gas_limit(
    content: Dict[str, Any],
    constants: Optional[Dict[str, Any]] = None,
) -> int:
    """Get default gas limit by operation kind.

    :param content: operation content {..., "kind": "transaction", ... }
    :param constants: constants block from context
    """
    if constants is None:
        constants = DEFAULT_CONSTANTS
    values: Dict[str, int] = {
        'reveal': 1000,
        'delegation': 1000,
        'origination': constants['hard_gas_limit_per_operation'],
        'transaction': constants['hard_gas_limit_per_operation']
        if content.get('destination', '').startswith('KT')
        else DEFAULT_TRANSACTION_GAS_LIMIT,
    }
    return values[content['kind']]


def default_storage_limit(
    content,
    constants: Optional[Dict[str, Any]] = None,
) -> int:
    """Get default storage limit by operation kind.

    :param content: operation content {..., "kind": "transaction", ... }
    :param constants: constants block from context
    """
    if constants is None:
        constants = DEFAULT_CONSTANTS
    values: Dict[str, int] = {
        'reveal': 0,
        'delegation': 0,
        'origination': constants['hard_storage_limit_per_operation'],
        'transaction': constants['hard_storage_limit_per_operation']
        if content.get('destination', '').startswith('KT')
        else DEFAULT_TRANSACTION_STORAGE_LIMIT,
    }
    return values[content['kind']]
