from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1MSZ(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1MSZ(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/code_KT1MSZ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/code_KT1MSZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1MSZ(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/code_KT1MSZ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/code_KT1MSZ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1MSZ(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/code_KT1MSZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1MSZ(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/storage_KT1MSZ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/storage_KT1MSZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1MSZ(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/storage_KT1MSZ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/storage_KT1MSZ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1MSZ(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/storage_KT1MSZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onwqBB(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_onwqBB.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_onwqBB.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onwqBB(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_onwqBB.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_onwqBB.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onwqBB(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_onwqBB.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooYBLf(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_ooYBLf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_ooYBLf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooYBLf(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_ooYBLf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_ooYBLf.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooYBLf(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_ooYBLf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opTdLV(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opTdLV.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opTdLV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opTdLV(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opTdLV.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opTdLV.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opTdLV(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opTdLV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oon8Ss(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oon8Ss.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oon8Ss.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oon8Ss(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oon8Ss.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oon8Ss.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oon8Ss(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oon8Ss.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oooRqc(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oooRqc.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oooRqc.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oooRqc(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oooRqc.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oooRqc.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oooRqc(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oooRqc.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oobXfo(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oobXfo.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oobXfo.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oobXfo(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oobXfo.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oobXfo.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oobXfo(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oobXfo.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opJKvo(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opJKvo.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opJKvo.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opJKvo(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opJKvo.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opJKvo.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opJKvo(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opJKvo.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
