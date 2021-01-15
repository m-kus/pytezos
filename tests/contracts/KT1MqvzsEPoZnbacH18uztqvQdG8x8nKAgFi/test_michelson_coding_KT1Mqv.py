from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Mqv(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Mqv(self):
        expected = get_data(
            path='contracts/KT1MqvzsEPoZnbacH18uztqvQdG8x8nKAgFi/code_KT1Mqv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MqvzsEPoZnbacH18uztqvQdG8x8nKAgFi/code_KT1Mqv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Mqv(self):
        expected = get_data(
            path='contracts/KT1MqvzsEPoZnbacH18uztqvQdG8x8nKAgFi/code_KT1Mqv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MqvzsEPoZnbacH18uztqvQdG8x8nKAgFi/code_KT1Mqv.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Mqv(self):
        expected = get_data(
            path='contracts/KT1MqvzsEPoZnbacH18uztqvQdG8x8nKAgFi/code_KT1Mqv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Mqv(self):
        expected = get_data(
            path='contracts/KT1MqvzsEPoZnbacH18uztqvQdG8x8nKAgFi/storage_KT1Mqv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MqvzsEPoZnbacH18uztqvQdG8x8nKAgFi/storage_KT1Mqv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Mqv(self):
        expected = get_data(
            path='contracts/KT1MqvzsEPoZnbacH18uztqvQdG8x8nKAgFi/storage_KT1Mqv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MqvzsEPoZnbacH18uztqvQdG8x8nKAgFi/storage_KT1Mqv.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Mqv(self):
        expected = get_data(
            path='contracts/KT1MqvzsEPoZnbacH18uztqvQdG8x8nKAgFi/storage_KT1Mqv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
