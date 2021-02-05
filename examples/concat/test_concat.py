from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface


class ConcatContractTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.concat = ContractInterface.create_from(join(dirname(__file__), 'concat.tz'))
        cls.maxDiff = None

    def test_concat(self):
        res = self.concat.call('bar').result(storage='foo')
        self.assertEqual('foobar', res.context)
