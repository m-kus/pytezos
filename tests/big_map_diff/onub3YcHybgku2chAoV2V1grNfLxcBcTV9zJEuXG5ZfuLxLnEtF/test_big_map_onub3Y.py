from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestonub3Y(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_onub3Y(self):    
        section = get_data(
            path='big_map_diff/onub3YcHybgku2chAoV2V1grNfLxcBcTV9zJEuXG5ZfuLxLnEtF/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/onub3YcHybgku2chAoV2V1grNfLxcBcTV9zJEuXG5ZfuLxLnEtF/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
