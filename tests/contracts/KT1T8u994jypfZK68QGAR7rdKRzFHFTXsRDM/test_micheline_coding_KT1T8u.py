from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1T8u(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/code_KT1T8u.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1T8u(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/storage_KT1T8u.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opEebx(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_opEebx.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oopo6v(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_oopo6v.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooyLp3(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_ooyLp3.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onrQxf(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_onrQxf.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
