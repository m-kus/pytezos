from unittest import TestCase

from pytezos import ContractInterface

code = """
parameter int;
storage int;
code { CAR;
       NIL operation;
       PAIR }
"""


class RepeaterContractTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ci = ContractInterface.create_from(code)

    def test_increment(self):
        result = self.ci.call(3).result(storage=0)
        self.assertEqual(3, result.context)
