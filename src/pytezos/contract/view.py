from pprint import pformat
from typing import Any, Dict, List, Optional

from pytezos.context.impl import ExecutionContext
from pytezos.context.mixin import ContextMixin  # type: ignore
from pytezos.contract.call import ContractCallResult, skip_nones
from pytezos.jupyter import get_class_docstring
from pytezos.logging import logger
from pytezos.michelson.micheline import MichelsonRuntimeError
from pytezos.michelson.repl import Interpreter
from pytezos.michelson.types.base import MichelsonType, generate_pydoc


def format_view_script(param_ty_expr, storage_ty_expr, return_ty_expr, code_expr):
    return dict(
        code=[
            {
                'prim': 'parameter',
                'args': [
                    {
                        'prim': 'pair',
                        'args': [
                            param_ty_expr,
                            storage_ty_expr['args'][0],
                        ],
                    },
                ],
            },
            {
                'prim': 'storage',
                'args': [
                    {
                        'prim': 'option',
                        'args': [return_ty_expr],
                    },
                ],
            },
            {
                'prim': 'code',
                'args': [
                    [
                        {'prim': 'CAR'},
                        code_expr,
                        {'prim': 'SOME'},
                        {
                            'prim': 'NIL',
                            'args': [
                                {'prim': 'operation'},
                            ],
                        },
                        {'prim': 'PAIR'},
                    ]
                ],
            },
        ]
    )


def format_view_params(param_expr, storage_expr):
    return {
        'entrypoint': 'default',
        'value': {
            'prim': 'Pair',
            'args': [param_expr, storage_expr],
        },
    }


class ContractView(ContextMixin):
    """Proxy class for handling off-chain and on-chain views"""

    def __init__(
        self,
        context: ExecutionContext,
        name: str,
        parameter: Optional[Dict[str, Any]],
        return_type: Dict[str, Any],
        code: List[Any],
    ) -> None:
        super().__init__(context=context)
        self.name = name
        self.param_ty_expr = parameter or {'prim': 'unit'}
        self.return_ty_expr = return_type
        self.code_expr = code
        self.__doc__ = generate_pydoc(MichelsonType.match(self.param_ty_expr), title=name)

    def __repr__(self) -> str:
        res = [
            super().__repr__(),
            f'.name\t{self.name}',
            f'\nBuiltin\n(*args, **kwargs)  # build view parameters (see typedef)',
            f'\nTypedef\n{self.__doc__}',
            '\nHelpers',
            get_class_docstring(self.__class__),
        ]
        return '\n'.join(res)

    def __call__(self, *args, **kwargs) -> 'ContractViewCall':
        """Spawn a contract call proxy initialized with the entrypoint name

        :param args: entrypoint args
        :param kwargs: entrypoint key-value args
        :rtype: ContractViewCall
        """
        if args:
            if len(args) == 1:
                py_obj = args[0]
            else:
                py_obj = args
        elif kwargs:
            py_obj = kwargs
        else:
            py_obj = None

        try:
            param_ty = MichelsonType.match(self.param_ty_expr)
            param_expr = param_ty.from_python_object(py_obj).to_micheline_value()
        except MichelsonRuntimeError as e:
            logger.info(self.__doc__)
            raise ValueError(f'Unexpected arguments: {pformat(py_obj)}', *e.args) from e

        return ContractViewCall(
            context=self.context,
            param_expr=param_expr,
            param_ty_expr=self.param_ty_expr,
            return_ty_expr=self.return_ty_expr,
            code_expr=self.code_expr,
            name=self.name,
        )


class ContractViewCall(ContextMixin):
    """Proxy class encapsulating a contract call: contract type scheme, contract address, parameters, and amount"""

    def __init__(
        self, context: ExecutionContext, param_expr: dict, param_ty_expr: dict, return_ty_expr: dict, code_expr: list, name: str
    ) -> None:
        super().__init__(context=context)
        self.name = name
        self.param_expr = param_expr
        self.param_ty_expr = param_ty_expr
        self.return_ty_expr = return_ty_expr
        self.code_expr = code_expr

    def _encode_storage(self, storage=None):
        try:
            storage_ty = MichelsonType.match(self.context.storage_expr)
            if storage is None:
                return storage_ty.dummy(self.context).to_micheline_value(lazy_diff=True)
            else:
                return storage_ty.from_python_object(storage).to_micheline_value(lazy_diff=True)
        except MichelsonRuntimeError as e:
            logger.info(self.__doc__)
            raise ValueError(f'Unexpected storage object: {pformat(storage)}', *e.args) from e

    def _get_storage(self, storage=None):
        if storage is None:
            storage_expr = self.context.get_storage_value(self.address)
            if storage_expr is None:
                return self._encode_storage()
            else:
                return storage_expr
        else:
            return self._encode_storage(storage)

    def _prepare_query(
        self,
        parameters=None,
        source=None,
        sender=None,
        balance=None,
        chain_id=None,
        gas_limit=None,
    ):
        script = format_view_script(
            param_ty_expr=self.param_ty_expr,
            storage_ty_expr=self.context.storage_expr,
            return_ty_expr=self.return_ty_expr,
            code_expr=self.code_expr,
        )
        return_ty = MichelsonType.match(self.return_ty_expr)
        initial_storage = return_ty.dummy(self.context).to_micheline_value(lazy_diff=True)
        return skip_nones(
            script=script,
            storage=initial_storage,
            entrypoint=parameters['entrypoint'],
            input=parameters['value'],
            amount='0',
            chain_id=chain_id or self.context.get_chain_id(),
            source=sender,
            payer=source,
            balance=str(balance or 0),
            gas=str(gas_limit) if gas_limit is not None else None,
        )

    def run_code(
        self,
        storage=None,
        source=None,
        sender=None,
        balance=None,
        chain_id=None,
        gas_limit=None,
    ) -> ContractCallResult:
        """Execute using RPC interpreter.

        :param storage: initial storage as Python object, leave None if you want to generate a dummy one
        :param source: patch SOURCE
        :param sender: patch SENDER
        :param balance: patch BALANCE
        :param chain_id: patch CHAIN_ID
        :param gas_limit: restrict max consumed gas
        :rtype: ContractCallResult
        """
        parameters = format_view_params(param_expr=self.param_expr, storage_expr=self._encode_storage(storage))
        query = self._prepare_query(
            source=source, sender=sender, balance=balance, chain_id=chain_id, gas_limit=gas_limit, parameters=parameters
        )
        res = self.shell.blocks[self.block_id].helpers.scripts.run_code.post(query)
        return ContractCallResult.from_run_code(res, parameters=parameters, context=self.context)

    def storage_view(self, storage=None):
        """Get return value of an off-chain view.

        :param storage: override current contract storage (as Python object)
        :returns: Decoded return value
        """
        parameters = format_view_params(param_expr=self.param_expr, storage_expr=self._get_storage(storage))
        script = format_view_script(
            param_ty_expr=self.param_ty_expr,
            storage_ty_expr=self.context.storage_expr,
            return_ty_expr=self.return_ty_expr,
            code_expr=self.code_expr,
        )
        _, storage, stdout, error = Interpreter.run_callback(
            parameter=parameters['value'],
            entrypoint=parameters['entrypoint'],
            storage={'prim': 'None'},
            context=self._spawn_context(script=script, address=self.address),
        )
        if error:
            logger.debug('\n'.join(stdout))
            raise error
        return storage  # type: ignore

    def onchain_view(self, storage=None, balance=None, view_results: Optional[Dict[str, Any]] = None):
        """Get return value of an on-chain view.

        :param storage: override current contract storage (as Python object)
        :param balance: patch BALANCE
        :param view_results: patch VIEW calls (keys must be string "address%view", values => Python objects)
        :returns: Decoded return value
        """
        ret, stdout, error = Interpreter.run_view(
            name=self.name,
            parameter=self.param_expr,
            storage=self._get_storage(storage),
            context=self._spawn_context(
                balance=balance,
                script={**self.context.script, 'storage': self._encode_storage(storage)},  # type: ignore
                view_results=view_results,
            ),
        )
        if error:
            logger.debug('\n'.join(stdout))
            raise error
        return ret  # type: ignore
