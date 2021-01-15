from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Tj1(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Tj1(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/code_KT1Tj1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/code_KT1Tj1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Tj1(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/code_KT1Tj1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/code_KT1Tj1.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Tj1(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/code_KT1Tj1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Tj1(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/storage_KT1Tj1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/storage_KT1Tj1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Tj1(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/storage_KT1Tj1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/storage_KT1Tj1.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Tj1(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/storage_KT1Tj1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op1Y8s(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_op1Y8s.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_op1Y8s.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op1Y8s(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_op1Y8s.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_op1Y8s.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op1Y8s(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_op1Y8s.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oowehx(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oowehx.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oowehx.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oowehx(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oowehx.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oowehx.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oowehx(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oowehx.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooxyRd(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooxyRd.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooxyRd.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooxyRd(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooxyRd.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooxyRd.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooxyRd(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooxyRd.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooD4De(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooD4De.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooD4De.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooD4De(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooD4De.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooD4De.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooD4De(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_ooD4De.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oounfN(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oounfN.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oounfN.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oounfN(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oounfN.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oounfN.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oounfN(self):
        expected = get_data(
            path='contracts/KT1Tj1P5c2e9q2ow8wcRc76amJj4njLsLpTw/parameter_oounfN.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
