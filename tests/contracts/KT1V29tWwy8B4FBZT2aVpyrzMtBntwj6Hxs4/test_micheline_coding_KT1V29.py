from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1V29(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/code_KT1V29.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1V29(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/storage_KT1V29.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opFeYT(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opFeYT.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo6a87(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo6a87.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo42py(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo42py.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opM17X(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opM17X.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooiaRh(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_ooiaRh.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onxCTv(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_onxCTv.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opQqHE(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opQqHE.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
