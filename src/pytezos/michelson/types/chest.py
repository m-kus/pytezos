from pytezos.michelson.types.core import BytesType


class ChestType(BytesType, prim='chest'):
    ...
    # TODO: https://gitlab.com/tezos/tezos/-/merge_requests/2940/diffs#2c09e5627158501e568f7f4a7c9245c90c357217


class ChestKeyType(BytesType, prim='chest_key'):
    ...
    # TODO:
