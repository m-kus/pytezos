from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1E7x(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1E7x(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/code_KT1E7x.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/code_KT1E7x.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1E7x(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/code_KT1E7x.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/code_KT1E7x.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1E7x(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/code_KT1E7x.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1E7x(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/storage_KT1E7x.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/storage_KT1E7x.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1E7x(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/storage_KT1E7x.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/storage_KT1E7x.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1E7x(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/storage_KT1E7x.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op6yDi(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op6yDi.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op6yDi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op6yDi(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op6yDi.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op6yDi.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op6yDi(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op6yDi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooT4MX(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooT4MX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooT4MX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooT4MX(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooT4MX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooT4MX.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooT4MX(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooT4MX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooSTpg(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooSTpg.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooSTpg.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooSTpg(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooSTpg.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooSTpg.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooSTpg(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooSTpg.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opMCWt(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_opMCWt.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_opMCWt.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opMCWt(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_opMCWt.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_opMCWt.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opMCWt(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_opMCWt.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op7GDV(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op7GDV.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op7GDV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op7GDV(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op7GDV.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op7GDV.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op7GDV(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op7GDV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooJS2C(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooJS2C.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooJS2C.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooJS2C(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooJS2C.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooJS2C.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooJS2C(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooJS2C.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
