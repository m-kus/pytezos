from functools import lru_cache

from pytezos.michelson.contract import Contract, ContractParameter
from pytezos.michelson.micheline import michelson_to_micheline

transfer_tz = """
(list %transfer 
  (pair 
    (nat %amount) 
    (address %tr_to)
  )
)
"""

transfer_from_tz = """
(list %transferFrom 
  (pair 
    (pair 
      (nat %amount) 
      (address %tr_from)
    )
    (address %tr_to)
  )
)
"""

mint_tz = """
(pair %mint 
  (nat %amount) 
  (address %tr_to)
)
"""

burn_tz = """
(pair %burn 
  (nat %amount) 
  (address %tr_to)
)
"""

set_allow_transfer_from_tz = """
(pair %setAllowTransferFrom
  (pair 
    (address %authority) 
    (nat %prev_amount)
  )
  (pair 
    (bool %remove)
    (pair %transfer_from_info 
      (nat %amount) 
      (address %transfer_for)
    )
  )
)
"""

token_parameter_tz = f'''
or 
  (or 
    {transfer_tz} 
    (or 
      {set_allow_transfer_from_tz} 
      {transfer_from_tz}
    )
  ) 
  (or 
    {mint_tz} 
    {burn_tz}
  )
'''


class NYXTokenImpl(Contract):

    @property
    @lru_cache(maxsize=None)
    def parameter(self) -> ContractParameter:
        return ContractParameter(michelson_to_micheline(token_parameter_tz))

    @classmethod
    def interface(cls):
        return cls(code=[{'prim': 'parameter',
                          'args': [michelson_to_micheline(token_parameter_tz)]}])
