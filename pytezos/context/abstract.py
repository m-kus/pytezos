from typing import Tuple, Optional

from pytezos.crypto.key import Key


class KeyHash(Key):

    def __init__(self, public_key_hash):
        super(KeyHash, self).__init__(0)
        self._pkh = public_key_hash

    def __repr__(self):
        res = [
            super(Key, self).__repr__(),
            f'\nPublic key hash',
            self.public_key_hash()
        ]
        return '\n'.join(res)

    def public_key_hash(self):
        return self._pkh

    def public_key(self):
        raise NotImplementedError

    def secret_key(self, passphrase=None, ed25519_seed=True):
        raise NotImplementedError

    def sign(self, message, generic=False):
        raise NotImplementedError

    def verify(self, signature, message):
        raise NotImplementedError


class AbstractContext:

    def reset(self):
        raise NotImplementedError

    def register_big_map(self, ptr: int, copy=False) -> int:
        raise NotImplementedError

    def get_tmp_big_map_id(self) -> int:
        raise NotImplementedError

    def get_big_map_diff(self, ptr: int) -> Tuple[Optional[int], int, str]:
        raise NotImplementedError

    def get_originated_address(self) -> str:
        raise NotImplementedError

    def spend_balance(self, amount: int):
        raise NotImplementedError

    def get_parameter_expr(self, address=None) -> Optional:
        raise NotImplementedError

    def get_storage_expr(self):
        raise NotImplementedError

    def get_code_expr(self):
        raise NotImplementedError

    def set_storage_expr(self, type_expr):
        raise NotImplementedError

    def set_parameter_expr(self, type_expr):
        raise NotImplementedError

    def set_code_expr(self, code_expr):
        raise NotImplementedError

    def get_big_map_value(self, ptr: int, key_hash: str):
        raise NotImplementedError

    def register_sapling_state(self, ptr: int):
        raise NotImplementedError

    def get_tmp_sapling_state_id(self) -> int:
        raise NotImplementedError

    def get_sapling_state_diff(self, offset_commitment=0, offset_nullifier=0) -> Tuple[int, list]:
        raise NotImplementedError

    def get_self_address(self) -> str:
        raise NotImplementedError

    def get_amount(self) -> int:
        raise NotImplementedError

    def get_voting_power(self, address: str) -> int:
        raise NotImplementedError

    def get_total_voting_power(self) -> int:
        raise NotImplementedError

    def get_sender(self) -> str:
        raise NotImplementedError

    def get_source(self) -> str:
        raise NotImplementedError

    def get_now(self) -> int:
        raise NotImplementedError

    def get_level(self) -> int:
        raise NotImplementedError

    def get_balance(self) -> int:
        raise NotImplementedError

    def get_chain_id(self) -> str:
        raise NotImplementedError

    def get_dummy_address(self) -> str:
        raise NotImplementedError

    def get_dummy_public_key(self) -> str:
        raise NotImplementedError

    def get_dummy_key_hash(self) -> str:
        raise NotImplementedError

    def get_dummy_signature(self) -> str:
        raise NotImplementedError

    def get_dummy_chain_id(self) -> str:
        raise NotImplementedError

    def get_dummy_lambda(self):
        raise NotImplementedError

    def set_total_voting_power(self, total_voting_power: int):
        raise NotImplementedError

    def set_voting_power(self, address: str, voting_power: int):
        raise NotImplementedError
