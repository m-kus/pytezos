from typing import Tuple, Optional

from pytezos.rpc.errors import RpcError
from pytezos.context.execution import ExecutionContext, get_originated_address
from pytezos.context.account import AccountContext
from pytezos.crypto.encoding import base58_encode
from pytezos.michelson.forge import optimize_timestamp
from pytezos.michelson.micheline import get_script_section


class REPLContext(ExecutionContext):

    def __init__(self, amount=None, chain_id=None, source=None, sender=None, balance=None,
                 voting_power=None, total_voting_power=None, block_id=None):
        self.origination_index = 1
        self.tmp_big_map_index = 1
        self.alloc_big_map_index = 0
        self.balance_update = 0
        self.big_maps = dict()
        self.balance = balance or 0
        self.amount = amount or 0
        self.voting_power = voting_power or 0
        self.total_voting_power = total_voting_power or 0
        self.now = 0
        self.level = 1
        self.sender = sender or self.get_dummy_key_hash()
        self.source = source or self.get_dummy_key_hash()
        self.chain_id = chain_id or self.get_dummy_chain_id()
        self.self_address = get_originated_address(0)
        self.parameter_expr = None
        self.storage_expr = None
        self.code_expr = None
        self.network = None
        self.block_id = block_id or 'head'

    def reset(self):
        self.origination_index = 1
        self.tmp_big_map_index = 1
        self.alloc_big_map_index = 0
        self.balance_update = 0
        self.big_maps.clear()

    def set_network(self, network: Optional[str]):
        self.network = network

    def set_block(self, block_id):
        self.block_id = block_id

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
        if self.network and address:
            ctx = AccountContext(shell=self.network)
            script = ctx.shell.contracts[address].script()
            return get_script_section(script, 'parameter')
        else:
            return None if address else self.parameter_expr

    def get_storage_expr(self):
        return self.storage_expr

    def get_code_expr(self):
        return self.code_expr

    def set_storage_expr(self, expr):
        self.storage_expr = expr

    def set_parameter_expr(self, expr):
        self.parameter_expr = expr

    def set_code_expr(self, expr):
        self.code_expr = expr

    def get_big_map_value(self, ptr: int, key_hash: str):
        if ptr < 0:
            return None
        assert self.network, f'network is undefined'
        try:
            ctx = AccountContext(shell=self.network)
            return ctx.shell.blocks[self.block_id].context.big_maps[ptr][key_hash]()
        except RpcError:
            return None

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
        if self.network:
            ctx = AccountContext(shell=self.network)
            header = ctx.shell.blocks[self.block_id].header()
            return optimize_timestamp(header['timestamp'])
        else:
            return self.now

    def get_level(self) -> int:
        if self.network:
            ctx = AccountContext(shell=self.network)
            header = ctx.shell.blocks[self.block_id].header()
            return int(header['level'])
        else:
            return self.level

    def get_balance(self) -> int:
        if self.network:
            ctx = AccountContext(shell=self.network)
            contract = ctx.shell.contracts[self.get_self_address()]()
            balance = int(contract['balance'])
        else:
            balance = self.balance
        return balance + self.balance_update

    def get_voting_power(self, address: str) -> int:
        if self.network:
            raise NotImplementedError
        else:
            return self.voting_power

    def get_total_voting_power(self) -> int:
        if self.network:
            raise NotImplementedError
        else:
            return self.total_voting_power

    def get_chain_id(self) -> str:
        if self.network:
            ctx = AccountContext(shell=self.network)
            return ctx.shell.chains.main.chain_id()
        else:
            return self.chain_id

    def get_dummy_address(self) -> str:
        return base58_encode(b'\x00' * 20, b'KT1').decode()

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
