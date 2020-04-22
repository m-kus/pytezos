from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT18jL(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/code_KT18jL.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT18jL(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/storage_KT18jL.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooyTGN(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooyTGN.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oob5KJ(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oob5KJ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opTQ68(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opTQ68.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opVjgM(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opVjgM.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooTgW1(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooTgW1.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oniaoz(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oniaoz.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onqNh2(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_onqNh2.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
