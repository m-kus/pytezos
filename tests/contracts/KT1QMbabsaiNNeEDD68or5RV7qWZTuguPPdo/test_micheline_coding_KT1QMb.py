from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1QMb(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/code_KT1QMb.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1QMb(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/storage_KT1QMb.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opV9Eg(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opV9Eg.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooA6bY(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooA6bY.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo8A7L(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_oo8A7L.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooh5VX(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooh5VX.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opSvca(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opSvca.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onfEem(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_onfEem.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooeavH(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooeavH.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
