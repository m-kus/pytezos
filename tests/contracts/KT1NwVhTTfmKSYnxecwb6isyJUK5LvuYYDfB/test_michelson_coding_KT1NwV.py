from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1NwV(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1NwV(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/code_KT1NwV.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/code_KT1NwV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1NwV(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/code_KT1NwV.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/code_KT1NwV.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1NwV(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/code_KT1NwV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1NwV(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/storage_KT1NwV.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/storage_KT1NwV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1NwV(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/storage_KT1NwV.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/storage_KT1NwV.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1NwV(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/storage_KT1NwV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oofBMc(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oofBMc.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oofBMc.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oofBMc(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oofBMc.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oofBMc.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oofBMc(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oofBMc.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onrPzn(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_onrPzn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_onrPzn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onrPzn(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_onrPzn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_onrPzn.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onrPzn(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_onrPzn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo7g8y(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oo7g8y.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oo7g8y.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo7g8y(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oo7g8y.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oo7g8y.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo7g8y(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oo7g8y.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opWEgz(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_opWEgz.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_opWEgz.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opWEgz(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_opWEgz.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_opWEgz.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opWEgz(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_opWEgz.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oogZVX(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oogZVX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oogZVX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oogZVX(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oogZVX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oogZVX.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oogZVX(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oogZVX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opLEjp(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_opLEjp.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_opLEjp.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opLEjp(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_opLEjp.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_opLEjp.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opLEjp(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_opLEjp.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo2ZBR(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oo2ZBR.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oo2ZBR.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo2ZBR(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oo2ZBR.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oo2ZBR.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo2ZBR(self):
        expected = get_data(
            path='contracts/KT1NwVhTTfmKSYnxecwb6isyJUK5LvuYYDfB/parameter_oo2ZBR.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
