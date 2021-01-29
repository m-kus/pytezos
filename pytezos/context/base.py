from typing import Tuple, Optional


class NodeContext:

    def register_big_map(self, ptr: int):
        raise NotImplementedError

    def get_tmp_big_map_id(self) -> int:
        raise NotImplementedError

    def get_big_map_action(self, ptr: int) -> Tuple[int, str]:
        raise NotImplementedError

    def get_big_map_value(self, ptr: int, key_hash: str):
        raise NotImplementedError

    def register_sapling_state(self, ptr: int):
        raise NotImplementedError

    def get_tmp_sapling_state_id(self) -> int:
        raise NotImplementedError

    def get_sapling_state_diff(self, offset_commitment=0, offset_nullifier=0) -> list:
        raise NotImplementedError

    def get_originated_address(self) -> str:
        raise NotImplementedError

    def get_self_address(self) -> str:
        raise NotImplementedError

    def get_operation_amount(self) -> int:
        raise NotImplementedError

    def get_operation_sender(self) -> str:
        raise NotImplementedError

    def get_operation_source(self) -> str:
        raise NotImplementedError

    def get_now(self) -> int:
        raise NotImplementedError

    def get_balance(self) -> int:
        raise NotImplementedError

    def get_chain_id(self) -> str:
        raise NotImplementedError

    def get_parameter_expr(self, address=None) -> Optional:
        raise NotImplementedError

    def get_storage_expr(self):
        raise NotImplementedError

    def get_code_expr(self):
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

    def set_storage_expr(self, type_expr):
        raise NotImplementedError

    def set_parameter_expr(self, type_expr):
        raise NotImplementedError

    def set_code_expr(self, code_expr):
        raise NotImplementedError

    def spend_balance(self, amount: int):
        raise NotImplementedError
