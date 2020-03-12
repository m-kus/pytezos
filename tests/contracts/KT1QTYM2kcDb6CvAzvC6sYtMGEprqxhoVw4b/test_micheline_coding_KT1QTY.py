from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1QTY(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/code_KT1QTY.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1QTY(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/storage_KT1QTY.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooWnpp(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooWnpp.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op3XFW(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_op3XFW.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opagwv(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opagwv.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opQ3nd(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opQ3nd.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooDVQW(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooDVQW.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooe25v(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooe25v.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onuauD(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_onuauD.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
