from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestopagwv(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_opagwv(self):    
        section = get_data(
            path='big_map_diff/opagwvR2FiTM2Tpd8DQqv6xL2qiyKvX7GfFUt96VgepUsAL2TmS/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/opagwvR2FiTM2Tpd8DQqv6xL2qiyKvX7GfFUt96VgepUsAL2TmS/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
