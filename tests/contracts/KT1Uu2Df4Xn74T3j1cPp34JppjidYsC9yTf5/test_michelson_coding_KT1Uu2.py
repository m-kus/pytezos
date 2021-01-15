from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Uu2(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Uu2(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/code_KT1Uu2.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/code_KT1Uu2.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Uu2(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/code_KT1Uu2.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/code_KT1Uu2.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Uu2(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/code_KT1Uu2.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Uu2(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/storage_KT1Uu2.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/storage_KT1Uu2.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Uu2(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/storage_KT1Uu2.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/storage_KT1Uu2.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Uu2(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/storage_KT1Uu2.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo8EVa(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_oo8EVa.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_oo8EVa.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo8EVa(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_oo8EVa.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_oo8EVa.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo8EVa(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_oo8EVa.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooPJLZ(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooPJLZ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooPJLZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooPJLZ(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooPJLZ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooPJLZ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooPJLZ(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooPJLZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opUGdv(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_opUGdv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_opUGdv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opUGdv(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_opUGdv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_opUGdv.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opUGdv(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_opUGdv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooT6Fw(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooT6Fw.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooT6Fw.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooT6Fw(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooT6Fw.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooT6Fw.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooT6Fw(self):
        expected = get_data(
            path='contracts/KT1Uu2Df4Xn74T3j1cPp34JppjidYsC9yTf5/parameter_ooT6Fw.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
