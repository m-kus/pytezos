from typing import Tuple, Optional

from pytezos.context.base import NodeContext, get_originated_address
from pytezos.crypto.encoding import base58_encode


class FakeContext(NodeContext):

    def __init__(self):
        self.origination_index = 1
        self.tmp_big_map_index = 1
        self.alloc_big_map_index = 0
        self.balance_update = 0
        self.big_maps = dict()
        self.balance = 100500
        self.amount = 0
        self.now = 0
        self.sender = self.get_dummy_key_hash()
        self.source = self.get_dummy_key_hash()
        self.chain_id = self.get_dummy_chain_id()
        self.self_address = get_originated_address(0)
        self.parameter_expr = None
        self.storage_expr = None
        self.code_expr = None

    def reset(self):
        self.origination_index = 1
        self.tmp_big_map_index = 1
        self.alloc_big_map_index = 0
        self.balance_update = 0
        self.big_maps.clear()

    def register_big_map(self, ptr: int, copy=False) -> int:
        tmp_ptr = self.get_tmp_big_map_id()
        self.big_maps[tmp_ptr] = (ptr, copy)
        return tmp_ptr

    def get_tmp_big_map_id(self) -> int:
        res = -self.tmp_big_map_index
        self.tmp_big_map_index += 1
        return res

    def get_big_map_diff(self, ptr: int) -> Tuple[Optional[int], int, str]:
        if ptr in self.big_maps:
            src_big_map, copy = self.big_maps[ptr]
            if copy:
                dst_big_map = self.alloc_big_map_index
                self.alloc_big_map_index += 1
                return src_big_map, dst_big_map, 'copy'
            else:
                return src_big_map, src_big_map, 'update'
        else:
            big_map = self.alloc_big_map_index
            self.alloc_big_map_index += 1
            return None, big_map, 'alloc'

    def get_originated_address(self) -> str:
        res = get_originated_address(self.origination_index)
        self.origination_index += 1
        return res

    def spend_balance(self, amount: int):
        balance = self.get_balance()
        assert amount <= balance, f'cannot spend {amount} tez, {balance} tez left'
        self.balance_update -= amount

    def get_parameter_expr(self, address=None) -> Optional:
        return self.parameter_expr if address else None

    def get_storage_expr(self):
        return self.storage_expr

    def get_code_expr(self):
        return self.code_expr

    def set_storage_expr(self, type_expr):
        self.storage_expr = type_expr

    def set_parameter_expr(self, type_expr):
        self.parameter_expr = type_expr

    def set_code_expr(self, code_expr):
        self.code_expr = code_expr

    def get_big_map_value(self, ptr: int, key_hash: str):
        raise NotImplementedError

    def register_sapling_state(self, ptr: int):
        raise NotImplementedError

    def get_tmp_sapling_state_id(self) -> int:
        raise NotImplementedError

    def get_sapling_state_diff(self, offset_commitment=0, offset_nullifier=0) -> list:
        raise NotImplementedError

    def get_self_address(self) -> str:
        return self.self_address

    def get_amount(self) -> int:
        return self.amount

    def get_sender(self) -> str:
        return self.sender

    def get_source(self) -> str:
        return self.source

    def get_now(self) -> int:
        return self.now

    def get_balance(self) -> int:
        return self.balance + self.balance_update

    def get_chain_id(self) -> str:
        return self.chain_id

    def get_dummy_address(self) -> str:
        return self.get_self_address()

    def get_dummy_public_key(self) -> str:
        return base58_encode(b'\x00' * 32, b'edpk').decode()

    def get_dummy_key_hash(self) -> str:
        return base58_encode(b'\x00' * 20, b'tz1').decode()

    def get_dummy_signature(self) -> str:
        return base58_encode(b'\x00' * 64, b'sig').decode()

    def get_dummy_chain_id(self) -> str:
        return base58_encode(b'\x00' * 4, b'Net').decode()

    def get_dummy_lambda(self):
        return {'prim': 'FAILWITH'}
