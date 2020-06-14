from functools import lru_cache

from pytezos.michelson.contract import Contract, ContractParameter, ContractStorage
from pytezos.michelson.micheline import michelson_to_micheline

parameter_tz = """
parameter 
    (or (or (nat %burn :token_id) (pair %mint (address %owner) (nat %token_id)))
        (pair %transfer (address %destination) (nat %token_id)))
"""
storage_tz = "storage (map nat address)"


class NonFungibleTokenImpl(Contract):
    """ This is an example of how to force contract interface (in case it's not annotated)
    """

    @property
    @lru_cache(maxsize=None)
    def parameter(self) -> ContractParameter:
        return ContractParameter(michelson_to_micheline(parameter_tz))

    @property
    @lru_cache(maxsize=None)
    def storage(self) -> ContractStorage:
        return ContractStorage(michelson_to_micheline(storage_tz))
