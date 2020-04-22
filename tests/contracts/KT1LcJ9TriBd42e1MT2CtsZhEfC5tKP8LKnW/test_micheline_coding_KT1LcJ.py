from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1LcJ(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/code_KT1LcJ.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1LcJ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/storage_KT1LcJ.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opNs7Z(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opNs7Z.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onhDUH(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onhDUH.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opQ1UQ(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_opQ1UQ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooRxcK(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_ooRxcK.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oob6Lc(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_oob6Lc.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onpzaB(self):
        expected = get_data(
            path='contracts/KT1LcJ9TriBd42e1MT2CtsZhEfC5tKP8LKnW/parameter_onpzaB.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
