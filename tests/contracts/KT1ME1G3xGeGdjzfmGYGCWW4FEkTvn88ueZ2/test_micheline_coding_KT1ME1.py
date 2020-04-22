from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1ME1(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/code_KT1ME1.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1ME1(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/storage_KT1ME1.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op47YG(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_op47YG.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oneuS6(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_oneuS6.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onznY6(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_onznY6.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooNSWi(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooNSWi.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooYecX(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooYecX.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooDukJ(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooDukJ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
