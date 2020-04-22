from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1FU7(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/code_KT1FU7.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1FU7(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/storage_KT1FU7.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onubKJ(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onubKJ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opGq1o(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_opGq1o.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onzwnR(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onzwnR.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooFdu3(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooFdu3.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooUc6Z(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooUc6Z.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onkkzM(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onkkzM.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op9zfX(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_op9zfX.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
