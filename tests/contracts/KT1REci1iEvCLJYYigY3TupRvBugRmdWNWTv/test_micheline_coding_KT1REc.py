from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1REc(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/code_KT1REc.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1REc(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/storage_KT1REc.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oor4gF(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oor4gF.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onkJnN(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onkJnN.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooGn8U(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooGn8U.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onqdd9(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onqdd9.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opGngn(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_opGngn.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooPeJR(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooPeJR.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oorduy(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oorduy.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
