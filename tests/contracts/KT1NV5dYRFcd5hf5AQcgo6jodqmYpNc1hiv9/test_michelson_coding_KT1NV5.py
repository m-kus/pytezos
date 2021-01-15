from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1NV5(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1NV5(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/code_KT1NV5.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/code_KT1NV5.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1NV5(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/code_KT1NV5.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/code_KT1NV5.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1NV5(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/code_KT1NV5.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1NV5(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/storage_KT1NV5.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/storage_KT1NV5.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1NV5(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/storage_KT1NV5.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/storage_KT1NV5.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1NV5(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/storage_KT1NV5.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooXx5e(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_ooXx5e.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_ooXx5e.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooXx5e(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_ooXx5e.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_ooXx5e.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooXx5e(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_ooXx5e.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onjy8C(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_onjy8C.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_onjy8C.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onjy8C(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_onjy8C.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_onjy8C.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onjy8C(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_onjy8C.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op4Sie(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op4Sie.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op4Sie.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op4Sie(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op4Sie.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op4Sie.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op4Sie(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op4Sie.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oodSov(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oodSov.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oodSov.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oodSov(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oodSov.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oodSov.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oodSov(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oodSov.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oojcqQ(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oojcqQ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oojcqQ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oojcqQ(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oojcqQ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oojcqQ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oojcqQ(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oojcqQ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op18hR(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op18hR.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op18hR.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op18hR(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op18hR.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op18hR.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op18hR(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_op18hR.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo47n8(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oo47n8.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oo47n8.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo47n8(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oo47n8.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oo47n8.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo47n8(self):
        expected = get_data(
            path='contracts/KT1NV5dYRFcd5hf5AQcgo6jodqmYpNc1hiv9/parameter_oo47n8.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
