"""
Welcome to PyTezos!

To start playing with the Tezos blockchain you need to get a PyTezosClient instance.
Just type:

>>> from pytezos import pytezos
>>> pytezos

And follow the interactive documentation.
"""

from pytezos.client import PyTezosClient
from pytezos.contract.interface import Contract, ContractInterface
from pytezos.crypto.key import Key
from pytezos.logging import logger
from pytezos.michelson.forge import forge_micheline, unforge_micheline
from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.micheline import MichelsonRuntimeError
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.types.base import MichelsonType, Undefined
from pytezos.michelson.types.core import Unit

__version__ = '3.1.0'

pytezos = PyTezosClient()
