from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1DMB(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/code_KT1DMB.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1DMB(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/storage_KT1DMB.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo2fTZ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oo2fTZ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op5cVM(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_op5cVM.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooxMFE(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooxMFE.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oot462(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oot462.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opWUQQ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_opWUQQ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooi5HZ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooi5HZ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
