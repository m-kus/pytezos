from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestopZNW1(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_opZNW1(self):    
        section = get_data(
            path='big_map_diff/opZNW17HfCduY3xoaGb5h19fPhH1Nyg5nV7dta1XYkfocQm254E/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/opZNW17HfCduY3xoaGb5h19fPhH1Nyg5nV7dta1XYkfocQm254E/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
