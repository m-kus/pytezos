from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestoparn9(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_oparn9(self):    
        section = get_data(
            path='big_map_diff/oparn99Xxxz8oBv5GssTcmERpm1Y7kr5sqsfDWNUD9dY5i8NGTX/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/oparn99Xxxz8oBv5GssTcmERpm1Y7kr5sqsfDWNUD9dY5i8NGTX/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
