from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT19ft(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT19ft(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/code_KT19ft.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/code_KT19ft.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT19ft(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/code_KT19ft.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/code_KT19ft.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT19ft(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/code_KT19ft.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT19ft(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/storage_KT19ft.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/storage_KT19ft.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT19ft(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/storage_KT19ft.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/storage_KT19ft.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT19ft(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/storage_KT19ft.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oonoqg(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oonoqg.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oonoqg.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oonoqg(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oonoqg.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oonoqg.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oonoqg(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oonoqg.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onwTWA(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onwTWA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onwTWA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onwTWA(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onwTWA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onwTWA.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onwTWA(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onwTWA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooHkLe(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooHkLe.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooHkLe.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooHkLe(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooHkLe.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooHkLe.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooHkLe(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooHkLe.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo93Y4(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oo93Y4.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oo93Y4.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo93Y4(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oo93Y4.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oo93Y4.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo93Y4(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oo93Y4.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onrTu8(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onrTu8.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onrTu8.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onrTu8(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onrTu8.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onrTu8.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onrTu8(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onrTu8.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooxsCt(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooxsCt.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooxsCt.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooxsCt(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooxsCt.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooxsCt.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooxsCt(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooxsCt.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onkjhr(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onkjhr.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onkjhr.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onkjhr(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onkjhr.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onkjhr.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onkjhr(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onkjhr.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
