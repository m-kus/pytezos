# PyTezos

[![PyPI version](https://badge.fury.io/py/pytezos.svg?)](https://badge.fury.io/py/pytezos)
[![Tests](https://github.com/baking-bad/pytezos/workflows/Tests/badge.svg?)](https://github.com/baking-bad/pytezos/actions?query=workflow%3ATests)
[![Docker Build Status](https://img.shields.io/docker/cloud/build/bakingbad/pytezos)](https://hub.docker.com/r/bakingbad/pytezos)
[![Made With](https://img.shields.io/badge/made%20with-python-blue.svg?)](ttps://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


* RPC query engine
* Cryptography
* Building and parsing operations
* Smart contract interaction
* Local forging/packing & vice versa
* Working with Michelson AST

#### PyTezos CLI
* Generating contract parameter/storage schema
* Activating and revealing accounts
* Deploying contracts (+ GitHub integration)

#### Michelson REPL
* Builtin interpreter (reimplemented)
* Set of extra helpers (stack visualization, blockchain context mocking)

#### Michelson Jupyter kernel
* Custom interpreter with runtime type checker
* Syntax highlighting, autocomplete with `Tab`
* In-place docstrings with `Shift+Tab`
* Macros support
* Verbose execution logging
* Debug helpers

#### Michelson integration testing framework
* Writing integration tests using `unittest` package
* Simulating contract execution using remote intepreter (via RPC) or builtin one


## Installation

### From PyPi

```shell
$ pip install pytezos
```

### [Google Colab](https://colab.research.google.com)

`````python
>>> !apt install libsodium-dev libsecp256k1-dev libgmp-dev
>>> !pip install pytezos
`````

### Docker container
Verified & minified images for CI/CD https://hub.docker.com/r/bakingbad/pytezos/tags
```shell
$ # 1. Use image from registry
$ docker pull bakingbad/pytezos
$ # or build it yourself
$ docker build . -t pytezos
$ # 2. Use included docker-compose.yml
$ docker-compose up -d notebook
```

### Building from sources

Requirements:
* Python 3.7+
* [Poetry](https://python-poetry.org/docs/#installation)
* libsodium, libsecp256k1, gmp
* make

```shell
$ # prepare environment
$ make install
# # run full CI with tests
$ make
```

You need to install cryptographic packages before building the project:

#### Linux


##### Ubuntu, Debian and other apt-based distributions
```shell
$ sudo apt install libsodium-dev libsecp256k1-dev libgmp-dev
```

##### Arch Linux
```shell
$ sudo pacman -Syu --needed libsodium libsecp256k1 gmp
```
#### MacOS

[Homebrew](https://brew.sh/) needs to be installed.
```shell
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

## Quick start
Read [quick start guide](https://pytezos.org/quick_start.html)

## API reference
Check out a complete [API reference](https://pytezos.org/contents.html)

### Inline documentation
If you are working in Jupyter/Google Colab or any other interactive console, 
you can display documentation for a particular class/method:

```python
>>> from pytezos import pytezos
>>> pytezos
```

## Jupyter kernel

![michelson](https://cdn-images-1.medium.com/max/800/1*r_kVx8Rsqa0TLcIaK_WUQw.gif)

### How it works
* Technical details of the REPL implementation  
https://forum.tezosagora.org/t/michelson-repl-in-a-jupyter-notebook/1749
* Interactive tutorial demonstrating REPL features  
https://mybinder.org/v2/gh/baking-bad/michelson-kernel/binder?filepath=michelson_quickstart.ipynb
* Same, but a rendered version  
https://nbviewer.jupyter.org/github/baking-bad/michelson-kernel/blob/binder/michelson_quickstart.ipynb

### Sample notebooks
Located in the current repository in a separate branch:  
https://github.com/baking-bad/michelson-kernel/tree/binder

### List of helpers
These instructions are not Michelson primitives and thus cannot be used outside of the Jupyter.  
In the Jupyter editor helpers are highlighted in blue.

#### `DUMP`
Returns the whole stack with values, types, and annotations if any.

#### `DUMP n`
Returns top `n` items from the stack.

#### `PRINT "fmt"`
Prints a formatted string to the stdout, referencing arbitrary stack elements is allowed:  
`PRINT "This is the top element {0}, and this is the second {1}"`

#### `DROP_ALL`
Clears the stack.

#### `EXPAND { code }`
Expands Michelson macros:  
`EXPAND { PAPAIIR }`

#### `INCLUDE path`
Loads Michelson source from the filesystem (absolute or relative path) `INCLUDE "test.tz"`, or from one of the Tezos networks `INCLUDE "mainnet:KT1VG2WtYdSWz5E7chTeAdDPZNy2MpP8pTfL"`. Initializes `parameter`, `storage`, and `code` sections. If loaded from the network, current storage is also written to the `STORAGE` variable and can be accessed later. 

#### `PATCH prim value`
Sets value for on of the context-dependent Michelson instructions: `AMOUNT`, `BALANCE`, `NOW`, `SOURCE`, `SENDER`, `CHAIN_ID`.

#### `DEBUG bool`
Enables or disables verbose output: `DEBUG False` or `DEBUG True`.

#### `BIG_MAP_DIFF`
Takes the top of the stack, searches for temporary `big_map` instances in that element, and displays what the big_map_diff would be like if it was a contract execution ending.

#### `BEGIN %entrypoint (param_expr) (storage_expr)`
Simulates the contract execution beginning. Requires `parameter` and `storage` sections initialized. Also, clears the stack.  
The `%entrypoint` argument can be omitted, `%default` will be used in that case.  
This helper also allocates temporary big_map instances if any in parameters or storage.  
You can use `STORAGE` variable for the `storage_expr`, in case you have previously loaded it from the network.

#### `COMMIT`
Simulates the contract execution ending. Requires a `Pair` of operation list and valid storage on top of the stack. Returns a list of internal operations, new storage, and big_map_diff.

#### `RESET`
Clears the stack, deletes all big_map instances.

#### `RESET "network"`
Does the same as the version without parameters, but also initializes `NETWORK` and `CHAIN_ID` variables.  
Can be used to set real network context in order to access blockchain data.

#### `RUN %entrypoint (param_expr) (storage_expr)`
Requires `code` section initializes. Internally calls `BEGIN`, then executes `code`, and finishes with `COMMIT`.

Check out the articles and tutorial for more technical details, also you can take a look at the [implementation](https://github.com/baking-bad/pytezos/blob/master/pytezos/repl/helpers.py).

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
* Telegram chat: [@baking_bad_chat](https://t.me/baking_bad_chat)
* Slack channel: [#baking-bad](https://tezos-dev.slack.com/archives/CV5NX7F2L)

## Credits
* The project was initially started by Arthur Breitman, now it's maintained by Baking Bad team.
* Baking Bad is supported by Tezos Foundation
* Michelson test set from the Tezos repo is used to ensure the interpreter workability
* Michelson structured documentation by Nomadic Labs is used for inline help
