from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Rvo(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Rvo(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/code_KT1Rvo.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/code_KT1Rvo.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Rvo(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/code_KT1Rvo.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/code_KT1Rvo.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Rvo(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/code_KT1Rvo.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Rvo(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/storage_KT1Rvo.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/storage_KT1Rvo.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Rvo(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/storage_KT1Rvo.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/storage_KT1Rvo.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Rvo(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/storage_KT1Rvo.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onfSmx(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_onfSmx.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_onfSmx.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onfSmx(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_onfSmx.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_onfSmx.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onfSmx(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_onfSmx.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oowFNb(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_oowFNb.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_oowFNb.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oowFNb(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_oowFNb.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_oowFNb.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oowFNb(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_oowFNb.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opCeKS(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_opCeKS.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_opCeKS.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opCeKS(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_opCeKS.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_opCeKS.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opCeKS(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_opCeKS.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooGbyw(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_ooGbyw.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_ooGbyw.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooGbyw(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_ooGbyw.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_ooGbyw.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooGbyw(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_ooGbyw.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op7xJA(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_op7xJA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_op7xJA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op7xJA(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_op7xJA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_op7xJA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op7xJA(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_op7xJA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onzWYC(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_onzWYC.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_onzWYC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onzWYC(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_onzWYC.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_onzWYC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onzWYC(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_onzWYC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooUiCY(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_ooUiCY.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_ooUiCY.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooUiCY(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_ooUiCY.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_ooUiCY.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooUiCY(self):
        expected = get_data(
            path='contracts/KT1RvoWEU4MfDBrTbJh4JEAdh3giXtjxkR7k/parameter_ooUiCY.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
