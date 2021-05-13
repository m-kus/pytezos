import logging
from decimal import Decimal
from typing import List, Optional, Tuple, Union

from pytezos.block.header import BlockHeader
from pytezos.context.mixin import ContextMixin  # type: ignore
from pytezos.contract.call import ContractCall
from pytezos.contract.interface import ContractInterface
from pytezos.crypto.key import Key
from pytezos.jupyter import get_class_docstring, is_interactive
from pytezos.logging import logger
from pytezos.operation.content import ContentMixin
from pytezos.operation.group import OperationGroup, validation_passes
from pytezos.operation.result import OperationResult
from pytezos.rpc import ShellQuery
from pytezos.rpc.node import RpcError
from pytezos.sandbox.parameters import get_protocol_parameters


class PyTezosClient(ContextMixin, ContentMixin):
    """ Entry point for a developer, start your script with:
    `from pytezos import pytezos`
    """

    def __repr__(self):
        res = [
            super(PyTezosClient, self).__repr__(),
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def operation_group(self, protocol=None, branch=None, contents=None, signature=None) -> OperationGroup:
        """ Create new operation group (multiple contents).
        You can leave all fields empty in order to create an empty operation group.

        :param protocol: Leave None for autocomplete, unless you know what you are doing
        :param branch: Leave None for autocomplete
        :param contents: List of operation contents (optional)
        :param signature: Can be set later
        :rtype: OperationGroup
        """
        return OperationGroup(
            context=self._spawn_context(),
            protocol=protocol,
            branch=branch,
            contents=contents,
            signature=signature
        )

    def operation(self, content: dict) -> OperationGroup:
        """ Create an operation group with single content.

        :param content: Operation body (depending on `kind`)
        :rtype: OperationGroup
        """
        return OperationGroup(context=self._spawn_context(), contents=[content])

    def bulk(self, *operations: Union[OperationGroup, ContractCall]) -> OperationGroup:
        """ Batch multiple operations and contract calls in a single operation group

        :param operations: a tuple of operations or contract calls
        :rtype: OperationGroup
        """
        contents = []
        reset_fields = {
            'pkh': '',
            'source': '',
            'delegate': '',
            'counter': '0',
            'secret': '',
            'period': '0',
            'public_key': '',
            'fee': '0',
            'gas_limit': '0',
            'storage_limit': '0'
        }
        for opg in operations:
            if isinstance(opg, ContractCall):
                opg = opg.as_transaction()
            else:
                assert isinstance(opg, OperationGroup), f'expected OperationGroup or ContractCall, got {opg}'
            for content in opg.contents:
                contents.append({k: reset_fields.get(k, v) for k, v in content.items()})
        return OperationGroup(context=self._spawn_context(), contents=contents)

    def account(self, account_id=None) -> dict:
        """ Shortcut for RPC contract request.

        :param account_id: tz/KT address, leave None to show info about current key
        """
        address = account_id or self.key.public_key_hash()
        return self.shell.contracts[address]()

    def balance(self) -> Decimal:
        """ Get account balance

        :return: amount in tez
        """
        balance_str = self.account()['balance']
        return (Decimal(balance_str) / 10 ** 6).quantize(Decimal('0.000001'))

    def now(self) -> int:
        """ Timestamp of the latest block + block time (UTC).
        """
        return self.context.get_now()

    def contract(self, address) -> ContractInterface:
        """ Get a high-level interface for a given smart contract id.

        :param address: KT address of a smart contract
        :rtype: ContractInterface
        """
        return ContractInterface.from_context(self._spawn_context(address=address))

    def using(
        self,
        shell: Optional[Union[ShellQuery, str]] = None,
        key: Optional[Union[Key, str, dict]] = None,
        mode: Optional[str] = None,
        ipfs_gateway: Optional[str] = None,
    ):
        """ Change current rpc endpoint and account (private key).

        :param shell: one of 'mainnet', '***net', or RPC node uri, or instance of `ShellQuery`
        :param key: base58 encoded key, path to the faucet file, faucet file itself, alias from tezos-client, or `Key`
        :param mode: whether to use `readable` or `optimized` encoding for parameters/storage/other
        :returns: A copy of current object with changes applied
        """
        return PyTezosClient(
            context=self._spawn_context(
                shell=shell,
                key=key,
                mode=mode,
                ipfs_gateway=ipfs_gateway,
            )
        )

    @property
    def loglevel(self) -> int:
        return logger.level

    @loglevel.setter
    def loglevel(self, value: Union[str, int]) -> None:
        if is_interactive():
            logging.getLogger().setLevel(value)
        logger.setLevel(value)

    def activate_protocol(self, protocol_hash: str) -> BlockHeader:
        """ Initiate user-activated upgrade (sandbox only)

        :param protocol_hash: Protocol hash
        :rtype: BlockHeader
        """
        return BlockHeader.activate_protocol(
            protocol_hash=protocol_hash,
            parameters=get_protocol_parameters(protocol_hash),
            context=self.context
        )

    def bake_block(self, min_fee: int = 0) -> BlockHeader:
        """ Create and inject new block with operations from mempool

        :param min_fee: filter operations by fee (default is 0)
        :rtype: BlockHeader
        """
        return BlockHeader.bake_block(
            min_fee=min_fee,
            context=self.context,
        )

    def sign_message(self, message: str, block: Union[str, int] = 'genesis') -> str:
        """Sign arbitrary message with guarantee that resulting operation won't be used onchain.

        :param message: Message to sign
        :param block: Specify block, defaults to genesis
        :returns: Base58-encoded signature (non-generic)
        """
        return self.key.sign(self.failing_noop(message).message(block=block))

    def check_message(self, message: str, public_key: str, signature: str,
                      block: str = 'genesis') -> None:
        """Check message signature

        :param message: Signed operation
        :param public_key: Signer's public key
        :param signature: Message signature
        :param block: Specify block, defaults to genesis
        """
        pk = Key.from_encoded_key(public_key)
        pk.verify(
            signature=signature,
            message=self.failing_noop(message).message(block=block),
        )

    def wait(
        self,
        *operation_groups: OperationGroup,
        min_confirmations: int = 1,
        num_blocks_wait: int = 5,
        time_between_blocks: Optional[int] = None,
        prev_hash: Optional[str] = None
    ) -> Tuple[OperationGroup, ...]:
        """Wait for multiple injected operations to get enough confirmations

        :param min_confirmations: number of block injections to wait for before returning
        :param num_blocks_wait: number of blocks to wait for injection
        :param time_between_blocks: override the corresponding parameter from constants
        :param prev_hash: Current block hash (optional). If not set, current head is used.
        """
        logger.info('Waiting for %s confirmations in %s blocks', min_confirmations, num_blocks_wait)
        confirmations = {opg.opg_hash: 0 for opg in operation_groups}
        for _ in range(num_blocks_wait):
            logger.info('Waiting for the next block')
            prev_hash = self.shell.wait_next_block(time_between_blocks=time_between_blocks, prev_hash=prev_hash)
            block_operations = self.shell.blocks[prev_hash].operations.managers()

            for opg in operation_groups:
                if confirmations[opg.opg_hash] == 0:
                    res = next((item for item in block_operations if item['hash'] == opg.opg_hash), None)
                    if res is not None:
                        logger.info('Operation %s was included in block %s', opg.opg_hash, prev_hash)
                        confirmations[opg.opg_hash] = 1
                        if not OperationResult.is_applied(res):
                            raise RpcError.from_errors(OperationResult.errors(res)) from None
                else:
                    confirmations[opg.opg_hash] += 1
                    logger.info('Got %s/%s confirmations for %s',
                                confirmations[opg.opg_hash], min_confirmations, opg.opg_hash)

            if any(value == 0 for value in confirmations.values()):
                pending_operations = self.shell.mempool.pending_operations.flatten()
                for opg in operation_groups:
                    if confirmations[opg.opg_hash] == 0:
                        res = next((item for item in pending_operations if item['hash'] == opg.opg_hash), None)
                        if res is not None:
                            logger.info('Operation %s is still in mempool', opg.opg_hash)
                            if not OperationResult.is_applied(res):
                                raise RpcError.from_errors(OperationResult.errors(res)) from None

            for opg in operation_groups:
                if confirmations[opg.opg_hash] == 0:
                    confirmations[opg.opg_hash] = self.shell.get_confirmations(
                        opg_hash=opg.opg_hash,
                        kind=opg.contents[0]['kind'],
                        branch=opg.branch,
                        head=prev_hash
                    )
                    if confirmations[opg.opg_hash] == 0:
                        raise ValueError(f'Operation {opg.opg_hash} is not found') from None

            if all(value >= min_confirmations for value in confirmations.values()):
                return operation_groups

        required_confirmations = min_confirmations * len(operation_groups)
        gathered_confirmations = sum(confirmations.values())
        raise TimeoutError(f'Operations got {gathered_confirmations}/{required_confirmations} confirmations in {num_blocks_wait} blocks')
