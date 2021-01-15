from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1At3(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1At3(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/code_KT1At3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/code_KT1At3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1At3(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/code_KT1At3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/code_KT1At3.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1At3(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/code_KT1At3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1At3(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/storage_KT1At3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/storage_KT1At3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1At3(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/storage_KT1At3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/storage_KT1At3.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1At3(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/storage_KT1At3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oozfkT(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oozfkT.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oozfkT.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oozfkT(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oozfkT.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oozfkT.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oozfkT(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oozfkT.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo2UMR(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oo2UMR.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oo2UMR.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo2UMR(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oo2UMR.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oo2UMR.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo2UMR(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oo2UMR.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onwvUM(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_onwvUM.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_onwvUM.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onwvUM(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_onwvUM.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_onwvUM.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onwvUM(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_onwvUM.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opGhNz(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_opGhNz.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_opGhNz.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opGhNz(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_opGhNz.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_opGhNz.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opGhNz(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_opGhNz.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oowDU8(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oowDU8.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oowDU8.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oowDU8(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oowDU8.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oowDU8.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oowDU8(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oowDU8.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onpSQy(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_onpSQy.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_onpSQy.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onpSQy(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_onpSQy.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_onpSQy.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onpSQy(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_onpSQy.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oopBY6(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oopBY6.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oopBY6.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oopBY6(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oopBY6.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oopBY6.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oopBY6(self):
        expected = get_data(
            path='contracts/KT1At3oM7k94ccMmFCqjAZy42QyaDh2uNqhD/parameter_oopBY6.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
