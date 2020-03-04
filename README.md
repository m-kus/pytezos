# PyTezos

[![PyPI version](https://badge.fury.io/py/pytezos.svg?)](https://badge.fury.io/py/pytezos)
[![Build Status](https://travis-ci.org/baking-bad/pytezos.svg?branch=master)](https://travis-ci.org/baking-bad/pytezos)
[![Made With](https://img.shields.io/badge/made%20with-python-blue.svg?)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python SDK for Tezos: RPC, cryptography, operations, smart contract interaction

### Requirements

* git
* python 3.6+
* pip 19.0.1+

You will also probably need to install several cryptographic packets.

#### Linux

Use apt or your favourite package manager:
```
$ sudo apt install libsodium-dev libsecp256k1-dev libgmp-dev
```

#### MacOS

Use homebrew:
```
$ brew tap cuber/homebrew-libsecp256k1
$ brew install libsodium libsecp256k1 gmp
```

#### Windows

The recommended way is to use WSL and then follow the instructions for Linux,
but if you feel lucky you can try to install natively:

1. Install MinGW from [https://osdn.net/projects/mingw/](https://osdn.net/projects/mingw/)
2. Make sure `C:\MinGW\bin` is added to your `PATH`
3. Download the latest libsodium-X.Y.Z-msvc.zip from [https://download.libsodium.org/libsodium/releases/](https://download.libsodium.org/libsodium/releases/).
4. Extract the Win64/Release/v143/dynamic/libsodium.dll from the zip file
5. Copy libsodium.dll to C:\Windows\System32\libsodium.dll

### Installation

```
$ pip install pytezos
```

#### Google Colab

`````python
>>> !apt install libsodium-dev libsecp256k1-dev libgmp-dev
>>> !pip install pytezos
`````

### Usage

Read [quick start guide](https://baking-bad.github.io/pytezos), or just enjoy surfing the interactive documentation using Python console/Jupyter:
```python
>>> from pytezos import pytezos
>>> pytezos
<pytezos.client.PyTezosClient object at 0x7f904cf339e8>

Properties
.key  # tz1grSQDByRpnVs7sPtaprNZRp531ZKz6Jmm
.shell  # https://tezos-dev.cryptonomic-infra.tech/ (alphanet)

Helpers
.account()
.activate_account()
.ballot()
.contract()
.delegation()
.double_baking_evidence()
.double_endorsement_evidence()
.endorsement()
.operation()
.operation_group()
.origination()
.proposals()
.reveal()
.seed_nonce_revelation()
.transaction()
.using()
```

### Publications

* Pytezos 2.0 release with embedded docs and smart contract interaction engine  
https://medium.com/coinmonks/high-level-interface-for-michelson-contracts-and-not-only-7264db76d7ae

* Materials from TQuorum:Berlin workshop - building an app on top of PyTezos and ConseilPy  
https://medium.com/coinmonks/atomic-tips-berlin-workshop-materials-c5c8ee3f46aa

* Materials from the EETH hackathon - setting up a local development infrastructure, deploying and interacting with a contract  
https://medium.com/tezoscommons/preparing-for-the-tezos-hackathon-with-baking-bad-45f2d5fca519

* Introducing integration testing engine  
https://medium.com/tezoscommons/testing-michelson-contracts-with-pytezos-513718499e93

### Additional materials

* Interacting with FA1.2 contract by TQTezos
https://assets.tqtezos.com/token-contracts/1-fa12-lorentz#interactusingpytezos
* Deploying a contract by Vadim Manaenko
https://blog.aira.life/tezos-dont-forget-the-mother-console-fd2001261e50

### Michelson test samples

* In this repo
https://github.com/baking-bad/pytezos/tree/master/examples
* Atomex (atomic swaps aka cross-chain transactions)
https://github.com/atomex-me/atomex-michelson/blob/master/tests/test_atomex.py
* Atomex for FA1.2 (includes cross-contract interaction and views)
https://github.com/atomex-me/atomex-fa12-ligo/tree/master/tests
* MultiAsset implementation tests (in a sandbox environment)
https://github.com/tqtezos/smart-contracts/tree/master/multi_asset/tezos_mac_tests

### Contact
If you have any questions, please write to our telegram chat: https://t.me/baking_bad_chat

### About
The project was initially started by Arthur Breitman, now it's maintained by Baking Bad team.
PyTezos development is supported by Tezos Foundation.
