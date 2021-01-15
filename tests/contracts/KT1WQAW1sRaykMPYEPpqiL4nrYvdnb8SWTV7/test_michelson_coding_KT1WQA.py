from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1WQA(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1WQA(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/code_KT1WQA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/code_KT1WQA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1WQA(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/code_KT1WQA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/code_KT1WQA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1WQA(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/code_KT1WQA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1WQA(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/storage_KT1WQA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/storage_KT1WQA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1WQA(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/storage_KT1WQA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/storage_KT1WQA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1WQA(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/storage_KT1WQA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onjMGH(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/parameter_onjMGH.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/parameter_onjMGH.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onjMGH(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/parameter_onjMGH.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/parameter_onjMGH.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onjMGH(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/parameter_onjMGH.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
