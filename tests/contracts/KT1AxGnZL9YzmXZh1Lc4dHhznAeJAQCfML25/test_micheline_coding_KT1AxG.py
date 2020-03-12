from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1AxG(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/code_KT1AxG.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1AxG(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/storage_KT1AxG.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op81ij(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_op81ij.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onyNJA(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onyNJA.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ont4Rq(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ont4Rq.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opSFzK(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_opSFzK.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onx2eB(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onx2eB.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooySE4(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooySE4.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooGd3B(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooGd3B.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
