from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestoowFNb(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_oowFNb(self):    
        section = get_data(
            path='big_map_diff/oowFNbN3VZprtALmezJQVpZ2Ves8ge4GFZLDvMAJVbui7t4dNtw/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/oowFNbN3VZprtALmezJQVpZ2Ves8ge4GFZLDvMAJVbui7t4dNtw/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
