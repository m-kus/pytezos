from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestopRZd1(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_opRZd1(self):    
        section = get_data(
            path='big_map_diff/opRZd1X7uq8aCeR1A6BZLBi8HGKrXPmcgURxBn23jF2W35seRYX/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/opRZd1X7uq8aCeR1A6BZLBi8HGKrXPmcgURxBn23jF2W35seRYX/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
