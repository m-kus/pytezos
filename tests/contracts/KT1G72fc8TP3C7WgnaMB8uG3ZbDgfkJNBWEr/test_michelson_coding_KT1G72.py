from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1G72(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1G72(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/code_KT1G72.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/code_KT1G72.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1G72(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/code_KT1G72.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/code_KT1G72.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1G72(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/code_KT1G72.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1G72(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/storage_KT1G72.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/storage_KT1G72.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1G72(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/storage_KT1G72.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/storage_KT1G72.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1G72(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/storage_KT1G72.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onmWHA(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onmWHA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onmWHA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onmWHA(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onmWHA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onmWHA.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onmWHA(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onmWHA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onnQTu(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onnQTu.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onnQTu.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onnQTu(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onnQTu.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onnQTu.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onnQTu(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_onnQTu.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooGRZm(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_ooGRZm.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_ooGRZm.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooGRZm(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_ooGRZm.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_ooGRZm.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooGRZm(self):
        expected = get_data(
            path='contracts/KT1G72fc8TP3C7WgnaMB8uG3ZbDgfkJNBWEr/parameter_ooGRZm.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
