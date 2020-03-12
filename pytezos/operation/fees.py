from pytezos.operation.forge import forge_operation

hard_gas_limit_per_operation = 1040000
hard_storage_limit_per_operation = 60000
minimal_fees = 100
minimal_nanotez_per_byte = 1
minimal_nanotez_per_gas_unit = .1


def calculate_fee(content, consumed_gas, extra_size, reserve=10):
    size = len(forge_operation(content)) + extra_size
    fee = minimal_fees \
        + minimal_nanotez_per_byte * size \
        + int(minimal_nanotez_per_gas_unit * consumed_gas)
    return fee + reserve


def default_fee(content):
    return calculate_fee(
        content=content,
        consumed_gas=default_gas_limit(content),
        extra_size=32 + 64 + 3 * 3  # branch, signature, fee:gas_limit:storage_limit mutez values (+3 bytes)
    )


def default_gas_limit(content):
    values = {
        'reveal': 10000,
        'delegation': 10000,
        'origination': hard_gas_limit_per_operation if content.get('script') else 10000,
        'transaction': hard_gas_limit_per_operation if content.get('parameters') else 10207
    }
    return values.get(content['kind'])


def default_storage_limit(content):
    values = {
        'reveal': 0,
        'delegation': 0,
        'origination': hard_storage_limit_per_operation if content.get('script') else 10207,
        'transaction': hard_storage_limit_per_operation if content.get('parameters') else 257
    }
    return values.get(content['kind'])


def burn_cap(content):
    values = {
        'reveal': 0,
        'delegation': 0,
        'origination': 257,
        'transaction': 0 if content.get('parameters') else 257
    }
    return values.get(content['kind'])
