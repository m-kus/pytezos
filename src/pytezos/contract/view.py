from pprint import pformat
from typing import Any, Dict, List, Optional

from pytezos.context.impl import ExecutionContext
from pytezos.context.mixin import ContextMixin  # type: ignore
from pytezos.contract.call import ContractCall
from pytezos.jupyter import get_class_docstring
from pytezos.logging import logger
from pytezos.michelson.micheline import MichelsonRuntimeError
from pytezos.michelson.types.base import MichelsonType, generate_pydoc


class OffChainView(ContextMixin):
    """Proxy class for handling off-chain TZIP-16 views"""

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
        self.param_expr = parameter or {'prim': 'unit'}
        self.rtype_expr = return_type
        self.code_expr = code
        self.__doc__ = generate_pydoc(MichelsonType.match(self.param_expr), title=name)

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

    @property
    def script(self) -> Dict[str, Any]:
        return dict(
            code=[
                {
                    'prim': 'parameter',
                    'args': [
                        {
                            'prim': 'pair',
                            'args': [
                                self.param_expr,
                                self.context.get_storage_expr()['args'][0],
                            ],
                        },
                    ],
                },
                {
                    'prim': 'storage',
                    'args': [
                        {
                            'prim': 'option',
                            'args': [self.rtype_expr],
                        },
                    ],
                },
                {
                    'prim': 'code',
                    'args': [
                        [
                            {'prim': 'CAR'},
                            self.code_expr,
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

    def __call__(self, *args, **kwargs) -> ContractCall:
        """Spawn a contract call proxy initialized with the entrypoint name

        :param args: entrypoint args
        :param kwargs: entrypoint key-value args
        :rtype: ContractCall
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

        return ContractCall(
            context=self._spawn_context(address=self.address, script=self.script),
            parameters=self.encode(py_obj),
        )

    def encode(self, py_obj) -> Dict[str, Any]:
        """Encode transaction parameters from the given Python object

        :param py_obj: Python object
        :return: {entrypoint, value}
        """
        try:
            view_param_ty = MichelsonType.match(self.param_expr)
            view_param_expr = view_param_ty.from_python_object(py_obj).to_micheline_value()
            storage_expr = self.shell.blocks[self.context.block_id].context.contracts[self.address].storage()
            return {
                'entrypoint': 'default',
                'value': {
                    'prim': 'Pair',
                    'args': [view_param_expr, storage_expr],
                },
            }
        except MichelsonRuntimeError as e:
            logger.info(self.__doc__)
            raise ValueError(f'Unexpected arguments: {pformat(py_obj)}', *e.args) from e
