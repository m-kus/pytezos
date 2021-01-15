from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1ME1(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1ME1(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/code_KT1ME1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/code_KT1ME1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1ME1(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/code_KT1ME1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/code_KT1ME1.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1ME1(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/code_KT1ME1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1ME1(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/storage_KT1ME1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/storage_KT1ME1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1ME1(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/storage_KT1ME1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/storage_KT1ME1.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1ME1(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/storage_KT1ME1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op47YG(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_op47YG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_op47YG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op47YG(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_op47YG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_op47YG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op47YG(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_op47YG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oneuS6(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_oneuS6.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_oneuS6.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oneuS6(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_oneuS6.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_oneuS6.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oneuS6(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_oneuS6.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onznY6(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_onznY6.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_onznY6.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onznY6(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_onznY6.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_onznY6.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onznY6(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_onznY6.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooNSWi(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooNSWi.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooNSWi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooNSWi(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooNSWi.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooNSWi.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooNSWi(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooNSWi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooYecX(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooYecX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooYecX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooYecX(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooYecX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooYecX.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooYecX(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooYecX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooDukJ(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooDukJ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooDukJ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooDukJ(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooDukJ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooDukJ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooDukJ(self):
        expected = get_data(
            path='contracts/KT1ME1G3xGeGdjzfmGYGCWW4FEkTvn88ueZ2/parameter_ooDukJ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
