from pprint import pformat
from typing import Any, Dict, List, Optional, Union

from deprecation import deprecated  # type: ignore

from pytezos.context.impl import ExecutionContext  # type: ignore
from pytezos.context.mixin import ContextMixin  # type: ignore
from pytezos.crypto.encoding import base58_encode, is_bh
from pytezos.crypto.key import blake2b_32
from pytezos.jupyter import get_class_docstring
from pytezos.logging import logger
from pytezos.michelson.forge import forge_base58
from pytezos.operation import DEFAULT_BURN_RESERVE, DEFAULT_GAS_RESERVE, MAX_OPERATIONS_TTL
from pytezos.operation.content import ContentMixin
from pytezos.operation.fees import calculate_fee, default_fee, default_gas_limit, default_storage_limit
from pytezos.operation.forge import forge_operation_group
from pytezos.operation.kind import validation_passes
from pytezos.operation.result import OperationResult
from pytezos.rpc.errors import RpcError


class OperationGroup(ContextMixin, ContentMixin):
    """Operation group representation: contents (single or multiple), signature, other fields,
    and also useful helpers for filling with precise fees, signing, forging, and injecting.
    """

    def __init__(
        self,
        context: ExecutionContext,
        contents: Optional[List[Dict[str, Any]]] = None,
        protocol: Optional[str] = None,
        chain_id: Optional[int] = None,
        branch: Optional[str] = None,
        signature: Optional[str] = None,
    ):
        super().__init__(context=context)
        self.contents = contents or []
        self.protocol = protocol
        self.chain_id = chain_id
        self.branch = branch
        self.signature = signature

    def __repr__(self):
        res = [
            super().__repr__(),
            '\nPayload',
            pformat(self.json_payload()),
            '\nHelpers',
            get_class_docstring(self.__class__),
        ]
        return '\n'.join(res)

    def _spawn(self, **kwargs) -> 'OperationGroup':
        return OperationGroup(
            context=self.context,
            contents=kwargs.get('contents', self.contents.copy()),
            protocol=kwargs.get('protocol', self.protocol),
            chain_id=kwargs.get('chain_id', self.chain_id),
            branch=kwargs.get('branch', self.branch),
            signature=kwargs.get('signature', self.signature),
        )

    def json_payload(self) -> dict:
        """ Get JSON payload used for the injection.
        """
        return {
            'protocol': self.protocol,
            'branch': self.branch,
            'contents': self.contents,
            'signature': self.signature,
        }

    def binary_payload(self) -> bytes:
        """Get binary payload used for injection/hash calculation."""
        if not self.signature:
            raise ValueError('Not signed')

        return bytes.fromhex(self.forge()) + forge_base58(self.signature)

    def operation(self, content):
        """Create new operation group with extra content added.

        :param content: Kind-specific operation body
        :rtype: OperationGroup
        """
        return self._spawn(contents=self.contents + [content])

    def fill(
        self,
        counter: Optional[int] = None,
        ttl: Optional[int] = None,
        **kwargs
    ) -> 'OperationGroup':
        """Try to fill all fields left unfilled, use approximate fees
        (not optimal, use `autofill` to simulate operation and get precise values).

        :param counter: Override counter value (for manual handling)
        :param ttl: Number of blocks to wait in the mempool before removal (default is 5 for public network, 60 for sandbox)
        :rtype: OperationGroup
        """
        if kwargs.get('branch_offset') is not None:
            logger.warning('`branch_offset` argument is deprecated, use `ttl` instead')
            ttl = MAX_OPERATIONS_TTL - kwargs['branch_offset']

        if ttl is None:
            ttl = self.context.get_operations_ttl()
        if not 0 < ttl <= MAX_OPERATIONS_TTL:
            raise Exception('`ttl` has to be in range (0, 60]')

        chain_id = self.chain_id or self.context.get_chain_id()
        branch = self.branch or self.shell.blocks[f'head-{MAX_OPERATIONS_TTL - ttl}'].hash()
        protocol = self.protocol or self.shell.head.header()['protocol']
        source = self.key.public_key_hash()

        if counter is not None:
            self.context.set_counter(counter)

        replace_map = {
            'pkh': source,
            'source': source,
            'delegate': source,  # self registration
            'counter': lambda x: str(self.context.get_counter()),
            'secret': lambda x: self.key.activation_code,
            'period': lambda x: str(self.shell.head.voting_period()),
            'public_key': lambda x: self.key.public_key(),
            'fee': lambda x: str(default_fee(x)),
            'gas_limit': lambda x: str(default_gas_limit(x, self.context.constants)),
            'storage_limit': lambda x: str(default_storage_limit(x, self.context.constants)),
        }

        def fill_content(content):
            content = content.copy()
            for k, v in replace_map.items():
                if content.get(k) in ['', '0']:
                    content[k] = v(content) if callable(v) else v
            return content

        return self._spawn(
            contents=list(map(fill_content, self.contents)),
            protocol=protocol,
            chain_id=chain_id,
            branch=branch,
        )

    def run(self, block_id='head'):
        """Simulate operation without signature checks.

        :param block_id: Specify a level at which this operation should be applied (default is head)
        :returns: RPC response from `run_operation`
        """
        return self.shell.blocks[block_id].helpers.scripts.run_operation.post(
            {
                'operation': {
                    'branch': self.branch,
                    'contents': self.contents,
                    'signature': base58_encode(b'0' * 64, b'sig').decode(),
                },
                'chain_id': self.chain_id,
            }
        )

    def forge(self, validate=False):
        """Convert json representation of the operation group into bytes.

        :param validate: Forge remotely also and compare results, default is False
        :returns: Hex string
        """
        payload = {
            'branch': self.branch,
            'contents': self.contents,
        }
        local_data = forge_operation_group(payload).hex()

        if validate:
            remote_data = self.shell.blocks[self.branch].helpers.forge.operations.post(payload)
            if local_data != remote_data:
                raise ValueError(f'Local forge result differs from remote one:\n\n{local_data}\n\n{remote_data}')

        return local_data

    def message(self, block: Union[str, int] = 'genesis') -> bytes:
        """Get payload for the failing noop operation

        :param block: Specify operation branch (default is genesis)
        :returns: Message bytes
        """
        if len(self.contents) != 1 or self.contents[0]['kind'] != 'failing_noop':
            raise NotImplementedError('Use for signing messages only')

        branch = block if is_bh(block) else self.shell.blocks[block].hash()
        return b'\x03' + bytes.fromhex(self._spawn(branch=branch).forge())

    def autofill(
        self,
        gas_reserve: int = DEFAULT_GAS_RESERVE,
        burn_reserve: int = DEFAULT_BURN_RESERVE,
        counter: Optional[int] = None,
        ttl: Optional[int] = None,
        fee: Optional[int] = None,
        gas_limit: Optional[int] = None,
        storage_limit: Optional[int] = None,
        **kwargs
    ) -> 'OperationGroup':
        """Fill the gaps and then simulate the operation in order to calculate fee, gas/storage limits.

        :param gas_reserve: Add a safe reserve for dynamically calculated gas limit (default is 100).
        :param burn_reserve: Add a safe reserve for dynamically calculated storage limit (default is 100).
        :param counter: Override counter value (for manual handling)
        :param ttl: Number of blocks to wait in the mempool before removal (default is 5 for public network, 60 for sandbox)
        :param fee: Explicitly set fee for operation. If not set fee will be calculated depeding on results of operation dry-run.
        :param gas_limit: Explicitly set gas limit for operation. If not set gas limit will be calculated depeding on results of
            operation dry-run.
        :param storage_limit: Explicitly set storage limit for operation. If not set storage limit will be calculated depeding on
            results of operation dry-run.
        :rtype: OperationGroup
        """
        if kwargs.get('branch_offset') is not None:
            logger.warning('`branch_offset` argument is deprecated, use `ttl` instead')
            ttl = MAX_OPERATIONS_TTL - kwargs['branch_offset']

        opg = self.fill(counter=counter, ttl=ttl)
        opg_with_metadata = opg.run()
        if not OperationResult.is_applied(opg_with_metadata):
            raise RpcError.from_errors(OperationResult.errors(opg_with_metadata))

        extra_size = (32 + 64) // len(opg.contents) + 1  # size of serialized branch and signature

        def fill_content(content: Dict[str, Any]) -> Dict[str, Any]:
            if validation_passes[content['kind']] == 3:
                _gas_limit, _storage_limit, _fee = gas_limit, storage_limit, fee

                if _gas_limit is None:
                    _gas_limit = OperationResult.consumed_gas(content)
                    if content['kind'] in ['origination', 'transaction']:
                        _gas_limit += gas_reserve

                if storage_limit is None:
                    _paid_storage_size_diff = OperationResult.paid_storage_size_diff(content)
                    _burned = OperationResult.burned(content)
                    _storage_limit = _paid_storage_size_diff + _burned
                    if content['kind'] in ['origination', 'transaction']:
                        _storage_limit += burn_reserve

                if _fee is None:
                    _fee = calculate_fee(content, _gas_limit, extra_size)

                current_counter = int(content['counter'])
                content.update(
                    gas_limit=str(_gas_limit),
                    storage_limit=str(_storage_limit),
                    fee=str(_fee),
                    counter=str(current_counter + self.context.get_counter_offset())
                )

            content.pop('metadata')
            logger.debug("autofilled transaction content: %s" % content)
            return content

        opg.contents = list(map(fill_content, opg_with_metadata['contents']))
        return opg

    def sign(self) -> 'OperationGroup':
        """Sign the operation group with the key specified by `using`.

        :rtype: OperationGroup
        """
        validation_pass = validation_passes[self.contents[0]['kind']]
        if any(map(lambda x: validation_passes[x['kind']] != validation_pass, self.contents)):
            raise ValueError('Mixed validation passes')

        if validation_pass == 0:
            chain_watermark = bytes.fromhex(self.shell.chains.main.watermark())
            watermark = b'\x02' + chain_watermark
        else:
            watermark = b'\x03'

        message = watermark + bytes.fromhex(self.forge())
        signature = self.key.sign(message=message, generic=True)

        return self._spawn(signature=signature)

    def hash(self) -> str:
        """Calculate the Base58 encoded operation group hash."""
        hash_digest = blake2b_32(self.binary_payload()).digest()
        return base58_encode(hash_digest, b'o').decode()

    def run_operation(self):
        # TODO: Docstring
        return self.shell.blocks['head'].helpers.scripts.run_operation.post(self.json_payload())

    @deprecated(deprecated_in='3.1.0', removed_in='4.0.0', details='use `run_operation()` instead')
    def preapply(self):
        """Preapply signed operation group.

        :returns: RPC response from `preapply`
        """
        if not self.signature:
            raise ValueError('Not signed')

        return self.run_operation()

    def inject(
        self,
        check_result: bool = True,
        num_blocks_wait: int = 5,
        time_between_blocks: Optional[int] = None,
        min_confirmations: int = 0,
        **kwargs
    ):
        """Inject the signed operation group.

        :param check_result: raise RpcError in case operation is applied but has runtime errors
        :param num_blocks_wait: number of blocks to wait for injection
        :param time_between_blocks: override the corresponding parameter from constants
        :param min_confirmations: number of block injections to wait for before returning
        :returns: operation group with metadata (raw RPC response)
        """
        if kwargs.get('_async'):
            logger.warning('`_async` argument is deprecated, use `min_confirmations` instead')
            min_confirmations = 0 if kwargs['_async'] is True else 1

        self.context.reset()

        opg_hash = self.shell.injection.operation.post(
            operation=self.binary_payload(),
            _async=False,
        )

        if min_confirmations == 0:
            return {
                'chain_id': self.chain_id,
                'hash': opg_hash,
                **self.json_payload(),
            }

        logger.info('Waiting for %s confirmations in %s blocks', min_confirmations, num_blocks_wait)
        in_mempool = True
        confirmations = 0
        for _ in range(num_blocks_wait):
            logger.info('Waiting for the next block')
            self.shell.wait_next_block(time_between_blocks=time_between_blocks)

            if in_mempool:
                try:
                    pending_opg = self.shell.mempool.pending_operations[opg_hash]
                    if not OperationResult.is_applied(pending_opg):
                        raise RpcError.from_errors(OperationResult.errors(pending_opg))
                    logger.info('Operation %s is still in mempool', opg_hash)
                    continue
                except StopIteration:
                    in_mempool = False

            try:
                res = self.shell.blocks[-1:].find_operation(opg_hash)
            except StopIteration:
                logger.info('Operation %s not found in lastest block', opg_hash)
                continue

            if check_result:
                if not OperationResult.is_applied(res):
                    raise RpcError.from_errors(OperationResult.errors(res))

            confirmations += 1
            logger.info('Got %s/%s confirmations', confirmations, min_confirmations)
            if confirmations == min_confirmations:
                return res

        raise TimeoutError(f'Operation {opg_hash} got {confirmations} confirmations in {num_blocks_wait} blocks')

    @deprecated(deprecated_in='3.1.0', removed_in='4.0.0', details='use `run_operation()` instead')
    def result(self) -> List[OperationResult]:
        """Parse the preapply result.

        :rtype: List[OperationResult]
        """
        return OperationResult.from_operation_group(self.preapply())
