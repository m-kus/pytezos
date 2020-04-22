from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Gqy(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/code_KT1Gqy.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Gqy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/storage_KT1Gqy.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op1vDy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_op1vDy.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooqAps(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooqAps.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onu43U(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_onu43U.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo6Wkn(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_oo6Wkn.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooHqAk(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooHqAk.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooU8MM(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooU8MM.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooBcbW(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooBcbW.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
