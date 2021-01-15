from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1HRu(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1HRu(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/code_KT1HRu.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/code_KT1HRu.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1HRu(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/code_KT1HRu.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/code_KT1HRu.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1HRu(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/code_KT1HRu.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1HRu(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/storage_KT1HRu.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/storage_KT1HRu.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1HRu(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/storage_KT1HRu.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/storage_KT1HRu.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1HRu(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/storage_KT1HRu.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opKGaY(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_opKGaY.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_opKGaY.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opKGaY(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_opKGaY.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_opKGaY.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opKGaY(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_opKGaY.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onkLH1(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_onkLH1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_onkLH1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onkLH1(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_onkLH1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_onkLH1.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onkLH1(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_onkLH1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooPA3v(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooPA3v.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooPA3v.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooPA3v(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooPA3v.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooPA3v.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooPA3v(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooPA3v.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooihn1(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooihn1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooihn1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooihn1(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooihn1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooihn1.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooihn1(self):
        expected = get_data(
            path='contracts/KT1HRuyp2NLSP9MKBfQyfKoNVUio6Fn7jeDi/parameter_ooihn1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
