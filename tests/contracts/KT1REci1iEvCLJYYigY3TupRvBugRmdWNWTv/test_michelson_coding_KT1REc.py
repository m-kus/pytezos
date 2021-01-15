from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1REc(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1REc(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/code_KT1REc.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/code_KT1REc.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1REc(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/code_KT1REc.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/code_KT1REc.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1REc(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/code_KT1REc.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1REc(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/storage_KT1REc.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/storage_KT1REc.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1REc(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/storage_KT1REc.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/storage_KT1REc.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1REc(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/storage_KT1REc.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oor4gF(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oor4gF.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oor4gF.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oor4gF(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oor4gF.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oor4gF.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oor4gF(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oor4gF.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onkJnN(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onkJnN.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onkJnN.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onkJnN(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onkJnN.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onkJnN.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onkJnN(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onkJnN.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooGn8U(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooGn8U.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooGn8U.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooGn8U(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooGn8U.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooGn8U.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooGn8U(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooGn8U.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onqdd9(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onqdd9.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onqdd9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onqdd9(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onqdd9.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onqdd9.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onqdd9(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_onqdd9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opGngn(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_opGngn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_opGngn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opGngn(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_opGngn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_opGngn.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opGngn(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_opGngn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooPeJR(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooPeJR.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooPeJR.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooPeJR(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooPeJR.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooPeJR.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooPeJR(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_ooPeJR.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oorduy(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oorduy.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oorduy.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oorduy(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oorduy.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oorduy.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oorduy(self):
        expected = get_data(
            path='contracts/KT1REci1iEvCLJYYigY3TupRvBugRmdWNWTv/parameter_oorduy.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
