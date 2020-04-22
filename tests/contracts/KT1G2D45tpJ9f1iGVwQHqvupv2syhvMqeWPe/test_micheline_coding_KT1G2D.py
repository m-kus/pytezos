from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1G2D(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/code_KT1G2D.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1G2D(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/storage_KT1G2D.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onydWh(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onydWh.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opZNW1(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_opZNW1.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
