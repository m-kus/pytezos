from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1G2D(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1G2D(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/code_KT1G2D.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/code_KT1G2D.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1G2D(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/code_KT1G2D.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/code_KT1G2D.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1G2D(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/code_KT1G2D.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1G2D(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/storage_KT1G2D.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/storage_KT1G2D.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1G2D(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/storage_KT1G2D.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/storage_KT1G2D.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1G2D(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/storage_KT1G2D.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onyWYA(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onyWYA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onyWYA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onyWYA(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onyWYA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onyWYA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onyWYA(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onyWYA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onydWh(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onydWh.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onydWh.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onydWh(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onydWh.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onydWh.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onydWh(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_onydWh.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opZNW1(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_opZNW1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_opZNW1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opZNW1(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_opZNW1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_opZNW1.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opZNW1(self):
        expected = get_data(
            path='contracts/KT1G2D45tpJ9f1iGVwQHqvupv2syhvMqeWPe/parameter_opZNW1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
