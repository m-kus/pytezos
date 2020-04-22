from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1QGq(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/code_KT1QGq.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1QGq(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/storage_KT1QGq.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opURFi(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opURFi.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onxkVd(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_onxkVd.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo5Fs5(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_oo5Fs5.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opKFsk(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opKFsk.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opRJZN(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opRJZN.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooGnEn(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_ooGnEn.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opZNoS(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opZNoS.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
