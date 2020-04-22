from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1HCi(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/code_KT1HCi.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1HCi(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/storage_KT1HCi.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo3N5b(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo3N5b.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo6Qxx(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo6Qxx.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooZcdF(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooZcdF.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oni9SN(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oni9SN.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooEon1(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooEon1.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooMV4k(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooMV4k.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oofZtV(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oofZtV.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
