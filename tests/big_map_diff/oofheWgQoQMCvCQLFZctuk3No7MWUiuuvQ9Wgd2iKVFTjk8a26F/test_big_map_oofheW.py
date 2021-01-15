from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestoofheW(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_oofheW(self):    
        section = get_data(
            path='big_map_diff/oofheWgQoQMCvCQLFZctuk3No7MWUiuuvQ9Wgd2iKVFTjk8a26F/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/oofheWgQoQMCvCQLFZctuk3No7MWUiuuvQ9Wgd2iKVFTjk8a26F/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
