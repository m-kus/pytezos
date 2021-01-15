from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Ffh(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Ffh(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/code_KT1Ffh.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/code_KT1Ffh.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Ffh(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/code_KT1Ffh.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/code_KT1Ffh.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Ffh(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/code_KT1Ffh.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Ffh(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/storage_KT1Ffh.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/storage_KT1Ffh.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Ffh(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/storage_KT1Ffh.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/storage_KT1Ffh.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Ffh(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/storage_KT1Ffh.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo6ZHj(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oo6ZHj.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oo6ZHj.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo6ZHj(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oo6ZHj.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oo6ZHj.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo6ZHj(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oo6ZHj.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooA6Vb(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooA6Vb.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooA6Vb.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooA6Vb(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooA6Vb.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooA6Vb.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooA6Vb(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooA6Vb.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oorUFL(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oorUFL.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oorUFL.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oorUFL(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oorUFL.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oorUFL.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oorUFL(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_oorUFL.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooExks(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooExks.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooExks.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooExks(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooExks.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooExks.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooExks(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooExks.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opBC7h(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_opBC7h.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_opBC7h.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opBC7h(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_opBC7h.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_opBC7h.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opBC7h(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_opBC7h.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooRry3(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooRry3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooRry3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooRry3(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooRry3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooRry3.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooRry3(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_ooRry3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onmeSo(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_onmeSo.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_onmeSo.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onmeSo(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_onmeSo.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_onmeSo.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onmeSo(self):
        expected = get_data(
            path='contracts/KT1FfhRBXiDLuurraaP2u6PkLaPhXSfAdPGY/parameter_onmeSo.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
