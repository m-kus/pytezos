# Michelson kernel
[![PyPI version](https://badge.fury.io/py/michelson-kernel.svg?)](https://badge.fury.io/py/michelson-kernel)
[![Docker Build Status](https://img.shields.io/docker/cloud/build/bakingbad/michelson-kernel)](https://hub.docker.com/r/bakingbad/michelson-kernel)
[![made_with pytezos](https://img.shields.io/badge/made_with-pytezos-yellowgreen.svg)](https://github.com/baking-bad/pytezos)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/baking-bad/michelson-kernel/binder?filepath=michelson_quickstart.ipynb)

Jupyter kernel for the Michelson language

![michelson](https://cdn-images-1.medium.com/max/800/1*r_kVx8Rsqa0TLcIaK_WUQw.gif)

## Features
* Custom interpreter with runtime type checker
* Syntax highlighter
* Autocomplete by `Tab`
* Inplace docstrings by `Shift+Tab`
* Macros support
* Verbose execution logging
* Debug helpers

## How to install

### Option 1: try online!
Powered by awesome Binder: https://mybinder.org/v2/gh/baking-bad/michelson-kernel/binder?filepath=michelson_quickstart.ipynb

### Option 2: run in docker
1. Get the latest image from dockerhub (only when new releases are published)
```
docker pull bakingbad/michelson-kernel
```
2. Create container using verified docker image:
```
docker run --rm -it -p 127.0.0.1:8888:8888 -v $(pwd):/home/jupyter/notebooks bakingbad/michelson-kernel
```
3. Open the link from container output in your browser
4. Save notebooks in the mapped folder in order not to loose them

### Option 3: install python package
1. Requires Python 3.5+. The recomended way to install it (especially if you plan to use multiple versions) is [pyenv](https://github.com/pyenv/pyenv-installer). Make sure you have all [necessary packets](https://github.com/pyenv/pyenv/wiki/Common-build-problems) installed. After that:
```
pyenv install 3.7.0
pyenv local 3.7.0   # per folder
pyenv global 3.7.9  # per system
```

2. Ensure you have several crypto libraries installed (see [pytezos docs](https://baking-bad.github.io/pytezos/#requirements)):
```
sudo apt install libsodium-dev libsecp256k1-dev libgmp-dev
```
3. Install the package using pip
```
pip install michelson-kernel
```
4. Install Jupyter
```
pip install jupyter
```
5. Check that Jupyter is now supporting Michelson kernel
```
jupyter kernelspec list
```
6. Run jupyter
```
jupyter notebook
```
Open the link from the command output, create new notebook with Michelson kernel.

### Option 4: install from sources
1. Follow steps 1-2 from "Option 3" to ensure you have correct Python version and packets required for the PyTezos library
2. Ensure the following packages are installed: `libssl-dev zlib1g-dev uuid-dev`
3. Get the sources, build and install
```
git clone https://github.com/baking-bad/michelson-kernel
cd michelson-kernel
make
```
4. Follow steps 4-6 from "Option 3"

## How to uninstall
1. Run the following command
```
jupyter kernelspec uninstall michelson -f
```
2. Check that Jupyter is no longer supporting Michelson kernel
```
jupyter kernelspec list
```
3. Uninstall Python package
```
pip uninstall michelson-kernel
```

## How it works
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

## Contact
* Telegram chat: [@baking_bad_chat](https://t.me/baking_bad_chat)
* Slack channel: [#baking-bad](https://tezos-dev.slack.com/archives/CV5NX7F2L)


## Credits
* This project is supported by Tezos Foundation
* Michelson test set from the Tezos repo is used to ensure the interpreter workability
* Michelson structured documentation by Nomadic Labs is used for inline help
