from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1NpC(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/code_KT1NpC.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1NpC(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/storage_KT1NpC.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oofSXx(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oofSXx.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opCGFQ(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opCGFQ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oojsnQ(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oojsnQ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooKXTr(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooKXTr.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooxskv(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooxskv.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooAm3B(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooAm3B.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opF6CW(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opF6CW.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
