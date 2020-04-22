from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Ktw(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/code_KT1Ktw.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Ktw(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/storage_KT1Ktw.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooJTZi(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooJTZi.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooEGeF(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooEGeF.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opWTeb(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opWTeb.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onmE5N(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_onmE5N.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opS1GR(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opS1GR.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opEdvx(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opEdvx.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oobGEG(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_oobGEG.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
