from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface


class CompareEnumContractTest(TestCase):
    def test_compare_enum(self):
        contract = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'compare_enum.tz'))
        contract.call().interpret()
