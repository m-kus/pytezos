"""
Welcome to PyTezos!

To start playing with the Tezos blockchain you need to get a PyTezosClient instance.
Just type:

>>> from pytezos import pytezos
>>> pytezos

And follow the interactive documentation.
"""

import importlib.metadata

from pytezos.client import PyTezosClient
from pytezos.contract.interface import Contract
from pytezos.contract.interface import ContractInterface
from pytezos.crypto.key import Key
from pytezos.logging import logger
from pytezos.michelson.forge import forge_micheline
from pytezos.michelson.forge import unforge_micheline
from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.micheline import MichelsonRuntimeError
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.types.base import Undefined
from pytezos.michelson.types.core import Unit

__version__ = importlib.metadata.version('pytezos')

pytezos = PyTezosClient()
