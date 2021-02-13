Quick start
=============

Introduction
------------

PyTezos library is a Python toolset for Tezos blockchain, including work with keys, signatures, contracts, operations,
RPC query builder, and a high-level interface for smart contract interaction. It can be used to build a full-fledged
application, but also it's perfect for doing researches in Jupyter interactive notebooks.
In this quick start guide, we'll go through the main concepts and inspect one of the common use cases.

Requirements
------------

First of all you'll probably need to install cryptographic libraries in your system.

*Linux*

Use apt or your favourite package manager:

.. code-block::

   $ sudo apt install libsodium-dev libsecp256k1-dev libgmp-dev

*MacOS*

Use homebrew:

.. code-block::

   $ brew tap cuber/homebrew-libsecp256k1
   $ brew install libsodium libsecp256k1 gmp

*Windows*

The recommended way is to use WSL and then follow the instructions for Linux,
but if you feel lucky you can try to install natively:


#. Install MinGW from `https://osdn.net/projects/mingw/ <https://osdn.net/projects/mingw/>`_
#. Make sure ``C:\MinGW\bin`` is added to your ``PATH``
#. Download the latest libsodium-X.Y.Z-msvc.zip from `https://download.libsodium.org/libsodium/releases/ <https://download.libsodium.org/libsodium/releases/>`_.
#. Extract the Win64/Release/v143/dynamic/libsodium.dll from the zip file
#. Copy libsodium.dll to C:\Windows\System32\libsodium.dll

Installation
------------

In console:

.. code-block::

   $ pip install pytezos

In Google Colab notebook:

.. code-block:: python

   >>> !apt install libsodium-dev libsecp256k1-dev libgmp-dev
   >>> !pip install pytezos
   [RESTART RUNTIME]

That's it! You can open Python console or Jupyter notebook and get to the next step.

Set key and RPC node
--------------------

All active interaction with the blockchain starts with the PyTezosClient:

.. code-block:: python

   >>> from pytezos import pytezos
   >>> pytezos
   <pytezos.client.PyTezosClient object at 0x7f480c03c190>

    Properties
    .key  # tz1grSQDByRpnVs7sPtaprNZRp531ZKz6Jmm
    .shell  # https://rpc.tzkt.io/edonet/ (edonet)
    .block_id  # head

    Helpers
    .account()
    .activate_account()
    .balance()
    .ballot()
    .bulk()
    .contract()
    .delegation()
    .double_baking_evidence()
    .double_endorsement_evidence()
    .endorsement()
    .now()
    .operation()
    .operation_group()
    .origination()
    .proposals()
    .reveal()
    .seed_nonce_revelation()
    .transaction()
    .using()

This is one of the cool features in the interactive mode: aside from the autocomplete and call docstrings,
you can see the list of available methods for class, or list of arguments and return value for a particular methods.
We are interested in ``using`` method, which is responsible for setting up manager key and RPC connection.

.. code-block:: python

   >>> pytezos.using
   <function PyTezosClient.using at 0x7f47fc123550>
    Change current rpc endpoint and account (private key).

    :param shell: one of 'mainnet', '***net', or RPC node uri, or instance of `ShellQuery`
    :param key: base58 encoded key, path to the faucet file, alias from tezos-client, or instance of `Key`
    :returns: A copy of current object with changes applied

Note, that by default ``pytezos`` is initialized with the latest testnet and a predefined private key for demo purpose,
so you can start to interact immediately, but it's highly recommended to use your own key. Let's do that!

Faucet account
^^^^^^^^^^^^^^

Go to the `https://faucet.tzalpha.net/ <https://faucet.tzalpha.net/>`_ and download key file.
Then configure the client (we can leave ``shell`` parameter empty, but we will set it explicitly for better understanding)

.. code-block:: python

   >>> pytezos = pytezos.using(key='~/Downloads/tz1cnQZXoznhduu4MVWfJF6GSyP6mMHMbbWa.json')


Sandboxed mode
^^^^^^^^^^^^^^

Accounts are pre-created in Sandboxed mode, this shows how to find the secret keys:

.. code-block::

   $ grep SECRET src/bin_client/tezos-init-sandboxed-client.sh
   export BOOTSTRAP1_SECRET="unencrypted:edsk3gUfUPyBSfrS9CCgmCiQsTCHGkviBDusMxDJstFtojtc1zcpsh"
   export BOOTSTRAP2_SECRET="unencrypted:edsk39qAm1fiMjgmPkw1EgQYkMzkJezLNewd7PLNHTkr6w9XA2zdfo"
   export BOOTSTRAP3_SECRET="unencrypted:edsk4ArLQgBTLWG5FJmnGnT689VKoqhXwmDPBuGx3z4cvwU9MmrPZZ"
   export BOOTSTRAP4_SECRET="unencrypted:edsk2uqQB9AY4FvioK2YMdfmyMrer5R8mGFyuaLLFfSRo8EoyNdht3"
   export BOOTSTRAP5_SECRET="unencrypted:edsk4QLrcijEffxV31gGdN2HU7UpyJjA8drFoNcmnB28n89YjPNRFm"
   export ACTIVATOR_SECRET="unencrypted:edsk31vznjHSSpGExDMHYASz45VZqXN4DPxvsa4hAyY8dHM28cZzp6"

Use one of these unencrypted private keys to connect to the sandbox:

.. code-block::

   >>> from pytezos import pytezos
   >>> pytezos.using(shell='http://localhost:18731', key='edsk3gUfUPyBSfrS9CCgmCiQsTCHGkviBDusMxDJstFtojtc1zcpsh')
   <pytezos.client.PyTezosClient object at 0x7f2c2d78da10>

   Properties
   .key  # tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx
   .shell  # http://localhost:18731 ()

Activate account
----------------

In order to start using our faucet account we need to claim balance.

.. code-block:: python

   >>> pytezos.activate_account
   <function ContentMixin.activate_account at 0x7f6f555e5400>

   Activate recommended allocations for contributions to the TF fundraiser.
   More info https://activate.tezos.com/
   :param pkh: Public key hash, leave empty for autocomplete
   :param activation_code: Secret code from pdf, leave empty for autocomplete
   :return: dict or OperationGroup

Cool! We can just leave all fields empty and let PyTezos do all the work. There are two autocomplete function available:
``fill`` and ``autofill``. The only difference is that ``autofill`` simulates the operation and sets precise values for fee
and gas/storage limits.

.. code-block:: python

   >>> pytezos.activate_account().autofill()
   <pytezos.operation.group.OperationGroup object at 0x7f291b7074e0>

   Properties
   .key  # tz1cnQZXoznhduu4MVWfJF6GSyP6mMHMbbWa
   .shell  # https://rpc.tzkt.io/edonet/ (edonet)

   Payload
   {'branch': 'BMNPpkcU6jzdaZC6AvtyVZzPkWLHFsyadCzDPQNxPDG8YUX8EyR',
    'contents': [{'kind': 'activate_account',
                  'pkh': 'tz1Ne4yzDRQPd5HFz6sTaCYCNHwFubT2MWsB',
                  'secret': 'ac4aab725c5f5c9323155778e9dec94a14df09eb'}],
    'protocol': 'PtEdoTezd3RHSC31mpxxo1npxFjoWWcFgQtxapi51Z8TLu6v6Uq',
    'signature': None}

   Helpers
   .activate_account()
   .autofill()
   .ballot()
   .binary_payload()
   .delegation()
   .double_baking_evidence()
   .double_endorsement_evidence()
   .endorsement()
   .fill()
   .forge()
   .hash()
   .inject()
   .json_payload()
   .operation()
   .origination()
   .preapply()
   .proposals()
   .reveal()
   .run()
   .seed_nonce_revelation()
   .sign()
   .transaction()
   .using()

Have you noticed that operation helpers are still available? We can easily chain operations but we cannot for example
put ``activate_account`` and ``reveal`` together because they are from different validation passes.
Ok, let's sign and preapply operation to see what's going to happen:

.. code-block:: python

   >>> pytezos.activate_account().fill().sign().preapply()
   [{'contents': [{'kind': 'activate_account',
       'pkh': 'tz1Ne4yzDRQPd5HFz6sTaCYCNHwFubT2MWsB',
       'secret': 'ac4aab725c5f5c9323155778e9dec94a14df09eb',
       'metadata': {'balance_updates': [{'kind': 'contract',
          'contract': 'tz1Ne4yzDRQPd5HFz6sTaCYCNHwFubT2MWsB',
          'change': '10848740286'}]}}],
     'signature': 'sigUbev7tsZbMXXJ6QWE12ukaJ9F6fQ9Gzxku2iDTv7j4ipRgxhS4g9P9hV39Fb1xGir1PYXNQt1y6qydGbRUgjAXWmzVjA4'}]

Everything looks good! Ready to inject the operation.

.. code-block:: python

   >>> pytezos.activate_account().fill().sign().inject()
   {'chain_id': 'NetXSp4gfdanies',
    'hash': 'ooTAsux9JZVh1ud2euNrFBFDxUCxWYg3d1tWZSa7WLavVs1wMc9',
    'protocol': 'PtEdoTezd3RHSC31mpxxo1npxFjoWWcFgQtxapi51Z8TLu6v6Uq',
    'branch': 'BMNPpkcU6jzdaZC6AvtyVZzPkWLHFsyadCzDPQNxPDG8YUX8EyR',
    'contents': [{'kind': 'activate_account',
      'pkh': 'tz1Ne4yzDRQPd5HFz6sTaCYCNHwFubT2MWsB',
      'secret': 'ac4aab725c5f5c9323155778e9dec94a14df09eb'}],
    'signature': 'sigUbev7tsZbMXXJ6QWE12ukaJ9F6fQ9Gzxku2iDTv7j4ipRgxhS4g9P9hV39Fb1xGir1PYXNQt1y6qydGbRUgjAXWmzVjA4'}

We can search our operation in the node mempool to check what status it has:

.. code-block:: python

   >>> pytezos.shell.mempool.pending_operations['ooTAsux9JZVh1ud2euNrFBFDxUCxWYg3d1tWZSa7WLavVs1wMc9']
   {'status': 'applied',
    'hash': 'ooTAsux9JZVh1ud2euNrFBFDxUCxWYg3d1tWZSa7WLavVs1wMc9',
    'branch': 'BMNPpkcU6jzdaZC6AvtyVZzPkWLHFsyadCzDPQNxPDG8YUX8EyR',
    'contents': [{'kind': 'activate_account',
      'pkh': 'tz1Ne4yzDRQPd5HFz6sTaCYCNHwFubT2MWsB',
      'secret': 'ac4aab725c5f5c9323155778e9dec94a14df09eb'}],
    'signature': 'sigUbev7tsZbMXXJ6QWE12ukaJ9F6fQ9Gzxku2iDTv7j4ipRgxhS4g9P9hV39Fb1xGir1PYXNQt1y6qydGbRUgjAXWmzVjA4'}

   >>> pytezos.account()
   {'balance': '42119864414', 'counter': '286565'}

Yay! We have claimed our account balance.

Reveal public key
-----------------

.. code-block:: python

   >>> pytezos.reveal().autofill().sign().inject()
   {'chain_id': 'NetXSp4gfdanies',
    'hash': 'opMnhvsnccU9ZRZc6gaF1WgLNnBkJW7G7j4RX1eKWLkiWSSXf2S',
    'protocol': 'PtEdoTezd3RHSC31mpxxo1npxFjoWWcFgQtxapi51Z8TLu6v6Uq',
    'branch': 'BMbaFNPvFYAUaY74YXtweKuv6khEiwEyFfggCUDawNLv6yTc8LP',
    'contents': [{'kind': 'reveal',
      'source': 'tz1Ne4yzDRQPd5HFz6sTaCYCNHwFubT2MWsB',
      'fee': '380',
      'counter': '286566',
      'gas_limit': '1200',
      'storage_limit': '0',
      'public_key': 'edpkvRPjGLLi8fHKuoffMni4Nqrq6YVYd5zGUCvHD4aoKkU2ZtGR6M'}],
    'signature': 'sigY7LffHKu7pnXsWTkqodYY2weG527zDKZgxnF5E7uhEQRpXyHsfT4T5kH33HRBD2z7tVGVyagP2ahoSvVb8pjnoyAqJUpZ'}

We can also search for operation by hash if we know exact block level or that it was injected recently:

.. code-block:: python

   >>> pytezos.shell.blocks[-20:].find_operation('opMnhvsnccU9ZRZc6gaF1WgLNnBkJW7G7j4RX1eKWLkiWSSXf2S')
   {'protocol': 'PtEdoTezd3RHSC31mpxxo1npxFjoWWcFgQtxapi51Z8TLu6v6Uq',
    'chain_id': 'NetXSp4gfdanies',
    'hash': 'opMnhvsnccU9ZRZc6gaF1WgLNnBkJW7G7j4RX1eKWLkiWSSXf2S',
    'branch': 'BMbaFNPvFYAUaY74YXtweKuv6khEiwEyFfggCUDawNLv6yTc8LP',
    'contents': [{'kind': 'reveal',
      'source': 'tz1Ne4yzDRQPd5HFz6sTaCYCNHwFubT2MWsB',
      'fee': '380',
      'counter': '286566',
      'gas_limit': '1200',
      'storage_limit': '0',
      'public_key': 'edpkvRPjGLLi8fHKuoffMni4Nqrq6YVYd5zGUCvHD4aoKkU2ZtGR6M',
      'metadata': {'balance_updates': [{'kind': 'contract',
         'contract': 'tz1Ne4yzDRQPd5HFz6sTaCYCNHwFubT2MWsB',
         'change': '-380'},
        {'kind': 'freezer',
         'category': 'fees',
         'delegate': 'tz1VpvtSaSxKvykrqajFJTZqCXgoVJ5cKaM1',
         'cycle': 101,
         'change': '380'}],
       'operation_result': {'status': 'applied',
        'consumed_gas': '1000',
        'consumed_milligas': '1000000'}}}],
    'signature': 'sigY7LffHKu7pnXsWTkqodYY2weG527zDKZgxnF5E7uhEQRpXyHsfT4T5kH33HRBD2z7tVGVyagP2ahoSvVb8pjnoyAqJUpZ'}

Originate contract
------------------

Now we can do something interesting. Let's deploy a Michelson smart contract! First we need to load data, in this
tutorial we will get it from Michelson source file. There are plenty of available methods, but we'are interested in
``script`` which gives us payload for origination.

.. code-block:: python

   >>> from pytezos import ContractInterface
   >>> contract = Contract.from_file('~/Documents/demo_contract.tz')
   >>> contract.script
   <function Contract.script at 0x7fe01c0d9c80>

   Generate script for contract origination
   :param storage: Python object, leave None to generate empty
   :return: {"code": $Micheline, "storage": $Micheline}

PyTezos can generate empty storage based on the type description. This is a small part of the high-level interface
functionality we will further learn.

.. code-block:: python

   >>> pytezos.origination(script=contract.script()).autofill().sign().inject()
   'op3ZRdR6LjmA8AeNEjKEimr2uQeAWwXSXEftUBiTVx4k86Rw66m'

   >>> opg = pytezos.shell.blocks[-5:].find_operation('op3ZRdR6LjmA8AeNEjKEimr2uQeAWwXSXEftUBiTVx4k86Rw66m')
   >>> contract_id = opg['contents'][0]['metadata']['operation_result']['originated_contracts'][0]
   >>> contract_id
   'KT1RX74ty3TqBfU6pBs7ce3uV7PLBrUEav6X'

Access storage
--------------

Let's play with `KT1HnvV5Z53naoh51jYvPF7w168nW8nfyx5v <https://better-call.dev/alpha/KT1HnvV5Z53naoh51jYvPF7w168nW8nfyx5v/operations>`_
as it has BigMap entries, named entrypoints, and non-trivial data scheme.

.. code-block:: python

   >>> ci = pytezos.contract('KT1HnvV5Z53naoh51jYvPF7w168nW8nfyx5v')
   >>> ci
   <pytezos.michelson.interface.ContractInterface object at 0x7f8bbb11c748>

   Properties
   .key -> tz1cnQZXoznhduu4MVWfJF6GSyP6mMHMbbWa
   .shell -> https://tezos-dev.cryptonomic-infra.tech/ (alphanet)
   .address -> KT1HnvV5Z53naoh51jYvPF7w168nW8nfyx5v

   Entrypoints
   .transfer()
   .approve()
   .transfer_from()
   .balance_of()
   .allowance()
   .create_account()
   .create_accounts()

   Helpers
   .big_map_get()
   .storage()
   .using()

You can access contract storage at any block level, just pass block id into the ``storage`` method:

.. code-block:: python

   >>> ci.storage(block_id='head~4096')
   {'accounts': {},
    'version': 1,
    'total_supply': 1000,
    'decimals': 0,
    'name': 'Calamares',
    'symbol': 'PLA',
    'owner': 'tz1WWLRiCFnSzT1uXQYjJYaMVcUefrMxWT25'}

Under the hood PyTezos has parsed the storage type, collapsed all nested structures, converted annotations into keys,
and in the result we get a simple Python object which is much easier to manipulate. Take a look at the storage scheme -
it looks like Tezos RPC API generated docs.

.. code-block:: python

   >>> ci.contract.storage
   <pytezos.michelson.contract.ContractStorage object at 0x7f5d1411f550>

   $storage:
       {
         "accounts": { $address : $account , ... }  /* big_map */,
         "version": $nat,
         "total_supply": $nat,
         "decimals": $nat,
         "name": string,
         "symbol": string,
         "owner": $address
       }

   $account:
       {
         "balance": $nat,
         "allowances": { $address : $nat , ... }
       }

   $nat:
       int  /* Natural number */

   $address:
       string  /* Base58 encoded `tz` or `KT` address */


   Helpers
   .big_map_decode()
   .big_map_diff_decode()
   .big_map_query()
   .decode()
   .default()
   .encode()

BigMap lookup
-------------

It looks like we are talking about some token,
let's take a peek at the `better-call.dev <https://better-call.dev/alpha/KT1HnvV5Z53naoh51jYvPF7w168nW8nfyx5v/operations>`_
and query balance for an account from the big map.

.. code-block:: python

   >>> ci.big_map_get('KT1FxfNNcmdEs3n38E1o2GcXhikmpGkyARDq')
   {'balance': 45, 'allowances': {}}

Pretty cool, hah?

Call entrypoint
---------------

We can do the same using special entrypoint ``balance_of``. Let's give a look at the interface:

.. code-block:: python

   >>> ci.balance_of
   <pytezos.michelson.interface.ContractEntrypoint object at 0x7f4f0cc76e48>

   Properties
   .key  # tz1cnQZXoznhduu4MVWfJF6GSyP6mMHMbbWa
   .shell  # https://tezos-dev.cryptonomic-infra.tech/ (alphanet)
   .address  # KT1HnvV5Z53naoh51jYvPF7w168nW8nfyx5v

   $kwargs:
       {
         "address": $address,
         "nat_contract": $contract (nat)
       }

   $contract:
       string  /* Base58 encoded `KT` address */

   $address:
       string  /* Base58 encoded `tz` or `KT` address */

Apparently, we need to pass an address which balance we want to retrieve and a contract address having a single ``nat``
parameter which will receive the balance (this is how view methods work in michelson).
Using `conseilpy <https://github.com/baking-bad/conseilpy>`_ we can find such contract
(for testing purposes, in order not to write our own).

.. code-block:: python

   >>> ci.balance_of(
   ...    address='KT1FxfNNcmdEs3n38E1o2GcXhikmpGkyARDq',
   ...    nat_contract='KT1JTpEkByTStHYTT3qD8khJomNnvvnrfh4v')
   <pytezos.michelson.interface.ContractCall object at 0x7f4f0cc980b8>

   Properties
   .key  # tz1cnQZXoznhduu4MVWfJF6GSyP6mMHMbbWa
   .shell  # https://tezos-dev.cryptonomic-infra.tech/ (alphanet)

   Payload
   {'branch': 'BMDPbTmdsLnD1JBurPAqiYE45UDunYTBad2UWgCtg5bgyi2UFxu',
    'contents': [{'amount': '0',
                  'counter': '715920',
                  'destination': 'KT1HnvV5Z53naoh51jYvPF7w168nW8nfyx5v',
                  'fee': '40364',
                  'gas_limit': '400000',
                  'kind': 'transaction',
                  'parameters': {'args': [{'args': [{'args': [{'args': [{'args': [{'string': 'KT1FxfNNcmdEs3n38E1o2GcXhikmpGkyARDq'},
                                                                                  {'string': 'KT1JTpEkByTStHYTT3qD8khJomNnvvnrfh4v'}],
                                                                         'prim': 'Pair'}],
                                                               'prim': 'Left'}],
                                                     'prim': 'Right'}],
                                           'prim': 'Right'}],
                                 'prim': 'Right'},
                  'source': 'tz1cnQZXoznhduu4MVWfJF6GSyP6mMHMbbWa',
                  'storage_limit': '60000'}],
    'protocol': 'Pt24m4xiPbLDhVgVfABUjirbmda3yohdN82Sp9FeuAXJ4eV9otd',
    'signature': None}

   Helpers
   .cmdline()
   .inject()
   .operation_group
   .using()
   .with_amount()

What we got is a ready to inject operation group with encoded parameters.
In our case we just want to view data, so we can use ``preapply`` to see actual result.

.. code-block:: python

   >>> ci.balance_of(address='KT1FxfNNcmdEs3n38E1o2GcXhikmpGkyARDq',
   ...               nat_contract='KT1JTpEkByTStHYTT3qD8khJomNnvvnrfh4v') \
   ...    .operation_group \
   ...    .sign() \
   ...    .preapply()
   [{'contents': [{'kind': 'transaction',
       'source': 'tz1cnQZXoznhduu4MVWfJF6GSyP6mMHMbbWa',
       'fee': '40364',
       'counter': '715920',
       'gas_limit': '400000',
       'storage_limit': '60000',
       'amount': '0',
       'destination': 'KT1HnvV5Z53naoh51jYvPF7w168nW8nfyx5v',
       'parameters': {'prim': 'Right',
        'args': [{'prim': 'Right',
          'args': [{'prim': 'Right',
            'args': [{'prim': 'Left',
              'args': [{'prim': 'Pair',
                'args': [{'string': 'KT1FxfNNcmdEs3n38E1o2GcXhikmpGkyARDq'},
                 {'string': 'KT1JTpEkByTStHYTT3qD8khJomNnvvnrfh4v'}]}]}]}]}]},
       'metadata': {'balance_updates': [{'kind': 'contract',
         <...>
        'internal_operation_results': [{'kind': 'transaction',
          'source': 'KT1HnvV5Z53naoh51jYvPF7w168nW8nfyx5v',
          'nonce': 0,
          'amount': '0',
          'destination': 'KT1JTpEkByTStHYTT3qD8khJomNnvvnrfh4v',
          'parameters': {'int': '45'},
          'result': {'status': 'applied',
           'storage': {'int': '45'},
           'consumed_gas': '12290',
           'storage_size': '86'}}]}}],
     'signature': 'sigsGCtnZKxWt4UD3HqkxPyemFTgeSVrgBDR4vawFBBFtLKok78JE8Jawn9VCp48ZZ9wYMZN52GhgZYHw8aCfk7fgAG5jMZS'}]

It worked! In the ``internal_operation_results`` we see a spawned transaction with parameters ``{'int': '45'}``
