# NOTE: Explaination: https://pytezos.baking-bad.org/tutorials/02.html#operation-group
validation_passes = {
    'failing_noop': -1,
    'endorsement': 0,
    'endorsement_with_slot': 0,
    'proposals': 1,
    'ballot': 1,
    'seed_nonce_revelation': 2,
    'double_endorsement_evidence': 2,
    'double_baking_evidence': 2,
    'activate_account': 2,
    'reveal': 3,
    'transaction': 3,
    'origination': 3,
    'delegation': 3,
}
operation_tags = {
    'endorsement': 0,
    'endorsement_with_slot': 10,
    'proposals': 5,
    'ballot': 6,
    'seed_nonce_revelation': 1,
    'double_endorsement_evidence': 2,
    'double_baking_evidence': 3,
    'activate_account': 4,
    'failing_noop': 17,
    'reveal': 107,
    'transaction': 108,
    'origination': 109,
    'delegation': 110
}
