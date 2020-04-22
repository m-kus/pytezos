from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Lb2(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1Lb2v9xrF9994tEZYogrX3og9UHgtRdZBg/code_KT1Lb2.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Lb2(self):
        expected = get_data(
            path='contracts/KT1Lb2v9xrF9994tEZYogrX3og9UHgtRdZBg/storage_KT1Lb2.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooso91(self):
        expected = get_data(
            path='contracts/KT1Lb2v9xrF9994tEZYogrX3og9UHgtRdZBg/parameter_ooso91.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opMCQC(self):
        expected = get_data(
            path='contracts/KT1Lb2v9xrF9994tEZYogrX3og9UHgtRdZBg/parameter_opMCQC.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooYrJr(self):
        expected = get_data(
            path='contracts/KT1Lb2v9xrF9994tEZYogrX3og9UHgtRdZBg/parameter_ooYrJr.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opJ56P(self):
        expected = get_data(
            path='contracts/KT1Lb2v9xrF9994tEZYogrX3og9UHgtRdZBg/parameter_opJ56P.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oovBBY(self):
        expected = get_data(
            path='contracts/KT1Lb2v9xrF9994tEZYogrX3og9UHgtRdZBg/parameter_oovBBY.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op6A4x(self):
        expected = get_data(
            path='contracts/KT1Lb2v9xrF9994tEZYogrX3og9UHgtRdZBg/parameter_op6A4x.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo6me4(self):
        expected = get_data(
            path='contracts/KT1Lb2v9xrF9994tEZYogrX3og9UHgtRdZBg/parameter_oo6me4.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
