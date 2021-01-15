from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Rbg(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Rbg(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/code_KT1Rbg.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/code_KT1Rbg.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Rbg(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/code_KT1Rbg.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/code_KT1Rbg.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Rbg(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/code_KT1Rbg.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Rbg(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/storage_KT1Rbg.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/storage_KT1Rbg.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Rbg(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/storage_KT1Rbg.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/storage_KT1Rbg.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Rbg(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/storage_KT1Rbg.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opPKEf(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opPKEf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opPKEf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opPKEf(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opPKEf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opPKEf.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opPKEf(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opPKEf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooADdh(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooADdh.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooADdh.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooADdh(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooADdh.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooADdh.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooADdh(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooADdh.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opDD3W(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opDD3W.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opDD3W.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opDD3W(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opDD3W.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opDD3W.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opDD3W(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opDD3W.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oovacQ(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_oovacQ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_oovacQ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oovacQ(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_oovacQ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_oovacQ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oovacQ(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_oovacQ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooyq1S(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooyq1S.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooyq1S.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooyq1S(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooyq1S.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooyq1S.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooyq1S(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooyq1S.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opNXFv(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opNXFv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opNXFv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opNXFv(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opNXFv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opNXFv.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opNXFv(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_opNXFv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooCpEk(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooCpEk.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooCpEk.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooCpEk(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooCpEk.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooCpEk.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooCpEk(self):
        expected = get_data(
            path='contracts/KT1RbgzW6RMPsjhrRRQWZ8fHTLWxW54JyxJm/parameter_ooCpEk.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
