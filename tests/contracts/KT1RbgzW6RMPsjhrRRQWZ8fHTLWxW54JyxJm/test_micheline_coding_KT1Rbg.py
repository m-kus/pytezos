from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Rbg(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/code_KT1Rbg.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Rbg(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/storage_KT1Rbg.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opPKEf(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opPKEf.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooADdh(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooADdh.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opDD3W(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opDD3W.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oovacQ(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_oovacQ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooyq1S(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooyq1S.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opNXFv(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opNXFv.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooCpEk(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooCpEk.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
