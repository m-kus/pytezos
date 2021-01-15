from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestopEg5T(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_opEg5T(self):    
        section = get_data(
            path='big_map_diff/opEg5TTBjcRcGHsqBPGBF2tqUPSTk79yzjBffMAwUr11YTV7kdr/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/opEg5TTBjcRcGHsqBPGBF2tqUPSTk79yzjBffMAwUr11YTV7kdr/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
