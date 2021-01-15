from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1V29(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1V29(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/code_KT1V29.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/code_KT1V29.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1V29(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/code_KT1V29.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/code_KT1V29.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1V29(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/code_KT1V29.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1V29(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/storage_KT1V29.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/storage_KT1V29.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1V29(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/storage_KT1V29.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/storage_KT1V29.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1V29(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/storage_KT1V29.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opFeYT(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opFeYT.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opFeYT.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opFeYT(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opFeYT.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opFeYT.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opFeYT(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opFeYT.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo6a87(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo6a87.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo6a87.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo6a87(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo6a87.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo6a87.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo6a87(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo6a87.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo42py(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo42py.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo42py.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo42py(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo42py.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo42py.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo42py(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_oo42py.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opM17X(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opM17X.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opM17X.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opM17X(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opM17X.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opM17X.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opM17X(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opM17X.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooiaRh(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_ooiaRh.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_ooiaRh.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooiaRh(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_ooiaRh.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_ooiaRh.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooiaRh(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_ooiaRh.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onxCTv(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_onxCTv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_onxCTv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onxCTv(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_onxCTv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_onxCTv.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onxCTv(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_onxCTv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opQqHE(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opQqHE.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opQqHE.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opQqHE(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opQqHE.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opQqHE.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opQqHE(self):
        expected = get_data(
            path='contracts/KT1V29tWwy8B4FBZT2aVpyrzMtBntwj6Hxs4/parameter_opQqHE.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
