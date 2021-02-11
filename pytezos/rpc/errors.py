from pytezos.rpc.node import RpcError


class MichelsonBadContractParameter(RpcError, error_id='michelson_v1.bad_contract_parameter'):
    """ Either no parameter was supplied to a contract with a non-unit parameter type, a non-unit parameter was passed
    to an account, or a parameter was supplied of the wrong type
    """


class MichelsonBadReturn(RpcError, error_id='michelson_v1.bad_return'):
    """ Unexpected stack at the end of a lambda or script
    """


class MichelsonError(RpcError, error_id='michelson_v1'):
    """ Catch all michelson_v1 errors
    """


class TezArithmeticError(RpcError, error_id='tez'):
    """ Catch all tez errors
    """


class MichelsonScriptRejected(RpcError, error_id='script_rejected'):
    """ A FAILWITH instruction was reached
    """
