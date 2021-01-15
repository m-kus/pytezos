from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestoow48d(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_oow48d(self):    
        section = get_data(
            path='big_map_diff/oow48divDE1w3e126PU9iAD3bckV9F34D5yuNk9wKVx9sCBxSkU/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/oow48divDE1w3e126PU9iAD3bckV9F34D5yuNk9wKVx9sCBxSkU/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
