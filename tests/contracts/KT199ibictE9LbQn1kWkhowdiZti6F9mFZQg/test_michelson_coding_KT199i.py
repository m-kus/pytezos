from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT199i(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT199i(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/code_KT199i.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/code_KT199i.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT199i(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/code_KT199i.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/code_KT199i.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT199i(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/code_KT199i.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT199i(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/storage_KT199i.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/storage_KT199i.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT199i(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/storage_KT199i.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/storage_KT199i.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT199i(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/storage_KT199i.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oomgeZ(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oomgeZ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oomgeZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oomgeZ(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oomgeZ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oomgeZ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oomgeZ(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oomgeZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oogdua(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oogdua.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oogdua.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oogdua(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oogdua.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oogdua.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oogdua(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oogdua.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oopFEw(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oopFEw.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oopFEw.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oopFEw(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oopFEw.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oopFEw.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oopFEw(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oopFEw.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oof2Jx(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oof2Jx.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oof2Jx.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oof2Jx(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oof2Jx.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oof2Jx.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oof2Jx(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oof2Jx.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oogbBk(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oogbBk.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oogbBk.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oogbBk(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oogbBk.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oogbBk.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oogbBk(self):
        expected = get_data(
            path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/parameter_oogbBk.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
