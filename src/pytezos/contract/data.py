from typing import Optional, Union

from deprecation import deprecated  # type: ignore

from pytezos.context.impl import ExecutionContext  # type: ignore
from pytezos.context.mixin import ContextMixin  # type: ignore
from pytezos.jupyter import get_class_docstring
from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.types.base import MichelsonType, generate_pydoc


class ContractData(ContextMixin):
    def __init__(self, context: ExecutionContext, data: MichelsonType, path='', title=None) -> None:
        super().__init__(context=context)
        self.data = data
        self.path = path
        self.__doc__ = generate_pydoc(type(self.data), title=title)

    def __repr__(self) -> str:
        res = [
            super().__repr__(),
            f'.path\t{self.path}',
            f'\nBuiltin\n()\t# get as Python object',
            f'[key]  # access child elements by name or index',
            f'\nTypedef\n{self.__doc__}',
            '\nHelpers',
            get_class_docstring(self.__class__),
        ]
        return '\n'.join(res)

    def __getitem__(self, item: Union[str, int]) -> 'ContractData':
        """Access child elements by name or index (depending on the type)

        :param item: field name (str) or index (int)
        :rtype: ContractData
        """
        res = self.data[item]
        if res is None:
            raise KeyError(item)
        return ContractData(self.context, res, path=f'{self.path}/{item}')

    def __call__(self, try_unpack=False):
        """Get Michelson value as a Python object

        :param try_unpack: try to unpack utf8-encoded strings or PACKed Michelson expressions
        """
        return self.data.to_python_object(try_unpack=try_unpack)

    def to_micheline(self, optimized=False):
        """Get as Micheline JSON expression

        :param optimized: use optimized data form for some domain types (timestamp, address, etc.)
        """
        return self.data.to_micheline_value(mode='optimized' if optimized else 'readable')

    def to_michelson(self, optimized=False):
        """Get as Michelson value

        :param optimized: use optimized data form for some domain types (timestamp, address, etc.)
        """
        return micheline_to_michelson(self.to_micheline(optimized=optimized))

    def decode(self, value):
        """Convert from Michelson to Python type system

        :param value: Micheline JSON expression or Michelson value
        :return: Python object
        """
        if isinstance(value, str):
            value = michelson_to_micheline(value)
        return type(self.data).from_micheline_value(value).to_python_object()

    def encode(self, py_obj, mode: Optional[str] = None):
        """Convert from Python to Michelson type system

        :param py_obj: Python object
        :param mode: whether to use `readable` or `optimized` (or `legacy_optimized`) encoding
        :return: Micheline JSON expression
        """
        return type(self.data).from_python_object(py_obj).to_micheline_value(mode=mode or self.context.mode)

    def dummy(self):
        """Try to generate a dummy (empty) value

        :return: Python object
        """
        return type(self.data).dummy(self.context).to_python_object(lazy_diff=True)

    @deprecated(deprecated_in='3.0.0', removed_in='3.1.0')
    def default(self):
        return self.dummy()
