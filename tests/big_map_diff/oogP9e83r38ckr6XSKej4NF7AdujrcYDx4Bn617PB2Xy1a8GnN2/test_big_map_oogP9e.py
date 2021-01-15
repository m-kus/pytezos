from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestoogP9e(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_oogP9e(self):    
        section = get_data(
            path='big_map_diff/oogP9e83r38ckr6XSKej4NF7AdujrcYDx4Bn617PB2Xy1a8GnN2/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/oogP9e83r38ckr6XSKej4NF7AdujrcYDx4Bn617PB2Xy1a8GnN2/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
