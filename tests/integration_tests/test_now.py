from unittest import TestCase

from pytezos import ContractInterface, pytezos
from parameterized import parameterized

code = """
parameter unit;
storage timestamp;
code { DROP ;
       NOW ;
       NIL operation ;
       PAIR }
"""


class TestNow(TestCase):

    @parameterized.expand([
        ('mainnet',),
        ('edo2net',),
        ('delphinet',),
    ])
    def test_now(self, network):
        contract = ContractInterface.from_michelson(code).using(network)
        now = pytezos.using(network).now()
        res = contract.default().run_code()
        self.assertEqual(now, res.storage)
