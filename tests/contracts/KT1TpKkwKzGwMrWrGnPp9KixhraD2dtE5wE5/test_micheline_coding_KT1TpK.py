from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1TpK(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/code_KT1TpK.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1TpK(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/storage_KT1TpK.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opPXR3(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_opPXR3.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooXbxf(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooXbxf.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooGmSN(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooGmSN.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oosH2o(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_oosH2o.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooMKby(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooMKby.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onmk5E(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_onmk5E.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op1yUC(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_op1yUC.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
