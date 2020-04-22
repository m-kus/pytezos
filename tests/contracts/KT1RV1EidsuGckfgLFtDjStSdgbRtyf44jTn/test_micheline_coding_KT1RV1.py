from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1RV1(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/code_KT1RV1.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1RV1(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/storage_KT1RV1.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op6A3j(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op6A3j.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onoZj3(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onoZj3.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooDZxK(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooDZxK.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opFUTY(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_opFUTY.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onj3Qf(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onj3Qf.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op3Rex(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op3Rex.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooK1di(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooK1di.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
