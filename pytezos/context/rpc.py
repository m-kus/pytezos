from typing import Tuple

from pytezos import RpcError
from pytezos.context.base import NodeContext
from pytezos.interop import Interop


class RPCNodeContext(Interop, NodeContext):

    def __init__(self, block_id='head', **kwargs):
        super(RPCNodeContext, self).__init__(**kwargs)
        self.block_id = block_id

    def _spawn(self, **kwargs):
        return RPCNodeContext(block_id=self.block_id, **kwargs)

    def register_big_map(self, ptr: int, action: str):
        assert ptr >= 0

    def get_tmp_big_map_id(self):
        assert False

    def get_big_map_action(self, ptr: int) -> Tuple[int, str]:
        return ptr, 'update'

    def get_big_map_value(self, ptr: int, key_hash: str):
        try:
            return self.shell.blocks[self.block_id].context.big_maps[ptr][key_hash]()
        except RpcError:
            return None

    def register_sapling_state(self, ptr: int):
        raise NotImplementedError

    def get_tmp_sapling_state_id(self) -> int:
        raise NotImplementedError

    def get_sapling_state_diff(self, offset_commitment=0, offset_nullifier=0) -> list:
        raise NotImplementedError
