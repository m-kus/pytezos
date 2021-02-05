from unittest import TestCase

from pytezos import ContractInterface

code = """
parameter bytes;
storage (pair :storage (big_map bytes timestamp) nat);
code { DUP ;
       DIP { CDR @storage_slash_1 } ;
       CAR @hash_slash_2 ;
       PUSH nat 1 ;
       { DIP { { DIP { DUP @storage } ; SWAP } } ; SWAP } ;
       CDR %counter ;
       ADD @counter ;
       { DIP { { DIP { DUP @storage } ; SWAP } } ; SWAP } ;
       CAR %records ;
       NOW ;
       { DIP { { DIP { { DIP { DUP @hash } ; SWAP } } ; SWAP } } ; SWAP } ;
       DIP { SOME } ;
       DIP { DIP { DIP { DIP { DROP ; DROP } } } } ;
       UPDATE @records ;
       PAIR %records %counter ;
       NIL operation ;
       PAIR }
"""


class CounterContractTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ci = ContractInterface.create_from(code)

    def test_increment(self):
        res = self.ci.call('deadbeef').result(storage=[{}, 0])
        self.assertEqual(1, res.context[1])
        self.assertIn('deadbeef', res.big_map_diff)
