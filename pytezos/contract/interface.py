from os.path import exists, expanduser
from typing import List, Optional, Union
from deprecation import deprecated
from decimal import Decimal

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
            attr.__doc__ = generate_pydoc(ty)
            setattr(self, entrypoint, attr)

    def __repr__(self):
        res = [
            super(ContractInterface, self).__repr__(),
            f'.address  # {self.address}',
            '\nEntrypoints',
            *list(map(lambda x: f'.{x}()', self.entrypoints)),
            '\nHelpers',
            get_class_docstring(self.__class__,
                                attr_filter=lambda x: not x.startswith('_') and x not in self.entrypoints)
        ]
        return '\n'.join(res)

    @staticmethod
    def from_file(path: str, context: Optional[ExecutionContext] = None) -> 'ContractInterface':
        with open(expanduser(path)) as f:
            return ContractInterface.from_michelson(f.read(), context)

    @staticmethod
    def from_michelson(source: str, context: Optional[ExecutionContext] = None) -> 'ContractInterface':
        return ContractInterface.from_micheline(michelson_to_micheline(source), context)

    @staticmethod
    def from_micheline(expression, context: Optional[ExecutionContext] = None) -> 'ContractInterface':
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
        program = MichelsonProgram.load(context, with_code=True)
        cls = type(ContractInterface.__name__, (ContractInterface,), dict(program=program))
        return cls(context)

    @classmethod
    @deprecated
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
        return self.program.as_micheline_expr()

    def to_michelson(self):
        return micheline_to_michelson(self.to_micheline())

    def to_file(self, path):
        with open(path, 'w+') as f:
            f.write(self.to_michelson())

    @deprecated
    def big_map_get(self, path, block_id='head'):
        """ Get BigMap entry as Python object by plain key and block height.

        :param path: Json path to the key (or just key to access default BigMap location). \
            Use `/` to separate nodes and `::` to separate tuple args. \
            In any other case you'd need to escape those symbols.
        :param block_id: Block height / hash / offset to use, default is `head`
        :returns: object
        """
        node = self.storage(block_id)
        for item in path.split('/'):
            if len(item) == 0:
                continue
            if isinstance(item, str):
                res = item.split('::')
                item = tuple(res) if len(res) > 1 else item
            node = node[item]
        return node() if node else None

    def storage(self, block_id='head') -> ContractData:
        """ Get storage as Python object at a specified block height.

        :param block_id: Block height / hash / offset to use, default is `head`
        :rtype: ContractData
        """
        expr = self.shell.blocks[block_id].context.contracts[self.address].storage()
        storage = self.program.storage.from_micheline_value(expr)
        return ContractData(self.create_storage_ctx(block_id), storage.item)

    def operation_result(self, operation_group: dict) -> List[ContractCallResult]:
        """ Get operation parameters, and resulting storage as Python objects.
        Can locate operation inside operation groups with multiple contents and/or internal operations.

        :param operation_group: {'branch', 'protocol', 'contents', 'signature'}
        :rtype: ContractCallResult
        """
        return ContractCallResult.from_run_operation(operation_group, context=self.context)

    def script(self, initial_storage=None, mode='readable') -> dict:
        """ Generate script for contract origination.

        :param initial_storage: Python object, leave None to generate default
        :param mode: either `readable` or `optimized`
        :return: {"code": $Micheline, "storage": $Micheline}
        """
        if initial_storage:
            storage = self.program.storage.from_python_object(initial_storage)
        else:
            storage = self.program.storage.dummy(self.context)
        return {
            'code': self.program.as_micheline_expr(),
            'storage': storage.to_micheline_value(mode=mode)
        }

    def originate(self, initial_storage=None, mode='readable',
                  balance: Union[int, Decimal] = 0,
                  delegate: Optional[str] = None) -> OperationGroup:
        """ Create an origination operation

        :param initial_storage: Python object, leave None to generate default
        :param mode: either `readable` or `optimized`
        :param balance:
        :param delegate:
        :rtype: OperationGroup
        """
        return OperationGroup(context=self.get_generic_ctx()) \
            .origination(script=self.script(initial_storage, mode=mode),
                         balance=balance,
                         delegate=delegate)
