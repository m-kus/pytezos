from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1QTY(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1QTY(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/code_KT1QTY.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/code_KT1QTY.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1QTY(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/code_KT1QTY.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/code_KT1QTY.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1QTY(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/code_KT1QTY.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1QTY(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/storage_KT1QTY.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/storage_KT1QTY.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1QTY(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/storage_KT1QTY.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/storage_KT1QTY.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1QTY(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/storage_KT1QTY.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooWnpp(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooWnpp.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooWnpp.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooWnpp(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooWnpp.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooWnpp.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooWnpp(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooWnpp.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op3XFW(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_op3XFW.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_op3XFW.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op3XFW(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_op3XFW.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_op3XFW.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op3XFW(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_op3XFW.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opagwv(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opagwv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opagwv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opagwv(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opagwv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opagwv.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opagwv(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opagwv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opQ3nd(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opQ3nd.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opQ3nd.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opQ3nd(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opQ3nd.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opQ3nd.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opQ3nd(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_opQ3nd.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooDVQW(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooDVQW.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooDVQW.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooDVQW(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooDVQW.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooDVQW.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooDVQW(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooDVQW.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooe25v(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooe25v.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooe25v.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooe25v(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooe25v.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooe25v.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooe25v(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_ooe25v.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onuauD(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_onuauD.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_onuauD.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onuauD(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_onuauD.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_onuauD.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onuauD(self):
        expected = get_data(
            path='contracts/KT1QTYM2kcDb6CvAzvC6sYtMGEprqxhoVw4b/parameter_onuauD.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
