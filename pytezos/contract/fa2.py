from functools import lru_cache

from pytezos.contract.script import ContractScript, ContractParameter
from pytezos.michelson.micheline import michelson_to_micheline

transfer_tz = """
(list %transfer
  (pair
    (address %from_)
    (list %txs
      (pair
        (address %to_)
        (pair
          (nat %token_id)
          (nat %amount)
        )
      )
    )
  )
)
"""

balance_of_tz = """
(pair %balance_of
  (list %requests
    (pair
      (address %owner)
      (nat %token_id)
    )
  )
  (contract %callback
    (list
      (pair
        (pair %request
          (address %owner)
          (nat %token_id)
        )
        (nat %balance)
      )
    )
  )
)
"""

update_operators_tz = """
(list %update_operators
  (or
    (pair %add_operator
      (address %owner)
      (address %operator)
    )
    (pair %remove_operator
      (address %owner)
      (address %operator)
    )
  )
)
"""

token_metadata_registry = """
(contract %token_metadata_registry address)
"""

parameter_tz = f'or (or {transfer_tz} {balance_of_tz}) (or {update_operators_tz} {token_metadata_registry})'


class FA2TokenImpl(ContractScript):

    @property
    @lru_cache(maxsize=None)
    def parameter(self) -> ContractParameter:
        return ContractParameter(michelson_to_micheline(parameter_tz))

    @classmethod
    def interface(cls):
        return cls(code=[{'prim': 'parameter',
                          'args': [michelson_to_micheline(parameter_tz)]}])
