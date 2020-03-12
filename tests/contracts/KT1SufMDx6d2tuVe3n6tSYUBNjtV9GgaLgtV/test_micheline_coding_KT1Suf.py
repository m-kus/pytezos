from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Suf(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/code_KT1Suf.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Suf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/storage_KT1Suf.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo3zPe(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_oo3zPe.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opJtR2(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJtR2.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooa5iW(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooa5iW.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooASVX(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooASVX.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opJh9L(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJh9L.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooKbwJ(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooKbwJ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op6Brf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_op6Brf.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
