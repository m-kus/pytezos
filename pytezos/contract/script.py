from typing import Type
from functools import lru_cache
from os.path import exists, expanduser

from pytezos.docstring import get_class_docstring, InlineDocstring
from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.types import ParameterType, StorageType, MichelsonType


class ContractParameter(metaclass=InlineDocstring):
    """ Encapsulates the `parameter` section of a Michelson script.
    """

    def __init__(self, section):
        self.code = section
        self.type = ParameterType.match(section)
        self.__doc__ = self.type.generate_pydoc()

    def __repr__(self):
        res = [
            super(ContractParameter, self).__repr__(),
            f'\n{self.__doc__}',
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def decode(self, data):
        """ Convert Micheline data into Python object using internal schema.

        :param data: Micheline expression or Michelson string or {entrypoint: "string", value: "expression"}
        :returns: Python object
        """
        return self.type.from_parameters(data).to_python_object()

    def encode(self, data):
        """ Convert Python object to Micheline expression using internal schema.

        :param data: Python object
        :returns: object
        """
        return self.type.from_python_object(data).to_parameters()

    def entries(self):
        """ Get list of entry points: names and docstrings.

        :returns: [("name", "docstring"), ...]
        """

        def make_doc(name, ty: Type[MichelsonType]):
            definitions = []
            return ty.generate_pydoc(definitions, inferred_name=name)

        return [(name, make_doc(name, ty)) for name, ty in self.type.list_entry_points()]


class ContractStorage(metaclass=InlineDocstring):
    """ Encapsulates the `storage` section of a Michelson script.
    """

    def __init__(self, section):
        self.code = section
        self.type = StorageType.match(section)
        self.__doc__ = self.type.generate_pydoc()

    def __repr__(self):
        res = [
            super(ContractStorage, self).__repr__(),
            f'\n{self.__doc__}',
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def decode(self, data):
        """ Convert Micheline data into Python object using internal schema.

        :param data: Micheline expression or Michelson string
        :returns: object
        """
        return self.type.from_micheline_value(data).to_python_object()

    def encode(self, data):
        """ Convert Python object to Micheline expression using internal schema.

        :param data: Python object
        :returns: object
        """
        return self.type.from_python_object(data).to_micheline_value()

    def default(self):
        """ Try to generate empty storage, returns Micheline expression.

        :returns: object
        """
        return self.type.dummy().to_micheline_value()


class ContractScript(metaclass=InlineDocstring):
    """ Represents a Michelson script.
    """

    def __init__(self, code: list):
        self.code = code

    def __repr__(self):
        res = [
            super(ContractScript, self).__repr__(),
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    def __str__(self):
        return self.text

    @property
    @lru_cache(maxsize=None)
    def parameter(self) -> ContractParameter:
        """ Returns `parameter` section wrapper.

        :rtype: ContractParameter
        """
        return ContractParameter(next(s for s in self.code if s['prim'] == 'parameter'))

    @property
    @lru_cache(maxsize=None)
    def storage(self) -> ContractStorage:
        """ Returns `storage` section wrapper.

        :rtype: ContractStorage
        """
        return ContractStorage(next(s for s in self.code if s['prim'] == 'storage'))

    @property
    @lru_cache(maxsize=None)
    def text(self):
        """ Get Michelson formatted code.
        """
        return micheline_to_michelson(self.code)

    @classmethod
    def from_micheline(cls, code):
        """ Create contract from micheline expression.

        :param code: [{'prim': 'parameter'}, {'prim': 'storage'}, {'prim': 'code'}]
        :rtype: ContractScript
        """
        return cls(code)

    @classmethod
    def from_michelson(cls, text):
        """ Create contract from michelson source code.

        :param text: Michelson source code.
        :rtype: ContractScript
        """
        return cls(michelson_to_micheline(text))

    @classmethod
    def from_file(cls, path):
        """ Create contract from michelson source code stored in file.

        :param path: Path to the `.tz` file
        :rtype: ContractScript
        """
        with open(expanduser(path)) as f:
            return cls.from_michelson(f.read())

    def save_file(self, path, overwrite=False):
        """ Save Michelson code to file.

        :param path: Output path
        :param overwrite: Default is False
        """
        path = expanduser(path)
        if exists(path) and not overwrite:
            raise FileExistsError(path)

        with open(path, 'w+') as f:
            f.write(self.text)

    def script(self, storage=None, original=True) -> dict:
        """ Generate script for contract origination.

        :param storage: Python object, leave None to generate empty
        :param original: Keep the original code (initialized), which is default. \
        Otherwise factory-specific changes may applied, e.g. different annotations
        :returns: {"code": $Micheline, "storage": $Micheline}
        """
        if storage is None:
            storage = self.storage.default()
        else:
            storage = self.storage.encode(storage)

        if original:
            code = self.code
        else:
            code = [
                self.parameter.code,
                self.storage.code,
                self.code[-1]
            ]

        return {
            "code": code,
            "storage": storage
        }
