from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1PF3(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/code_KT1PF3.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1PF3(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/storage_KT1PF3.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oom6TD(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oom6TD.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oog5Rn(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oog5Rn.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oofw5X(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oofw5X.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opTCKd(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_opTCKd.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooAUgp(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooAUgp.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooDrNz(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooDrNz.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onr1XX(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_onr1XX.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
