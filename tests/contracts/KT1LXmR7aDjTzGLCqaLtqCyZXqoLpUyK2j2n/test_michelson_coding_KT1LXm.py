from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1LXm(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1LXm(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/code_KT1LXm.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/code_KT1LXm.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1LXm(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/code_KT1LXm.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/code_KT1LXm.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1LXm(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/code_KT1LXm.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1LXm(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/storage_KT1LXm.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/storage_KT1LXm.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1LXm(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/storage_KT1LXm.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/storage_KT1LXm.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1LXm(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/storage_KT1LXm.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooaNEK(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooaNEK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooaNEK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooaNEK(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooaNEK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooaNEK.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooaNEK(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooaNEK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooHaxf(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooHaxf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooHaxf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooHaxf(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooHaxf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooHaxf.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooHaxf(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooHaxf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op29rr(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_op29rr.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_op29rr.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op29rr(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_op29rr.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_op29rr.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op29rr(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_op29rr.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onigBP(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_onigBP.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_onigBP.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onigBP(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_onigBP.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_onigBP.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onigBP(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_onigBP.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo43iG(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_oo43iG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_oo43iG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo43iG(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_oo43iG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_oo43iG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo43iG(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_oo43iG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooqbZV(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooqbZV.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooqbZV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooqbZV(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooqbZV.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooqbZV.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooqbZV(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_ooqbZV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opBxS5(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_opBxS5.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_opBxS5.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opBxS5(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_opBxS5.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_opBxS5.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opBxS5(self):
        expected = get_data(
            path='contracts/KT1LXmR7aDjTzGLCqaLtqCyZXqoLpUyK2j2n/parameter_opBxS5.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
