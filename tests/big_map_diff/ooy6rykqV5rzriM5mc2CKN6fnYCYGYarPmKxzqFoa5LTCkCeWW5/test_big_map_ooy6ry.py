from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestooy6ry(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_ooy6ry(self):    
        section = get_data(
            path='big_map_diff/ooy6rykqV5rzriM5mc2CKN6fnYCYGYarPmKxzqFoa5LTCkCeWW5/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/ooy6rykqV5rzriM5mc2CKN6fnYCYGYarPmKxzqFoa5LTCkCeWW5/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
