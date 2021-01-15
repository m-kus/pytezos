from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1TpK(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1TpK(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/code_KT1TpK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/code_KT1TpK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1TpK(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/code_KT1TpK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/code_KT1TpK.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1TpK(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/code_KT1TpK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1TpK(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/storage_KT1TpK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/storage_KT1TpK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1TpK(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/storage_KT1TpK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/storage_KT1TpK.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1TpK(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/storage_KT1TpK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opPXR3(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_opPXR3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_opPXR3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opPXR3(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_opPXR3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_opPXR3.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opPXR3(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_opPXR3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooXbxf(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooXbxf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooXbxf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooXbxf(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooXbxf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooXbxf.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooXbxf(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooXbxf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooGmSN(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooGmSN.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooGmSN.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooGmSN(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooGmSN.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooGmSN.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooGmSN(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooGmSN.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oosH2o(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_oosH2o.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_oosH2o.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oosH2o(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_oosH2o.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_oosH2o.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oosH2o(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_oosH2o.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooMKby(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooMKby.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooMKby.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooMKby(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooMKby.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooMKby.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooMKby(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_ooMKby.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onmk5E(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_onmk5E.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_onmk5E.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onmk5E(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_onmk5E.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_onmk5E.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onmk5E(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_onmk5E.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op1yUC(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_op1yUC.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_op1yUC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op1yUC(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_op1yUC.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_op1yUC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op1yUC(self):
        expected = get_data(
            path='contracts/KT1TpKkwKzGwMrWrGnPp9KixhraD2dtE5wE5/parameter_op1yUC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
