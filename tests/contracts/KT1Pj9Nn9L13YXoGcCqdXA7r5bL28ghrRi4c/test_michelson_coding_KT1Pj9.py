from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Pj9(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Pj9(self):
        expected = get_data(
            path='contracts/KT1Pj9Nn9L13YXoGcCqdXA7r5bL28ghrRi4c/code_KT1Pj9.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Pj9Nn9L13YXoGcCqdXA7r5bL28ghrRi4c/code_KT1Pj9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Pj9(self):
        expected = get_data(
            path='contracts/KT1Pj9Nn9L13YXoGcCqdXA7r5bL28ghrRi4c/code_KT1Pj9.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Pj9Nn9L13YXoGcCqdXA7r5bL28ghrRi4c/code_KT1Pj9.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Pj9(self):
        expected = get_data(
            path='contracts/KT1Pj9Nn9L13YXoGcCqdXA7r5bL28ghrRi4c/code_KT1Pj9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Pj9(self):
        expected = get_data(
            path='contracts/KT1Pj9Nn9L13YXoGcCqdXA7r5bL28ghrRi4c/storage_KT1Pj9.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Pj9Nn9L13YXoGcCqdXA7r5bL28ghrRi4c/storage_KT1Pj9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Pj9(self):
        expected = get_data(
            path='contracts/KT1Pj9Nn9L13YXoGcCqdXA7r5bL28ghrRi4c/storage_KT1Pj9.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Pj9Nn9L13YXoGcCqdXA7r5bL28ghrRi4c/storage_KT1Pj9.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Pj9(self):
        expected = get_data(
            path='contracts/KT1Pj9Nn9L13YXoGcCqdXA7r5bL28ghrRi4c/storage_KT1Pj9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
