from typing import Any
from typing import Dict

from pytezos.crypto.key import Key

EDO = 'PtEdo2ZkT9oKpimTah6x2embF25oss54njMuPzkJTEi5RqfdZFA'
FLORENCE = 'PsFLorenaUUuikDWvMDr6fGBRG8kt3e3D3fHoXK1j1BFRxeSH4i'
GRANADA = 'PtGRANADsDU8R9daYKAgWnQYAJ64omN1o3KMGVCykShA97vQbvV'
HANGZHOU = 'PtHangz2aRngywmSRGGvrcTyMbbdpWdpFKuS4uMWxg2RaH9i1qx'
ITHACA = 'Psithaca2MLRFYargivpo7YvUr7wUDqyxrdhC5CQq78mRvimz6A'
JAKARTA = 'PtJakart2xVj7pYXJBXrqHgd82rdkLey5ZeeGwDgPp9rhQUbSqY'
KATHMANDU = 'PtKathmankSpLLDALzWw7CGD2j2MtyveTwboEYokqUCP4a1LxMg'
LIMA = 'PtLimaPtLMwfNinJi9rCfDPWea8dFgTZ1MeJ9f1m2SRic6ayiwW'
LATEST = LIMA

protocol_version = {
    EDO: 8,
    FLORENCE: 9,
    GRANADA: 10,
    HANGZHOU: 11,
    ITHACA: 12,
    JAKARTA: 13,
    KATHMANDU: 14,
    LIMA: 15,
}

sandbox_commitment = {
    "mnemonic": [
        "arctic",
        "blame",
        "brush",
        "economy",
        "solar",
        "swallow",
        "canvas",
        "live",
        "vote",
        "two",
        "post",
        "neutral",
        "spare",
        "split",
        "fall",
    ],
    "activation_code": "7375ef222cc038001b6c8fb768246c86e994745b",
    "amount": "38323962971",
    "pkh": "tz1W86h1XuWy6awbNUTRUgs6nk8q5vqXQwgk",
    "password": "ZuPOpZgMNM",
    "email": "nbhcylbg.xllfjgrk@tezos.example.org",
}

sandbox_addresses = {
    'activator': 'tz1TGu6TN5GSez2ndXXeDX6LgUDvLzPLqgYV',
    'bootstrap5': 'tz1ddb9NMYHZi5UzPdzTZMYQQZoMub195zgv',
    'bootstrap4': 'tz1b7tUupMgCNw2cCLpKTkSD1NZzB5TkP2sv',
    'bootstrap3': 'tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU',
    'bootstrap2': 'tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN',
    'bootstrap1': 'tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx',
}

sandbox_params: Dict[str, Any] = {
    'bootstrap_accounts': [
        ['edpkuBknW28nW72KG6RoHtYW7p12T6GKc7nAbwYX5m8Wd9sDVC9yav', '4000000000000'],
        ['edpktzNbDAUjUk697W7gYg2CRuBQjyPxbEg8dLccYYwKSKvkPvjtV9', '4000000000000'],
        ['edpkuTXkJDGcFd5nh6VvMz8phXxU3Bi7h6hqgywNFi1vZTfQNnS1RV', '4000000000000'],
        ['edpkuFrRoDSEbJYgxRtLx2ps82UdaYc1WwfS9sE11yhauZt5DgCHbU', '4000000000000'],
        ['edpkv8EUUH68jmo3f7Um5PezmfGrRF24gnfLpH3sVNwJnV5bVCxL2n', '4000000000000'],
    ],
    'bootstrap_contracts': [],
    'commitments': [
        [
            Key.from_faucet(sandbox_commitment).blinded_public_key_hash(),
            '100500000000',
        ],
    ],
    'preserved_cycles': 2.0,
    'blocks_per_cycle': 8.0,
    'blocks_per_commitment': 4.0,
    'cycles_per_voting_period': 64.0,
    'hard_gas_limit_per_operation': '1040000',
    'hard_gas_limit_per_block': '10400000',
    'proof_of_work_threshold': str((1 << 63) - 1),
    'seed_nonce_revelation_tip': '125000',
    'origination_size': 257.0,
    'cost_per_byte': '250',
    'hard_storage_limit_per_operation': '60000',
    'quorum_min': 2000.0,
    'quorum_max': 7000.0,
    'min_proposal_quorum': 500.0,
}


def get_protocol_parameters(protocol_hash: str) -> Dict[str, Any]:
    return {
        **sandbox_params.copy(),
        'cache_sampler_state_cycles': 8.0,
        'tx_rollup_enable': True,
        'tx_rollup_origination_size': 4000.0,
        'liquidity_baking_toggle_ema_threshold': 1000000000.0,
        'cache_script_size': 100000000.0,
        'cache_stake_distribution_cycles': 8.0,
        'tx_rollup_hard_size_limit_per_inbox': 500000.0,
        'tx_rollup_hard_size_limit_per_message': 5000.0,
        'tx_rollup_max_withdrawals_per_batch': 15.0,
        'tx_rollup_commitment_bond': '10000000000',
        'tx_rollup_finality_period': 40000.0,
        'tx_rollup_withdraw_period': 40000.0,
        'tx_rollup_max_inboxes_count': 40100.0,
        'tx_rollup_max_messages_per_inbox': 1010.0,
        'tx_rollup_max_commitments_count': 80100.0,
        'tx_rollup_cost_per_byte_ema_factor': 120.0,
        'tx_rollup_max_ticket_payload_size': 2048.0,
        'tx_rollup_rejection_max_proof_size': 30000.0,
        'tx_rollup_sunset_level': 3473409.0,
        'sc_rollup_enable': False,
        'sc_rollup_origination_size': 6314.0,
        'sc_rollup_challenge_window_in_blocks': 20160.0,
        'sc_rollup_max_number_of_messages_per_commitment_period': 300000000.0,
        'sc_rollup_stake_amount': '32000000',
        'sc_rollup_commitment_period_in_blocks': 30.0,
        'sc_rollup_max_lookahead_in_blocks': 30000.0,
        'sc_rollup_max_active_outbox_levels': 20160.0,
        'sc_rollup_max_outbox_messages_per_level': 100.0,
        'sc_rollup_number_of_sections_in_dissection': 32.0,
        'sc_rollup_timeout_period_in_blocks': 20160.0,
        'sc_rollup_max_number_of_cemented_commitments': 5.0,
        'zk_rollup_enable': False,
        'zk_rollup_origination_size': 4000.0,
        'zk_rollup_min_pending_to_process': 10.0,
        'blocks_per_stake_snapshot': 4.0,
        'consensus_committee_size': 526.0,
        'consensus_threshold': 0.0,
        'baking_reward_fixed_portion': '333333',
        'baking_reward_bonus_per_slot': '3921',
        'endorsing_reward_per_slot': '2604',
        'max_slashing_period': 2.0,
        'frozen_deposits_percentage': 5.0,
        'max_operations_time_to_live': 120.0,
        'delay_increment_per_round': '1',
        'minimal_participation_ratio': {'numerator': 2.0, 'denominator': 3.0},
        'double_baking_punishment': '640000000',
        'ratio_of_frozen_deposits_slashed_per_double_endorsement': {'numerator': 1.0, 'denominator': 2.0},
        'minimal_block_delay': '1',
        'liquidity_baking_subsidy': '2500000',
        'nonce_revelation_threshold': 2.0,
        'vdf_difficulty': '50000',
        'dal_parametric': {
            'feature_enable': False,
            'number_of_slots': 16.0,
            'number_of_shards': 256.0,
            'endorsement_lag': 1.0,
            'availability_threshold': 50.0,
            'slot_size': 1048576.0,
            'redundancy_factor': 16.0,
            'page_size': 4096.0
        },
        'minimal_stake': '6000'
    }
