from unittest import TestCase

from tests import get_data
from pytezos.contract.script import ContractStorage


class BigMapCodingTestooTXhd(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_ooTXhd(self):    
        section = get_data(
            path='big_map_diff/ooTXhdhf4edpJ2ro3qhsPo6DkU79fM36Ykdx2Swf9yyPgqvCRFE/storage_section.json')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='big_map_diff/ooTXhdhf4edpJ2ro3qhsPo6DkU79fM36Ykdx2Swf9yyPgqvCRFE/big_map_diff.json')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
