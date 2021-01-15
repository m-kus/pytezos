from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1T6C(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1T6C(self):
        expected = get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/code_KT1T6C.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/code_KT1T6C.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1T6C(self):
        expected = get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/code_KT1T6C.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/code_KT1T6C.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1T6C(self):
        expected = get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/code_KT1T6C.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1T6C(self):
        expected = get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/storage_KT1T6C.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/storage_KT1T6C.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1T6C(self):
        expected = get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/storage_KT1T6C.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/storage_KT1T6C.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1T6C(self):
        expected = get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/storage_KT1T6C.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooQKSw(self):
        expected = get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/parameter_ooQKSw.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/parameter_ooQKSw.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooQKSw(self):
        expected = get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/parameter_ooQKSw.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/parameter_ooQKSw.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooQKSw(self):
        expected = get_data(
            path='contracts/KT1T6CDRQLRiFU5dszBZWWQwQc8aCbfwX3Mg/parameter_ooQKSw.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
