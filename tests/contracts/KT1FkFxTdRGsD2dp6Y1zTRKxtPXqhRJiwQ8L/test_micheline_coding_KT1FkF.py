from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1FkF(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/code_KT1FkF.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1FkF(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/storage_KT1FkF.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opLE7r(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opLE7r.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo5Vx5(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oo5Vx5.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oosWqk(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oosWqk.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oojFmp(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oojFmp.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oogsgh(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oogsgh.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooksL3(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_ooksL3.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opXdxc(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opXdxc.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
