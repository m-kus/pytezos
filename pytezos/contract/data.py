from pytezos.context.impl import ExecutionContext
from pytezos.context.mixin import ContextMixin
from pytezos.michelson.types.base import MichelsonType, generate_pydoc
from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.jupyter import get_class_docstring


class ContractData(ContextMixin):

    def __init__(self, context: ExecutionContext, data: MichelsonType, path=''):
        super(ContractData, self).__init__(context=context)
        self.data = data
        self.path = path
        self.__doc__ = generate_pydoc(type(self.data))

    def __repr__(self):
        res = [
            super(ContractData, self).__repr__(),
            f'.address  # {self.address}',
            f'.block_id  # {self.context.block_id}',
            f'.path  # {self.path}',
            f'\nTypedef\n{self.__doc__}',
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def __getitem__(self, item) -> 'ContractData':
        res = self.data[item]
        return ContractData(self.context, res, path=f'{self.path}/{item}')

    def __call__(self, try_unpack=False):
        """ Get Michelson value as a Python object

        :param try_unpack: try to unpack utf8-encoded strings or PACKed Michelson expressions
        """
        return self.data.to_python_object(try_unpack=try_unpack)

    def to_micheline(self, optimized=False):
        """ Get as Micheline JSON expression

        :param optimized: use optimized data form for some domain types (timestamp, address, etc.)
        """
        return self.data.to_micheline_value(mode='optimized' if optimized else 'readable')

    def to_michelson(self, optimized=False):
        """ Get as Michelson value

        :param optimized: use optimized data form for some domain types (timestamp, address, etc.)
        """
        return micheline_to_michelson(self.to_micheline(optimized=optimized))

    def decode(self, value):
        """ Convert from Michelson to Python type system

        :param value: Micheline JSON expression or Michelson value
        :return: Python object
        """
        if isinstance(value, str):
            value = michelson_to_micheline(value)
        return type(self.data).from_micheline_value(value).to_python_object()

    def encode(self, py_obj, optimized=False):
        """ Convert from Python to Michelson type system

        :param py_obj: Python object
        :param optimized: use optimized data form for some domain types (timestamp, address, etc.)
        :return: Micheline JSON expression
        """
        mode = 'optimized' if optimized else 'readable'
        return type(self.data).from_python_object(py_obj).to_micheline_value(mode=mode)

    def dummy(self):
        """ Try to generate a dummy (empty) value

        :return: Python object
        """
        return type(self.data).dummy(self.context).to_python_object(lazy_diff=True)
