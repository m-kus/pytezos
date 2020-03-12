from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1HRu(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/code_KT1HRu.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1HRu(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/storage_KT1HRu.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opKGaY(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_opKGaY.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onkLH1(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_onkLH1.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooPA3v(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooPA3v.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooihn1(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooihn1.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
