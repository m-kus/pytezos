from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1DV3(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1DV3(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/code_KT1DV3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/code_KT1DV3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1DV3(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/code_KT1DV3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/code_KT1DV3.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1DV3(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/code_KT1DV3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1DV3(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/storage_KT1DV3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/storage_KT1DV3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1DV3(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/storage_KT1DV3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/storage_KT1DV3.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1DV3(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/storage_KT1DV3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo5gaT(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo5gaT.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo5gaT.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo5gaT(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo5gaT.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo5gaT.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo5gaT(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo5gaT.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opPGAB(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_opPGAB.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_opPGAB.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opPGAB(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_opPGAB.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_opPGAB.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opPGAB(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_opPGAB.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ootr5F(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_ootr5F.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_ootr5F.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ootr5F(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_ootr5F.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_ootr5F.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ootr5F(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_ootr5F.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo64jf(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo64jf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo64jf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo64jf(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo64jf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo64jf.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo64jf(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo64jf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onk5NH(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_onk5NH.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_onk5NH.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onk5NH(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_onk5NH.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_onk5NH.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onk5NH(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_onk5NH.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooc8Cj(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_ooc8Cj.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_ooc8Cj.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooc8Cj(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_ooc8Cj.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_ooc8Cj.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooc8Cj(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_ooc8Cj.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo9js3(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo9js3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo9js3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo9js3(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo9js3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo9js3.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo9js3(self):
        expected = get_data(
            path='contracts/KT1DV3mNYRrdpSBzcsJMk9Zd9q43c3iNW9mW/parameter_oo9js3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
