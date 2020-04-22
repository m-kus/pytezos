from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1MUt(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/code_KT1MUt.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1MUt(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/storage_KT1MUt.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooaeRJ(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooaeRJ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op6E1L(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op6E1L.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op16Ra(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op16Ra.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onnwwM(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_onnwwM.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ookN7L(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ookN7L.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooqMbo(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooqMbo.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ongS8k(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ongS8k.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
