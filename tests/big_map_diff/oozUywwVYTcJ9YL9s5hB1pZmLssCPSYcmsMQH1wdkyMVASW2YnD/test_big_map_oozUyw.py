from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestoozUyw(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_oozUyw(self):    
        section = get_data(
            path='big_map_diff/oozUywwVYTcJ9YL9s5hB1pZmLssCPSYcmsMQH1wdkyMVASW2YnD/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/oozUywwVYTcJ9YL9s5hB1pZmLssCPSYcmsMQH1wdkyMVASW2YnD/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
