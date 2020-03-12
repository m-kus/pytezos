from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Ffh(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/code_KT1Ffh.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Ffh(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/storage_KT1Ffh.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo6ZHj(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oo6ZHj.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooA6Vb(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooA6Vb.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oorUFL(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oorUFL.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooExks(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooExks.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opBC7h(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_opBC7h.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooRry3(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooRry3.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onmeSo(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_onmeSo.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
