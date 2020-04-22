from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1KXA(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/code_KT1KXA.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1KXA(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/storage_KT1KXA.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oob71y(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oob71y.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oovEPa(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oovEPa.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onsNL6(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onsNL6.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onkKtd(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onkKtd.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo1gZ9(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oo1gZ9.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onrnbX(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onrnbX.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op1reV(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_op1reV.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
