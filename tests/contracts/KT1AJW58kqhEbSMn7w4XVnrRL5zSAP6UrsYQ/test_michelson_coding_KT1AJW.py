from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1AJW(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1AJW(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/code_KT1AJW.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/code_KT1AJW.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1AJW(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/code_KT1AJW.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/code_KT1AJW.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1AJW(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/code_KT1AJW.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1AJW(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/storage_KT1AJW.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/storage_KT1AJW.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1AJW(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/storage_KT1AJW.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/storage_KT1AJW.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1AJW(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/storage_KT1AJW.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opWfWZ(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opWfWZ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opWfWZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opWfWZ(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opWfWZ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opWfWZ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opWfWZ(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opWfWZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onn9yH(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_onn9yH.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_onn9yH.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onn9yH(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_onn9yH.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_onn9yH.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onn9yH(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_onn9yH.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooft1h(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ooft1h.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ooft1h.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooft1h(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ooft1h.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ooft1h.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooft1h(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ooft1h.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opZM8B(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opZM8B.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opZM8B.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opZM8B(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opZM8B.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opZM8B.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opZM8B(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_opZM8B.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo9GoT(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oo9GoT.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oo9GoT.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo9GoT(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oo9GoT.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oo9GoT.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo9GoT(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oo9GoT.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oogM43(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oogM43.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oogM43.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oogM43(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oogM43.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oogM43.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oogM43(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_oogM43.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ootoxT(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ootoxT.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ootoxT.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ootoxT(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ootoxT.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ootoxT.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ootoxT(self):
        expected = get_data(
            path='contracts/KT1AJW58kqhEbSMn7w4XVnrRL5zSAP6UrsYQ/parameter_ootoxT.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
