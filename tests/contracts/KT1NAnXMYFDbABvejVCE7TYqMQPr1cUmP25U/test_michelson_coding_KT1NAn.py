from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1NAn(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1NAn(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/code_KT1NAn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/code_KT1NAn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1NAn(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/code_KT1NAn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/code_KT1NAn.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1NAn(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/code_KT1NAn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1NAn(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/storage_KT1NAn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/storage_KT1NAn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1NAn(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/storage_KT1NAn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/storage_KT1NAn.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1NAn(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/storage_KT1NAn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooJRq1(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_ooJRq1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_ooJRq1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooJRq1(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_ooJRq1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_ooJRq1.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooJRq1(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_ooJRq1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opYqMC(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opYqMC.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opYqMC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opYqMC(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opYqMC.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opYqMC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opYqMC(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opYqMC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opKWiC(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opKWiC.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opKWiC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opKWiC(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opKWiC.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opKWiC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opKWiC(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opKWiC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooZs8c(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_ooZs8c.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_ooZs8c.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooZs8c(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_ooZs8c.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_ooZs8c.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooZs8c(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_ooZs8c.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opMiJz(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opMiJz.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opMiJz.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opMiJz(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opMiJz.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opMiJz.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opMiJz(self):
        expected = get_data(
            path='contracts/KT1NAnXMYFDbABvejVCE7TYqMQPr1cUmP25U/parameter_opMiJz.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
