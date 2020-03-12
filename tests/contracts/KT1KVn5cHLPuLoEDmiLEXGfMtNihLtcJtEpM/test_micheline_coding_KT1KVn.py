from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1KVn(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/code_KT1KVn.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1KVn(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/storage_KT1KVn.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oodpad(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oodpad.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op5JXz(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_op5JXz.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opWTsh(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opWTsh.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oovB4n(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oovB4n.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opVpjK(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opVpjK.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooSTG6(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_ooSTG6.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opPcx1(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opPcx1.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
