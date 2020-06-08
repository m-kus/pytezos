from unittest import TestCase

from pytezos import ContractInterface

code = """
parameter (pair nat (contract (pair (nat (big_map string string)))));
storage (big_map string string);
code {
    DUP ; DUP ; CAR ; 
    PUSH mutez 0 ; DIG 2 ; DUP ; CAAR ; DIP { CDR } ; PAIR ; DIP 2 { CDR } ;
    TRANSFER_TOKENS ; 
    NIL operation ; SWAP ; CONS ;
    DIP { CDR } ; PAIR
}
"""


class TestTrasferTokens(TestCase):

    def test_transfer_tokens(self):
        ci = ContractInterface.create_from(code)
        res = ci.call(0, 'KT1SmF5SCC5DrzkSm28HP9ovWVqcA5cmqZ1q').interpret(storage={"haha": "nice"})
        self.assertEqual(1, len(res.operations))
