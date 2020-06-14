High-level interfaces
================================

PyTezos client
++++++++++++++++
.. autoclass:: pytezos.client.PyTezosClient
   :members:
   :inherited-members:

Contract interface
++++++++++++++++++++
.. autoclass:: pytezos.michelson.interface.ContractInterface
   :members:
   :inherited-members:

Contract entrypoint proxy
+++++++++++++++++++++++++++
.. autoclass:: pytezos.michelson.interface.ContractEntrypoint
   :members:
   :special-members: __call__
   :inherited-members:

Contract call proxy
+++++++++++++++++++++
.. autoclass:: pytezos.michelson.interface.ContractCall
   :members:
   :inherited-members:

Contract call result
++++++++++++++++++++++
.. autoclass:: pytezos.michelson.interface.ContractCallResult
   :members:
