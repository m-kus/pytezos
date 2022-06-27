from unittest import TestCase

from pytezos import ContractInterface

bob = "tz1iBobBobBobBobBobBobBobBobBodTWLCX"
code = """
{ parameter address ;
  storage nat ;
  code { LAMBDA (pair (option nat) nat) nat { UNPAIR ; IF_NONE {} { SWAP ; DROP } } ;
         PUSH address "tz1iA1iceA1iceA1iceA1iceA1ice9ydjsaW" ;
         DIG 2 ;
         CAR ;
         EMPTY_BIG_MAP address nat ;
         PUSH nat 7 ;
         DUP 4 ;
         SWAP ;
         SOME ;
         SWAP ;
         UPDATE ;
         PUSH nat 0 ;
         SWAP ;
         DUP ;
         DUG 2 ;
         DIG 3 ;
         GET ;
         PAIR ;
         DUP 4 ;
         SWAP ;
         EXEC ;
         PUSH nat 0 ;
         DIG 2 ;
         DIG 3 ;
         GET ;
         PAIR ;
         DIG 2 ;
         SWAP ;
         EXEC ;
         ADD ;
         NIL operation ;
         PAIR } }
"""


class LambdaExecTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.ct = ContractInterface.from_michelson(code)

    def test_simplest(self):
        res = self.ct.default(bob).interpret()

        print(res.storage)
