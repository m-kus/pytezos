from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestopEGe5(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_opEGe5(self):    
        section = get_data(
            path='big_map_diff/opEGe5SfgxRJpEuSUocQ3tz7snA5f6LZ3HU4sZP8gbudAozVL4g/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/opEGe5SfgxRJpEuSUocQ3tz7snA5f6LZ3HU4sZP8gbudAozVL4g/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
