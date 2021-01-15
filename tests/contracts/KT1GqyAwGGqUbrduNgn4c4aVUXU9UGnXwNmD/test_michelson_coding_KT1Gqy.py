from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Gqy(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Gqy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/code_KT1Gqy.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/code_KT1Gqy.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Gqy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/code_KT1Gqy.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/code_KT1Gqy.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Gqy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/code_KT1Gqy.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Gqy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/storage_KT1Gqy.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/storage_KT1Gqy.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Gqy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/storage_KT1Gqy.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/storage_KT1Gqy.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Gqy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/storage_KT1Gqy.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op1vDy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_op1vDy.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_op1vDy.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op1vDy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_op1vDy.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_op1vDy.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op1vDy(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_op1vDy.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooqAps(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooqAps.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooqAps.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooqAps(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooqAps.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooqAps.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooqAps(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooqAps.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onu43U(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_onu43U.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_onu43U.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onu43U(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_onu43U.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_onu43U.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onu43U(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_onu43U.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo6Wkn(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_oo6Wkn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_oo6Wkn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo6Wkn(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_oo6Wkn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_oo6Wkn.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo6Wkn(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_oo6Wkn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooHqAk(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooHqAk.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooHqAk.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooHqAk(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooHqAk.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooHqAk.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooHqAk(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooHqAk.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooU8MM(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooU8MM.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooU8MM.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooU8MM(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooU8MM.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooU8MM.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooU8MM(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooU8MM.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooBcbW(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooBcbW.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooBcbW.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooBcbW(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooBcbW.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooBcbW.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooBcbW(self):
        expected = get_data(
            path='contracts/KT1GqyAwGGqUbrduNgn4c4aVUXU9UGnXwNmD/parameter_ooBcbW.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
