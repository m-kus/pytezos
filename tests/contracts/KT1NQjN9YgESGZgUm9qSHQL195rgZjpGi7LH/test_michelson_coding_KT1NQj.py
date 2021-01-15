from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1NQj(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1NQj(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/code_KT1NQj.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/code_KT1NQj.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1NQj(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/code_KT1NQj.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/code_KT1NQj.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1NQj(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/code_KT1NQj.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1NQj(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/storage_KT1NQj.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/storage_KT1NQj.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1NQj(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/storage_KT1NQj.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/storage_KT1NQj.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1NQj(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/storage_KT1NQj.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooeA7c(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/parameter_ooeA7c.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/parameter_ooeA7c.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooeA7c(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/parameter_ooeA7c.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/parameter_ooeA7c.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooeA7c(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/parameter_ooeA7c.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
