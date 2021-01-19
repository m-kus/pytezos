"""
Welcome to PyTezos!

To start playing with the Tezos blockchain you need to get a PyTezosClient instance.
Just type:

>>> from pytezos import pytezos
>>> pytezos

And follow the interactive documentation.
"""

from pytezos.rpc import RpcProvider
from pytezos.rpc.errors import *
from pytezos.crypto.key import Key
from pytezos.client import PyTezosClient
from pytezos.operation.group import OperationGroup
from pytezos.contract.script import ContractScript as Contract  # backward compatibility
from pytezos.contract.interface import ContractInterface
from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.forge import forge_micheline, unforge_micheline

pytezos = PyTezosClient()
