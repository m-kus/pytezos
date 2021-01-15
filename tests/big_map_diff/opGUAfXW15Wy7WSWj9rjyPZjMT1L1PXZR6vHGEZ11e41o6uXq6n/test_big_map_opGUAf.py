from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestopGUAf(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_opGUAf(self):    
        section = get_data(
            path='big_map_diff/opGUAfXW15Wy7WSWj9rjyPZjMT1L1PXZR6vHGEZ11e41o6uXq6n/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/opGUAfXW15Wy7WSWj9rjyPZjMT1L1PXZR6vHGEZ11e41o6uXq6n/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
