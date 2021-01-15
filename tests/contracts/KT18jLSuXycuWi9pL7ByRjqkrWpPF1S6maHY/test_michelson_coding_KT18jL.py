from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT18jL(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT18jL(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/code_KT18jL.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/code_KT18jL.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT18jL(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/code_KT18jL.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/code_KT18jL.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT18jL(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/code_KT18jL.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT18jL(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/storage_KT18jL.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/storage_KT18jL.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT18jL(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/storage_KT18jL.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/storage_KT18jL.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT18jL(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/storage_KT18jL.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooyTGN(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooyTGN.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooyTGN.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooyTGN(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooyTGN.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooyTGN.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooyTGN(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooyTGN.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oob5KJ(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oob5KJ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oob5KJ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oob5KJ(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oob5KJ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oob5KJ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oob5KJ(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oob5KJ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opTQ68(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opTQ68.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opTQ68.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opTQ68(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opTQ68.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opTQ68.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opTQ68(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opTQ68.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opVjgM(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opVjgM.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opVjgM.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opVjgM(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opVjgM.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opVjgM.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opVjgM(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_opVjgM.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooTgW1(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooTgW1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooTgW1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooTgW1(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooTgW1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooTgW1.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooTgW1(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_ooTgW1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oniaoz(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oniaoz.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oniaoz.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oniaoz(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oniaoz.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oniaoz.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oniaoz(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_oniaoz.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onqNh2(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_onqNh2.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_onqNh2.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onqNh2(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_onqNh2.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_onqNh2.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onqNh2(self):
        expected = get_data(
            path='contracts/KT18jLSuXycuWi9pL7ByRjqkrWpPF1S6maHY/parameter_onqNh2.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
