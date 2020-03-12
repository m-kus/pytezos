from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1EUT(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/code_KT1EUT.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1EUT(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/storage_KT1EUT.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooLpuA(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooLpuA.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooCD9m(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooCD9m.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onpm7h(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_onpm7h.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooy1mv(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooy1mv.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oosjDx(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oosjDx.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oocS2Y(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocS2Y.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oocB4e(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocB4e.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
