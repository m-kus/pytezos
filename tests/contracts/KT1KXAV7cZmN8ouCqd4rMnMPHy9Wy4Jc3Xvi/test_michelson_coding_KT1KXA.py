from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1KXA(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1KXA(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/code_KT1KXA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/code_KT1KXA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1KXA(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/code_KT1KXA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/code_KT1KXA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1KXA(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/code_KT1KXA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1KXA(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/storage_KT1KXA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/storage_KT1KXA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1KXA(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/storage_KT1KXA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/storage_KT1KXA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1KXA(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/storage_KT1KXA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oob71y(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oob71y.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oob71y.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oob71y(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oob71y.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oob71y.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oob71y(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oob71y.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oovEPa(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oovEPa.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oovEPa.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oovEPa(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oovEPa.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oovEPa.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oovEPa(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oovEPa.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onsNL6(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onsNL6.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onsNL6.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onsNL6(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onsNL6.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onsNL6.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onsNL6(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onsNL6.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onkKtd(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onkKtd.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onkKtd.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onkKtd(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onkKtd.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onkKtd.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onkKtd(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onkKtd.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo1gZ9(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oo1gZ9.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oo1gZ9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo1gZ9(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oo1gZ9.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oo1gZ9.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo1gZ9(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_oo1gZ9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onrnbX(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onrnbX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onrnbX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onrnbX(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onrnbX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onrnbX.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onrnbX(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_onrnbX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op1reV(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_op1reV.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_op1reV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op1reV(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_op1reV.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_op1reV.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op1reV(self):
        expected = get_data(
            path='contracts/KT1KXAV7cZmN8ouCqd4rMnMPHy9Wy4Jc3Xvi/parameter_op1reV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
