from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1EUT(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1EUT(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/code_KT1EUT.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/code_KT1EUT.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1EUT(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/code_KT1EUT.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/code_KT1EUT.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1EUT(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/code_KT1EUT.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1EUT(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/storage_KT1EUT.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/storage_KT1EUT.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1EUT(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/storage_KT1EUT.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/storage_KT1EUT.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1EUT(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/storage_KT1EUT.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooLpuA(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooLpuA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooLpuA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooLpuA(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooLpuA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooLpuA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooLpuA(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooLpuA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooCD9m(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooCD9m.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooCD9m.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooCD9m(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooCD9m.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooCD9m.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooCD9m(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooCD9m.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onpm7h(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_onpm7h.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_onpm7h.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onpm7h(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_onpm7h.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_onpm7h.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onpm7h(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_onpm7h.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooy1mv(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooy1mv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooy1mv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooy1mv(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooy1mv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooy1mv.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooy1mv(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_ooy1mv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oosjDx(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oosjDx.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oosjDx.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oosjDx(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oosjDx.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oosjDx.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oosjDx(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oosjDx.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oocS2Y(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocS2Y.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocS2Y.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oocS2Y(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocS2Y.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocS2Y.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oocS2Y(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocS2Y.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oocB4e(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocB4e.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocB4e.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oocB4e(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocB4e.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocB4e.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oocB4e(self):
        expected = get_data(
            path='contracts/KT1EUTxJch3jR9VuQ5wV4HeWbs5BnUfQp3N3/parameter_oocB4e.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
