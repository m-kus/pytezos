from typing import Tuple


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
