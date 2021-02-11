from typing import Optional, Union
from decimal import Decimal

from pytezos.rpc import ShellQuery
from pytezos.crypto.key import Key
from pytezos.operation.group import OperationGroup
from pytezos.operation.content import ContentMixin
from pytezos.contract.interface import ContractInterface
from pytezos.contract.call import ContractCall
from pytezos.context.mixin import ContextMixin
from pytezos.jupyter import get_class_docstring


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

        :param protocol: Leave None for autocomplete, otherwise you know what to do
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

    def using(self, shell: Optional[Union[ShellQuery, str]] = None, key: Optional[Union[Key, str]] = None):
        """ Change current rpc endpoint and account (private key).

        :param shell: one of 'mainnet', '***net', or RPC node uri, or instance of `ShellQuery`
        :param key: base58 encoded key, path to the faucet file, alias from tezos-client, or instance of `Key`
        :returns: A copy of current object with changes applied
        """
        return PyTezosClient(context=self._spawn_context(shell, key))
