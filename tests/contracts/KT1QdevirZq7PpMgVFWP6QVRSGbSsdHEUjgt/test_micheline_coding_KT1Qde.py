from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Qde(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/code_KT1Qde.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Qde(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/storage_KT1Qde.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo3Zu4(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo3Zu4.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooTYSp(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooTYSp.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oovxpk(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oovxpk.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooWRVq(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooWRVq.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooDitX(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooDitX.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo7BsA(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo7BsA.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onncXB(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_onncXB.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
