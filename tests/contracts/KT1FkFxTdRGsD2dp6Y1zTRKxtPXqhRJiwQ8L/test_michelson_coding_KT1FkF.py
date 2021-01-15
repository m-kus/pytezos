from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1FkF(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1FkF(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/code_KT1FkF.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/code_KT1FkF.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1FkF(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/code_KT1FkF.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/code_KT1FkF.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1FkF(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/code_KT1FkF.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1FkF(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/storage_KT1FkF.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/storage_KT1FkF.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1FkF(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/storage_KT1FkF.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/storage_KT1FkF.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1FkF(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/storage_KT1FkF.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opLE7r(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opLE7r.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opLE7r.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opLE7r(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opLE7r.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opLE7r.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opLE7r(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opLE7r.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo5Vx5(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oo5Vx5.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oo5Vx5.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo5Vx5(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oo5Vx5.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oo5Vx5.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo5Vx5(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oo5Vx5.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oosWqk(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oosWqk.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oosWqk.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oosWqk(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oosWqk.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oosWqk.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oosWqk(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oosWqk.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oojFmp(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oojFmp.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oojFmp.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oojFmp(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oojFmp.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oojFmp.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oojFmp(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oojFmp.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oogsgh(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oogsgh.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oogsgh.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oogsgh(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oogsgh.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oogsgh.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oogsgh(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_oogsgh.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooksL3(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_ooksL3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_ooksL3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooksL3(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_ooksL3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_ooksL3.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooksL3(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_ooksL3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opXdxc(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opXdxc.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opXdxc.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opXdxc(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opXdxc.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opXdxc.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opXdxc(self):
        expected = get_data(
            path='contracts/KT1FkFxTdRGsD2dp6Y1zTRKxtPXqhRJiwQ8L/parameter_opXdxc.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
