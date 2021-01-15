from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1T1Q(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1T1Q(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/code_KT1T1Q.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/code_KT1T1Q.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1T1Q(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/code_KT1T1Q.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/code_KT1T1Q.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1T1Q(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/code_KT1T1Q.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1T1Q(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/storage_KT1T1Q.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/storage_KT1T1Q.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1T1Q(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/storage_KT1T1Q.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/storage_KT1T1Q.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1T1Q(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/storage_KT1T1Q.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opDY37(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opDY37.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opDY37.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opDY37(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opDY37.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opDY37.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opDY37(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opDY37.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooFVFm(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_ooFVFm.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_ooFVFm.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooFVFm(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_ooFVFm.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_ooFVFm.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooFVFm(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_ooFVFm.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op3JH8(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op3JH8.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op3JH8.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op3JH8(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op3JH8.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op3JH8.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op3JH8(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op3JH8.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opJuDD(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opJuDD.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opJuDD.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opJuDD(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opJuDD.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opJuDD.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opJuDD(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_opJuDD.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op9fva(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op9fva.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op9fva.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op9fva(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op9fva.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op9fva.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op9fva(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op9fva.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op6G8U(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op6G8U.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op6G8U.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op6G8U(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op6G8U.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op6G8U.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op6G8U(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_op6G8U.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onmrnk(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_onmrnk.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_onmrnk.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onmrnk(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_onmrnk.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_onmrnk.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onmrnk(self):
        expected = get_data(
            path='contracts/KT1T1QYR6VD2LLtRSP4CHNyKkGbAPHoVu7wc/parameter_onmrnk.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
