from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestonfQ12(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_onfQ12(self):    
        section = get_data(
            path='big_map_diff/onfQ12Pm1ck55hsVzC9egZ5KpMoC5EaKr4nx1c4SCQhtgs7nB3X/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/onfQ12Pm1ck55hsVzC9egZ5KpMoC5EaKr4nx1c4SCQhtgs7nB3X/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
