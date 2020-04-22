from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1XFn(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/code_KT1XFn.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1XFn(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/storage_KT1XFn.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opTSR4(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opTSR4.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opY1b9(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opY1b9.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooUr5S(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooUr5S.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooam8Y(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooam8Y.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opFPwz(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opFPwz.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooaqNF(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooaqNF.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oovLAg(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_oovLAg.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
