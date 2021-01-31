from typing import Optional

from pytezos import RpcError
from pytezos.context.fake import FakeContext
from pytezos.interop import Interop
from pytezos.michelson.forge import optimize_timestamp


class RPCNodeContext(Interop, FakeContext):

    def __init__(self, block_id='head', address=None, **kwargs):
        super(RPCNodeContext, self).__init__(**kwargs)
        self.block_id = block_id
        self.self_address = address

    def _spawn(self, **kwargs):
        return RPCNodeContext(**kwargs)

    def get_big_map_value(self, ptr: int, key_hash: str):
        try:
            return self.shell.blocks[self.block_id].context.big_maps[ptr][key_hash]()
        except RpcError:
            return None

    def get_now(self) -> int:
        header = self.shell.blocks[self.block_id].header()
        return optimize_timestamp(header['timestamp'])

    def get_balance(self) -> int:
        contract = self.shell.contracts[self.get_self_address()]()
        return int(contract['balance'])

    def get_chain_id(self) -> str:
        return self.shell.chains.main.chain_id()

    def get_parameter_expr(self, address=None) -> Optional:
        if address:
            contract = self.shell.contracts[address]()
            return next(section for section in contract['script']['code'] if section['prim'] == 'parameter')

    def get_dummy_public_key(self) -> str:
        return self.key.public_key()

    def get_dummy_key_hash(self) -> str:
        return self.key.public_key_hash()

    def get_dummy_chain_id(self) -> str:
        return self.get_chain_id()
