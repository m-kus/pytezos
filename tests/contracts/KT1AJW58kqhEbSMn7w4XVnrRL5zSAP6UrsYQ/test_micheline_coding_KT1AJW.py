from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1AJW(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/code_KT1AJW.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1AJW(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/storage_KT1AJW.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opWfWZ(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opWfWZ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onn9yH(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_onn9yH.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooft1h(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ooft1h.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opZM8B(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opZM8B.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo9GoT(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oo9GoT.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oogM43(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oogM43.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ootoxT(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ootoxT.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
