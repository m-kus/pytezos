from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Tj1(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/code_KT1Tj1.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Tj1(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/storage_KT1Tj1.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op1Y8s(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_op1Y8s.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oowehx(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oowehx.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooxyRd(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooxyRd.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooD4De(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooD4De.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oounfN(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oounfN.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
