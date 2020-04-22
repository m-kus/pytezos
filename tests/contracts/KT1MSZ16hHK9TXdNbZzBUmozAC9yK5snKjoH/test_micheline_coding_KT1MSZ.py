from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1MSZ(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/code_KT1MSZ.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1MSZ(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/storage_KT1MSZ.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onwqBB(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_onwqBB.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooYBLf(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_ooYBLf.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opTdLV(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opTdLV.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oon8Ss(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oon8Ss.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oooRqc(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oooRqc.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oobXfo(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_oobXfo.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opJKvo(self):
        expected = get_data(
            path='contracts/KT1MSZ16hHK9TXdNbZzBUmozAC9yK5snKjoH/parameter_opJKvo.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
