from pprint import pformat
from decimal import Decimal
from typing import Union
from deprecation import deprecated

from pytezos.contract.result import ContractCallResult
from pytezos.operation.group import OperationGroup
from pytezos.jupyter import get_class_docstring
from pytezos.context.mixin import ContextMixin
from pytezos.michelson.format import micheline_to_michelson
from pytezos.operation.content import format_tez, format_mutez
from pytezos.operation.result import OperationResult
from pytezos.context.impl import ExecutionContext
from pytezos.michelson.repl import Interpreter
from pytezos.michelson.sections.storage import StorageSection
from pytezos.michelson.program import MichelsonProgram


def skip_nones(**kwargs) -> dict:
    return {k: v for k, v in kwargs.items() if v is not None}


def is_edo(context: ExecutionContext) -> bool:
    return context.shell.head.header()['protocol'].startswith('PtEdo')


class ContractCall(ContextMixin):
    """ Proxy class encapsulating a contract call: contract type scheme, contract address, parameters, and amount
    """

    def __init__(self, context: ExecutionContext, parameters: dict, amount: Union[int, Decimal] = 0):
        super(ContractCall, self).__init__(context=context)
        self.parameters = parameters
        self.amount = amount

    def __repr__(self):
        res = [
            super(ContractCall, self).__repr__(),
            f'.amount  # {self.amount}',
            '\nParameters',
            pformat(self.parameters),
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def with_amount(self, amount: Union[int, Decimal]):
        """ Send funds to the contract too.

        :param amount: amount in microtez (int) or tez (Decimal)
        :rtype: ContractCall
        """
        return ContractCall(context=self.context,
                            parameters=self.parameters,
                            amount=amount)

    def as_transaction(self) -> OperationGroup:
        """ Get operation content

        :rtype: OperationGroup
        """
        return OperationGroup(context=self._spawn_context()) \
            .transaction(destination=self.address,
                         amount=self.amount,
                         parameters=self.parameters)

    @property
    @deprecated(deprecated_in='3.0.0', removed_in='3.1.0')
    def operation_group(self) -> OperationGroup:
        return self.as_transaction().fill()

    @deprecated(deprecated_in='3.0.0', removed_in='3.1.0')
    def inject(self, _async=True, preapply=True, check_result=True, num_blocks_wait=2):
        return self.operation_group.autofill().sign().inject(
            _async=_async,
            preapply=preapply,
            check_result=check_result,
            num_blocks_wait=num_blocks_wait)

    def cmdline(self):
        """ Generate command line for tezos client.
        """
        arg = micheline_to_michelson(self.parameters['value'], inline=True)
        source = self.key.public_key_hash()
        amount = format_tez(self.amount)
        entrypoint = self.parameters['entrypoint']
        return f'transfer {amount} from {source} to {self.address} --entrypoint \'{entrypoint}\' --arg \'{arg}\''

    def interpret(self, storage=None,
                  source=None, sender=None, amount=None, balance=None, chain_id=None, level=None, now=None) \
            -> ContractCallResult:
        """ Run code in the builtin REPL (WARNING! Not recommended for critical tasks).

        :param storage: initial storage as Python object, leave None if you want to generate a dummy one
        :param source: patch SOURCE
        :param sender: patch SENDER
        :param amount: patch AMOUNT
        :param balance: patch BALANCE
        :param chain_id: patch CHAIN_ID
        :param level: patch LEVEL
        :param now: patch NOW
        :rtype: pytezos.contract.result.ContractCallResult
        """
        storage_ty = StorageSection.match(self.context.storage_expr)
        if storage is None:
            initial_storage = storage_ty.dummy(self.context).to_micheline_value(lazy_diff=True)
        else:
            initial_storage = storage_ty.from_python_object(storage).to_micheline_value(lazy_diff=True)
        operations, storage, lazy_diff, stdout, error = Interpreter.run_code(
            parameter=self.parameters['value'],
            entrypoint=self.parameters['entrypoint'],
            storage=initial_storage,
            script=self.context.script['code'],
            source=source,
            sender=sender or source,
            amount=amount or self.amount,
            balance=balance,
            chain_id=chain_id,
            level=level,
            now=now
        )
        if error:
            print('\n'.join(stdout))
            raise error
        res = {
            'operations': operations,
            'storage': storage,
            'lazy_diff': lazy_diff
        }
        return ContractCallResult.from_run_code(res, parameters=self.parameters, context=self.context)

    def run_code(self, storage=None,
                 source=None, sender=None, amount=None, balance=None, chain_id=None, gas_limit=None) \
            -> ContractCallResult:
        """ Execute using RPC interpreter

        :param storage: initial storage as Python object, leave None if you want to generate a dummy one
        :param source: patch SOURCE
        :param sender: patch SENDER
        :param amount: patch AMOUNT
        :param balance: patch BALANCE
        :param chain_id: patch CHAIN_ID
        :param gas_limit: restrict max comsumed gas
        :rtype: ContractCallResult
        """
        storage_ty = StorageSection.match(self.context.storage_expr)
        if storage is None:
            initial_storage = storage_ty.dummy(self.context).to_micheline_value(lazy_diff=True)
        else:
            initial_storage = storage_ty.from_python_object(storage).to_micheline_value(lazy_diff=True)
        script = [self.context.parameter_expr, self.context.storage_expr, self.context.code_expr]
        query = skip_nones(
            script=script,
            storage=initial_storage,
            entrypoint=self.parameters['entrypoint'],
            input=self.parameters['value'],
            amount=format_mutez(amount or self.amount),
            chain_id=chain_id or self.context.get_chain_id(),
            source=sender,
            payer=source,
            balance=str(balance or 0) if is_edo(self.context) else None,
            gas=str(gas_limit) if gas_limit is not None else None
        )
        res = self.shell.head.helpers.scripts.run_code.post(query)
        return ContractCallResult.from_run_code(res, parameters=self.parameters, context=self.context)

    def run_operation(self) -> ContractCallResult:
        """ Simulate operation using real context

        :rtype: ContractCallResult
        """
        opg_with_metadata = self.as_transaction().fill().run()
        results = ContractCallResult.from_run_operation(opg_with_metadata, context=self.context)
        assert len(results) == 1
        return results[0]

    @deprecated(deprecated_in='3.0.0', removed_in='3.1.0')
    def result(self, storage=None, source=None, sender=None, gas_limit=None) -> ContractCallResult:
        """ Simulate operation and parse the result.

        :param storage: Python object only. If storage is specified, `run_code` is called instead of `run_operation`.
        :param source: Can be specified for unit testing purposes
        :param sender: Can be specified for unit testing purposes, \
        see https://tezos.gitlab.io/whitedoc/michelson.html#operations-on-contracts for the difference
        :param gas_limit: Specify gas limit (default is gas hard limit)
        :rtype: ContractCallResult
        """
        if storage or source or sender or gas_limit:
            return self.run_code(storage=storage, source=source, sender=sender, gas_limit=gas_limit)
        else:
            return self.run_operation()

    @deprecated(deprecated_in='3.0.0', removed_in='3.1.0')
    def view(self):
        """ Get return value of a view method.

        :returns: object
        """
        opg_with_metadata = self.as_transaction().fill().run()
        internal_operations = OperationResult.get_contents(opg_with_metadata, source=self.address)
        assert len(internal_operations) == 1, f'multiple internal operations, not sure which to pick'
        view_script = self.shell.contracts[internal_operations[0]['destination']].code()
        view = MichelsonProgram.match(view_script)
        return view.parameter.from_parameters(internal_operations[0]['parameters']).to_python_object()
