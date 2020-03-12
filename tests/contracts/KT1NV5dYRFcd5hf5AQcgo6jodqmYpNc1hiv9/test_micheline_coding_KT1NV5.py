from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1NV5(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/code_KT1NV5.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1NV5(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/storage_KT1NV5.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooXx5e(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_ooXx5e.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onjy8C(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_onjy8C.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op4Sie(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op4Sie.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oodSov(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oodSov.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oojcqQ(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oojcqQ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op18hR(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op18hR.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo47n8(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oo47n8.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
