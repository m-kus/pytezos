from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1T1Q(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/code_KT1T1Q.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1T1Q(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/storage_KT1T1Q.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opDY37(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opDY37.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooFVFm(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_ooFVFm.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op3JH8(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op3JH8.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opJuDD(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opJuDD.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op9fva(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op9fva.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op6G8U(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op6G8U.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onmrnk(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_onmrnk.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
