from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT19ft(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/code_KT19ft.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT19ft(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/storage_KT19ft.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oonoqg(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oonoqg.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onwTWA(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onwTWA.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooHkLe(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooHkLe.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo93Y4(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_oo93Y4.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onrTu8(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onrTu8.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooxsCt(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_ooxsCt.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onkjhr(self):
        expected = get_data(
            path='contracts/KT19fth8xoanAobcfdbssDjRTv7So1BCSQt4/parameter_onkjhr.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
