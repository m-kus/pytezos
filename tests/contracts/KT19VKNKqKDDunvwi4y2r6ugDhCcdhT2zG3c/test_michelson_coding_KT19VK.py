from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT19VK(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT19VK(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/code_KT19VK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/code_KT19VK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT19VK(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/code_KT19VK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/code_KT19VK.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT19VK(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/code_KT19VK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT19VK(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/storage_KT19VK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/storage_KT19VK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT19VK(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/storage_KT19VK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/storage_KT19VK.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT19VK(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/storage_KT19VK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onr6zv(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_onr6zv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_onr6zv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onr6zv(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_onr6zv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_onr6zv.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onr6zv(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_onr6zv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onzZ9j(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_onzZ9j.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_onzZ9j.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onzZ9j(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_onzZ9j.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_onzZ9j.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onzZ9j(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_onzZ9j.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooCm5y(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_ooCm5y.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_ooCm5y.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooCm5y(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_ooCm5y.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_ooCm5y.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooCm5y(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_ooCm5y.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oozEnM(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oozEnM.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oozEnM.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oozEnM(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oozEnM.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oozEnM.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oozEnM(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oozEnM.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo9VWb(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oo9VWb.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oo9VWb.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo9VWb(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oo9VWb.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oo9VWb.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo9VWb(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oo9VWb.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opP9oc(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_opP9oc.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_opP9oc.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opP9oc(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_opP9oc.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_opP9oc.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opP9oc(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_opP9oc.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo73cY(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oo73cY.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oo73cY.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo73cY(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oo73cY.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oo73cY.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo73cY(self):
        expected = get_data(
            path='contracts/KT19VKNKqKDDunvwi4y2r6ugDhCcdhT2zG3c/parameter_oo73cY.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
