from unittest import TestCase
from glob import glob
from os.path import dirname, join
from parameterized import parameterized

from pytezos.contract.interface import ContractInterface


class ParsingTestCase(TestCase):

    @parameterized.expand([
        (path,) for path in glob(join(dirname(__file__), 'mini_scenarios', '*.tz'))
    ])
    def test_mini_scenarios(self, path):
        ci = ContractInterface.from_file(path)
        ci.script()

    @parameterized.expand([
        (path,) for path in glob(join(dirname(__file__), 'attic', '*.tz'))
    ])
    def test_attic(self, path):
        ci = ContractInterface.from_file(path)
        ci.script()

    @parameterized.expand([
        (path,) for path in glob(join(dirname(__file__), 'entrypoints', '*.tz'))
    ])
    def test_entrypoints(self, path):
        ci = ContractInterface.from_file(path)
        ci.script()
