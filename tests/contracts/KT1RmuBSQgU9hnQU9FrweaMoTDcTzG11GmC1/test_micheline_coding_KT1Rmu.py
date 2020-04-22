from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Rmu(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/code_KT1Rmu.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Rmu(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/storage_KT1Rmu.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oopTEr(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_oopTEr.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ongmUn(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ongmUn.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooNuuj(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooNuuj.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onutQC(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_onutQC.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opNidE(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_opNidE.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooxTNm(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooxTNm.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
