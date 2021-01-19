from os.path import exists, expanduser
from typing import List

from pytezos.context.rpc import RPCNodeContext
from pytezos.contract.call import ContractCallResult
from pytezos.contract.entrypoint import ContractEntrypoint
from pytezos.contract.script import ContractScript
from pytezos.interop import Interop
from pytezos.jupyter import get_class_docstring
from pytezos.michelson.micheline import is_micheline


class ContractInterface(Interop):
    """ Proxy class for interacting with a contract.
    """

    def __init__(self, address=None, script: ContractScript = None, shell=None, key=None):
        super(ContractInterface, self).__init__(shell=shell, key=key)
        if script is None:
            assert address is not None
            code = self.shell.contracts[address].code()
            script = ContractScript.from_micheline(code)

        self.script = script
        self.address = address

        for entry_name, docstring in script.parameter.entries():
            entry_point = ContractEntrypoint(
                name=entry_name,
                address=self.address,
                script=script,
                shell=self.shell,
                key=self.key
            )
            entry_point.__doc__ = docstring
            setattr(self, entry_name, entry_point)

    def _spawn(self, **kwargs):
        return ContractInterface(
            address=self.address,
            script=self.script,
            shell=kwargs.get('shell', self.shell),
            key=kwargs.get('key', self.key)
        )

    def __repr__(self):
        entrypoints, _ = zip(*self.script.parameter.entries())
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
    def create_from(cls, source, shell=None):
        """ Initialize from contract code.

        :param source: Michelson code
        :param shell: A `Shell` instance (optional)
        :rtype: ContractInterface
        """
        if isinstance(source, str) and exists(expanduser(source)):
            contract = ContractScript.from_file(source)
        elif is_micheline(source):
            contract = ContractScript.from_micheline(source)
        else:
            contract = ContractScript.from_michelson(source)

        return ContractInterface(script=contract, shell=shell)

    def at(self, address, shell=None):
        return ContractInterface(
            address=address,
            script=self.script,
            shell=shell or self.shell,
            key=self.key
        )

    def big_map_get(self, path, block_id='head'):
        """ Get BigMap entry as Python object by plain key and block height.

        :param path: Json path to the key (or just key to access default BigMap location). \
            Use `/` to separate nodes and `::` to separate tuple args. \
            In any other case you'd need to escape those symbols.
        :param block_id: Block height / hash / offset to use, default is `head`
        :returns: object
        """

        storage_expr = self.shell.blocks[block_id].context.contracts[self.address].storage()
        storage = self.script.storage.type.from_micheline_value(storage_expr)
        storage.attach_context(RPCNodeContext(shell=self.shell, block_id=block_id))

        node = storage
        for item in path.split('/'):
            if len(item) == 0:
                continue
            if isinstance(item, str):
                res = item.split('::')
                item = tuple(res) if len(res) > 1 else item
            node = node[item]
        return node.to_python_object() if node else None

    def storage(self, block_id='head'):
        """ Get storage as Python object at a specified block height.

        :param block_id: Block height / hash / offset to use, default is `head`
        :returns: object
        """
        storage = self.shell.blocks[block_id].context.contracts[self.address].storage()
        return self.script.storage.decode(storage)

    def operation_result(self, operation_group: dict) -> List[ContractCallResult]:
        """ Get operation parameters, storage and big_map_diff as Python objects.
        Can locate operation inside operation groups with multiple contents and/or internal operations.

        :param operation_group: {'branch', 'protocol', 'contents', 'signature'}
        :rtype: ContractCallResult
        """
        return ContractCallResult.from_contract_call(
            operation_group, address=self.address, script=self.script)
