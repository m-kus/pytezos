from pprint import pformat

from pytezos.operation.group import OperationGroup
from pytezos.contract.script import ContractScript
from pytezos.jupyter import get_class_docstring
from pytezos.interop import Interop
from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.repl import Interpreter
from pytezos.operation.content import format_tez, format_mutez
from pytezos.operation.result import OperationResult


def skip_nones(**kwargs) -> dict:
    return {k: v for k, v in kwargs.items() if v is not None}


class ContractCallResult(OperationResult):
    """ Encapsulates the result of a contract invocation.
    """

    @classmethod
    def from_contract_call(cls, operation_group: dict, address, script: ContractScript) -> list:
        """ Get a list of results from an operation group content with metadata.

        :param operation_group: {..., "contents": [{..., kind: "transaction", ...}]}
        :param address: address of the invoked contract
        :param script: invoked contract
        :rtype: List[ContractCallResult]
        """
        results = list()
        for content in OperationResult.iter_contents(operation_group):
            if content['kind'] == 'transaction':
                if content['destination'] == address:
                    results.append(cls.from_transaction(content))
            elif content['kind'] == 'origination':
                result = cls.get_result(content)
                if address in result.get('originated_contracts', []):
                    results.append(cls.from_origination(content))

        def decode_result(res):
            storage = script.storage.type.from_micheline_value(res.context)
            kwargs = dict(storage=storage.to_python_object())
            if hasattr(res, 'lazy_diff'):
                extended_storage = storage.merge_lazy_diff(res.lazy_diff)
                kwargs.update(storage_diff=extended_storage.to_python_object(lazy_diff=True))
            if hasattr(res, 'parameters'):
                kwargs.update(parameters=script.parameter.decode(data=res.parameters))
            if hasattr(res, 'operations'):
                kwargs.update(operations=res.operations)
            return cls(**kwargs)

        return list(map(decode_result, results))

    @classmethod
    def from_code_run(cls, code_run: dict, parameters, script: ContractScript):
        """ Parse a result of `run_code` execution.

        :param code_run: RPC response (json)
        :param parameters: Micheline expression
        :param script: invoked contract
        :rtype: ContractCallResult
        """
        storage = script.storage.type.from_micheline_value(code_run['storage'])
        extended_storage = storage.merge_lazy_diff(code_run.get('lazy_diff', []))
        return cls(
            parameters=script.parameter.decode(parameters),
            storage=storage.to_python_object(),
            storage_diff=extended_storage.to_python_object(lazy_diff=True),
            operations=code_run.get('operations', [])
        )

    @classmethod
    def from_repl_result(cls, res: dict, parameters, contract: ContractScript):
        """ Parse an output of the builtin interpreter.

        :param res: Interpreter output
        :param parameters: Micheline expression
        :param contract: invoked contract
        :returns: ContractCallResult
        """
        contract.storage.big_map_init(res['result']['storage'].val_expr)
        return cls(
            parameters=contract.parameter.decode(parameters),
            storage=contract.storage.decode(res['result']['storage'].val_expr),
            big_map_diff=contract.storage.big_map_diff_decode(res['result']['big_map_diff']),
            operations=[x.content for x in res['result']['operations']]
        )


class ContractCall(Interop):
    """ Proxy class encapsulating a contract call: contract type scheme, contract address, parameters, and amount
    """

    def __init__(self, parameters,
                 address=None, script: ContractScript = None, amount=0, shell=None, key=None):
        super(ContractCall, self).__init__(shell=shell, key=key)
        self.parameters = parameters
        self.address = address
        self.amount = amount

        if script is None:
            assert address is not None
            script = ContractScript.from_micheline(self.shell.contracts[address].code())

        self.script = script

    def _spawn(self, **kwargs):
        return ContractCall(
            parameters=self.parameters,
            address=self.address,
            script=self.script,
            amount=kwargs.get('amount', self.amount),
            shell=kwargs.get('shell', self.shell),
            key=kwargs.get('key', self.key)
        )

    def __repr__(self):
        res = [
            super(ContractCall, self).__repr__(),
            f'.address  # {self.address}',
            f'.amount  # {self.amount}',
            '\nParameters',
            pformat(self.parameters),
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def with_amount(self, amount):
        """ Send funds to the contract too.

        :param amount: amount in microtez (int) or tez (Decimal)
        :rtype: ContractCall
        """
        return self._spawn(amount=amount)

    @property
    def operation_group(self) -> OperationGroup:
        """ Show generated operation group.

        :rtype: OperationGroup
        """
        return OperationGroup(shell=self.shell, key=self.key) \
            .transaction(destination=self.address,
                         amount=self.amount,
                         parameters=self.parameters) \
            .fill()

    def inject(self, _async=True, preapply=True, check_result=True, num_blocks_wait=2):
        """ Autofill, sign and inject resulting operation group.

        :param _async: do not wait for operation inclusion (default is True)
        :param preapply: do a preapply before injection
        :param check_result: raise RpcError in case operation is refused
        :param num_blocks_wait: number of blocks to wait for injection
        """
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
        return f'transfer {amount} from {source} to {self.address} ' \
               f'--entrypoint \'{entrypoint}\' --arg \'{arg}\''

    def interpret(self, storage, source=None, sender=None, amount=None, balance=None, chain_id=None, now=None):
        """ Run code in the builtin REPL (WARNING! Not recommended for critical tasks).

        :param storage: Python object
        :param source: patch SOURCE
        :param sender: patch SENDER
        :param amount: patch AMOUNT
        :param balance: patch BALANCE
        :param chain_id: patch CHAIN_ID
        :param now: patch NOW
        :rtype: ContractCallResult
        """
        i = Interpreter()
        i.execute(self.script.text)

        if source is None:
            source = self.key.public_key_hash()
        if sender is None:
            sender = source
        if amount is None:
            amount = self.amount or 0
        if balance is None:
            balance = 0

        patch_map = {
            'SOURCE': source,
            'SENDER': sender,
            'AMOUNT': amount,
            'BALANCE': balance,
            'CHAIN_ID': chain_id,
            'NOW': now
        }
        for instr, value in patch_map.items():
            if value is not None:
                value = f'"{value}"' if isinstance(value, str) else value
                i.execute(f'PATCH {instr} {value}')

        s_expr = micheline_to_michelson(self.script.storage.encode(storage), inline=True, wrap=True)
        p_expr = micheline_to_michelson(self.parameters['value'], inline=True, wrap=True)
        res = i.execute(f'RUN %{self.parameters["entrypoint"]} {p_expr} {s_expr}')

        return ContractCallResult.from_repl_result(
            res, parameters=self.parameters, contract=self.script)

    def result(self, storage=None, source=None, sender=None, gas_limit=None):
        """ Simulate operation and parse the result.

        :param storage: Python object only. If storage is specified, `run_code` is called instead of `run_operation`.
        :param source: Can be specified for unit testing purposes
        :param sender: Can be specified for unit testing purposes, \
        see https://tezos.gitlab.io/whitedoc/michelson.html#operations-on-contracts for the difference
        :param gas_limit: Specify gas limit (default is gas hard limit)
        :rtype: ContractCallResult
        """
        chain_id = self.shell.chains.main.chain_id()
        if storage is not None or source or sender or gas_limit:
            query = skip_nones(
                script=self.script.code,
                storage=self.script.storage.encode(storage),
                entrypoint=self.parameters['entrypoint'],
                input=self.parameters['value'],
                amount=format_mutez(self.amount),
                chain_id=chain_id,
                source=sender,
                payer=source,
                gas=str(gas_limit) if gas_limit is not None else None
            )
            code_run_res = self.shell.head.helpers.scripts.run_code.post(query)
            return ContractCallResult.from_code_run(
                code_run_res, parameters=self.parameters, script=self.script)
        else:
            opg_with_metadata = self.operation_group.fill().run()
            res = ContractCallResult.from_contract_call(
                opg_with_metadata, address=self.address, script=self.script)
            return res[0] if res else None

    def view(self):
        """ Get return value of a view method.

        :returns: object
        """
        opg_with_metadata = self.operation_group.fill().run()
        view_operation = OperationResult.get_contents(opg_with_metadata, source=self.address)[0]
        view_contract = ContractScript.from_micheline(self.shell.contracts[view_operation['destination']].code())
        return view_contract.parameter.decode(view_operation['parameters'])
