from pprint import pformat
from typing import Any, Dict, List, Optional, Tuple

import bson  # type: ignore

from pytezos.block.forge import forge_block_header, forge_protocol_data, forge_signed_operation
from pytezos.context.impl import ExecutionContext
from pytezos.context.mixin import ContextMixin
from pytezos.crypto.encoding import base58_encode
from pytezos.crypto.key import blake2b_32
from pytezos.jupyter import get_class_docstring
from pytezos.michelson.forge import forge_array, forge_base58


# NOTE: Comment out to increment first octet
def fitness_tuple_to_int(fitness_tuple: Tuple[str, str]) -> int:
    return int(fitness_tuple[1], 16)


def fitness_int_to_tuple(fitness_int: int) -> Tuple[str, str]:
    fitness_str = "%0.16X" % fitness_int
    return ("00", fitness_str)


# NOTE: Uncomment to increment first octet
# def fitness_tuple_to_int(fitness_tuple: Tuple[str, str]) -> int:
#     return int(fitness_tuple[0] + fitness_tuple[1], 16)

# def fitness_int_to_tuple(fitness_int: int) -> Tuple[str, str]:
#     fitness_str = "%0.18X" % fitness_int
#     return (fitness_str[:2], fitness_str[2:])


class BlockHeader(ContextMixin):
    def __init__(
        self,
        context: ExecutionContext,
        protocol_data: Optional[Dict[str, Any]] = None,
        operations: Optional[List[List[Dict[str, Any]]]] = None,
        shell_header: Optional[Dict[str, Any]] = None,
        signature: Optional[str] = None,
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
    def activate_protocol(
        cls,
        protocol_hash: str,
        parameters: Dict[str, Any],
        context: ExecutionContext,
        fitness: int = 1,
    ) -> 'BlockHeader':
        protocol_data = {
            "content": {
                "command": "activate",
                "hash": protocol_hash,
                "fitness": fitness_int_to_tuple(fitness),
                "protocol_parameters": forge_array(bson.dumps(parameters)).hex(),
            }
        }
        return BlockHeader(
            context=context,
            protocol_data=protocol_data,
        )

    @classmethod
    def bake_block(cls, context: ExecutionContext, min_fee: int = 0) -> 'BlockHeader':
        pending_operations = context.shell.mempool.pending_operations()  # type: ignore
        operations: List[Dict[str, Any]] = [
            op for op in pending_operations['applied'] if sum(map(lambda x: int(x['fee']), op['contents'])) >= min_fee  # handle batch case
        ]
        # NOTE: Real values will be set during autofill
        protocol_data = {
            "priority": 0,
            "proof_of_work_nonce": "0000000000000000",
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

    def fill(self, genesis=False) -> 'BlockHeader':
        """Fill missing fields essential for preapply

        :rtype: BlockHeader
        """
        protocol = self.shell.blocks.head.protocols()['next_protocol']
        genesis_protocol = self.shell.blocks.genesis.protocols()['next_protocol']

        protocol_data = {
            'protocol': genesis_protocol if genesis else protocol,
            **self.protocol_data,
        }

        if 'priority' in protocol_data:
            baker = self.key.public_key_hash()
            baking_rights = self.shell.blocks.head.helpers.baking_rights(delegate=baker)
            protocol_data['priority'] = next(item['priority'] for item in baking_rights if item['delegate'] == baker)  # Fail if no rights

        dummy_signature = base58_encode(b'\x00' * 64, b'sig').decode()

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
        res = self.shell.head.helpers.preapply.block.post(
            block=payload,
            sort=True,
            timestamp=self.context.timestamp,
        )

        return self._spawn(
            shell_header=res['shell_header'],
            protocol_data=protocol_data,
            operations=operations,
            signature=dummy_signature,
        )

    def work(self):
        header = self
        threshold = self.context.constants['proof_of_work_threshold']
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
                    'data': forge_signed_operation(operation).hex(),
                }
                for operation in operation_list
            ]
            for operation_list in self.operations
        ]

        payload = {
            "data": self.binary_payload().hex(),
            "operations": operations,
        }
        return self.shell.injection.block.post(
            block=payload,
            timestamp=self.context.timestamp,
            _async=False,
            force=force,
        )
