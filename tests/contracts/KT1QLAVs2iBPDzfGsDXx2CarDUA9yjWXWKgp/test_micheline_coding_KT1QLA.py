from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1QLA(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/code_KT1QLA.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1QLA(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/storage_KT1QLA.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opNpQp(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opNpQp.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opQLA4(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opQLA4.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooK7pF(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooK7pF.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oohjwZ(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_oohjwZ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooCesN(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooCesN.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
