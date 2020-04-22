from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1G72(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/code_KT1G72.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1G72(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/storage_KT1G72.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onmWHA(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onmWHA.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onnQTu(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onnQTu.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooGRZm(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_ooGRZm.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
