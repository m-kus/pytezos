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
from pytezos.protocol.protocol import Protocol
from pytezos.client import PyTezosClient
from pytezos.operation.group import OperationGroup
from pytezos.contract.interface import ContractInterface

pytezos = PyTezosClient()
