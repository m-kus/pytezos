from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestooLbRA(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_ooLbRA(self):    
        section = get_data(
            path='big_map_diff/ooLbRA1Yho5YP8kVay7qZCxSE9ZR7sntpKeLs6bspYcvJccjjyg/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/ooLbRA1Yho5YP8kVay7qZCxSE9ZR7sntpKeLs6bspYcvJccjjyg/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
