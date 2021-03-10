from pprint import pformat
from typing import Any, Dict, List, Optional

import bson  # type: ignore

from pytezos.block.forge import forge_protocol_data, forge_block_header, forge_signed_operation
from pytezos.context.impl import ExecutionContext  # type: ignore
from pytezos.context.mixin import ContextMixin  # type: ignore
from pytezos.crypto.encoding import base58_encode
from pytezos.jupyter import get_class_docstring
from pytezos.michelson.forge import forge_array, forge_base58


class BlockHeader(ContextMixin):
    def __init__(
        self,
        context: ExecutionContext,
        protocol_data: Optional[Dict[str, Any]] = None,
        operations: Optional[List[List[Dict[str, Any]]]] = None,
        shell_header: Optional[Dict[str, Any]] = None,
        signature: Optional[str] = None
    ):
        super().__init__(context=context)
        self.protocol_data = protocol_data or {}
        self.operations = operations or []
        self.shell_header = shell_header or {}
        self.signature = signature

    def __repr__(self):
        res = [
            super().__repr__(),
            '\nHeader',
            pformat({
                **self.shell_header,
                'protocol_data': {
                    **self.protocol_data,
                    'signature': self.signature
                }
            }),
            '\nOperations',
            pformat(self.operations),
            '\nHelpers',
            get_class_docstring(self.__class__),
        ]
        return '\n'.join(res)

    @classmethod
    def activate_protocol(cls, protocol_hash: str, parameters: Dict[str, Any], context: ExecutionContext) \
            -> 'BlockHeader':
        protocol_data = {
            "content": {
                "command": "activate",
                "hash": protocol_hash,
                "fitness": ["00", "0000000000000001"],  # TODO: int <-> fitness converter
                "protocol_parameters": forge_array(bson.dumps(parameters)).hex(),
            }
        }
        return BlockHeader(
            context=context,
            protocol_data=protocol_data,
        )

    @classmethod
    def bake_block(cls, context: ExecutionContext, min_fee: int = 0) -> 'BlockHeader':
        pending_operations = context.shell.mempool.pending_operations()
        operations: List[Dict[str, Any]] = [
            op
            for op in pending_operations['applied']
            if sum(map(lambda x: int(x['fee']), op['contents'])) >= min_fee  # handle batch case
        ]
        protocol_data = {
            "priority": 0,  # default
            "proof_of_work_nonce": "0000000000000000"  # dummy nonce
        }
        return BlockHeader(
            context=context,
            operations=[[], [], [], operations],  # TODO: group by validation pass
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

    def fill(self) -> 'BlockHeader':
        """Fill missing fields essential for preapply

        :rtype: BlockHeader
        """
        protocol = self.shell.head.protocols()['next_protocol']
        protocol_data = {
            'protocol': protocol,
            **self.protocol_data
        }

        if 'priority' in protocol_data:
            baker = self.key.public_key_hash()
            baking_rights = self.shell.blocks.head.helpers.baking_rights(delegate=baker)
            protocol_data['priority'] = next(
                item['priority']
                for item in baking_rights
                if item['delegate'] == baker)  # Fail if no rights

        dummy_signature = base58_encode(b'\x00' * 64, b'sig').decode()

        operations = [
            [
                {
                    'protocol': protocol,
                    'branch': operation['branch'],
                    'contents': operation['contents'],
                    'signature': operation['signature']
                }
                for operation in operation_list
            ]
            for operation_list in self.operations
        ]

        payload = {
            'protocol_data': {
                **protocol_data,
                'signature': dummy_signature
            },
            'operations': operations,
        }
        res = self.shell.head.helpers.preapply.block.post(block=payload, sort=True)

        return self._spawn(shell_header=res['shell_header'],
                           protocol_data=protocol_data,
                           operations=operations,
                           signature=dummy_signature)

    def binary_payload(self) -> bytes:
        """Get binary payload used for injection/hash calculation."""
        if self.signature is None:
            raise ValueError('Not signed')
        return self.forge() + forge_base58(self.signature)

    def forge(self) -> bytes:
        """Convert json representation of the block header into bytes.

        :returns: Binary payload (unsigned)
        """
        return forge_block_header({
            **self.shell_header,
            'protocol_data': forge_protocol_data(self.protocol_data).hex()
        })

    def sign(self):
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
        operations = [
            [
                {
                    'branch': operation['branch'],
                    'data': forge_signed_operation(operation).hex()
                }
                for operation in operation_list
            ]
            for operation_list in self.operations
        ]

        payload = {
            "data": self.binary_payload().hex(),
            "operations": operations
        }
        return self.shell.injection.block.post(block=payload, _async=False, force=force)
