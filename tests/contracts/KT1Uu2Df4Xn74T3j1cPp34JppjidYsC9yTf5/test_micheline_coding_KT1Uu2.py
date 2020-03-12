from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Uu2(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/code_KT1Uu2.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Uu2(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/storage_KT1Uu2.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo8EVa(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_oo8EVa.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooPJLZ(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooPJLZ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opUGdv(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_opUGdv.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooT6Fw(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooT6Fw.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
