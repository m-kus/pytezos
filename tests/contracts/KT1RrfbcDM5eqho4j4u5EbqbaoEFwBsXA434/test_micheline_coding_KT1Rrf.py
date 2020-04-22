from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Rrf(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/code_KT1Rrf.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Rrf(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/storage_KT1Rrf.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opV3vx(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_opV3vx.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oojLES(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oojLES.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onk3tb(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onk3tb.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oorRMp(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oorRMp.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onh2C5(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onh2C5.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
