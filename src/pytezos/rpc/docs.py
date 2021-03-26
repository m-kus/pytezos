rpc_docs = {
  "/": {
    "props": [
      "chains",
      "config",
      "errors",
      "fetch_protocol",
      "injection",
      "monitor",
      "network",
      "protocols",
      "stats",
      "version",
      "workers"
    ]
  },
  "/chains": {
    "item": {
      "name": "chain_id",
      "descr": "A chain identifier. This is either a chain hash in Base58Check notation or a one the predefined aliases: 'main', 'test'."
    }
  },
  "/chains/{}": {
    "PATCH": {
      "descr": "Forcefully set the bootstrapped flag of the node",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "blocks",
      "chain_id",
      "checkpoint",
      "invalid_blocks",
      "is_bootstrapped",
      "mempool"
    ]
  },
  "/chains/{}/blocks": {
    "GET": {
      "descr": "Lists block hashes from '<chain>', up to the last checkpoint, sorted with decreasing fitness. Without arguments it returns the head of the chain. Optional arguments allow to return the list of predecessors of a given block or of a set of blocks.",
      "args": [
        {
          "name": "length",
          "descr": "The requested number of predecessors to return (per request; see next argument)."
        },
        {
          "name": "head",
          "descr": "An empty argument requests blocks starting with the current head. A non empty list allows to request one or more specific fragments of the chain."
        },
        {
          "name": "min_date",
          "descr": "When `min_date` is provided, blocks with a timestamp before `min_date` are filtered out"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "block_id",
      "descr": "A block identifier. This is either a block hash in Base58Check notation, one the predefined aliases: 'genesis', 'head' or a block level (index in the chain). One might also use 'head~N' or '<hash>~N' where N is an integer to denote the Nth predecessor of the designated block.Also, '<hash>+N' denotes the Nth successor of a block."
    }
  },
  "/chains/{}/chain_id": {
    "GET": {
      "descr": "The chain unique identifier.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/checkpoint": {
    "GET": {
      "descr": "The current checkpoint for this chain.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/invalid_blocks": {
    "GET": {
      "descr": "Lists blocks that have been declared invalid along with the errors that led to them being declared invalid.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "block_hash",
      "descr": "block_hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/invalid_blocks/{}": {
    "GET": {
      "descr": "The errors that appears during the block (in)validation.",
      "args": [],
      "ret": "Object"
    },
    "DELETE": {
      "descr": "Remove an invalid block for the tezos storage",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/is_bootstrapped": {
    "GET": {
      "descr": "The bootstrap status of a chain",
      "args": [],
      "ret": "Object"
    }
  },
  "/config": {
    "GET": {
      "descr": "Return the runtime node configuration (this takes into account the command-line arguments and the on-disk configuration file)",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "network"
    ]
  },
  "/config/network": {
    "props": [
      "user_activated_protocol_overrides",
      "user_activated_upgrades"
    ]
  },
  "/config/network/user_activated_protocol_overrides": {
    "GET": {
      "descr": "List of protocols which replace other protocols",
      "args": [],
      "ret": "Object"
    }
  },
  "/config/network/user_activated_upgrades": {
    "GET": {
      "descr": "List of protocols to switch to at given levels",
      "args": [],
      "ret": "Object"
    }
  },
  "/errors": {
    "GET": {
      "descr": "Schema for all the RPC errors from the shell",
      "args": [],
      "ret": "Object"
    }
  },
  "/fetch_protocol": {
    "item": {
      "name": "Protocol_hash",
      "descr": "Protocol_hash (Base58Check-encoded)"
    }
  },
  "/fetch_protocol/{}": {
    "GET": {
      "descr": "Fetch a protocol from the network.",
      "args": [],
      "ret": "Object"
    }
  },
  "/injection": {
    "props": [
      "block",
      "operation",
      "protocol"
    ]
  },
  "/injection/block": {
    "POST": {
      "descr": "Inject a block in the node and broadcast it. The `operations` embedded in `blockHeader` might be pre-validated using a contextual RPCs from the latest block (e.g. '/blocks/head/context/preapply'). Returns the ID of the block. By default, the RPC will wait for the block to be validated before answering. If ?async is true, the function returns immediately. Otherwise, the block will be validated before the result is returned. If ?force is true, it will be injected even on non strictly increasing fitness. An optional ?chain parameter can be used to specify whether to inject on the test chain or the main chain.",
      "args": [
        {
          "name": "async",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "force",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "chain",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/injection/operation": {
    "POST": {
      "descr": "Inject an operation in node and broadcast it. Returns the ID of the operation. The `signedOperationContents` should be constructed using a contextual RPCs from the latest block and signed by the client. By default, the RPC will wait for the operation to be (pre-)validated before answering. See RPCs under /blocks/prevalidation for more details on the prevalidation context. If ?async is true, the function returns immediately. Otherwise, the operation will be validated before the result is returned. An optional ?chain parameter can be used to specify whether to inject on the test chain or the main chain.",
      "args": [
        {
          "name": "async",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "chain",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/injection/protocol": {
    "POST": {
      "descr": "Inject a protocol in node. Returns the ID of the protocol. If ?async is true, the function returns immediately. Otherwise, the protocol will be validated before the result is returned.",
      "args": [
        {
          "name": "async",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/monitor": {
    "props": [
      "active_chains",
      "bootstrapped",
      "commit_hash",
      "heads",
      "protocols",
      "valid_blocks"
    ]
  },
  "/monitor/active_chains": {
    "GET": {
      "descr": "Monitor every chain creation and destruction. Currently active chains will be given as first elements",
      "args": [],
      "ret": "Array"
    }
  },
  "/monitor/bootstrapped": {
    "GET": {
      "descr": "Wait for the node to have synchronized its chain with a few peers (configured by the node's administrator), streaming head updates that happen during the bootstrapping process, and closing the stream at the end. If the node was already bootstrapped, returns the current head immediately.",
      "args": [],
      "ret": "Object"
    }
  },
  "/monitor/commit_hash": {
    "GET": {
      "descr": "DEPRECATED: use `version` instead.",
      "args": [],
      "ret": "Object"
    }
  },
  "/monitor/heads": {
    "item": {
      "name": "chain_id",
      "descr": "A chain identifier. This is either a chain hash in Base58Check notation or a one the predefined aliases: 'main', 'test'."
    }
  },
  "/monitor/heads/{}": {
    "GET": {
      "descr": "Monitor all blocks that are successfully validated by the node and selected as the new head of the given chain.",
      "args": [
        {
          "name": "next_protocol",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/monitor/protocols": {
    "GET": {
      "descr": "Monitor all economic protocols that are retrieved and successfully loaded and compiled by the node.",
      "args": [],
      "ret": "Object"
    }
  },
  "/monitor/valid_blocks": {
    "GET": {
      "descr": "Monitor all blocks that are successfully validated by the node, disregarding whether they were selected as the new head or not.",
      "args": [
        {
          "name": "protocol",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "next_protocol",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "chain",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/network": {
    "props": [
      "connections",
      "greylist",
      "log",
      "peers",
      "points",
      "self",
      "stat",
      "version",
      "versions"
    ]
  },
  "/network/connections": {
    "GET": {
      "descr": "List the running P2P connection.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "peer_id",
      "descr": "A cryptographic node identity (Base58Check-encoded)"
    }
  },
  "/network/connections/{}": {
    "GET": {
      "descr": "Details about the current P2P connection to the given peer.",
      "args": [],
      "ret": "Object"
    },
    "DELETE": {
      "descr": "Forced close of the current P2P connection to the given peer.",
      "args": [
        {
          "name": "wait",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/network/greylist": {
    "props": [
      "clear"
    ]
  },
  "/network/greylist/clear": {
    "GET": {
      "descr": "Clear all greylists tables.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/log": {
    "GET": {
      "descr": "Stream of all network events",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/peers": {
    "GET": {
      "descr": "List the peers the node ever met.",
      "args": [
        {
          "name": "filter",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "peer_id",
      "descr": "A cryptographic node identity (Base58Check-encoded)"
    }
  },
  "/network/peers/{}": {
    "GET": {
      "descr": "Details about a given peer.",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "ban",
      "banned",
      "log",
      "trust",
      "unban",
      "untrust"
    ]
  },
  "/network/peers/{}/ban": {
    "GET": {
      "descr": "Blacklist the given peer and remove it from the whitelist if present.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/peers/{}/banned": {
    "GET": {
      "descr": "Check if a given peer is blacklisted or greylisted.",
      "args": [],
      "ret": "Boolean"
    }
  },
  "/network/peers/{}/log": {
    "GET": {
      "descr": "Monitor network events related to a given peer.",
      "args": [
        {
          "name": "monitor",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    }
  },
  "/network/peers/{}/trust": {
    "GET": {
      "descr": "Whitelist a given peer permanently and remove it from the blacklist if present. The peer cannot be blocked (but its host IP still can).",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/peers/{}/unban": {
    "GET": {
      "descr": "Remove the given peer from the blacklist.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/peers/{}/untrust": {
    "GET": {
      "descr": "Remove a given peer from the whitelist.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/points": {
    "GET": {
      "descr": "List the pool of known `IP:port` used for establishing P2P connections.",
      "args": [
        {
          "name": "filter",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "point",
      "descr": "A network point (ipv4:port or [ipv6]:port)."
    }
  },
  "/network/points/{}": {
    "GET": {
      "descr": "Details about a given `IP:addr`.",
      "args": [],
      "ret": "Object"
    },
    "PUT": {
      "descr": "Connect to a peer",
      "args": [
        {
          "name": "timeout",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "ban",
      "banned",
      "log",
      "trust",
      "unban",
      "untrust"
    ]
  },
  "/network/points/{}/ban": {
    "GET": {
      "descr": "Blacklist the given address and remove it from the whitelist if present.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/points/{}/banned": {
    "GET": {
      "descr": "Check is a given address is blacklisted or greylisted.",
      "args": [],
      "ret": "Boolean"
    }
  },
  "/network/points/{}/log": {
    "GET": {
      "descr": "Monitor network events related to an `IP:addr`.",
      "args": [
        {
          "name": "monitor",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    }
  },
  "/network/points/{}/trust": {
    "GET": {
      "descr": "Trust a given address permanently and remove it from the blacklist if present. Connections from this address can still be closed on authentication if the peer is greylisted.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/points/{}/unban": {
    "GET": {
      "descr": "Remove an address from the blacklist.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/points/{}/untrust": {
    "GET": {
      "descr": "Remove an address from the whitelist.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/self": {
    "GET": {
      "descr": "Return the node's peer id",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/stat": {
    "GET": {
      "descr": "Global network bandwidth statistics in B/s.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/version": {
    "GET": {
      "descr": "DEPRECATED: use `version` instead.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/versions": {
    "GET": {
      "descr": "DEPRECATED: use `version` instead.",
      "args": [],
      "ret": "Array"
    }
  },
  "/protocols": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "Protocol_hash",
      "descr": "Protocol_hash (Base58Check-encoded)"
    }
  },
  "/protocols/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "environment"
    ]
  },
  "/protocols/{}/environment": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [],
      "ret": "Object"
    }
  },
  "/stats": {
    "props": [
      "gc",
      "memory"
    ]
  },
  "/stats/gc": {
    "GET": {
      "descr": "Gets stats from the OCaml Garbage Collector",
      "args": [],
      "ret": "Object"
    }
  },
  "/stats/memory": {
    "GET": {
      "descr": "Gets memory usage stats",
      "args": [],
      "ret": "Object"
    }
  },
  "/version": {
    "GET": {
      "descr": "Get information on the node version",
      "args": [],
      "ret": "Object"
    }
  },
  "/workers": {
    "props": [
      "block_validator",
      "chain_validators",
      "prevalidators"
    ]
  },
  "/workers/block_validator": {
    "GET": {
      "descr": "Introspect the state of the block_validator worker.",
      "args": [],
      "ret": "Object"
    }
  },
  "/workers/chain_validators": {
    "GET": {
      "descr": "Lists the chain validator workers and their status.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "chain_id",
      "descr": "A chain identifier. This is either a chain hash in Base58Check notation or a one the predefined aliases: 'main', 'test'."
    }
  },
  "/workers/chain_validators/{}": {
    "GET": {
      "descr": "Introspect the state of a chain validator worker.",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "ddb",
      "peers_validators"
    ]
  },
  "/workers/chain_validators/{}/ddb": {
    "GET": {
      "descr": "Introspect the state of the DDB attached to a chain validator worker.",
      "args": [],
      "ret": "Object"
    }
  },
  "/workers/chain_validators/{}/peers_validators": {
    "GET": {
      "descr": "Lists the peer validator workers and their status.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "peer_id",
      "descr": "A cryptographic node identity (Base58Check-encoded)"
    }
  },
  "/workers/chain_validators/{}/peers_validators/{}": {
    "GET": {
      "descr": "Introspect the state of a peer validator worker.",
      "args": [],
      "ret": "Object"
    }
  },
  "/workers/prevalidators": {
    "GET": {
      "descr": "Lists the Prevalidator workers and their status.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "chain_id",
      "descr": "A chain identifier. This is either a chain hash in Base58Check notation or a one the predefined aliases: 'main', 'test'."
    }
  },
  "/workers/prevalidators/{}": {
    "GET": {
      "descr": "Introspect the state of prevalidator workers.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/mempool": {
    "props": [
      "filter",
      "monitor_operations",
      "pending_operations",
      "request_operations"
    ]
  },
  "/chains/{}/mempool/filter": {
    "GET": {
      "descr": "Get the configuration of the mempool filter.",
      "args": [],
      "ret": "Object"
    },
    "POST": {
      "descr": "Set the configuration of the mempool filter.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/mempool/monitor_operations": {
    "GET": {
      "descr": "Monitor the mempool operations.",
      "args": [
        {
          "name": "applied",
          "descr": "Include applied operations (set by default)"
        },
        {
          "name": "refused",
          "descr": "Include refused operations"
        },
        {
          "name": "branch_refused",
          "descr": "Include branch refused operations"
        },
        {
          "name": "branch_delayed",
          "descr": "Include branch delayed operations (set by default)"
        }
      ],
      "ret": "Array"
    }
  },
  "/chains/{}/mempool/pending_operations": {
    "GET": {
      "descr": "List the prevalidated operations.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/mempool/request_operations": {
    "POST": {
      "descr": "Request the operations of your peers.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}": {
    "GET": {
      "descr": "All the information about a block. The associated metadata may not be present depending on the history mode and block's distance from the head.",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "context",
      "endorsing_power",
      "hash",
      "header",
      "helpers",
      "live_blocks",
      "metadata",
      "metadata_hash",
      "minimal_valid_time",
      "operation_hashes",
      "operation_metadata_hashes",
      "operations",
      "operations_metadata_hash",
      "protocols",
      "required_endorsements",
      "votes"
    ]
  },
  "/chains/{}/blocks/{}/context": {
    "props": [
      "big_maps",
      "constants",
      "contracts",
      "delegates",
      "nonces",
      "raw",
      "sapling",
      "seed"
    ]
  },
  "/chains/{}/blocks/{}/context/big_maps": {
    "item": {
      "name": "big_map_id",
      "descr": "A big map identifier"
    }
  },
  "/chains/{}/blocks/{}/context/big_maps/{}": {
    "item": {
      "name": "script_expr",
      "descr": "script_expr (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/big_maps/{}/{}": {
    "GET": {
      "descr": "Access the value associated with a key in a big map.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/constants": {
    "GET": {
      "descr": "All constants",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "errors"
    ]
  },
  "/chains/{}/blocks/{}/context/constants/errors": {
    "GET": {
      "descr": "Schema for all the RPC errors from this protocol version",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts": {
    "GET": {
      "descr": "All existing contracts (including non-empty default contracts).",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "contract_id",
      "descr": "A contract identifier encoded in b58check."
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}": {
    "GET": {
      "descr": "Access the complete status of a contract.",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "balance",
      "big_map_get",
      "counter",
      "delegate",
      "entrypoints",
      "manager_key",
      "script",
      "single_sapling_get_diff",
      "storage"
    ]
  },
  "/chains/{}/blocks/{}/context/contracts/{}/balance": {
    "GET": {
      "descr": "Access the balance of a contract.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/big_map_get": {
    "POST": {
      "descr": "Access the value associated with a key in a big map of the contract (deprecated).",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/counter": {
    "GET": {
      "descr": "Access the counter of a contract, if any.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/delegate": {
    "GET": {
      "descr": "Access the delegate of a contract, if any.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/entrypoints": {
    "GET": {
      "descr": "Return the list of entrypoints of the contract",
      "args": [],
      "ret": "Object"
    },
    "item": {
      "name": "string",
      "descr": "\u00af\\_(\u30c4)_/\u00af"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/entrypoints/{}": {
    "GET": {
      "descr": "Return the type of the given entrypoint of the contract",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/manager_key": {
    "GET": {
      "descr": "Access the manager of a contract.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/script": {
    "GET": {
      "descr": "Access the code and data of the contract.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/single_sapling_get_diff": {
    "GET": {
      "descr": "Returns the root and a diff of a state starting from an optional offset which is zero by default.",
      "args": [
        {
          "name": "offset_commitment",
          "descr": "Commitments and ciphertexts are returned from the specified offset up to the most recent."
        },
        {
          "name": "offset_nullifier",
          "descr": "Nullifiers are returned from the specified offset up to the most recent."
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/storage": {
    "GET": {
      "descr": "Access the data of the contract.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates": {
    "GET": {
      "descr": "Lists all registered delegates.",
      "args": [
        {
          "name": "active",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "inactive",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}": {
    "GET": {
      "descr": "Everything about a delegate.",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "balance",
      "deactivated",
      "delegated_balance",
      "delegated_contracts",
      "frozen_balance",
      "frozen_balance_by_cycle",
      "grace_period",
      "staking_balance",
      "voting_power"
    ]
  },
  "/chains/{}/blocks/{}/context/delegates/{}/balance": {
    "GET": {
      "descr": "Returns the full balance of a given delegate, including the frozen balances.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/deactivated": {
    "GET": {
      "descr": "Tells whether the delegate is currently tagged as deactivated or not.",
      "args": [],
      "ret": "Boolean"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/delegated_balance": {
    "GET": {
      "descr": "Returns the balances of all the contracts that delegate to a given delegate. This excludes the delegate's own balance and its frozen balances.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/delegated_contracts": {
    "GET": {
      "descr": "Returns the list of contracts that delegate to a given delegate.",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/frozen_balance": {
    "GET": {
      "descr": "Returns the total frozen balances of a given delegate, this includes the frozen deposits, rewards and fees.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/frozen_balance_by_cycle": {
    "GET": {
      "descr": "Returns the frozen balances of a given delegate, indexed by the cycle by which it will be unfrozen",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/grace_period": {
    "GET": {
      "descr": "Returns the cycle by the end of which the delegate might be deactivated if she fails to execute any delegate action. A deactivated delegate might be reactivated (without loosing any rolls) by simply re-registering as a delegate. For deactivated delegates, this value contains the cycle by which they were deactivated.",
      "args": [],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/staking_balance": {
    "GET": {
      "descr": "Returns the total amount of tokens delegated to a given delegate. This includes the balances of all the contracts that delegate to it, but also the balance of the delegate itself and its frozen fees and deposits. The rewards do not count in the delegated balance until they are unfrozen.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/voting_power": {
    "GET": {
      "descr": "The number of rolls in the vote listings for a given delegate",
      "args": [],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/nonces": {
    "item": {
      "name": "block_level",
      "descr": "A level integer"
    }
  },
  "/chains/{}/blocks/{}/context/nonces/{}": {
    "GET": {
      "descr": "Info about the nonce of a previous block.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw": {
    "props": [
      "bytes",
      "json"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/bytes": {
    "GET": {
      "descr": "Returns the raw context.",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/sapling": {
    "item": {
      "name": "sapling_state_id",
      "descr": "A sapling state identifier"
    }
  },
  "/chains/{}/blocks/{}/context/sapling/{}": {
    "props": [
      "get_diff"
    ]
  },
  "/chains/{}/blocks/{}/context/sapling/{}/get_diff": {
    "GET": {
      "descr": "Returns the root and a diff of a state starting from an optional offset which is zero by default.",
      "args": [
        {
          "name": "offset_commitment",
          "descr": "Commitments and ciphertexts are returned from the specified offset up to the most recent."
        },
        {
          "name": "offset_nullifier",
          "descr": "Nullifiers are returned from the specified offset up to the most recent."
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/seed": {
    "POST": {
      "descr": "Seed of the cycle to which the block belongs.",
      "args": [],
      "ret": "String"
    }
  },
  "/chains/{}/blocks/{}/endorsing_power": {
    "POST": {
      "descr": "Get the endorsing power of an endorsement, that is, the number of slots that the endorser has",
      "args": [],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/hash": {
    "GET": {
      "descr": "The block's hash, its unique identifier.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/header": {
    "GET": {
      "descr": "The whole block header.",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "protocol_data",
      "raw",
      "shell"
    ]
  },
  "/chains/{}/blocks/{}/header/protocol_data": {
    "GET": {
      "descr": "The version-specific fragment of the block header.",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "raw"
    ]
  },
  "/chains/{}/blocks/{}/header/protocol_data/raw": {
    "GET": {
      "descr": "The version-specific fragment of the block header (unparsed).",
      "args": [],
      "ret": "String"
    }
  },
  "/chains/{}/blocks/{}/header/raw": {
    "GET": {
      "descr": "The whole block header (unparsed).",
      "args": [],
      "ret": "String"
    }
  },
  "/chains/{}/blocks/{}/header/shell": {
    "GET": {
      "descr": "The shell-specific fragment of the block header.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers": {
    "props": [
      "baking_rights",
      "complete",
      "current_level",
      "endorsing_rights",
      "forge",
      "forge_block_header",
      "levels_in_current_cycle",
      "parse",
      "preapply",
      "scripts"
    ]
  },
  "/chains/{}/blocks/{}/helpers/baking_rights": {
    "GET": {
      "descr": "Retrieves the list of delegates allowed to bake a block.\nBy default, it gives the best baking priorities for bakers that have at least one opportunity below the 64th priority for the next block.\nParameters `level` and `cycle` can be used to specify the (valid) level(s) in the past or future at which the baking rights have to be returned. When asked for (a) whole cycle(s), baking opportunities are given by default up to the priority 8.\nParameter `delegate` can be used to restrict the results to the given delegates. If parameter `all` is set, all the baking opportunities for each baker at each level are returned, instead of just the first one.\nReturns the list of baking slots. Also returns the minimal timestamps that correspond to these slots. The timestamps are omitted for levels in the past, and are only estimates for levels later that the next block, based on the hypothesis that all predecessor blocks were baked at the first priority.",
      "args": [
        {
          "name": "level",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "cycle",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "delegate",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "max_priority",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "all",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/helpers/complete": {
    "item": {
      "name": "prefix",
      "descr": "\u00af\\_(\u30c4)_/\u00af"
    }
  },
  "/chains/{}/blocks/{}/helpers/complete/{}": {
    "GET": {
      "descr": "Try to complete a prefix of a Base58Check-encoded data. This RPC is actually able to complete hashes of block, operations, public_keys and contracts.",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/helpers/current_level": {
    "GET": {
      "descr": "Returns the level of the interrogated block, or the one of a block located `offset` blocks after in the chain (or before when negative). For instance, the next block if `offset` is 1.",
      "args": [
        {
          "name": "offset",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/endorsing_rights": {
    "GET": {
      "descr": "Retrieves the delegates allowed to endorse a block.\nBy default, it gives the endorsement slots for delegates that have at least one in the next block.\nParameters `level` and `cycle` can be used to specify the (valid) level(s) in the past or future at which the endorsement rights have to be returned. Parameter `delegate` can be used to restrict the results to the given delegates.\nReturns the list of endorsement slots. Also returns the minimal timestamps that correspond to these slots. The timestamps are omitted for levels in the past, and are only estimates for levels later that the next block, based on the hypothesis that all predecessor blocks were baked at the first priority.",
      "args": [
        {
          "name": "level",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "cycle",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "delegate",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/helpers/forge": {
    "props": [
      "operations",
      "protocol_data"
    ]
  },
  "/chains/{}/blocks/{}/helpers/forge/operations": {
    "POST": {
      "descr": "Forge an operation",
      "args": [],
      "ret": "String"
    }
  },
  "/chains/{}/blocks/{}/helpers/forge/protocol_data": {
    "POST": {
      "descr": "Forge the protocol-specific part of a block header",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/forge_block_header": {
    "POST": {
      "descr": "Forge a block header",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/levels_in_current_cycle": {
    "GET": {
      "descr": "Levels of a cycle",
      "args": [
        {
          "name": "offset",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/parse": {
    "props": [
      "block",
      "operations"
    ]
  },
  "/chains/{}/blocks/{}/helpers/parse/block": {
    "POST": {
      "descr": "Parse a block",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/parse/operations": {
    "POST": {
      "descr": "Parse operations",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/helpers/preapply": {
    "props": [
      "block",
      "operations"
    ]
  },
  "/chains/{}/blocks/{}/helpers/preapply/block": {
    "POST": {
      "descr": "Simulate the validation of a block that would contain the given operations and return the resulting fitness and context hash.",
      "args": [
        {
          "name": "sort",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "timestamp",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/preapply/operations": {
    "POST": {
      "descr": "Simulate the validation of an operation.",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts": {
    "props": [
      "entrypoint",
      "entrypoints",
      "pack_data",
      "run_code",
      "run_operation",
      "trace_code",
      "typecheck_code",
      "typecheck_data"
    ]
  },
  "/chains/{}/blocks/{}/helpers/scripts/entrypoint": {
    "POST": {
      "descr": "Return the type of the given entrypoint",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/entrypoints": {
    "POST": {
      "descr": "Return the list of entrypoints of the given script",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/pack_data": {
    "POST": {
      "descr": "Computes the serialized version of some data expression using the same algorithm as script instruction PACK",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/run_code": {
    "POST": {
      "descr": "Run a piece of code in the current context",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/run_operation": {
    "POST": {
      "descr": "Run an operation without signature checks",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/trace_code": {
    "POST": {
      "descr": "Run a piece of code in the current context, keeping a trace",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/typecheck_code": {
    "POST": {
      "descr": "Typecheck a piece of code in the current context",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/typecheck_data": {
    "POST": {
      "descr": "Check that some data expression is well formed and of a given type in the current context",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/live_blocks": {
    "GET": {
      "descr": "List the ancestors of the given block which, if referred to as the branch in an operation header, are recent enough for that operation to be included in the current block.",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/metadata": {
    "GET": {
      "descr": "All the metadata associated to the block.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/metadata_hash": {
    "GET": {
      "descr": "Hash of the metadata associated to the block. This is only set on blocks starting from environment V1.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/minimal_valid_time": {
    "GET": {
      "descr": "Minimal valid time for a block given a priority and an endorsing power.",
      "args": [
        {
          "name": "priority",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "endorsing_power",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/operation_hashes": {
    "GET": {
      "descr": "The hashes of all the operations included in the block.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "list_offset",
      "descr": "Index `n` of the requested validation pass."
    }
  },
  "/chains/{}/blocks/{}/operation_hashes/{}": {
    "GET": {
      "descr": "All the operations included in `n-th` validation pass of the block.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "operation_offset",
      "descr": "Index `m` of the requested operation in its validation pass."
    }
  },
  "/chains/{}/blocks/{}/operation_hashes/{}/{}": {
    "GET": {
      "descr": "The hash of then `m-th` operation in the `n-th` validation pass of the block.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/operation_metadata_hashes": {
    "GET": {
      "descr": "The hashes of all the operation metadata included in the block. This is only set on blocks starting from environment V1.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "list_offset",
      "descr": "Index `n` of the requested validation pass."
    }
  },
  "/chains/{}/blocks/{}/operation_metadata_hashes/{}": {
    "GET": {
      "descr": "All the operation metadata included in `n-th` validation pass of the block. This is only set on blocks starting from environment V1.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "operation_offset",
      "descr": "Index `m` of the requested operation in its validation pass."
    }
  },
  "/chains/{}/blocks/{}/operation_metadata_hashes/{}/{}": {
    "GET": {
      "descr": "The hash of then `m-th` operation metadata in the `n-th` validation pass of the block. This is only set on blocks starting from environment V1.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/operations": {
    "GET": {
      "descr": "All the operations included in the block.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "list_offset",
      "descr": "Index `n` of the requested validation pass."
    }
  },
  "/chains/{}/blocks/{}/operations/{}": {
    "GET": {
      "descr": "All the operations included in `n-th` validation pass of the block.",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "operation_offset",
      "descr": "Index `m` of the requested operation in its validation pass."
    }
  },
  "/chains/{}/blocks/{}/operations/{}/{}": {
    "GET": {
      "descr": "The `m-th` operation in the `n-th` validation pass of the block.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/operations_metadata_hash": {
    "GET": {
      "descr": "The root hash of the operations metadata from the block. This is only set on blocks starting from environment V1.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/protocols": {
    "GET": {
      "descr": "Current and next protocol.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/required_endorsements": {
    "GET": {
      "descr": "Minimum number of endorsements for a block to be valid, given a delay of the block's timestamp with respect to the minimum time to bake at the block's priority",
      "args": [
        {
          "name": "block_delay",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/votes": {
    "props": [
      "ballot_list",
      "ballots",
      "current_period",
      "current_period_kind",
      "current_proposal",
      "current_quorum",
      "listings",
      "proposals",
      "successor_period",
      "total_voting_power"
    ]
  },
  "/chains/{}/blocks/{}/votes/ballot_list": {
    "GET": {
      "descr": "Ballots casted so far during a voting period.",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/votes/ballots": {
    "GET": {
      "descr": "Sum of ballots casted so far during a voting period.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/votes/current_period": {
    "GET": {
      "descr": "Returns the voting period (index, kind, starting position) and related information (position, remaining) of the interrogated block.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/votes/current_period_kind": {
    "GET": {
      "descr": "Current period kind. This RPC is DEPRECATED: use `..<block_id>/votes/current_period` RPC instead.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/votes/current_proposal": {
    "GET": {
      "descr": "Current proposal under evaluation.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/votes/current_quorum": {
    "GET": {
      "descr": "Current expected quorum.",
      "args": [],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/votes/listings": {
    "GET": {
      "descr": "List of delegates with their voting weight, in number of rolls.",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/votes/proposals": {
    "GET": {
      "descr": "List of proposals with number of supporters.",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/votes/successor_period": {
    "GET": {
      "descr": "Returns the voting period (index, kind, starting position) and related information (position, remaining) of the next block.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/votes/total_voting_power": {
    "GET": {
      "descr": "Total number of rolls for the delegates in the voting listings.",
      "args": [],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "active_delegates_with_rolls",
      "big_maps",
      "block_priority",
      "commitments",
      "contracts",
      "cycle",
      "delegates",
      "delegates_with_frozen_balance",
      "ramp_up",
      "rolls",
      "sapling",
      "votes"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/active_delegates_with_rolls": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/active_delegates_with_rolls/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Boolean"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/big_maps": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "index",
      "next"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/big_maps/index": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "big_map_id",
      "descr": "A big map identifier"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/big_maps/index/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "contents",
      "key_type",
      "total_bytes",
      "value_type"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/big_maps/index/{}/contents": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "script_expr",
      "descr": "script_expr (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/big_maps/index/{}/contents/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/big_maps/index/{}/key_type": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/big_maps/index/{}/total_bytes": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/big_maps/index/{}/value_type": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/big_maps/next": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/block_priority": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/commitments": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "Blinded public key hash",
      "descr": "Blinded public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/commitments/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "global_counter",
      "index"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/global_counter": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "contract_id",
      "descr": "A contract identifier encoded in b58check."
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "balance",
      "change",
      "code",
      "counter",
      "delegate",
      "delegate_desactivation",
      "delegated",
      "frozen_balance",
      "inactive_delegate",
      "manager",
      "paid_bytes",
      "roll_list",
      "storage",
      "used_bytes"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/balance": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/change": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/code": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/counter": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/delegate": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/delegate_desactivation": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/delegated": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "contract_id",
      "descr": "A contract identifier encoded in b58check."
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/delegated/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Boolean"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/frozen_balance": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "block_cycle",
      "descr": "A cycle integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/frozen_balance/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "deposits",
      "fees",
      "rewards"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/frozen_balance/{}/deposits": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/frozen_balance/{}/fees": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/frozen_balance/{}/rewards": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/inactive_delegate": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Boolean"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/manager": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/paid_bytes": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/roll_list": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/storage": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/used_bytes": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/cycle": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "block_cycle",
      "descr": "A cycle integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "last_roll",
      "nonces",
      "random_seed",
      "roll_snapshot"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/last_roll": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "int",
      "descr": "\u00af\\_(\u30c4)_/\u00af"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/last_roll/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/nonces": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "block_level",
      "descr": "A level integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/nonces/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/random_seed": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "String"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/roll_snapshot": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/delegates": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/delegates/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Boolean"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/delegates_with_frozen_balance": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "block_cycle",
      "descr": "A cycle integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/delegates_with_frozen_balance/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/delegates_with_frozen_balance/{}/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Boolean"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/ramp_up": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "deposits",
      "rewards"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/ramp_up/deposits": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "block_cycle",
      "descr": "A cycle integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/ramp_up/deposits/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/ramp_up/rewards": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "block_cycle",
      "descr": "A cycle integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/ramp_up/rewards/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "index",
      "limbo",
      "next",
      "owner"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/index": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "roll",
      "descr": "\u00af\\_(\u30c4)_/\u00af"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/index/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "successor"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/index/{}/successor": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/limbo": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/next": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/owner": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "current",
      "snapshot"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/owner/current": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "roll",
      "descr": "\u00af\\_(\u30c4)_/\u00af"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/owner/current/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/owner/snapshot": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "block_cycle",
      "descr": "A cycle integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/owner/snapshot/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "int",
      "descr": "\u00af\\_(\u30c4)_/\u00af"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/owner/snapshot/{}/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "roll",
      "descr": "\u00af\\_(\u30c4)_/\u00af"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/rolls/owner/snapshot/{}/{}/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "index",
      "next"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "sapling_state_id",
      "descr": "A sapling state identifier"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "ciphertexts",
      "commitments",
      "commitments_size",
      "memo_size",
      "nullifiers_hashed",
      "nullifiers_ordered",
      "nullifiers_size",
      "roots",
      "roots_level",
      "roots_pos",
      "total_bytes"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/ciphertexts": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "sapling_ciphertext_position",
      "descr": "The position of a sapling ciphertext"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/ciphertexts/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/commitments": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "sapling_node_position",
      "descr": "The position of a node in a sapling commitment tree"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/commitments/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/commitments_size": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/memo_size": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/nullifiers_hashed": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "sapling_nullifier",
      "descr": "A sapling nullifier"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/nullifiers_hashed/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/nullifiers_ordered": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "sapling_nullifier_position",
      "descr": "A sapling nullifier position"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/nullifiers_ordered/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/nullifiers_size": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/roots": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "sapling_root",
      "descr": "A sapling root"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/roots/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/roots_level": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/roots_pos": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/index/{}/total_bytes": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sapling/next": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    },
    "props": [
      "ballots",
      "current_period",
      "current_period_kind",
      "current_proposal",
      "listings",
      "listings_size",
      "participation_ema",
      "pred_period_kind",
      "proposals",
      "proposals_count"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/ballots": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/ballots/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "String"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/current_period": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/current_period_kind": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/current_proposal": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/listings": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/listings/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/listings_size": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/participation_ema": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/pred_period_kind": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/proposals": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "Protocol_hash",
      "descr": "Protocol_hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/proposals/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/proposals/{}/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Boolean"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/proposals_count": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    },
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/proposals_count/{}": {
    "GET": {
      "descr": "\u00af\\_(\u30c4)_/\u00af",
      "args": [
        {
          "name": "depth",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  }
}
