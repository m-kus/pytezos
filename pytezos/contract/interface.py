from os.path import exists, expanduser
from typing import List, Optional, Union
from deprecation import deprecated
from decimal import Decimal

from pytezos.rpc import ShellQuery
from pytezos.crypto.key import Key
from pytezos.operation.group import OperationGroup
from pytezos.contract.result import ContractCallResult
from pytezos.contract.entrypoint import ContractEntrypoint
from pytezos.michelson.program import MichelsonProgram
from pytezos.contract.data import ContractData
from pytezos.context.mixin import ContextMixin, ExecutionContext
from pytezos.jupyter import get_class_docstring
from pytezos.michelson.micheline import is_micheline
from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.types.base import generate_pydoc


class ContractInterface(ContextMixin):
    """ Proxy class for interacting with a contract.
    """
    program: MichelsonProgram

    def __init__(self, context: ExecutionContext):
        super(ContractInterface, self).__init__(context=context)
        self.entrypoints = self.program.parameter.list_entrypoints()
        for entrypoint, ty in self.entrypoints.items():
            attr = ContractEntrypoint(context=context, entrypoint=entrypoint)
            attr.__doc__ = generate_pydoc(ty, entrypoint)
            setattr(self, entrypoint, attr)

    def __repr__(self):
        res = [
            super(ContractInterface, self).__repr__(),
            '.storage',
            '.parameter',
            '\nEntrypoints',
            *list(map(lambda x: f'.{x}()', self.entrypoints)),
            '\nHelpers',
            get_class_docstring(self.__class__, attr_filter=lambda x: x not in self.entrypoints)
        ]
        return '\n'.join(res)

    def __getattr__(self, item: str) -> ContractEntrypoint:
        raise AttributeError(f'unexpected entrypoint {item}')

    @staticmethod
    def from_file(path: str, context: Optional[ExecutionContext] = None) -> 'ContractInterface':
        """ Create contract from michelson source code stored in a file.

        :param path: Path to the `.tz` file
        :param context: optional execution context
        :rtype: ContractInterface
        """
        with open(expanduser(path)) as f:
            return ContractInterface.from_michelson(f.read(), context)

    @staticmethod
    def from_michelson(source: str, context: Optional[ExecutionContext] = None) -> 'ContractInterface':
        """ Create contract from michelson source code.

        :param source: Michelson source code
        :param context: optional execution context
        :rtype: ContractInterface
        """
        return ContractInterface.from_micheline(michelson_to_micheline(source), context)

    @staticmethod
    def from_micheline(expression, context: Optional[ExecutionContext] = None) -> 'ContractInterface':
        """ Create contract from micheline expression.

        :param expression: [{'prim': 'parameter'}, {'prim': 'storage'}, {'prim': 'code'}]
        :param context: optional execution context
        :rtype: ContractInterface
        """
        program = MichelsonProgram.match(expression)
        cls = type(ContractInterface.__name__, (ContractInterface,), dict(program=program))
        context = ExecutionContext(
            shell=context.shell if context else None,
            key=context.key if context else None,
            script=dict(code=expression)
        )
        return cls(context)

    @staticmethod
    def from_context(context: ExecutionContext) -> 'ContractInterface':
        """ Create contract from the previously loaded context data.

        :param context: execution context
        :return: ContractInterface
        """
        program = MichelsonProgram.load(context, with_code=True)
        cls = type(ContractInterface.__name__, (ContractInterface,), dict(program=program))
        return cls(context)

    @classmethod
    @deprecated(deprecated_in='3.0.0', removed_in='3.1.0')
    def create_from(cls, source):
        """ Initialize from contract code.

        :param source: Michelson code
        :rtype: ContractInterface
        """
        if isinstance(source, str) and exists(expanduser(source)):
            return ContractInterface.from_file(source)
        elif is_micheline(source):
            return ContractInterface.from_micheline(source)
        else:
            return ContractInterface.from_michelson(source)

    def to_micheline(self):
        """ Get contract script in Micheline JSON

        :return:  [{'prim': 'parameter'}, {'prim': 'storage'}, {'prim': 'code'}]
        """
        return self.program.as_micheline_expr()

    def to_michelson(self):
        """ Get contract listing in formatted Michelson

        :return: string
        """
        return micheline_to_michelson(self.to_micheline())

    def to_file(self, path):
        """ Write contract source to a .tz file

        :param path: path to the file
        """
        with open(path, 'w+') as f:
            f.write(self.to_michelson())

    @deprecated(deprecated_in='3.0.0', removed_in='3.1.0')
    def big_map_get(self, path):
        """ Get BigMap entry as Python object by plain key and block height.

        :param path: Json path to the key (or just key to access default BigMap location). \
            Use `/` to separate nodes and `::` to separate tuple args. \
            In any other case you'd need to escape those symbols.
        :returns: object
        """
        node = self.storage
        for item in path.split('/'):
            if len(item) == 0:
                continue
            if isinstance(item, str):
                res = item.split('::')
                item = tuple(res) if len(res) > 1 else item
            node = node[item]
        return node() if node else None

    def using(self,
              shell: Optional[Union[ShellQuery, str]] = None,
              key: Optional[Union[Key, str]] = None,
              block_id: Optional[Union[str, int]] = None) -> 'ContractInterface':
        """ Change the block at which the current contract is inspected.
        Also, if address is undefined you can specify RPC endpoint, and private key.

        :param shell: one of 'mainnet', '***net', or RPC node uri, or instance of `ShellQuery`
        :param key: base58 encoded key, path to the faucet file, alias from tezos-client, or instance of `Key`
        :param block_id: block height / hash / offset to use, default is `head`
        :rtype: ContractInterface
        """
        has_address = self.context.address is not None
        return type(self)(self._spawn_context(shell=None if has_address else shell,
                                              key=None if has_address else key,
                                              address=self.context.address,
                                              block_id=block_id))

    @property
    def storage(self) -> ContractData:
        expr = self.shell.blocks[self.context.block_id].context.contracts[self.address].storage()
        storage = self.program.storage.from_micheline_value(expr)
        storage.attach_context(self.context)
        return ContractData(self.context, storage.item)

    @property
    def parameter(self) -> ContractEntrypoint:
        if 'root' in self.entrypoints:
            return getattr(self, 'root')
        else:
            assert 'default' in self.entrypoints, f'`default` entrypoint is undefined'
            return getattr(self, 'default')

    @property
    @deprecated(deprecated_in='3.0.0', removed_in='3.1.0')
    def call(self) -> ContractEntrypoint:
        return self.parameter

    def operation_result(self, operation_group: dict) -> List[ContractCallResult]:
        """ Get operation parameters, and resulting storage as Python objects.
        Can locate operation inside operation groups with multiple contents and/or internal operations.

        :param operation_group: {'branch', 'protocol', 'contents', 'signature'}
        :rtype: ContractCallResult
        """
        return ContractCallResult.from_run_operation(operation_group, context=self.context)

    def script(self, initial_storage=None, optimized=False) -> dict:
        """ Generate script for contract origination.

        :param initial_storage: Python object, leave None to generate default
        :param optimized: use optimized data form for some domain types (timestamp, address, etc.)
        :return: {"code": $Micheline, "storage": $Micheline}
        """
        if initial_storage:
            storage = self.program.storage.from_python_object(initial_storage)
        else:
            storage = self.program.storage.dummy(self.context)
        return {
            'code': self.program.as_micheline_expr(),
            'storage': storage.to_micheline_value(mode='optimized' if optimized else 'readable',
                                                  lazy_diff=True)
        }

    def originate(self, initial_storage=None, optimized=False,
                  balance: Union[int, Decimal] = 0,
                  delegate: Optional[str] = None) -> OperationGroup:
        """ Create an origination operation

        :param initial_storage: Python object, leave None to generate default
        :param optimized: use optimized data form for some domain types (timestamp, address, etc.)
        :param balance: initial balance
        :param delegate: initial delegator
        :rtype: OperationGroup
        """
        return OperationGroup(context=self._spawn_context()) \
            .origination(script=self.script(initial_storage, optimized=optimized),
                         balance=balance,
                         delegate=delegate)
