from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface


class TestBuiltin(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ci = ContractInterface.create_from(join(dirname(__file__), 'test.tz'))
        cls.maxDiff = None

    def test_call_option_none(self):
        res = self.ci.callAnotherContract(None).interpret(storage=None)
        self.assertEqual(0, len(res.operations))

    def test_call_option_some(self):
        res = self.ci.callAnotherContract('KT1VG2WtYdSWz5E7chTeAdDPZNy2MpP8pTfL').interpret(storage=None)
        print(self.ci.script.parameter)
        self.assertEqual(1, len(res.operations))
