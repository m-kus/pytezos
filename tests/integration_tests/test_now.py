from unittest import TestCase

from pytezos import ContractInterface, pytezos

code = """
parameter unit;
storage timestamp;
code { DROP ;
       NOW ;
       NIL operation ;
       PAIR }
"""


class TestNow(TestCase):

    def test_now(self):
        contract = ContractInterface.from_michelson(code).using('mainnet')
        now = pytezos.using('mainnet').now()
        res = contract.default().run_code()
        self.assertEqual(now, res.storage)
