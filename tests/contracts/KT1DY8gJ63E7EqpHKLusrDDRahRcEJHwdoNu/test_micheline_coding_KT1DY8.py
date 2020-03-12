from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1DY8(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/code_KT1DY8.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1DY8(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/storage_KT1DY8.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opW9sC(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_opW9sC.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ootyPG(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ootyPG.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ook7XD(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ook7XD.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooMTro(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ooMTro.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
