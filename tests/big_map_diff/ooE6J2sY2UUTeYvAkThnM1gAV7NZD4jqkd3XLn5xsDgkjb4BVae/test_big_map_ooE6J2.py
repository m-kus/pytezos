from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestooE6J2(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_ooE6J2(self):    
        section = get_data(
            path='big_map_diff/ooE6J2sY2UUTeYvAkThnM1gAV7NZD4jqkd3XLn5xsDgkjb4BVae/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/ooE6J2sY2UUTeYvAkThnM1gAV7NZD4jqkd3XLn5xsDgkjb4BVae/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
