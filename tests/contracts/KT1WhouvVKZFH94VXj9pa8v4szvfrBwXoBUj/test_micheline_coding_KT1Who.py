from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Who(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/code_KT1Who.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Who(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/storage_KT1Who.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oozD2D(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oozD2D.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opECec(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opECec.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooaH79(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooaH79.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oonu1M(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oonu1M.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onvCMZ(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_onvCMZ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooqB2A(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooqB2A.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opGvHd(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opGvHd.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
