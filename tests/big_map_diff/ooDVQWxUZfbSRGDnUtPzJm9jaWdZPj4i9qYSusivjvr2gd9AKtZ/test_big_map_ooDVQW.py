from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestooDVQW(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_ooDVQW(self):    
        section = get_data(
            path='big_map_diff/ooDVQWxUZfbSRGDnUtPzJm9jaWdZPj4i9qYSusivjvr2gd9AKtZ/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/ooDVQWxUZfbSRGDnUtPzJm9jaWdZPj4i9qYSusivjvr2gd9AKtZ/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
