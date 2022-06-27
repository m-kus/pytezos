from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface

code = """
parameter (big_map nat nat);
storage (big_map nat nat);
code { CAR ; NIL operation ; PAIR }
"""
bob = "tz1iBobBobBobBobBobBobBobBobBodTWLCX"


class BigMapArgTest(TestCase):
    def test_pass_big_map_diff(self):
        ci = ContractInterface.from_michelson(code)
        res = ci.call({2: 2}).interpret(storage={1: 1})
        self.assertEqual({2: 2}, res.storage)

    def test_pass_big_map_ptr(self):
        ci = ContractInterface.from_michelson(code)
        res = ci.call(123).interpret(storage={1: 1})  # FIXME: this should fail with something like "Big_map not found"
        self.assertEqual({}, res.storage)

    def test_big_map_composite_key(self):
        ct = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'big_map_composite_key.tz'))
        res = ct.default(bob).interpret()
        print(res.storage)
