from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Rmu(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Rmu(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/code_KT1Rmu.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/code_KT1Rmu.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Rmu(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/code_KT1Rmu.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/code_KT1Rmu.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Rmu(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/code_KT1Rmu.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Rmu(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/storage_KT1Rmu.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/storage_KT1Rmu.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Rmu(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/storage_KT1Rmu.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/storage_KT1Rmu.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Rmu(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/storage_KT1Rmu.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oopTEr(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_oopTEr.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_oopTEr.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oopTEr(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_oopTEr.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_oopTEr.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oopTEr(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_oopTEr.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ongmUn(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ongmUn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ongmUn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ongmUn(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ongmUn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ongmUn.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ongmUn(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ongmUn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooNuuj(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooNuuj.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooNuuj.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooNuuj(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooNuuj.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooNuuj.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooNuuj(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooNuuj.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onutQC(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_onutQC.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_onutQC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onutQC(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_onutQC.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_onutQC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onutQC(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_onutQC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opNidE(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_opNidE.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_opNidE.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opNidE(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_opNidE.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_opNidE.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opNidE(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_opNidE.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooxTNm(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooxTNm.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooxTNm.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooxTNm(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooxTNm.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooxTNm.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooxTNm(self):
        expected = get_data(
            path='contracts/KT1RmuBSQgU9hnQU9FrweaMoTDcTzG11GmC1/parameter_ooxTNm.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
