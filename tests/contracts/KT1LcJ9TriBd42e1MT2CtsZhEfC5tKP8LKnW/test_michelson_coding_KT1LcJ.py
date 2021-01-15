from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1LcJ(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1LcJ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/code_KT1LcJ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/code_KT1LcJ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1LcJ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/code_KT1LcJ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/code_KT1LcJ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1LcJ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/code_KT1LcJ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1LcJ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/storage_KT1LcJ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/storage_KT1LcJ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1LcJ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/storage_KT1LcJ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/storage_KT1LcJ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1LcJ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/storage_KT1LcJ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opNs7Z(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opNs7Z.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opNs7Z.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opNs7Z(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opNs7Z.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opNs7Z.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opNs7Z(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opNs7Z.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onhDUH(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onhDUH.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onhDUH.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onhDUH(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onhDUH.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onhDUH.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onhDUH(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onhDUH.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opQ1UQ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opQ1UQ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opQ1UQ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opQ1UQ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opQ1UQ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opQ1UQ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opQ1UQ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opQ1UQ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooRxcK(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_ooRxcK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_ooRxcK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooRxcK(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_ooRxcK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_ooRxcK.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooRxcK(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_ooRxcK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oob6Lc(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_oob6Lc.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_oob6Lc.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oob6Lc(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_oob6Lc.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_oob6Lc.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oob6Lc(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_oob6Lc.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onpzaB(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onpzaB.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onpzaB.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onpzaB(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onpzaB.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onpzaB.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onpzaB(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onpzaB.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
