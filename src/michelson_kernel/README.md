## Michelson kernel for Jupyter notebook

![michelson](https://cdn-images-1.medium.com/max/800/1*r_kVx8Rsqa0TLcIaK_WUQw.gif)

### How it works
* Technical details of the REPL implementation  
https://forum.tezosagora.org/t/michelson-repl-in-a-jupyter-notebook/1749
* Interactive tutorial demonstrating REPL features  
https://mybinder.org/v2/gh/baking-bad/pytezos/binder?filepath=michelson_quickstart.ipynb
* Same, but a rendered version  
https://nbviewer.jupyter.org/github/baking-bad/pytezos/blob/binder/michelson_quickstart.ipynb

### Sample notebooks
Located in the current repository:  
https://github.com/baking-bad/pytezos/tree/master/notebooks

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
