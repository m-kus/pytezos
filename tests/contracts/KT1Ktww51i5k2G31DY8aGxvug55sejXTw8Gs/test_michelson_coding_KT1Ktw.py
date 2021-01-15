from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Ktw(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Ktw(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/code_KT1Ktw.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/code_KT1Ktw.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Ktw(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/code_KT1Ktw.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/code_KT1Ktw.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Ktw(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/code_KT1Ktw.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Ktw(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/storage_KT1Ktw.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/storage_KT1Ktw.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Ktw(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/storage_KT1Ktw.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/storage_KT1Ktw.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Ktw(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/storage_KT1Ktw.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooJTZi(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooJTZi.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooJTZi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooJTZi(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooJTZi.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooJTZi.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooJTZi(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooJTZi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooEGeF(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooEGeF.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooEGeF.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooEGeF(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooEGeF.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooEGeF.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooEGeF(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_ooEGeF.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opWTeb(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opWTeb.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opWTeb.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opWTeb(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opWTeb.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opWTeb.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opWTeb(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opWTeb.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onmE5N(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_onmE5N.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_onmE5N.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onmE5N(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_onmE5N.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_onmE5N.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onmE5N(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_onmE5N.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opS1GR(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opS1GR.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opS1GR.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opS1GR(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opS1GR.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opS1GR.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opS1GR(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opS1GR.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opEdvx(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opEdvx.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opEdvx.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opEdvx(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opEdvx.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opEdvx.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opEdvx(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_opEdvx.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oobGEG(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_oobGEG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_oobGEG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oobGEG(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_oobGEG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_oobGEG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oobGEG(self):
        expected = get_data(
            path='contracts/KT1Ktww51i5k2G31DY8aGxvug55sejXTw8Gs/parameter_oobGEG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
