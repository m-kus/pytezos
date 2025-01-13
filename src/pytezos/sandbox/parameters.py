import json
from pathlib import Path
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
PARIS = 'PtParisBxoLz5gzMmn3d9WBQNoPSZakgnkMC2VNuQ3KXfUtUQeZ'
PARISC = 'PsParisCZo7KAh1Z1smVd9ZMZ1HHn5gkzbM94V3PLCpknFWhUAi'
QUEBEC = 'PsQuebecnLByd3JwTiGadoG4nGWi3HYiLXUjkibeFV8dCFeVMUg'
LATEST = QUEBEC

protocol_hashes = {
    'edo': EDO,
    'florence': FLORENCE,
    'granada': GRANADA,
    'hangzhou': HANGZHOU,
    'ithaca': ITHACA,
    'jakarta': JAKARTA,
    'kathmandu': KATHMANDU,
    'lima': LIMA,
    'mumbai': MUMBAI,
    'nairobi': NAIROBI,
    'oxford': OXFORD,
    'paris': PARIS,
    'parisc': PARISC,
    'quebec': QUEBEC,
}

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
    PARIS: 19,
    PARISC: 20,
    QUEBEC: 21,
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

# NOTE: Run `make sandbox-params` to update this file
sandbox_params = json.loads(Path(__file__).parent.joinpath('parameters.json').read_text())

# NOTE: https://rpc.tzkt.io/quebecnet/chains/main/blocks/head/context/constants/parametric
protocol_params = {
    "consensus_rights_delay": 2,
    "blocks_preservation_cycles": 1,
    "delegate_parameters_activation_delay": 3,
    "blocks_per_cycle": 210,
    "blocks_per_commitment": 25,
    "nonce_revelation_threshold": 50,
    "cycles_per_voting_period": 1,
    "hard_gas_limit_per_operation": "1040000",
    "hard_gas_limit_per_block": "3328000",
    "proof_of_work_threshold": "-1",
    "minimal_stake": "6000000000",
    "minimal_frozen_stake": "600000000",
    "vdf_difficulty": "10000000",
    "origination_size": 257,
    "issuance_weights": {
        "base_total_issued_per_minute": "85007812",
        "baking_reward_fixed_portion_weight": 5120,
        "baking_reward_bonus_weight": 5120,
        "attesting_reward_weight": 10240,
        "seed_nonce_revelation_tip_weight": 1,
        "vdf_revelation_tip_weight": 1,
    },
    "cost_per_byte": "250",
    "hard_storage_limit_per_operation": "60000",
    "quorum_min": 2000,
    "quorum_max": 7000,
    "min_proposal_quorum": 500,
    "liquidity_baking_subsidy": "5000000",
    "liquidity_baking_toggle_ema_threshold": 100000,
    "max_operations_time_to_live": 187,
    "minimal_block_delay": "4",
    "delay_increment_per_round": "4",
    "consensus_committee_size": 7000,
    "consensus_threshold": 4667,
    "minimal_participation_ratio": {"numerator": 2, "denominator": 3},
    "limit_of_delegation_over_baking": 9,
    "percentage_of_frozen_deposits_slashed_per_double_baking": 700,
    "percentage_of_frozen_deposits_slashed_per_double_attestation": 5000,
    "max_slashing_per_block": 10000,
    "max_slashing_threshold": 2334,
    "testnet_dictator": "tz1e1TX7KghsqWUBXWmBTAAtPK3W6JTbNc82",
    "cache_script_size": 100000000,
    "cache_stake_distribution_cycles": 8,
    "cache_sampler_state_cycles": 8,
    "dal_parametric": {
        "feature_enable": True,
        "incentives_enable": False,
        "number_of_slots": 32,
        "attestation_lag": 8,
        "attestation_threshold": 66,
        "redundancy_factor": 8,
        "page_size": 3967,
        "slot_size": 126944,
        "number_of_shards": 512,
    },
    "smart_rollup_arith_pvm_enable": True,
    "smart_rollup_origination_size": 6314,
    "smart_rollup_challenge_window_in_blocks": 62,
    "smart_rollup_stake_amount": "32000000",
    "smart_rollup_commitment_period_in_blocks": 31,
    "smart_rollup_max_lookahead_in_blocks": 46875,
    "smart_rollup_max_active_outbox_levels": 31500,
    "smart_rollup_max_outbox_messages_per_level": 100,
    "smart_rollup_number_of_sections_in_dissection": 32,
    "smart_rollup_timeout_period_in_blocks": 781,
    "smart_rollup_max_number_of_cemented_commitments": 5,
    "smart_rollup_max_number_of_parallel_games": 32,
    "smart_rollup_reveal_activation_level": {
        "raw_data": {"Blake2B": 0},
        "metadata": 0,
        "dal_page": 1,
        "dal_parameters": 1,
        "dal_attested_slots_validity_lag": 241920,
    },
    "smart_rollup_private_enable": True,
    "smart_rollup_riscv_pvm_enable": True,
    "zk_rollup_enable": True,
    "zk_rollup_origination_size": 4000,
    "zk_rollup_min_pending_to_process": 10,
    "zk_rollup_max_ticket_payload_size": 2048,
    "global_limit_of_staking_over_baking": 9,
    "edge_of_staking_over_delegation": 3,
    "adaptive_issuance_launch_ema_threshold": 0,
    "adaptive_rewards_params": {
        "issuance_ratio_final_min": {"numerator": "1", "denominator": "400"},
        "issuance_ratio_final_max": {"numerator": "1", "denominator": "10"},
        "issuance_ratio_initial_min": {"numerator": "9", "denominator": "200"},
        "issuance_ratio_initial_max": {"numerator": "11", "denominator": "200"},
        "initial_period": 10,
        "transition_period": 50,
        "max_bonus": "50000000000000",
        "growth_rate": {"numerator": "1", "denominator": "100"},
        "center_dz": {"numerator": "1", "denominator": "2"},
        "radius_dz": {"numerator": "1", "denominator": "50"},
    },
    "adaptive_issuance_activation_vote_enable": True,
    "autostaking_enable": True,
    "adaptive_issuance_force_activation": False,
    "ns_enable": True,
    "direct_ticket_spending_enable": False,
}


def get_protocol_parameters(protocol_hash: str) -> Dict[str, Any]:
    return {
        **protocol_params,
        **sandbox_params,
    }
