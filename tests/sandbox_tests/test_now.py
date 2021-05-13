from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos import ContractInterface

code = """
parameter unit;
storage timestamp;
code { DROP ;
       NOW ;
       NIL operation ;
       PAIR }
"""


class TestNow(SandboxedNodeTestCase):

    def test_now(self):
        contract = ContractInterface.from_michelson(code).using(shell=self.client.shell)
        now = self.client.now()
        res = contract.default().run_code()
        self.assertEqual(now, res.storage)
