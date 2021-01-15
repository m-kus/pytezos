from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestoozxt5(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_oozxt5(self):    
        section = get_data(
            path='big_map_diff/oozxt5CvNMmUtutgC48aVq8W1e6jzzQtjjz6n9iLc1YSyXod7tN/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/oozxt5CvNMmUtutgC48aVq8W1e6jzzQtjjz6n9iLc1YSyXod7tN/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
