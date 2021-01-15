from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1XFn(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1XFn(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/code_KT1XFn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/code_KT1XFn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1XFn(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/code_KT1XFn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/code_KT1XFn.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1XFn(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/code_KT1XFn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1XFn(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/storage_KT1XFn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/storage_KT1XFn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1XFn(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/storage_KT1XFn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/storage_KT1XFn.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1XFn(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/storage_KT1XFn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opTSR4(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opTSR4.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opTSR4.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opTSR4(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opTSR4.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opTSR4.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opTSR4(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opTSR4.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opY1b9(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opY1b9.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opY1b9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opY1b9(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opY1b9.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opY1b9.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opY1b9(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opY1b9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooUr5S(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooUr5S.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooUr5S.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooUr5S(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooUr5S.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooUr5S.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooUr5S(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooUr5S.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooam8Y(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooam8Y.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooam8Y.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooam8Y(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooam8Y.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooam8Y.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooam8Y(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooam8Y.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opFPwz(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opFPwz.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opFPwz.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opFPwz(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opFPwz.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opFPwz.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opFPwz(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_opFPwz.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooaqNF(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooaqNF.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooaqNF.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooaqNF(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooaqNF.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooaqNF.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooaqNF(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_ooaqNF.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oovLAg(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_oovLAg.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_oovLAg.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oovLAg(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_oovLAg.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_oovLAg.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oovLAg(self):
        expected = get_data(
            path='contracts/KT1XFnSFqmXsBmNQVPByuYYkBFoNcXne4Ktu/parameter_oovLAg.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
