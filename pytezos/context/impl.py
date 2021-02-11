from typing import Tuple, Optional
from datetime import datetime
from pyblake2 import blake2b

from pytezos.rpc.errors import RpcError
from pytezos.crypto.key import Key
from pytezos.rpc.shell import ShellQuery
from pytezos.context.abstract import AbstractContext
from pytezos.crypto.encoding import base58_encode, base58_decode
from pytezos.michelson.micheline import get_script_section


def get_originated_address(index: int, opg_hash=None):
    prefix = base58_decode(opg_hash) if opg_hash else b'\x00' * 32
    nonce = prefix + index.to_bytes(4, 'big')
    nonce_hash = blake2b(data=nonce, digest_size=20).digest()
    return base58_encode(nonce_hash, b'KT1').decode()


class ExecutionContext(AbstractContext):

    def __init__(self, amount=None, chain_id=None, source=None, sender=None, balance=None,
                 block_id=None, now=None, level=None, voting_power=None, total_voting_power=None,
                 key=None, shell=None, address=None, counter=None, script=None):
        self.key: Optional[Key] = key
        self.shell: Optional[ShellQuery] = shell
        self.counter = counter
        self.block_id = block_id or 'head'
        self.address = address
        self.balance = balance
        self.amount = amount
        self.now = now
        self.level = level
        self.sender = sender
        self.source = source
        self.chain_id = chain_id
        self.voting_power = voting_power
        self.total_voting_power = total_voting_power
        self.parameter_expr = get_script_section(script, 'parameter') if script else None
        self.storage_expr = get_script_section(script, 'storage') if script else None
        self.code_expr = get_script_section(script, 'code') if script else None
        self.origination_index = 1
        self.tmp_big_map_index = 0
        self.tmp_sapling_index = 0
        self.alloc_big_map_index = 0
        self.alloc_sapling_index = 0
        self.balance_update = 0
        self.big_maps = {}

    def reset(self):
        self.counter = None
        self.origination_index = 1
        self.tmp_big_map_index = 0
        self.tmp_sapling_index = 0
        self.alloc_big_map_index = 0
        self.alloc_sapling_index = 0
        self.balance_update = 0
        self.big_maps.clear()

    @property
    def script(self) -> Optional[dict]:
        if self.parameter_expr and self.storage_expr and self.code_expr:
            return dict(code=[self.parameter_expr, self.storage_expr, self.code_expr])
        else:
            return None

    def set_counter(self, counter: int):
        self.counter = counter

    def get_counter(self) -> int:
        if self.counter is None:
            assert self.key, f'key is undefined'
            self.counter = int(self.shell.contracts[self.key.public_key_hash()]()['counter'])
        self.counter += 1
        return self.counter

    def register_big_map(self, ptr: int, copy=False) -> int:
        tmp_ptr = self.get_tmp_big_map_id()
        self.big_maps[tmp_ptr] = (ptr, copy)
        return tmp_ptr

    def get_tmp_big_map_id(self) -> int:
        self.tmp_big_map_index += 1
        return -self.tmp_big_map_index

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
        if self.shell and address:
            script = self.shell.contracts[address].script()
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
        assert self.shell, f'shell is undefined'
        try:
            return self.shell.blocks[self.block_id].context.big_maps[ptr][key_hash]()
        except RpcError:
            return None

    def register_sapling_state(self, ptr: int):
        raise NotImplementedError

    def get_tmp_sapling_state_id(self) -> int:
        self.tmp_sapling_index += 1
        return -self.tmp_sapling_index

    def get_sapling_state_diff(self, offset_commitment=0, offset_nullifier=0) -> Tuple[int, list]:
        ptr = self.alloc_sapling_index
        self.alloc_sapling_index += 1
        return ptr, []

    def get_self_address(self) -> str:
        return self.address or get_originated_address(0)

    def get_amount(self) -> int:
        return self.amount or 0

    def get_sender(self) -> str:
        return self.sender or self.get_dummy_key_hash()

    def get_source(self) -> str:
        return self.source or self.get_dummy_key_hash()

    def get_now(self) -> int:
        if self.now is not None:
            return self.now
        elif self.shell:
            constants = self.shell.block.context.constants()  # cached
            ts = self.shell.head.header()['timestamp']
            dt = datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ')
            first_delay = constants['time_between_blocks'][0]
            return int((dt - datetime(1970, 1, 1)).total_seconds()) + int(first_delay)
        else:
            return 0

    def get_level(self) -> int:
        if self.level is not None:
            return self.level
        elif self.shell:
            header = self.shell.blocks[self.block_id].header()
            return int(header['level'])
        else:
            return 1

    def get_balance(self) -> int:
        if self.balance is not None:
            balance = self.balance
        elif self.shell:
            contract = self.shell.contracts[self.get_self_address()]()
            balance = int(contract['balance'])
        else:
            balance = 0
        return balance + self.balance_update

    def get_voting_power(self, address: str) -> int:
        if self.voting_power is not None:
            return self.voting_power.get(address, 0)
        elif self.shell:
            raise NotImplementedError
        else:
            return 0

    def get_total_voting_power(self) -> int:
        if self.total_voting_power is not None:
            return self.total_voting_power
        elif self.shell:
            raise NotImplementedError
        else:
            return 0

    def get_chain_id(self) -> str:
        if self.chain_id:
            return self.chain_id
        elif self.shell:
            return self.shell.chains.main.chain_id()
        else:
            return self.get_dummy_chain_id()

    def get_dummy_address(self) -> str:
        return base58_encode(b'\x00' * 20, b'KT1').decode()

    def get_dummy_public_key(self) -> str:
        if self.key:
            return self.key.public_key()
        else:
            return base58_encode(b'\x00' * 32, b'edpk').decode()

    def get_dummy_key_hash(self) -> str:
        if self.key:
            return self.key.public_key_hash()
        else:
            return base58_encode(b'\x00' * 20, b'tz1').decode()

    def get_dummy_signature(self) -> str:
        return base58_encode(b'\x00' * 64, b'sig').decode()

    def get_dummy_chain_id(self) -> str:
        return base58_encode(b'\x00' * 4, b'Net').decode()

    def get_dummy_lambda(self):
        return {'prim': 'FAILWITH'}

    def set_total_voting_power(self, total_voting_power: int):
        self.total_voting_power = total_voting_power

    def set_voting_power(self, address: str, voting_power: int):
        self.voting_power[address] = voting_power
