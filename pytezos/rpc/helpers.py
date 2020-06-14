from pytezos.rpc.query import RpcQuery


class BakingRightsQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/baking_rights'):

    def __call__(self, level=None, cycle=None, delegate=None, max_priority=None, _all=None):
        """ Retrieves the list of delegates allowed to bake a block.
        By default, it gives the best baking priorities for bakers that have at least one opportunity
        below the 64th priority for the next block.

        :param level: Specify the (valid) level in the past or future at which the baking rights have to be returned.
        :param cycle: Specify the (valid) levels in the past or future at which the baking rights have to be returned.
        :param delegate: Restrict the results to the given delegates.
        :param max_priority:
        :param _all: If parameter `all` is set, all the baking opportunities for each baker at each level are returned,\
         instead of just the first one.
        :returns: Returns the list of baking slots. Also returns the minimal timestamps that correspond to these slots.\
         The timestamps are omitted for levels in the past, and are only estimates for levels later that the next block,\
         based on the hypothesis that all predecessor blocks were baked at the first priority.
        """
        return self._get(params={
            'level': level,
            'cycle': cycle,
            'delegate': delegate,
            'max_priority': max_priority,
            'all': _all
        })


class ForgeOperationsQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/forge/operations'):

    def post(self, operation):
        """ Get raw bytes encoding of an unsigned operation

        :param operation: Json input
            {
                "branch": <block hash>,
                "contents": [{ <operation_content> }]
            }
        :returns: Hex string
        """
        return self._post(json=operation)


class ForgeProtocolDataQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/forge/protocol_data'):

    def post(self, protocol_data):
        """ Forge the protocol-specific part of a block header.

        :param protocol_data: Json input
            {
                "priority": <integer>,
                "nonce_hash": <Base58 nonce hash>,  // optional
                "proof_of_work_nonce": <hex encoded>  // optional
            }
        :returns: { "protocol_data": <hex encoded> }
        """
        return self._post(json=protocol_data)


class ForgeBlockHeaderQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/forge_block_header'):

    def post(self, block_header):
        """ Forge block header.

        :param block_header: Json input
            {
                "level": <integer>,
                "proto": <integer>,
                "predecessor": <block hash>,
                "timestamp": <timestamp>,
                "validation_pass": <integer>,
                "operations_hash": <Operation_list_list_hash>,
                "fitness": <integer (hex)>,
                "context": <Context_hash>,
                "protocol_data": <hex encoded>
            }
        :returns: { "block": <hex encoded> }
        """
        return self._post(json=block_header)


class ParseBlockQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/parse/block'):

    def post(self, block_header):
        """ Retrieves protocol-specific part of a block header and signature.

        :param block_header: Json input
            {
                "level": <integer>,
                "proto": <integer>,
                "predecessor": <block hash>,
                "timestamp": <timestamp>,
                "validation_pass": <integer>,
                "operations_hash": <Operation_list_list_hash>,
                "fitness": <integer (hex)>,
                "context": <Context_hash>,
                "protocol_data": <hex encoded>
            }
        :returns: Json object
        """
        return self._post(json=block_header)


class ParseOperationsQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/parse/operations'):

    def post(self, operations):
        """ Extracts contents and signatures from the forged and optionally signed operations (bulk).

        :param operations: Json input
            {
                "operations": [ {
                    "branch": <block_hash>,
                    "data": <hex encoded>
                } ... ],
                "check_signature": <boolean>  // optional
            }
        :returns: Json object
        """
        return self._post(json=operations)


class PreapplyBlockQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/preapply/block'):

    def post(self, block, sort=None, timestamp=None):
        """ Simulate the validation of a block that would contain the given operations
        and return the resulting fitness and context hash.

        :param block: Json input
            {
                "protocol_data": {
                    "protocol": "Pt24m4xiPbLDhVgVfABUjirbmda3yohdN82Sp9FeuAXJ4eV9otd",
                    "priority": <integer>,
                    "proof_of_work_nonce": <hex encoded>
                    "seed_nonce_hash": <Base58 encoded>,  // optional
                    "signature": <Base58 encoded>
                },
                "operations": [ [ {
                    "protocol": "Pt24m4xiPbLDhVgVfABUjirbmda3yohdN82Sp9FeuAXJ4eV9otd",
                    "branch": <block_hash>,
                    "contents": [ {} ... ],  // kind-specific
                    "signature": <Base58 encoded>
                }... ] ... ]
            }
        :param sort: by what?
        :param timestamp: timestamp
        :returns: Json object
        """
        return self._post(
            json=block,
            params=dict(sort=sort, timestamp=timestamp)
        )


class PreapplyOperationsQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/preapply/operations'):

    def post(self, operations):
        """ Simulate the validation of operation(s).

        :param operations: Json input
            [{
                "protocol": "Pt24m4xiPbLDhVgVfABUjirbmda3yohdN82Sp9FeuAXJ4eV9otd",
                "branch": <block_hash>,
                "contents": [ {} ... ],  // kind-specific
                "signature": <Base58 encoded>
            }]
        :returns: Json array (operations with metadata)
        """
        return self._post(json=operations)


class ScriptsEntrypoint(RpcQuery, path='/chains/{}/blocks/{}/helpers/scripts/entrypoint'):

    def post(self, script, entrypoint=None):
        """ Return the type of the given entrypoint.

        :param script: Micheline expression
        :param entrypoint: Name of the entrypoint (leave None if there's only one)
        """
        payload = {'script': script}
        if entrypoint:
            payload['entrypoint'] = entrypoint

        return self._post(payload)


class ScriptsEntrypoints(RpcQuery, path='/chains/{}/blocks/{}/helpers/scripts/entrypoints'):

    def post(self, script):
        """ Return the list of entrypoints of the given script.

        :param script: Micheline expression
        """
        return self._post({'script': script})


class ScriptsPackDataQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/scripts/pack_data'):

    def post(self, expression):
        """ Computes the serialized version of some data expression using the same algorithm as script instruction PACK.

        :param expression: Json input
            {
                "data": <michelson expression>,
                "type": <michelson expression>,
                "gas": <bignum>  // optional
            }
        :returns: Packed data (hex encoded)
        """
        return self._post(json=expression)


class ScriptsRunCodeQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/scripts/run_code'):

    def post(self, invocation):
        """ Run a piece of code in the current context.

        :param invocation: Json input
            {
                "script": <michelson expression>,
                "storage": <michelson expression>,
                "input": <michelson expression>,
                "amount": <mutez>,
                "source": <account address>,  // optional
                "payer": <account address>,  // optional
                "gas": <bignum>  // optional
            }
        :returns: Resulting storage, spawned operations, and bigmap diff
        """
        return self._post(json=invocation)


class ScriptsRunOperationQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/scripts/run_operation'):

    def post(self, operation):
        """ Run an operation without signature checks.

        :param operation: Json input
            {
                "branch": <block_hash>,
                "contents": [ {} ... ],  // kind-specific
                "signature": <Base58 encoded>
            }
        :returns: Json object (operation with metadata)
        """
        return self._post(json=operation)


class ScriptsTraceCodeQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/scripts/trace_code'):

    def post(self, invocation):
        """ Run a piece of code in the current context, keeping a trace.

        :param invocation: Json input
            {
                "script": <michelson expression>,
                "storage": <michelson expression>,
                "input": <michelson expression>,
                "amount": <mutez>,
                "source": <account address>,  // optional
                "payer": <account address>,  // optional
                "gas": <bignum>  // optional
            }
        :returns: Resulting storage, spawned operations, bigmap diff, and trace
        """
        return self._post(json=invocation)


class ScriptsTypecheckCodeQuery(RpcQuery, path='/chains/{}/blocks/{}/helpers/scripts/typecheck_code'):

    def post(self, expression):
        """ Check that some data expression is well formed and of a given type in the current context.

        :param expression: Json input
            {
                "data": <michelson expression>,
                "type": <michelson expression>,
                "gas": <bignum>  // optional
            }
        :returns: Json object
        """
        return self._post(json=expression)
