from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos import ContractInterface

code = """
{ parameter string ;
  storage (big_map string nat) ;
  code { UNPAIR ;
         SWAP ;
         PUSH nat 1 ;
         SOME ;
         DIG 2 ;
         UPDATE ;
         NIL operation ;
         PAIR } }
"""


class TestRunCode(SandboxedNodeTestCase):

    def test_lazy_storage_diff(self):
        contract = ContractInterface.from_michelson(code).using(shell=self.client.shell)
        res = contract.using('mainnet').default('hello').run_code()
        self.assertEqual({'hello': 1}, res.storage)
        self.assertEqual(1, len(res.lazy_diff))
        res1 = contract.default('hello').interpret()
        self.assertEqual({'hello': 1}, res1.storage)
