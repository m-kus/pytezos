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
      "private",
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
      "levels",
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
          "descr": "When `min_date` is provided, blocks with a timestamp before `min_date` are filtered out. However, if the `length` parameter is also provided, then up to that number of predecessors will be returned regardless of their date."
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
      "descr": "DEPRECATED: use `../levels/{checkpoint, savepoint, caboose, history_mode}` instead. The current checkpoint for this chain.",
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
  "/chains/{}/levels": {
    "props": [
      "caboose",
      "checkpoint",
      "savepoint"
    ]
  },
  "/chains/{}/levels/caboose": {
    "GET": {
      "descr": "The current caboose for this chain.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/levels/checkpoint": {
    "GET": {
      "descr": "The current checkpoint for this chain.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/levels/savepoint": {
    "GET": {
      "descr": "The current savepoint for this chain.",
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
      "history_mode",
      "logging",
      "network"
    ]
  },
  "/config/history_mode": {
    "GET": {
      "descr": "Returns the history mode of the node's underlying storage.",
      "args": [],
      "ret": "Object"
    }
  },
  "/config/logging": {
    "PUT": {
      "descr": "Replace the logging configuration of the node.",
      "args": [],
      "ret": "Object"
    }
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
      "ret": "Array"
    }
  },
  "/config/network/user_activated_upgrades": {
    "GET": {
      "descr": "List of protocols to switch to at given levels",
      "args": [],
      "ret": "Array"
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
      "descr": "Inject an operation in node and broadcast it. Returns the ID of the operation. The `signedOperationContents` should be constructed using contextual RPCs from the latest block and signed by the client. The injection of the operation will apply it on the current mempool context. This context may change at each operation injection or operation reception from peers. By default, the RPC will wait for the operation to be (pre-)validated before returning. However, if ?async is true, the function returns immediately. The optional ?chain parameter can be used to specify whether to inject on the test chain or the main chain.",
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
    "DELETE": {
      "descr": "Clear all greylists tables. This will unban all addresses and peers automatically greylisted by the system.",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "clear",
      "ips",
      "peers"
    ]
  },
  "/network/greylist/clear": {
    "GET": {
      "descr": "DEPRECATED: Clear all greylists tables. This will unban all addresses and peers automatically greylisted by the system. Use DELETE `/network/greylist` instead",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/greylist/ips": {
    "GET": {
      "descr": "Returns an object that contains a list of IP and the field \"not_reliable_since\".\n           If the field \"not_reliable_since\" is None then the list contains the currently greylisted IP addresses.\n           If the field \"not_reliable_since\" Contains a date, this means that the greylist has been overflowed and it is no more possible to obtain the exact list of greylisted IPs. Since the greylist of IP addresses has been design to work whatever his size, there is no security issue related to this overflow.\n          Reinitialize the ACL structure by calling \"delete /network/greylist\" to get back this list reliable.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/greylist/peers": {
    "GET": {
      "descr": "List of the last greylisted peers.",
      "args": [],
      "ret": "Array"
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
    "PATCH": {
      "descr": "Change the permissions of a given peer. With `{acl: ban}`: blacklist the given peer and remove it from the whitelist if present. With `{acl: open}`: removes the peer from the blacklist and whitelist. With `{acl: trust}`: trust the given peer permanently and remove it from the blacklist if present. The peer cannot be blocked (but its host IP still can).",
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
      "descr": "DEPRECATED: Blacklist the given peer and remove it from the whitelist if present. Use PATCH `network/peers/<peer_id>` instead.",
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
      "descr": "DEPRECATED: Whitelist a given peer permanently and remove it from the blacklist if present. The peer cannot be blocked (but its host IP still can). Use PATCH `network/peers/<peer_id>` instead.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/peers/{}/unban": {
    "GET": {
      "descr": "DEPRECATED: Remove the given peer from the blacklist. Use PATCH `network/peers/<peer_id>` instead.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/peers/{}/untrust": {
    "GET": {
      "descr": "DEPRECATED: Remove a given peer from the whitelist. Use PATCH `network/peers/<peer_id>` instead.",
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
    "PATCH": {
      "descr": "Change the connectivity state of a given `IP:addr`. With `{acl : ban}`: blacklist the given address and remove it from the whitelist if present. With `{acl: open}`: removes an address from the blacklist and whitelist. With `{acl: trust}`: trust a given address permanently and remove it from the blacklist if present. With `{peer_id: <id>}` set the peerId of the point. Connections from this address can still be closed on authentication if the peer is greylisted. ",
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
  "/network/points/{}/ban": {
    "GET": {
      "descr": "DEPRECATED: Blacklist the given address and remove it from the whitelist if present. Use PATCH `/network/point/<point_id>` instead.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/points/{}/banned": {
    "GET": {
      "descr": "Check if a given address is blacklisted or greylisted. Port component is unused.",
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
      "descr": "DEPRECATED: Trust a given address permanently and remove it from the blacklist if present. Connections from this address can still be closed on authentication if the peer is greylisted. Use PATCH`/network/point/<point_id>` instead.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/points/{}/unban": {
    "GET": {
      "descr": "DEPRECATED: Remove an address from the blacklist. Use PATCH `/network/point/<point_id>` instead.",
      "args": [],
      "ret": "Object"
    }
  },
  "/network/points/{}/untrust": {
    "GET": {
      "descr": "DEPRECATED: Remove an address from the whitelist. Use PATCH `/network/point/<point_id>` instead.",
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
  "/private": {
    "props": [
      "injection"
    ]
  },
  "/private/injection": {
    "props": [
      "operation",
      "operations"
    ]
  },
  "/private/injection/operation": {
    "POST": {
      "descr": "Inject an operation in node and broadcast it. Returns the ID of the operation. The `signedOperationContents` should be constructed using contextual RPCs from the latest block and signed by the client. The injection of the operation will apply it on the current mempool context. This context may change at each operation injection or operation reception from peers. By default, the RPC will wait for the operation to be (pre-)validated before returning. However, if ?async is true, the function returns immediately. The optional ?chain parameter can be used to specify whether to inject on the test chain or the main chain.",
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
  "/private/injection/operations": {
    "POST": {
      "descr": "Inject a list of operations in a node. If [force] is [true] then the operations are immediatly injected. The injection will succeed, but it does not mean the operations are (all) valid. In any case, the injection will be quick, hence [async] will be taken into account but should have almost no impact. If [async] is [true], all the promises returned by injecting an operation will be dropped. Each injection is done independently, and does not depend on the other injected operations result. Otherwise ([async]=[force]=[false]), for each operation, we record a list of promises. If all the injections succeed, the result is the list of operation hashes injected, otherwise an error (\"injection_operations_error\") is returned. This error is followed by markers for each operation: \"injection_operation_succeed\" for success and \"injection_operation_error\" for failure (followed by the errors specific to this injection).",
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
      "ret": "Integer"
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
      "ban_operation",
      "filter",
      "monitor_operations",
      "pending_operations",
      "request_operations",
      "unban_all_operations",
      "unban_operation"
    ]
  },
  "/chains/{}/mempool/ban_operation": {
    "POST": {
      "descr": "Remove an operation from the mempool if present, reverting its effect if it was applied. Add it to the set of banned operations to prevent it from being fetched/processed/injected in the future. Note: If the baker has already received the operation, then it's necessary to restart it to flush the operation from it.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/mempool/filter": {
    "GET": {
      "descr": "Get the configuration of the mempool filter. The minimal_fees are in mutez. Each field minimal_nanotez_per_xxx is a rational number given as a numerator and a denominator, e.g. \"minimal_nanotez_per_gas_unit\": [ \"100\", \"1\" ].",
      "args": [
        {
          "name": "include_default",
          "descr": "Show fields equal to their default value (set by default)"
        }
      ],
      "ret": "Object"
    },
    "POST": {
      "descr": "Set the configuration of the mempool filter. **If any of the fields is absent from the input JSON, then it is set to the default value for this field (i.e. its value in the default configuration), even if it previously had a different value.** If the input JSON does not describe a valid configuration, then the configuration is left unchanged. Also return the new configuration (which may differ from the input if it had omitted fields or was invalid). You may call [./octez-client rpc get '/chains/main/mempool/filter?include_default=true'] to see an example of JSON describing a valid configuration.",
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
          "name": "outdated",
          "descr": "Include outdated operations"
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
      "args": [
        {
          "name": "version",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "applied",
          "descr": "Include applied operations (true by default)"
        },
        {
          "name": "refused",
          "descr": "Include refused operations (true by default)"
        },
        {
          "name": "outdated",
          "descr": "Include outdated operations (true by default)"
        },
        {
          "name": "branch_refused",
          "descr": "Include branch refused operations (true by default)"
        },
        {
          "name": "branch_delayed",
          "descr": "Include branch delayed operations (true by default)"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/mempool/request_operations": {
    "POST": {
      "descr": "Request the operations of our peers or a specific peer if specified via a query parameter.",
      "args": [
        {
          "name": "peer_id",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/mempool/unban_all_operations": {
    "POST": {
      "descr": "Clear the set of banned operations.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/mempool/unban_operation": {
    "POST": {
      "descr": "Remove an operation from the set of banned operations (nothing happens if it was not banned).",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}": {
    "GET": {
      "descr": "All the information about a block. The associated metadata may not be present depending on the history mode and block's distance from the head.",
      "args": [
        {
          "name": "force_metadata",
          "descr": "DEPRECATED: Forces to recompute the operations metadata if it was considered as too large."
        },
        {
          "name": "metadata",
          "descr": "Specifies whether or not if the operations metadata should be returned. To get the metadata, even if it is needed to recompute them, use \"always\". To avoid getting the metadata, use \"never\". By default, the metadata will be returned depending on the node's metadata size limit policy."
        }
      ],
      "ret": "Object"
    },
    "props": [
      "context",
      "hash",
      "header",
      "helpers",
      "live_blocks",
      "metadata",
      "metadata_hash",
      "operation_hashes",
      "operation_metadata_hashes",
      "operations",
      "operations_metadata_hash",
      "protocols",
      "votes"
    ]
  },
  "/chains/{}/blocks/{}/context": {
    "props": [
      "big_maps",
      "cache",
      "constants",
      "contracts",
      "dal",
      "delegates",
      "liquidity_baking",
      "merkle_tree",
      "merkle_tree_v2",
      "nonces",
      "raw",
      "sapling",
      "sc_rollup",
      "seed",
      "seed_computation",
      "selected_snapshot",
      "tx_rollup"
    ]
  },
  "/chains/{}/blocks/{}/context/big_maps": {
    "item": {
      "name": "big_map_id",
      "descr": "A big map identifier"
    }
  },
  "/chains/{}/blocks/{}/context/big_maps/{}": {
    "GET": {
      "descr": "Get the (optionally paginated) list of values in a big map. Order of values is unspecified, but is guaranteed to be consistent.",
      "args": [
        {
          "name": "offset",
          "descr": "Skip the first [offset] values. Useful in combination with [length] for pagination."
        },
        {
          "name": "length",
          "descr": "Only retrieve [length] values. Useful in combination with [offset] for pagination."
        }
      ],
      "ret": "Array"
    },
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
    },
    "props": [
      "normalized"
    ]
  },
  "/chains/{}/blocks/{}/context/big_maps/{}/{}/normalized": {
    "POST": {
      "descr": "Access the value associated with a key in a big map, normalize the output using the requested unparsing mode.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/cache": {
    "props": [
      "contracts"
    ]
  },
  "/chains/{}/blocks/{}/context/cache/contracts": {
    "props": [
      "all",
      "rank",
      "size",
      "size_limit"
    ]
  },
  "/chains/{}/blocks/{}/context/cache/contracts/all": {
    "GET": {
      "descr": "Return the list of cached contracts",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/context/cache/contracts/rank": {
    "POST": {
      "descr": "Return the number of cached contracts older than the provided contract",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/cache/contracts/size": {
    "GET": {
      "descr": "Return the size of the contract cache",
      "args": [],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/cache/contracts/size_limit": {
    "GET": {
      "descr": "Return the size limit of the contract cache",
      "args": [],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/constants": {
    "GET": {
      "descr": "All constants",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "errors",
      "parametric"
    ]
  },
  "/chains/{}/blocks/{}/context/constants/errors": {
    "GET": {
      "descr": "Schema for all the RPC errors from this protocol version",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/constants/parametric": {
    "GET": {
      "descr": "Parametric constants",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts": {
    "GET": {
      "descr": "All existing contracts (excluding empty implicit contracts).",
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
      "args": [
        {
          "name": "normalize_types",
          "descr": "Whether types should be normalized (annotations removed, combs flattened) or kept as they appeared in the original script."
        }
      ],
      "ret": "Object"
    },
    "props": [
      "balance",
      "balance_and_frozen_bonds",
      "big_map_get",
      "counter",
      "delegate",
      "entrypoints",
      "frozen_bonds",
      "manager_key",
      "script",
      "single_sapling_get_diff",
      "storage"
    ]
  },
  "/chains/{}/blocks/{}/context/contracts/{}/balance": {
    "GET": {
      "descr": "Access the spendable balance of a contract, excluding frozen bonds.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/balance_and_frozen_bonds": {
    "GET": {
      "descr": "Access the sum of the spendable balance and frozen bonds of a contract. This sum is part of the contract's stake, and it is exactly the contract's stake if the contract is not a delegate.",
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
      "ret": "String"
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
      "args": [
        {
          "name": "normalize_types",
          "descr": "Whether types should be normalized (annotations removed, combs flattened) or kept as they appeared in the original script."
        }
      ],
      "ret": "Object"
    },
    "item": {
      "name": "entrypoint",
      "descr": "A Michelson entrypoint (string of length < 32)"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/entrypoints/{}": {
    "GET": {
      "descr": "Return the type of the given entrypoint of the contract",
      "args": [
        {
          "name": "normalize_types",
          "descr": "Whether types should be normalized (annotations removed, combs flattened) or kept as they appeared in the original script."
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/frozen_bonds": {
    "GET": {
      "descr": "Access the frozen bonds of a contract.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/manager_key": {
    "GET": {
      "descr": "Access the manager of an implicit contract.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/script": {
    "GET": {
      "descr": "Access the code and data of the contract.",
      "args": [],
      "ret": "Object"
    },
    "props": [
      "normalized"
    ]
  },
  "/chains/{}/blocks/{}/context/contracts/{}/script/normalized": {
    "POST": {
      "descr": "Access the script of the contract and normalize it using the requested unparsing mode.",
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
    },
    "props": [
      "normalized",
      "paid_space",
      "used_space"
    ]
  },
  "/chains/{}/blocks/{}/context/contracts/{}/storage/normalized": {
    "POST": {
      "descr": "Access the data of the contract and normalize it using the requested unparsing mode.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/storage/paid_space": {
    "GET": {
      "descr": "Access the paid storage space of the contract.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/contracts/{}/storage/used_space": {
    "GET": {
      "descr": "Access the used storage space of the contract.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/dal": {
    "props": [
      "confirmed_slots_history"
    ]
  },
  "/chains/{}/blocks/{}/context/dal/confirmed_slots_history": {
    "GET": {
      "descr": "Returns the value of the DAL confirmed slots history skip list if DAL is enabled, or [None] otherwise.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates": {
    "GET": {
      "descr": "Lists all registered delegates by default. The arguments `active`, `inactive`, `with_minimal_stake`, and `without_minimal_stake` allow to enumerate only the delegates that are active, inactive, have at least a minimal stake to participate in consensus and in governance, or do not have such a minimal stake, respectively. Note, setting these arguments to false has no effect.",
      "args": [
        {
          "name": "active",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "inactive",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "with_minimal_stake",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "without_minimal_stake",
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
      "consensus_key",
      "current_frozen_deposits",
      "deactivated",
      "delegated_balance",
      "delegated_contracts",
      "frozen_deposits",
      "frozen_deposits_limit",
      "full_balance",
      "grace_period",
      "participation",
      "staking_balance",
      "voting_info",
      "voting_power"
    ]
  },
  "/chains/{}/blocks/{}/context/delegates/{}/consensus_key": {
    "GET": {
      "descr": "The active consensus key for a given delegate and the pending consensus keys.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/current_frozen_deposits": {
    "GET": {
      "descr": "Returns the current amount of the frozen deposits (in mutez).",
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
      "descr": "Returns the sum (in mutez) of all balances of all the contracts that delegate to a given delegate. This excludes the delegate's own balance, its frozen deposits and its frozen bonds.",
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
  "/chains/{}/blocks/{}/context/delegates/{}/frozen_deposits": {
    "GET": {
      "descr": "Returns the initial amount (that is, at the beginning of a cycle) of the frozen deposits (in mutez). This amount is the same as the current amount of the frozen deposits, unless the delegate has been punished.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/frozen_deposits_limit": {
    "GET": {
      "descr": "Returns the frozen deposits limit for the given delegate or none if no limit is set.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/full_balance": {
    "GET": {
      "descr": "Returns the full balance (in mutez) of a given delegate, including the frozen deposits and the frozen bonds. It does not include its delegated balance.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/grace_period": {
    "GET": {
      "descr": "Returns the cycle by the end of which the delegate might be deactivated if she fails to execute any delegate action. A deactivated delegate might be reactivated (without loosing any stake) by simply re-registering as a delegate. For deactivated delegates, this value contains the cycle at which they were deactivated.",
      "args": [],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/participation": {
    "GET": {
      "descr": "Returns cycle and level participation information. In particular this indicates, in the field 'expected_cycle_activity', the number of slots the delegate is expected to have in the cycle based on its active stake. The field 'minimal_cycle_activity' indicates the minimal endorsing slots in the cycle required to get endorsing rewards. It is computed based on 'expected_cycle_activity. The fields 'missed_slots' and 'missed_levels' indicate the number of missed endorsing slots and missed levels (for endorsing) in the cycle so far. 'missed_slots' indicates the number of missed endorsing slots in the cycle so far. The field 'remaining_allowed_missed_slots' indicates the remaining amount of endorsing slots that can be missed in the cycle before forfeiting the rewards. Finally, 'expected_endorsing_rewards' indicates the endorsing rewards that will be distributed at the end of the cycle if activity at that point will be greater than the minimal required; if the activity is already known to be below the required minimum, then the rewards are zero.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/staking_balance": {
    "GET": {
      "descr": "Returns the total amount of tokens (in mutez) delegated to a given delegate. This includes the balances of all the contracts that delegate to it, but also the balance of the delegate itself, its frozen deposits, and its frozen bonds.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/voting_info": {
    "GET": {
      "descr": "Returns the delegate info (e.g. voting power) found in the listings of the current voting period.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/delegates/{}/voting_power": {
    "GET": {
      "descr": "The voting power in the vote listings for a given delegate.",
      "args": [],
      "ret": "String"
    }
  },
  "/chains/{}/blocks/{}/context/liquidity_baking": {
    "props": [
      "cpmm_address"
    ]
  },
  "/chains/{}/blocks/{}/context/liquidity_baking/cpmm_address": {
    "GET": {
      "descr": "Liquidity baking CPMM address",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/merkle_tree": {
    "GET": {
      "descr": "Returns the merkle tree of a piece of context.",
      "args": [
        {
          "name": "holey",
          "descr": "Send only hashes, omit data of key"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/merkle_tree_v2": {
    "GET": {
      "descr": "Returns the Irmin merkle tree of a piece of context.",
      "args": [
        {
          "name": "holey",
          "descr": "Send only hashes, omit data of key"
        }
      ],
      "ret": "Object"
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
  "/chains/{}/blocks/{}/context/sc_rollup": {
    "GET": {
      "descr": "List of all originated smart contract rollups",
      "args": [],
      "ret": "Array"
    },
    "item": {
      "name": "Sc_rollup_hash",
      "descr": "Sc_rollup_hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}": {
    "props": [
      "boot_sector",
      "can_be_cemented",
      "commitment",
      "conflicts",
      "dal_slot_subscriptions",
      "game",
      "genesis_info",
      "inbox",
      "initial_pvm_state_hash",
      "kind",
      "last_cemented_commitment_hash_with_level",
      "staker",
      "timeout",
      "timeout_reached"
    ]
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/boot_sector": {
    "GET": {
      "descr": "Boot sector of smart-contract rollup",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/can_be_cemented": {
    "GET": {
      "descr": "Returns true if and only if the provided commitment can be cemented.",
      "args": [
        {
          "name": "commitment",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Boolean"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/commitment": {
    "item": {
      "name": "commitment_hash",
      "descr": "commitment_hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/commitment/{}": {
    "GET": {
      "descr": "Commitment for a smart contract rollup from its hash",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/conflicts": {
    "GET": {
      "descr": "List of stakers in conflict with the given staker",
      "args": [
        {
          "name": "staker",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/dal_slot_subscriptions": {
    "item": {
      "name": "block_level",
      "descr": "A level integer"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/dal_slot_subscriptions/{}": {
    "GET": {
      "descr": "List of slot indices to which a rollup is subscribed to at a given level",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/game": {
    "GET": {
      "descr": "Ongoing refufation game for a given staker",
      "args": [
        {
          "name": "staker",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/genesis_info": {
    "GET": {
      "descr": "Genesis information (level and commitment hash) for a smart-contract rollup",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/inbox": {
    "GET": {
      "descr": "Inbox for a smart-contract rollup",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/initial_pvm_state_hash": {
    "GET": {
      "descr": "Initial PVM state hash of smart-contract rollup",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/kind": {
    "GET": {
      "descr": "Kind of smart-contract rollup",
      "args": [],
      "ret": "String"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/last_cemented_commitment_hash_with_level": {
    "GET": {
      "descr": "Level and hash of the last cemented commitment for a smart-contract rollup",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/staker": {
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/staker/{}": {
    "props": [
      "staked_on_commitment"
    ]
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/staker/{}/staked_on_commitment": {
    "GET": {
      "descr": "The hash of the commitment on which the operator has staked on for a smart-contract rollup",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/timeout": {
    "GET": {
      "descr": "Returns the timeout of players.",
      "args": [
        {
          "name": "staker1",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "staker2",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/sc_rollup/{}/timeout_reached": {
    "GET": {
      "descr": "Returns whether the timeout creates a result for the game.",
      "args": [
        {
          "name": "staker1",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "staker2",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
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
  "/chains/{}/blocks/{}/context/seed_computation": {
    "GET": {
      "descr": "Seed computation status",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/selected_snapshot": {
    "GET": {
      "descr": "Returns the index of the selected snapshot for the current cycle or for the specific `cycle` passed as argument, if any.",
      "args": [
        {
          "name": "cycle",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/tx_rollup": {
    "item": {
      "name": "tx_rollup_id",
      "descr": "A tx rollup identifier encoded in b58check."
    }
  },
  "/chains/{}/blocks/{}/context/tx_rollup/{}": {
    "props": [
      "commitment",
      "has_bond",
      "inbox",
      "pending_bonded_commitments",
      "state"
    ]
  },
  "/chains/{}/blocks/{}/context/tx_rollup/{}/commitment": {
    "item": {
      "name": "block_level",
      "descr": "A level integer"
    }
  },
  "/chains/{}/blocks/{}/context/tx_rollup/{}/commitment/{}": {
    "GET": {
      "descr": "Return the commitment for a level, if any",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/tx_rollup/{}/has_bond": {
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/tx_rollup/{}/has_bond/{}": {
    "GET": {
      "descr": "Returns true if the public key hash already deposited a bond  for the given rollup",
      "args": [],
      "ret": "Boolean"
    }
  },
  "/chains/{}/blocks/{}/context/tx_rollup/{}/inbox": {
    "item": {
      "name": "block_level",
      "descr": "A level integer"
    }
  },
  "/chains/{}/blocks/{}/context/tx_rollup/{}/inbox/{}": {
    "GET": {
      "descr": "Get the inbox of a transaction rollup",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/context/tx_rollup/{}/pending_bonded_commitments": {
    "item": {
      "name": "pkh",
      "descr": "A Secp256k1 of a Ed25519 public key hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/tx_rollup/{}/pending_bonded_commitments/{}": {
    "GET": {
      "descr": "Get the number of pending bonded commitments for a pkh on a rollup",
      "args": [],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/context/tx_rollup/{}/state": {
    "GET": {
      "descr": "Access the state of a rollup.",
      "args": [],
      "ret": "Object"
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
      "round",
      "scripts",
      "validators"
    ]
  },
  "/chains/{}/blocks/{}/helpers/baking_rights": {
    "GET": {
      "descr": "Retrieves the list of delegates allowed to bake a block.\nBy default, it gives the best baking opportunities (in terms of rounds) for bakers that have at least one opportunity below the 64th round for the next block.\nParameters `level` and `cycle` can be used to specify the (valid) level(s) in the past or future at which the baking rights have to be returned.\nParameter `delegate` can be used to restrict the results to the given delegates. Parameter `consensus_key` can be used to restrict the results to the given consensus_keys. If parameter `all` is set, all the baking opportunities for each baker at each level are returned, instead of just the first one.\nReturns the list of baking opportunities up to round 64. Also returns the minimal timestamps that correspond to these opportunities. The timestamps are omitted for levels in the past, and are only estimates for levels higher that the next block's, based on the hypothesis that all predecessor blocks were baked at the first round.",
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
          "name": "consensus_key",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "max_round",
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
      "descr": "Returns the level of the interrogated block, or the one of a block located `offset` blocks after it in the chain. For instance, the next block if `offset` is 1. The offset cannot be negative.",
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
      "descr": "Retrieves the delegates allowed to endorse a block.\nBy default, it gives the endorsing power for delegates that have at least one endorsing slot for the next block.\nParameters `level` and `cycle` can be used to specify the (valid) level(s) in the past or future at which the endorsing rights have to be returned. Parameter `delegate` can be used to restrict the results to the given delegates.\nParameter `consensus_key` can be used to restrict the results to the given consensus_keys. \nReturns the smallest endorsing slots and the endorsing power. Also returns the minimal timestamp that corresponds to endorsing at the given level. The timestamps are omitted for levels in the past, and are only estimates for levels higher that the next block's, based on the hypothesis that all predecessor blocks were baked at the first round.",
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
          "name": "consensus_key",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/helpers/forge": {
    "props": [
      "operations",
      "protocol_data",
      "tx_rollup"
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
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup": {
    "props": [
      "commitment",
      "inbox",
      "withdraw"
    ]
  },
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup/commitment": {
    "props": [
      "merkle_tree_hash",
      "merkle_tree_path",
      "message_result_hash"
    ]
  },
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup/commitment/merkle_tree_hash": {
    "POST": {
      "descr": "Compute the merkle tree hash of a commitment",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup/commitment/merkle_tree_path": {
    "POST": {
      "descr": "Compute a path of a message result hash in the commitment merkle tree",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup/commitment/message_result_hash": {
    "POST": {
      "descr": "Compute the message result hash",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup/inbox": {
    "props": [
      "merkle_tree_hash",
      "merkle_tree_path",
      "message_hash"
    ]
  },
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup/inbox/merkle_tree_hash": {
    "POST": {
      "descr": "Compute the merkle tree hash of an inbox",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup/inbox/merkle_tree_path": {
    "POST": {
      "descr": "Compute a path of an inbox message in a merkle tree",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup/inbox/message_hash": {
    "POST": {
      "descr": "Compute the hash of a message",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup/withdraw": {
    "props": [
      "withdraw_list_hash"
    ]
  },
  "/chains/{}/blocks/{}/helpers/forge/tx_rollup/withdraw/withdraw_list_hash": {
    "POST": {
      "descr": "Compute the hash of a withdraw list",
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
      "descr": "Simulate the application of the operations with the context of the given block and return the result of each operation application.",
      "args": [],
      "ret": "Array"
    }
  },
  "/chains/{}/blocks/{}/helpers/round": {
    "GET": {
      "descr": "Returns the round of the interrogated block, or the one of a block located `offset` blocks after in the chain (or before when negative). For instance, the next block if `offset` is 1.",
      "args": [],
      "ret": "Integer"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts": {
    "props": [
      "entrypoint",
      "entrypoints",
      "normalize_data",
      "normalize_script",
      "normalize_type",
      "pack_data",
      "run_code",
      "run_operation",
      "run_script_view",
      "run_view",
      "script_size",
      "simulate_operation",
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
  "/chains/{}/blocks/{}/helpers/scripts/normalize_data": {
    "POST": {
      "descr": "Normalizes some data expression using the requested unparsing mode",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/normalize_script": {
    "POST": {
      "descr": "Normalizes a Michelson script using the requested unparsing mode",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/normalize_type": {
    "POST": {
      "descr": "Normalizes some Michelson type by expanding `pair a b c` as `pair a (pair b c)",
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
      "descr": "Run an operation with the context of the given block and without signature checks. Return the operation application result, including the consumed gas. This RPC does not support consensus operations.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/run_script_view": {
    "POST": {
      "descr": "Simulate a call to a michelson view",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/run_view": {
    "POST": {
      "descr": "Simulate a call to a view following the TZIP-4 standard. See https://gitlab.com/tezos/tzip/-/blob/master/proposals/tzip-4/tzip-4.md#view-entrypoints.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/script_size": {
    "POST": {
      "descr": "Compute the size of a script in the current context",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/helpers/scripts/simulate_operation": {
    "POST": {
      "descr": "Simulate running an operation at some future moment (based on the number of blocks given in the `latency` argument), and return the operation application result. The result is the same as run_operation except for the consumed gas, which depends on the contents of the cache at that future moment. This RPC estimates future gas consumption by trying to predict the state of the cache using some heuristics.",
      "args": [
        {
          "name": "successor_level",
          "descr": "If true, the simulation is done on the successor level of the current context."
        }
      ],
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
  "/chains/{}/blocks/{}/helpers/validators": {
    "GET": {
      "descr": "Retrieves the level, the endorsement slots and the public key hash of each delegate allowed to endorse a block.\nBy default, it provides this information for the next level.\nParameter `level` can be used to specify the (valid) level(s) in the past or future at which the endorsement rights have to be returned. Parameter `delegate` can be used to restrict the results results to the given delegates. Parameter `consensus_key` can be used to restrict the results to the given consensus_keys.\n",
      "args": [
        {
          "name": "level",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "delegate",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        },
        {
          "name": "consensus_key",
          "descr": "\u00af\\_(\u30c4)_/\u00af"
        }
      ],
      "ret": "Array"
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
      "args": [
        {
          "name": "force_metadata",
          "descr": "DEPRECATED: Forces to recompute the operations metadata if it was considered as too large."
        },
        {
          "name": "metadata",
          "descr": "Specifies whether or not if the operations metadata should be returned. To get the metadata, even if it is needed to recompute them, use \"always\". To avoid getting the metadata, use \"never\". By default, the metadata will be returned depending on the node's metadata size limit policy."
        }
      ],
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
      "args": [
        {
          "name": "force_metadata",
          "descr": "DEPRECATED: Forces to recompute the operations metadata if it was considered as too large."
        },
        {
          "name": "metadata",
          "descr": "Specifies whether or not if the operations metadata should be returned. To get the metadata, even if it is needed to recompute them, use \"always\". To avoid getting the metadata, use \"never\". By default, the metadata will be returned depending on the node's metadata size limit policy."
        }
      ],
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
      "args": [
        {
          "name": "force_metadata",
          "descr": "DEPRECATED: Forces to recompute the operations metadata if it was considered as too large."
        },
        {
          "name": "metadata",
          "descr": "Specifies whether or not if the operations metadata should be returned. To get the metadata, even if it is needed to recompute them, use \"always\". To avoid getting the metadata, use \"never\". By default, the metadata will be returned depending on the node's metadata size limit policy."
        }
      ],
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
  "/chains/{}/blocks/{}/votes": {
    "props": [
      "ballot_list",
      "ballots",
      "current_period",
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
      "descr": "List of delegates with their voting power.",
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
      "descr": "Returns the voting period (index, kind, starting position) and related information (position, remaining) of the next block.Useful to craft operations that will be valid in the next block.",
      "args": [],
      "ret": "Object"
    }
  },
  "/chains/{}/blocks/{}/votes/total_voting_power": {
    "GET": {
      "descr": "Total voting power in the voting listings.",
      "args": [],
      "ret": "String"
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
      "active_delegate_with_one_roll",
      "big_maps",
      "block_round",
      "commitments",
      "consensus_keys",
      "contracts",
      "cycle",
      "dal",
      "delegates",
      "endorsement_branch",
      "first_level_of_protocol",
      "global_constant",
      "grand_parent_branch",
      "last_snapshot",
      "liquidity_baking_cpmm_address",
      "liquidity_baking_escape_ema",
      "pending_migration_balance_updates",
      "pending_migration_operation_results",
      "ramp_up",
      "sapling",
      "sc_rollup",
      "seed_status",
      "staking_balance",
      "ticket_balance",
      "tx_rollup",
      "vdf_challenge",
      "votes",
      "zk_rollup"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/active_delegate_with_one_roll": {
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
  "/chains/{}/blocks/{}/context/raw/json/active_delegate_with_one_roll/current": {
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
  "/chains/{}/blocks/{}/context/raw/json/active_delegate_with_one_roll/current/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/active_delegate_with_one_roll/snapshot": {
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
  "/chains/{}/blocks/{}/context/raw/json/active_delegate_with_one_roll/snapshot/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/active_delegate_with_one_roll/snapshot/{}/{}": {
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
      "ret": "String"
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
  "/chains/{}/blocks/{}/context/raw/json/block_round": {
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
  "/chains/{}/blocks/{}/context/raw/json/consensus_keys": {
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
  "/chains/{}/blocks/{}/context/raw/json/consensus_keys/{}": {
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
      "ret": "String"
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
      "bond_id_index",
      "code",
      "consensus_key",
      "counter",
      "delegate",
      "delegate_desactivation",
      "delegated",
      "frozen_deposits",
      "frozen_deposits_limit",
      "inactive_delegate",
      "manager",
      "missed_endorsements",
      "paid_bytes",
      "storage",
      "total_frozen_bonds",
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
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/bond_id_index": {
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
      "name": "bond_id",
      "descr": "A bond identifier."
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/bond_id_index/{}": {
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
      "frozen_bonds"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/bond_id_index/{}/frozen_bonds": {
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
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/consensus_key": {
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
      "active",
      "pendings"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/consensus_key/active": {
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
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/consensus_key/pendings": {
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
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/consensus_key/pendings/{}": {
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
      "ret": "String"
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
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/frozen_deposits": {
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
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/frozen_deposits_limit": {
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
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/missed_endorsements": {
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
      "ret": "String"
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
  "/chains/{}/blocks/{}/context/raw/json/contracts/index/{}/total_frozen_bonds": {
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
      "ret": "String"
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
      "delegate_sampler_state",
      "nonces",
      "random_seed",
      "selected_stake_distribution",
      "slashed_deposits",
      "total_active_stake"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/delegate_sampler_state": {
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
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/selected_stake_distribution": {
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
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/slashed_deposits": {
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
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/slashed_deposits/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/slashed_deposits/{}/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/cycle/{}/total_active_stake": {
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
  "/chains/{}/blocks/{}/context/raw/json/dal": {
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
      "level",
      "slots_history"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/dal/level": {
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
  "/chains/{}/blocks/{}/context/raw/json/dal/level/{}": {
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
      "slots"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/dal/level/{}/slots": {
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
  "/chains/{}/blocks/{}/context/raw/json/dal/slots_history": {
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
  "/chains/{}/blocks/{}/context/raw/json/endorsement_branch": {
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
  "/chains/{}/blocks/{}/context/raw/json/first_level_of_protocol": {
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
  "/chains/{}/blocks/{}/context/raw/json/global_constant": {
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
  "/chains/{}/blocks/{}/context/raw/json/global_constant/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/grand_parent_branch": {
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
  "/chains/{}/blocks/{}/context/raw/json/last_snapshot": {
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
  "/chains/{}/blocks/{}/context/raw/json/liquidity_baking_cpmm_address": {
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
  "/chains/{}/blocks/{}/context/raw/json/liquidity_baking_escape_ema": {
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
  "/chains/{}/blocks/{}/context/raw/json/pending_migration_balance_updates": {
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
  "/chains/{}/blocks/{}/context/raw/json/pending_migration_operation_results": {
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
      "rewards"
    ]
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
      "ret": "String"
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
      "ret": "String"
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
      "ret": "String"
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
      "ret": "String"
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
      "ret": "String"
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
      "ret": "String"
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup": {
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
      "index"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index": {
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
      "name": "sc_rollup_address",
      "descr": "A smart contract rollup address."
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}": {
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
      "boot_sector",
      "commitment_added",
      "commitment_stake_count",
      "commitments",
      "dal",
      "game",
      "game_timeout",
      "genesis_info",
      "inbox",
      "kind",
      "last_cemented_commitment",
      "level_index",
      "opponent",
      "parameters_type",
      "staker_count",
      "stakers"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/boot_sector": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/commitment_added": {
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
      "name": "commitment_hash",
      "descr": "commitment_hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/commitment_added/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/commitment_stake_count": {
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
      "name": "commitment_hash",
      "descr": "commitment_hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/commitment_stake_count/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/commitments": {
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
      "name": "commitment_hash",
      "descr": "commitment_hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/commitments/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/dal": {
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
      "level"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/dal/level": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/dal/level/{}": {
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
      "slot_subscriptions"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/dal/level/{}/slot_subscriptions": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/game": {
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
      "name": "game_index",
      "descr": "A pair of stakers that index a smart contract rollup refutation game."
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/game/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/game_timeout": {
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
      "name": "game_index",
      "descr": "A pair of stakers that index a smart contract rollup refutation game."
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/game_timeout/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/genesis_info": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/inbox": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/kind": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/last_cemented_commitment": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/level_index": {
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
      "name": "level_index",
      "descr": "The level index for applied outbox message records"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/level_index/{}": {
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
      "applied_outbox_messages"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/level_index/{}/applied_outbox_messages": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/opponent": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/opponent/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/parameters_type": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/staker_count": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/stakers": {
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
  "/chains/{}/blocks/{}/context/raw/json/sc_rollup/index/{}/stakers/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/seed_status": {
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
  "/chains/{}/blocks/{}/context/raw/json/staking_balance": {
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
  "/chains/{}/blocks/{}/context/raw/json/staking_balance/current": {
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
  "/chains/{}/blocks/{}/context/raw/json/staking_balance/current/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/staking_balance/snapshot": {
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
  "/chains/{}/blocks/{}/context/raw/json/staking_balance/snapshot/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/staking_balance/snapshot/{}/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/ticket_balance": {
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
      "paid_bytes",
      "table",
      "used_bytes"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/ticket_balance/paid_bytes": {
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
  "/chains/{}/blocks/{}/context/raw/json/ticket_balance/table": {
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
  "/chains/{}/blocks/{}/context/raw/json/ticket_balance/table/{}": {
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
  "/chains/{}/blocks/{}/context/raw/json/ticket_balance/used_bytes": {
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
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup": {
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
      "name": "tx_rollup_id",
      "descr": "A tx rollup identifier encoded in b58check."
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup/{}": {
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
      "bond",
      "state",
      "tx_level"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup/{}/bond": {
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
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup/{}/bond/{}": {
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
      "commitment"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup/{}/bond/{}/commitment": {
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
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup/{}/state": {
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
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup/{}/tx_level": {
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
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup/{}/tx_level/{}": {
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
      "commitment",
      "inbox",
      "withdrawals"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup/{}/tx_level/{}/commitment": {
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
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup/{}/tx_level/{}/inbox": {
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
  "/chains/{}/blocks/{}/context/raw/json/tx_rollup/{}/tx_level/{}/withdrawals": {
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
  "/chains/{}/blocks/{}/context/raw/json/vdf_challenge": {
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
      "current_proposal",
      "listings",
      "participation_ema",
      "pred_period_kind",
      "proposals",
      "proposals_count",
      "voting_power_in_listings"
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
      "ret": "String"
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
  },
  "/chains/{}/blocks/{}/context/raw/json/votes/voting_power_in_listings": {
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
  "/chains/{}/blocks/{}/context/raw/json/zk_rollup": {
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
      "name": "Zk_rollup_hash",
      "descr": "Zk_rollup_hash (Base58Check-encoded)"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/zk_rollup/{}": {
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
      "account",
      "pending_list",
      "pending_operations"
    ]
  },
  "/chains/{}/blocks/{}/context/raw/json/zk_rollup/{}/account": {
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
  "/chains/{}/blocks/{}/context/raw/json/zk_rollup/{}/pending_list": {
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
  "/chains/{}/blocks/{}/context/raw/json/zk_rollup/{}/pending_operations": {
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
      "name": "zkru_pending_op_position",
      "descr": "The position of an operation in a pending operations list"
    }
  },
  "/chains/{}/blocks/{}/context/raw/json/zk_rollup/{}/pending_operations/{}": {
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
  }
}
