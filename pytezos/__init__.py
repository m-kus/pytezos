"""
Welcome to PyTezos!

To start playing with the Tezos blockchain you need to get a PyTezosClient instance.
Just type:

>>> from pytezos import pytezos
>>> pytezos

And follow the interactive documentation.
"""

from pytezos.rpc import RpcProvider, localhost, mainnet, dalphanet, delphinet, carthagenet
from pytezos.rpc.errors import *
from pytezos.crypto import Key
from pytezos.proto import Proto
from pytezos.michelson.micheline import Unit
from pytezos.michelson.contract import Contract
from pytezos.michelson.formatter import format_timestamp
from pytezos.client import PyTezosClient
from pytezos.operation.group import OperationGroup
from pytezos.michelson.interface import ContractInterface
from pytezos.standards.non_fungible_token import NonFungibleTokenImpl

pytezos = PyTezosClient()
