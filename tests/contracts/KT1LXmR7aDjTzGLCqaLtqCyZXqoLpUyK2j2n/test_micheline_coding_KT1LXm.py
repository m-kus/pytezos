from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1LXm(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/code_KT1LXm.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1LXm(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/storage_KT1LXm.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooaNEK(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooaNEK.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooHaxf(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooHaxf.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op29rr(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_op29rr.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onigBP(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_onigBP.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo43iG(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_oo43iG.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooqbZV(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooqbZV.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opBxS5(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_opBxS5.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
