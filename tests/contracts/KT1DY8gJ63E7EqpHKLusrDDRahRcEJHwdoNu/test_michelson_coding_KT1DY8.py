from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1DY8(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1DY8(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/code_KT1DY8.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/code_KT1DY8.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1DY8(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/code_KT1DY8.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/code_KT1DY8.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1DY8(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/code_KT1DY8.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1DY8(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/storage_KT1DY8.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/storage_KT1DY8.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1DY8(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/storage_KT1DY8.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/storage_KT1DY8.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1DY8(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/storage_KT1DY8.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opW9sC(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_opW9sC.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_opW9sC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opW9sC(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_opW9sC.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_opW9sC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opW9sC(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_opW9sC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ootyPG(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ootyPG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ootyPG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ootyPG(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ootyPG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ootyPG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ootyPG(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ootyPG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ook7XD(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ook7XD.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ook7XD.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ook7XD(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ook7XD.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ook7XD.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ook7XD(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ook7XD.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooMTro(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ooMTro.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ooMTro.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooMTro(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ooMTro.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ooMTro.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooMTro(self):
        expected = get_data(
            path='contracts/KT1DY8gJ63E7EqpHKLusrDDRahRcEJHwdoNu/parameter_ooMTro.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
