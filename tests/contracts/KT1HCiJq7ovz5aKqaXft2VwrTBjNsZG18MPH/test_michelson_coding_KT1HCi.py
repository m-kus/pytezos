from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1HCi(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1HCi(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/code_KT1HCi.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/code_KT1HCi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1HCi(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/code_KT1HCi.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/code_KT1HCi.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1HCi(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/code_KT1HCi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1HCi(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/storage_KT1HCi.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/storage_KT1HCi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1HCi(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/storage_KT1HCi.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/storage_KT1HCi.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1HCi(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/storage_KT1HCi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo3N5b(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo3N5b.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo3N5b.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo3N5b(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo3N5b.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo3N5b.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo3N5b(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo3N5b.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo6Qxx(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo6Qxx.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo6Qxx.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo6Qxx(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo6Qxx.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo6Qxx.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo6Qxx(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oo6Qxx.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooZcdF(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooZcdF.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooZcdF.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooZcdF(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooZcdF.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooZcdF.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooZcdF(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooZcdF.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oni9SN(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oni9SN.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oni9SN.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oni9SN(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oni9SN.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oni9SN.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oni9SN(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oni9SN.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooEon1(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooEon1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooEon1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooEon1(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooEon1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooEon1.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooEon1(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooEon1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooMV4k(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooMV4k.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooMV4k.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooMV4k(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooMV4k.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooMV4k.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooMV4k(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_ooMV4k.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oofZtV(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oofZtV.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oofZtV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oofZtV(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oofZtV.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oofZtV.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oofZtV(self):
        expected = get_data(
            path='contracts/KT1HCiJq7ovz5aKqaXft2VwrTBjNsZG18MPH/parameter_oofZtV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
