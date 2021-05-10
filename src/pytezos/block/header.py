from pprint import pformat
from typing import Any, Dict, List, Optional

import bson  # type: ignore

from pytezos.block.forge import bump_fitness, forge_block_header, forge_protocol_data
from pytezos.context.impl import ExecutionContext
from pytezos.context.mixin import ContextMixin
from pytezos.crypto.encoding import base58_encode
from pytezos.crypto.key import blake2b_32
from pytezos.jupyter import get_class_docstring
from pytezos.michelson.forge import forge_array, forge_base58, optimize_timestamp
from pytezos.rpc.kind import validation_passes
from pytezos.sandbox.parameters import sandbox_params


class BlockHeader(ContextMixin):
    """Representation of block creation call"""

    def __init__(
        self,
        context: ExecutionContext,
        protocol_data: Optional[Dict[str, Any]] = None,
        operations: Optional[List[List[Dict[str, Any]]]] = None,
        shell_header: Optional[Dict[str, Any]] = None,
        signature: Optional[str] = None,
    ) -> None:
        super().__init__(context=context)
        self.protocol_data = protocol_data or {}
        self.operations = operations or []
        self.shell_header = shell_header or {}
        self.signature = signature

    def __repr__(self) -> str:
        res = [
            super().__repr__(),
            '\nHeader',
            pformat(
                {
                    **self.shell_header,
                    'protocol_data': {
                        **self.protocol_data,
                        'signature': self.signature,
                    },
                }
            ),
            '\nOperations',
            pformat(self.operations),
            '\nHelpers',
            get_class_docstring(self.__class__),
        ]
        return '\n'.join(res)

    @classmethod
    def activate_protocol(cls, protocol_hash: str, parameters: Dict[str, Any], context: ExecutionContext) -> 'BlockHeader':
        """Create call to bake genesis block with specified parameters

        :param protocol_hash: protocol hash (ex. PsFLorenaUUuikDWvMDr6fGBRG8kt3e3D3fHoXK1j1BFRxeSH4i)
        :param parameters: protocol parameters
        :param context: execution context
        """
        prev_fitness = context.shell.head.header()['fitness']  # type: ignore
        protocol_data = {
            "content": {
                "command": "activate",
                "hash": protocol_hash,
                "fitness": bump_fitness(prev_fitness),
                "protocol_parameters": forge_array(bson.dumps(parameters)).hex(),
            }
        }
        return BlockHeader(
            context=context,
            protocol_data=protocol_data,
        )

    @classmethod
    def bake_block(cls, context: ExecutionContext, min_fee: int = 0) -> 'BlockHeader':
        """Create call to bake new block

        :param min_fee: Minimum fee of transaction to be included in block
        """
        pending_operations = context.shell.mempool.pending_operations()  # type: ignore
        operations: List[List[Dict[str, Any]]] = [[], [], [], []]

        for opg in pending_operations['applied']:
            validation_pass = validation_passes[opg['contents'][0]['kind']]
            if validation_pass == 3 and sum(map(lambda x: int(x['fee']), opg['contents'])) < min_fee:
                continue
            operations[validation_pass].append(opg)

        # NOTE: Real values will be set during fill
        protocol_data = {
            "priority": 0,
            "proof_of_work_nonce": "0000000000000000",
        }
        return BlockHeader(
            context=context,
            operations=operations,
            protocol_data=protocol_data,
        )

    def _spawn(self, **kwargs):
        return BlockHeader(
            context=self.context,
            protocol_data=kwargs.get('protocol_data', self.protocol_data.copy()),
            operations=kwargs.get('operations', self.operations.copy()),
            shell_header=kwargs.get('shell_header', self.shell_header.copy()),
            signature=kwargs.get('signature', self.signature),
        )

    def fill(self, block_id='head') -> 'BlockHeader':
        """Fill missing fields essential for preapply

        :param block_id: head or genesis
        :rtype: BlockHeader
        """
        pred_shell_header = self.shell.blocks[block_id].header.shell()
        timestamp = optimize_timestamp(pred_shell_header['timestamp']) + 1
        protocol = self.shell.blocks[block_id].protocols()['next_protocol']
        level = int(pred_shell_header['level']) + 1
        dummy_signature = base58_encode(b'\x00' * 64, b'sig').decode()

        protocol_data = {
            'protocol': protocol,
            **self.protocol_data,
        }

        if level % int(sandbox_params['blocks_per_commitment']) == 0:  # type: ignore
            protocol_data['seed_nonce_hash'] = base58_encode(b'\x00' * 32, b'nce').decode()

        if 'priority' in protocol_data:
            baker = self.key.public_key_hash()
            baking_rights = self.shell.blocks[block_id].helpers.baking_rights(delegate=baker)
            # NOTE: Fails if baker has no baking rights
            protocol_data['priority'] = next(item['priority'] for item in baking_rights if item['delegate'] == baker)

        operations = [
            [
                {
                    'protocol': protocol,
                    'branch': operation['branch'],
                    'contents': operation['contents'],
                    'signature': operation['signature'],
                }
                for operation in operation_list
            ]
            for operation_list in self.operations
        ]

        payload = {
            'protocol_data': {
                **protocol_data,
                'signature': dummy_signature,
            },
            'operations': operations,
        }

        res = self.shell.blocks[block_id].helpers.preapply.block.post(
            block=payload,
            sort=True,
            timestamp=timestamp,
        )

        forged_operations = [
            [
                {
                    'branch': operation['branch'],
                    'data': operation['data'],
                }
                for operation in operation_list['applied']
            ]
            for operation_list in res['operations']
        ]

        return self._spawn(
            shell_header=res['shell_header'],
            operations=forged_operations,
            protocol_data=protocol_data,
            signature=dummy_signature,
        )

    def work(self) -> 'BlockHeader':
        """Perform calculations to find proof-of-work nonce"""
        header = self
        threshold = int(sandbox_params['proof_of_work_threshold'])
        nonce = 1

        while header.pow_stamp() > threshold:
            header = self._spawn(
                protocol_data={
                    **self.protocol_data,
                    'proof_of_work_nonce': nonce.to_bytes(8, 'big').hex(),
                }
            )
            nonce += 1

        return header

    def binary_payload(self) -> bytes:
        """Get binary payload used for injection/hash calculation."""
        if self.signature is None:
            raise ValueError('Not signed')
        return self.forge() + forge_base58(self.signature)

    def forge(self) -> bytes:
        """Convert json representation of the block header into bytes.

        :returns: Binary payload (unsigned)
        """
        return forge_block_header(
            {
                **self.shell_header,
                'protocol_data': forge_protocol_data(self.protocol_data).hex(),
            }
        )

    def pow_stamp(self) -> int:
        data = self.forge() + b'\x00' * 64
        hash_digest = blake2b_32(data).digest()
        return int.from_bytes(hash_digest[:8], 'big')

    def hash(self) -> str:
        hash_digest = blake2b_32(self.binary_payload()).digest()
        return base58_encode(hash_digest, b'B').decode()

    def sign(self) -> 'BlockHeader':
        """Sign the block header with the key specified by `using`.

        :rtype: BlockHeader
        """
        chain_watermark = bytes.fromhex(self.shell.chains.main.watermark())
        watermark = b'\x01' + chain_watermark
        signature = self.key.sign(message=watermark + self.forge())
        return self._spawn(signature=signature)

    def inject(self, force=False) -> str:
        """Inject the signed block header.

        :returns: block hash
        """
        payload = {
            "data": self.binary_payload().hex(),
            "operations": self.operations,
        }
        return self.shell.injection.block.post(
            block=payload,
            _async=False,
            force=force,
        )
