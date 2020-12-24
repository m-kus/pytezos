from typing import Optional


class LazyStorage:

    def register_big_map_id(self, ptr: int):
        raise NotImplementedError

    def allocate_big_map_id(self) -> int:
        raise NotImplementedError

    def copy_big_map(self, src_ptr: int, dst_ptr: int):
        raise NotImplementedError

    def get_big_map_value(self, key_hash) -> Optional:
        raise NotImplementedError
