from os.path import dirname, join
from unittest import TestCase

from pytezos import pytezos, ContractInterface


class TestBuiltin(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ci = ContractInterface.create_from(join(dirname(__file__), 'test.tz'))
        cls.maxDiff = None

    def test_call_option_none(self):
        res = self.ci.callAnotherContract(None).interpret(storage=None)
        self.assertEqual(0, res.operations)
