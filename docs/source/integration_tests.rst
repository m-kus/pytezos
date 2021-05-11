Michelson integration tests
=============================

Step by step guide
--------------------

Read this Medium article: https://medium.com/tezoscommons/testing-michelson-contracts-with-pytezos-513718499e93

Loading contract
------------------

First step in testing contracts is to create :class:`pytezos.contract.interface.ContractInterface` from Michelson code, .tz file or existing deployed contract.

.. code-block:: python

  from os.path import dirname, join
  from pytezos import ContractInterface, pytezos

  contract_michelson = """
    parameter string;
    storage string;
    code { DUP;
          DIP { CAR ; NIL string ; SWAP ; CONS } ;
          CDR ; CONS ;
          CONCAT ;
          NIL operation; PAIR }
  """

  # From blockchain
  contract = pytezos.contract('KT1...')

  # From michelson
  contract = ContractInterface.from_michelson(contract_michelson)

  # From file
  with open('my_contract.tz', 'w+') as file:
    file.write(contract_michelson)
  contract = ContractInterface.from_file('my_contract.tz')

  # From URL
  contract = ContractInterface.from_url('https://raw.githubusercontent.com/atomex-me/atomex-michelson/master/src/atomex.tz')

Calling contract entrypoints
------------------------------

Entrypoints are accessed by name of contract attributes. Call them with parameters to create :class:`pytezos.contract.call.ContractCall` wrapper.

.. code-block:: python

  # Create call to `default` entrypoint
  call = contract.default("foo")

  # Add amount to transaction
  call = call.with_amount('0.01')

Now you can call `inject` method to send operation to blockchain. But we're interested in simulating contract calls without interacting with public blockchain. There are several methods to do this:

* Use remote node interpreter
* Use built-in Michelson interpreter (result may vary from node interpreter)
* Interact with real contract deployed on sandboxed node

Let's talk about the first two methods.

.. code-block:: python

  # Node interpreter
  result = call.run_code(storage="foo")

  # Built-in interpreter
  result = call.interpret(storage="foo")

  # In both cases you could patch SENDER, AMOUNT and other context variables
  result = call.interpret(storage="foo", balance=1000)

Each method will return :class:`pytezos.contract.result.ContractCallResult` instance. Now let's ensure our call has modified storage correctly.

.. code-block:: python

  assert result.storage == "foobar"

Deploying contract to sandboxed node
--------------------------------------

Another option is to deploy contract to sandboxed node and interact with it with real transactions. PyTezos has :class:`pytezos.sandbox.node.SandboxedNodeTestCase` helper to simplify spinning up sandboxed node in Docker. You can use `self.get_client` method to interact with it from within your tests.

.. code-block:: python

  from pytezos import ContractInterface
  from pytezos.sandbox.node import SandboxedNodeTestCase
  from pytezos.contract.result import ContractCallResult

  contract_michelson = """
      parameter string;
      storage string;
      code { DUP;
          DIP { CAR ; NIL string ; SWAP ; CONS } ;
          CDR ; CONS ;
          CONCAT ;
          NIL operation; PAIR }
  """

  class SandboxedContractTest(SandboxedNodeTestCase):
      def test_deploy_contract(self):
          # Create client
          client = self.get_client().using(key='bootstrap1')
          client.reveal()

          # Originate contract with initial storage
          contract = ContractInterface.from_michelson(contract_michelson)
          opg = contract.using(shell=self.get_node_url(), key='bootstrap1').originate(initial_storage="foo")
          opg = opg.fill().sign().inject()

          self.bake_block()

          # Find originated contract address by operation hash
          opg = client.shell.blocks['head':].find_operation(opg['hash'])
          contract_address = opg['contents'][0]['metadata']['operation_result']['originated_contracts'][0]

          # Load originated contract from blockchain
          originated_contract = client.contract(contract_address).using(shell=self.get_node_url(), key='bootstrap1')

          # Perform real contract call
          call = originated_contract.default("bar")
          opg = call.inject()

          self.bake_block()

          # Get injected operation and convert to ContractCallResult
          opg = client.shell.blocks['head':].find_operation(opg['hash'])
          result = ContractCallResult.from_operation_group(opg)[0]

          self.assertEqual({'string': 'foobar'}, result.storage)

Sandboxed node will be rolled back to genesis block between run of multiple testcases.

Examples
--------------

Contract tests: https://github.com/baking-bad/pytezos/tree/master/tests/contract_tests
Tests with sandboxed node: https://github.com/baking-bad/pytezos/tree/master/tests/sandbox_tests

Projects using PyTezos
------------------------
See how PyTezos testing engine is used in production:

- Atomex
  https://github.com/atomex-me/atomex-michelson/blob/master/tests/test_atomex.py
- Atomex FA1.2
  https://github.com/atomex-me/atomex-fa12-ligo/tree/master/tests
- TQTezos MAC
  https://github.com/tqtezos/smart-contracts/tree/master/multi_asset/tezos_mac_tests
- Equisafe NYX
  https://gitlab.com/equisafe/nyx/-/tree/master/tests