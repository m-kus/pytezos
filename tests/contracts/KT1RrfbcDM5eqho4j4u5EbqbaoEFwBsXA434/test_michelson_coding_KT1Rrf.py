from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Rrf(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Rrf(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/code_KT1Rrf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/code_KT1Rrf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Rrf(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/code_KT1Rrf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/code_KT1Rrf.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Rrf(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/code_KT1Rrf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Rrf(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/storage_KT1Rrf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/storage_KT1Rrf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Rrf(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/storage_KT1Rrf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/storage_KT1Rrf.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Rrf(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/storage_KT1Rrf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opV3vx(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_opV3vx.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_opV3vx.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opV3vx(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_opV3vx.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_opV3vx.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opV3vx(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_opV3vx.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oojLES(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oojLES.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oojLES.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oojLES(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oojLES.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oojLES.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oojLES(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oojLES.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onk3tb(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onk3tb.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onk3tb.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onk3tb(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onk3tb.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onk3tb.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onk3tb(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onk3tb.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oorRMp(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oorRMp.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oorRMp.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oorRMp(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oorRMp.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oorRMp.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oorRMp(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_oorRMp.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onh2C5(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onh2C5.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onh2C5.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onh2C5(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onh2C5.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onh2C5.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onh2C5(self):
        expected = get_data(
            path='contracts/KT1RrfbcDM5eqho4j4u5EbqbaoEFwBsXA434/parameter_onh2C5.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
