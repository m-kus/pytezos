from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1BDM(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1BDMQEhMATgVAcwtgqNgZNBM6LEM1PANuM/code_KT1BDM.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1BDM(self):
        expected = get_data(
            path='contracts/KT1BDMQEhMATgVAcwtgqNgZNBM6LEM1PANuM/storage_KT1BDM.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooMDoN(self):
        expected = get_data(
            path='contracts/KT1BDMQEhMATgVAcwtgqNgZNBM6LEM1PANuM/parameter_ooMDoN.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooT7Uy(self):
        expected = get_data(
            path='contracts/KT1BDMQEhMATgVAcwtgqNgZNBM6LEM1PANuM/parameter_ooT7Uy.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onuB3S(self):
        expected = get_data(
            path='contracts/KT1BDMQEhMATgVAcwtgqNgZNBM6LEM1PANuM/parameter_onuB3S.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooArSr(self):
        expected = get_data(
            path='contracts/KT1BDMQEhMATgVAcwtgqNgZNBM6LEM1PANuM/parameter_ooArSr.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onrCFo(self):
        expected = get_data(
            path='contracts/KT1BDMQEhMATgVAcwtgqNgZNBM6LEM1PANuM/parameter_onrCFo.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ongBCW(self):
        expected = get_data(
            path='contracts/KT1BDMQEhMATgVAcwtgqNgZNBM6LEM1PANuM/parameter_ongBCW.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooe4gB(self):
        expected = get_data(
            path='contracts/KT1BDMQEhMATgVAcwtgqNgZNBM6LEM1PANuM/parameter_ooe4gB.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
