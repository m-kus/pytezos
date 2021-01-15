from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Myq(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Myq(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/code_KT1Myq.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/code_KT1Myq.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Myq(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/code_KT1Myq.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/code_KT1Myq.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Myq(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/code_KT1Myq.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Myq(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/storage_KT1Myq.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/storage_KT1Myq.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Myq(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/storage_KT1Myq.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/storage_KT1Myq.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Myq(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/storage_KT1Myq.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooZMtN(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooZMtN.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooZMtN.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooZMtN(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooZMtN.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooZMtN.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooZMtN(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooZMtN.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooGGqi(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooGGqi.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooGGqi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooGGqi(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooGGqi.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooGGqi.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooGGqi(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooGGqi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opYTCv(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_opYTCv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_opYTCv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opYTCv(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_opYTCv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_opYTCv.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opYTCv(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_opYTCv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op1CjT(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_op1CjT.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_op1CjT.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op1CjT(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_op1CjT.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_op1CjT.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op1CjT(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_op1CjT.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onyJat(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_onyJat.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_onyJat.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onyJat(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_onyJat.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_onyJat.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onyJat(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_onyJat.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooPQUi(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooPQUi.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooPQUi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooPQUi(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooPQUi.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooPQUi.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooPQUi(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_ooPQUi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op1KRF(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_op1KRF.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_op1KRF.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op1KRF(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_op1KRF.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_op1KRF.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op1KRF(self):
        expected = get_data(
            path='contracts/KT1Myqcyxp8MNgdB1aAhMpBApZHgVJ634nhm/parameter_op1KRF.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
