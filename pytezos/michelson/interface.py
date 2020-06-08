from os.path import exists, expanduser
from typing import List
from pprint import pformat

from pytezos.operation.result import OperationResult
from pytezos.michelson.contract import Contract
from pytezos.michelson.converter import convert
from pytezos.michelson.micheline import skip_nones
from pytezos.michelson.formatter import micheline_to_michelson
from pytezos.operation.group import OperationGroup
from pytezos.operation.content import format_mutez, format_tez
from pytezos.interop import Interop
from pytezos.tools.docstring import get_class_docstring
from pytezos.repl.interpreter import Interpreter


class ContractCallResult(OperationResult):

    @classmethod
    def from_contract_call(cls, operation_group: dict, address, contract: Contract) -> list:
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
            kwargs = dict(storage=contract.storage.decode(res.storage))
            if hasattr(res, 'big_map_diff'):
                contract.storage.big_map_init(res.storage)
                kwargs.update(big_map_diff=contract.storage.big_map_diff_decode(res.big_map_diff))
            if hasattr(res, 'parameters'):
                kwargs.update(parameters=contract.parameter.decode(data=res.parameters))
            if hasattr(res, 'operations'):
                kwargs.update(operations=res.operations)
            return cls(**kwargs)

        return list(map(decode_result, results))

    @classmethod
    def from_code_run(cls, code_run: dict, parameters, contract: Contract):
        contract.storage.big_map_init(code_run['storage'])
        return cls(
            parameters=contract.parameter.decode(parameters),
            storage=contract.storage.decode(code_run['storage']),
            big_map_diff=contract.storage.big_map_diff_decode(code_run.get('big_map_diff', [])),
            operations=code_run.get('operations', [])
        )

    @classmethod
    def from_repl_result(cls, res: dict, parameters, contract: Contract):
        contract.storage.big_map_init(res['result']['storage'].val_expr)
        return cls(
            parameters=contract.parameter.decode(parameters),
            storage=contract.storage.decode(res['result']['storage'].val_expr),
            big_map_diff=contract.storage.big_map_diff_decode(res['result']['big_map_diff']),
            operations=[x.content for x in res['result']['operations']]
        )


class ContractCall(Interop):

    def __init__(self, parameters,
                 address=None, contract: Contract = None, factory=Contract, amount=0, shell=None, key=None):
        super(ContractCall, self).__init__(shell=shell, key=key)
        self.parameters = parameters
        self.address = address
        self.amount = amount

        if contract is None:
            assert address is not None
            contract = factory.from_micheline(self.shell.contracts[address].code())

        self.contract = contract

    def _spawn(self, **kwargs):
        return ContractCall(
            parameters=self.parameters,
            address=self.address,
            contract=self.contract,
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
        """
        Send funds to the contract too.
        :param amount: amount in microtez (int) or tez (Decimal)
        :return: ContractCall
        """
        return self._spawn(amount=amount)

    @property
    def operation_group(self) -> OperationGroup:
        """
        Show generated operation group.
        :return: OperationGroup
        """
        return OperationGroup(shell=self.shell, key=self.key) \
            .transaction(destination=self.address,
                         amount=self.amount,
                         parameters=self.parameters) \
            .fill()

    def inject(self):
        """
        Autofill, sign and inject resulting operation group.
        """
        return self.operation_group.autofill().sign().inject()

    def cmdline(self):
        """
        Generate command line for tezos client.
        :return: str
        """
        arg = micheline_to_michelson(self.parameters['value'], inline=True)
        source = self.key.public_key_hash()
        amount = format_tez(self.amount)
        entrypoint = self.parameters['entrypoint']
        return f'transfer {amount} from {source} to {self.address} ' \
               f'--entrypoint \'{entrypoint}\' --arg \'{arg}\''

    def interpret(self, storage, source=None, sender=None, amount=None, balance=None, chain_id=None, now=None):
        """
        Run code in the builtin REPL (WARNING! Not recommended for critical tasks)
        :param storage: Python object
        :param source: patch SOURCE
        :param sender: patch SENDER
        :param amount: patch AMOUNT
        :param balance: patch BALANCE
        :param chain_id: patch CHAIN_ID
        :param now: patch NOW
        :return: ContractCallResult
        """
        i = Interpreter()
        i.execute(self.contract.text)

        if source is None:
            source = self.key.public_key_hash()
        if sender is None:
            sender = source
        if amount is None:
            amount = 0
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

        s_expr = micheline_to_michelson(self.contract.storage.encode(storage), inline=True, wrap=True)
        p_expr = micheline_to_michelson(self.parameters['value'], inline=True, wrap=True)
        res = i.execute(f'RUN %{self.parameters["entrypoint"]} {p_expr} {s_expr}')

        return ContractCallResult.from_repl_result(
            res, parameters=self.parameters, contract=self.contract)

    def result(self, storage=None, source=None, sender=None, gas_limit=None):
        """
        Simulate operation and parse the result.
        :param storage: Python object only. If storage is specified, `run_code` is called instead of `run_operation`.
        :param source: Can be specified for unit testing purposes
        :param sender: Can be specified for unit testing purposes,
        see https://tezos.gitlab.io/whitedoc/michelson.html#operations-on-contracts for the difference
        :param gas_limit: Specify gas limit (default is gas hard limit)
        :return: ContractCallResult
        """
        chain_id = self.shell.chains.main.chain_id()
        if storage is not None or source or sender or gas_limit:
            query = skip_nones(
                script=self.contract.code,
                storage=self.contract.storage.encode(storage),
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
                code_run_res, parameters=self.parameters, contract=self.contract)
        else:
            opg_with_metadata = self.operation_group.fill().run()
            res = ContractCallResult.from_contract_call(
                opg_with_metadata, address=self.address, contract=self.contract)
            return res[0] if res else None

    def view(self):
        """
        Get return value of a view method.
        :return: object
        """
        opg_with_metadata = self.operation_group.fill().run()
        view_operation = OperationResult.get_contents(opg_with_metadata, source=self.address)[0]
        view_contract = Contract.from_micheline(self.shell.contracts[view_operation['destination']].code())
        return view_contract.parameter.decode(view_operation['parameters'])


class ContractEntrypoint(Interop):

    def __init__(self, name, address=None, contract: Contract = None, factory=Contract, shell=None, key=None):
        super(ContractEntrypoint, self).__init__(shell=shell, key=key)
        if contract is None:
            assert address is not None
            code = self.shell.contracts[address].code()
            contract = factory.from_micheline(code)

        self.contract = contract
        self.name = name
        self.address = address

    def _spawn(self, **kwargs):
        return ContractEntrypoint(
            name=self.name,
            contract=self.contract,
            address=self.address,
            shell=kwargs.get('shell', self.shell),
            key=kwargs.get('key', self.key),
        )

    def __repr__(self):
        res = [
            super(ContractEntrypoint, self).__repr__(),
            f'.address  # {self.address}',
            f'\n{self.__doc__}'
        ]
        return '\n'.join(res)

    def __call__(self, *args, **kwargs):
        if args:
            if len(args) == 1:
                (data, is_single) = (args[0], True)
            else:
                (data, is_single) = (list(args), False)
        elif kwargs:
            (data, is_single) = (kwargs, False)
        else:
            (data, is_single) = ([], False)

        if self.name:
            data = {self.name: data} if data or is_single else self.name

        parameters = self.contract.parameter.encode(data)
        return ContractCall(
            parameters=parameters,
            address=self.address,
            contract=self.contract,
            shell=self.shell,
            key=self.key,
        )


class ContractInterface(Interop):
    __default_entry__ = 'call'

    def __init__(self, address=None, contract: Contract = None, factory=Contract, shell=None, key=None):
        super(ContractInterface, self).__init__(shell=shell, key=key)
        if contract is None:
            assert address is not None
            code = self.shell.contracts[address].code()
            contract = factory.from_micheline(code)

        self.contract = contract
        self.address = address

        for entry_name, docstring in contract.parameter.entries(default=self.__default_entry__):
            entry_point = ContractEntrypoint(
                name=entry_name if entry_name != self.__default_entry__ else None,
                address=self.address,
                contract=contract,
                shell=self.shell,
                key=self.key
            )
            entry_point.__doc__ = docstring
            setattr(self, entry_name, entry_point)

    def _spawn(self, **kwargs):
        return ContractInterface(
            address=self.address,
            contract=self.contract,
            shell=kwargs.get('shell', self.shell),
            key=kwargs.get('key', self.key)
        )

    def __repr__(self):
        entrypoints, _ = zip(*self.contract.parameter.entries(default=self.__default_entry__))
        res = [
            super(ContractInterface, self).__repr__(),
            f'.address  # {self.address}',
            '\nEntrypoints',
            *list(map(lambda x: f'.{x}()', entrypoints)),
            '\nHelpers',
            get_class_docstring(self.__class__,
                                attr_filter=lambda x: not x.startswith('_') and x not in entrypoints)
        ]
        return '\n'.join(res)

    @classmethod
    def create_from(cls, source, shell=None, factory=Contract):
        if isinstance(source, str) and exists(expanduser(source)):
            contract = factory.from_file(source)
        else:
            contract = factory(convert(source, output='micheline'))

        return ContractInterface(contract=contract, shell=shell)

    def big_map_get(self, path, block_id='head'):
        """
        Get BigMap entry as Python object by plain key and block height
        :param path: Json path to the key (or just key to access default BigMap location).
            Use `/` to separate nodes and `:` to separate tuple args.
            In any other case you'd need to escape those symbols.
        :param block_id: Block height / hash / offset to use, default is `head`
        :return: object
        """
        if not self.contract.storage.big_map_schema:
            storage = self.shell.blocks[block_id].context.contracts[self.address].storage()
            self.contract.storage.big_map_init(storage)

        query = self.contract.storage.big_map_query(path)
        if query.get('big_map_id'):
            value = self.shell.blocks[block_id].context.big_maps[query['big_map_id']][query['script_expr']]()
        else:
            value = self.shell.blocks[block_id].context.contracts[self.address].big_map_get.post(query)
        return self.contract.storage.big_map_decode(value, query.get('big_map_id'))

    def storage(self, block_id='head'):
        """
        Get storage as Pythons object at specified block height.
        :param block_id: Block height / hash / offset to use, default is `head`
        :return: object
        """
        storage = self.shell.blocks[block_id].context.contracts[self.address].storage()
        return self.contract.storage.decode(storage)

    def operation_result(self, operation_group: dict) -> List[ContractCallResult]:
        """
        Get operation parameters, storage and big_map_diff as Python objects.
        Can locate operation inside operation groups with multiple contents and/or internal operations.
        :param operation_group: {'branch', 'protocol', 'contents', 'signature'}
        :return: ContractCallResult
        """
        return ContractCallResult.from_contract_call(
            operation_group, address=self.address, contract=self.contract)

    def manager(self):
        """
        Get contract manager address (tz)
        :return: str
        """
        return self.shell.block.context.contracts[self.address].manager()
