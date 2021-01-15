from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestoourtP(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_oourtP(self):    
        section = get_data(
            path='big_map_diff/oourtPVx6v95weX6y3LxjJonVbez8Um4W32wVSuQ9yp5ns5hoLL/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/oourtPVx6v95weX6y3LxjJonVbez8Um4W32wVSuQ9yp5ns5hoLL/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
