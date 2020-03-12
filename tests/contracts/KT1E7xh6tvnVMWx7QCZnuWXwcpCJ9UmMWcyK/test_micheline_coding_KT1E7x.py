from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1E7x(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/code_KT1E7x.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1E7x(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/storage_KT1E7x.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op6yDi(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op6yDi.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooT4MX(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooT4MX.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooSTpg(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooSTpg.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opMCWt(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_opMCWt.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op7GDV(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_op7GDV.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooJS2C(self):
        expected = get_data(
            path='contracts/KT1E7xh6tvnVMWx7QCZnuWXwcpCJ9UmMWcyK/parameter_ooJS2C.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
