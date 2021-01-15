from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1T8u(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1T8u(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/code_KT1T8u.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/code_KT1T8u.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1T8u(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/code_KT1T8u.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/code_KT1T8u.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1T8u(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/code_KT1T8u.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1T8u(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/storage_KT1T8u.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/storage_KT1T8u.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1T8u(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/storage_KT1T8u.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/storage_KT1T8u.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1T8u(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/storage_KT1T8u.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opEebx(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_opEebx.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_opEebx.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opEebx(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_opEebx.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_opEebx.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opEebx(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_opEebx.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oopo6v(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_oopo6v.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_oopo6v.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oopo6v(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_oopo6v.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_oopo6v.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oopo6v(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_oopo6v.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooyLp3(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_ooyLp3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_ooyLp3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooyLp3(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_ooyLp3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_ooyLp3.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooyLp3(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_ooyLp3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onrQxf(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_onrQxf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_onrQxf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onrQxf(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_onrQxf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_onrQxf.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onrQxf(self):
        expected = get_data(
            path='contracts/KT1T8u994jypfZK68QGAR7rdKRzFHFTXsRDM/parameter_onrQxf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
