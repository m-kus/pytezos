from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Md4(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Md4(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/code_KT1Md4.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/code_KT1Md4.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Md4(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/code_KT1Md4.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/code_KT1Md4.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Md4(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/code_KT1Md4.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Md4(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/storage_KT1Md4.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/storage_KT1Md4.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Md4(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/storage_KT1Md4.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/storage_KT1Md4.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Md4(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/storage_KT1Md4.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oov3xH(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/parameter_oov3xH.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/parameter_oov3xH.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oov3xH(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/parameter_oov3xH.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/parameter_oov3xH.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oov3xH(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/parameter_oov3xH.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
