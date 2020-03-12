from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Kmm(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/code_KT1Kmm.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Kmm(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/storage_KT1Kmm.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oon1yX(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oon1yX.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooZyyN(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooZyyN.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op8NAr(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_op8NAr.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo1zTK(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo1zTK.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo9EBk(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo9EBk.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooksLV(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooksLV.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
