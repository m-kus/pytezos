from pytezos.context.impl import ExecutionContext
from pytezos.context.mixin import ContextMixin
from pytezos.michelson.types.base import MichelsonType


class ContractData(ContextMixin):

    def __init__(self, context: ExecutionContext, data: MichelsonType):
        super(ContractData, self).__init__(context=context)
        self.data = data

    def __repr__(self):
        res = [
            super(ContractData, self).__repr__(),
            f'.address  # {self.address}',
            f'.block_id  # {self.context.block_id}'
            '\nType schema'
        ]
        self.data.generate_pydoc(res)
        return '\n'.join(res)

    def __getitem__(self, item) -> 'ContractData':
        res = self.data[item]
        return ContractData(self.context, res)

    def __call__(self, try_unpack=False):
        """ Get Michelson value as a Python object

        :param try_unpack: try to unpack utf8-encoded strings or PACKed Michelson expressions
        :return:
        """
        return self.data.to_python_object(try_unpack=try_unpack)
