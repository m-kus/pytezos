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
MUMBAI = 'PtMumbai2TmsJHNGRkD8v8YDbtao7BLUC3wjASn1inAKLFCjaH1'
NAIROBI = 'PtNairobiyssHuh87hEhfVBGCVrK3WnS8Z2FT4ymB5tAa4r1nQf'
OXFORD = 'ProxfordYmVfjWnRcgjWH36fW6PArwqykTFzotUxRs6gmTcZDuH'
LATEST = OXFORD

protocol_version = {
    EDO: 8,
    FLORENCE: 9,
    GRANADA: 10,
    HANGZHOU: 11,
    ITHACA: 12,
    JAKARTA: 13,
    KATHMANDU: 14,
    LIMA: 15,
    MUMBAI: 16,
    NAIROBI: 17,
    OXFORD: 18,
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
    # NOTE: Built-in accounts
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
    # NOTE: Shorter cycles and voting periods
    'preserved_cycles': 0,
    'blocks_per_cycle': 8,
    'blocks_per_commitment': 4,
    'nonce_revelation_threshold': 1,
    'blocks_per_stake_snapshot': 8,
    'cycles_per_voting_period': 64,
    'proof_of_work_threshold': str((1 << 63) - 1),
    # NOTE: Faster block time. Otherwise, fails with round_of_past_timestamp/malformed_period. Yes, it's a string.
    'minimal_block_delay': '1',
    # NOTE: proto.018-Proxford.validate.block.not_enough_attestations
    'consensus_threshold': 0,
}

# NOTE: https://rpc.tzkt.io/oxfordnet/chains/main/blocks/head/context/constants/parametric
oxford_params = {
    "preserved_cycles": 3,
    "blocks_per_cycle": 8192,
    "blocks_per_commitment": 64,
    "nonce_revelation_threshold": 512,
    "blocks_per_stake_snapshot": 512,
    "cycles_per_voting_period": 1,
    "hard_gas_limit_per_operation": "1040000",
    "hard_gas_limit_per_block": "2600000",
    "proof_of_work_threshold": "-1",
    "minimal_stake": "6000000000",
    "minimal_frozen_stake": "600000000",
    "vdf_difficulty": "10000000000",
    "origination_size": 257,
    "issuance_weights": {
        "base_total_issued_per_minute": "85007812",
        "baking_reward_fixed_portion_weight": 5120,
        "baking_reward_bonus_weight": 5120,
        "attesting_reward_weight": 10240,
        "liquidity_baking_subsidy_weight": 1280,
        "seed_nonce_revelation_tip_weight": 1,
        "vdf_revelation_tip_weight": 1,
    },
    "cost_per_byte": "250",
    "hard_storage_limit_per_operation": "60000",
    "quorum_min": 2000,
    "quorum_max": 7000,
    "min_proposal_quorum": 500,
    "liquidity_baking_toggle_ema_threshold": 1000000000,
    "max_operations_time_to_live": 240,
    "minimal_block_delay": "8",
    "delay_increment_per_round": "3",
    "consensus_committee_size": 7000,
    "consensus_threshold": 4667,
    "minimal_participation_ratio": {"numerator": 2, "denominator": 3},
    "limit_of_delegation_over_baking": 9,
    "percentage_of_frozen_deposits_slashed_per_double_baking": 5,
    "percentage_of_frozen_deposits_slashed_per_double_attestation": 50,
    "testnet_dictator": "tz1Xf8zdT3DbAX9cHw3c3CXh79rc4nK4gCe8",
    "cache_script_size": 100000000,
    "cache_stake_distribution_cycles": 8,
    "cache_sampler_state_cycles": 8,
    "dal_parametric": {
        "feature_enable": False,
        "number_of_slots": 256,
        "attestation_lag": 4,
        "attestation_threshold": 50,
        "blocks_per_epoch": 1,
        "redundancy_factor": 16,
        "page_size": 4096,
        "slot_size": 1048576,
        "number_of_shards": 2048,
    },
    "smart_rollup_arith_pvm_enable": False,
    "smart_rollup_origination_size": 6314,
    "smart_rollup_challenge_window_in_blocks": 40,
    "smart_rollup_stake_amount": "10000000000",
    "smart_rollup_commitment_period_in_blocks": 20,
    "smart_rollup_max_lookahead_in_blocks": 30000,
    "smart_rollup_max_active_outbox_levels": 20160,
    "smart_rollup_max_outbox_messages_per_level": 100,
    "smart_rollup_number_of_sections_in_dissection": 32,
    "smart_rollup_timeout_period_in_blocks": 500,
    "smart_rollup_max_number_of_cemented_commitments": 5,
    "smart_rollup_max_number_of_parallel_games": 32,
    "smart_rollup_reveal_activation_level": {
        "raw_data": {"Blake2B": 0},
        "metadata": 0,
        "dal_page": 2147483646,
        "dal_parameters": 2147483646,
    },
    "smart_rollup_private_enable": True,
    "smart_rollup_riscv_pvm_enable": False,
    "zk_rollup_enable": False,
    "zk_rollup_origination_size": 4000,
    "zk_rollup_min_pending_to_process": 10,
    "zk_rollup_max_ticket_payload_size": 2048,
    "global_limit_of_staking_over_baking": 5,
    "edge_of_staking_over_delegation": 2,
    "adaptive_issuance_launch_ema_threshold": 100000000,
    "adaptive_rewards_params": {
        "issuance_ratio_min": {"numerator": "1", "denominator": "2000"},
        "issuance_ratio_max": {"numerator": "1", "denominator": "20"},
        "max_bonus": "50000000000000",
        "growth_rate": {"numerator": "1", "denominator": "100"},
        "center_dz": {"numerator": "1", "denominator": "2"},
        "radius_dz": {"numerator": "1", "denominator": "50"},
    },
    "adaptive_issuance_activation_vote_enable": False,
    "autostaking_enable": True,
}


def get_protocol_parameters(protocol_hash: str) -> Dict[str, Any]:
    # https://gitlab.com/tezos/tezos/-/blob/master/src/proto_018_Proxford/lib_parameters/default_parameters.ml
    return {
        **oxford_params,
        # **old_params,
        **sandbox_params,
    }
