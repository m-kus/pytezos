from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestopEh62(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_opEh62(self):    
        section = get_data(
            path='big_map_diff/opEh622NZ8Kg86rias2t8Kocb9kNrV3f6WYB7V3o11qx5iKJRN5/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/opEh622NZ8Kg86rias2t8Kocb9kNrV3f6WYB7V3o11qx5iKJRN5/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
