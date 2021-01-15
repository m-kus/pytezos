from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1QGq(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1QGq(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/code_KT1QGq.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/code_KT1QGq.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1QGq(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/code_KT1QGq.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/code_KT1QGq.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1QGq(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/code_KT1QGq.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1QGq(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/storage_KT1QGq.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/storage_KT1QGq.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1QGq(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/storage_KT1QGq.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/storage_KT1QGq.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1QGq(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/storage_KT1QGq.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opURFi(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opURFi.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opURFi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opURFi(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opURFi.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opURFi.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opURFi(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opURFi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onxkVd(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_onxkVd.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_onxkVd.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onxkVd(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_onxkVd.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_onxkVd.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onxkVd(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_onxkVd.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo5Fs5(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_oo5Fs5.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_oo5Fs5.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo5Fs5(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_oo5Fs5.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_oo5Fs5.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo5Fs5(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_oo5Fs5.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opKFsk(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opKFsk.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opKFsk.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opKFsk(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opKFsk.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opKFsk.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opKFsk(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opKFsk.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opRJZN(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opRJZN.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opRJZN.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opRJZN(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opRJZN.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opRJZN.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opRJZN(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opRJZN.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooGnEn(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_ooGnEn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_ooGnEn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooGnEn(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_ooGnEn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_ooGnEn.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooGnEn(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_ooGnEn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opZNoS(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opZNoS.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opZNoS.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opZNoS(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opZNoS.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opZNoS.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opZNoS(self):
        expected = get_data(
            path='contracts/KT1QGqm97QhfRujyZZt67QRaXUnNavjnFngg/parameter_opZNoS.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
