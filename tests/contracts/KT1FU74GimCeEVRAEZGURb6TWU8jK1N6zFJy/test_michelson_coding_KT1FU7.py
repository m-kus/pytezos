from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1FU7(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1FU7(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/code_KT1FU7.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/code_KT1FU7.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1FU7(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/code_KT1FU7.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/code_KT1FU7.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1FU7(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/code_KT1FU7.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1FU7(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/storage_KT1FU7.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/storage_KT1FU7.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1FU7(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/storage_KT1FU7.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/storage_KT1FU7.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1FU7(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/storage_KT1FU7.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onubKJ(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onubKJ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onubKJ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onubKJ(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onubKJ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onubKJ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onubKJ(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onubKJ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opGq1o(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_opGq1o.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_opGq1o.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opGq1o(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_opGq1o.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_opGq1o.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opGq1o(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_opGq1o.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onzwnR(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onzwnR.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onzwnR.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onzwnR(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onzwnR.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onzwnR.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onzwnR(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onzwnR.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooFdu3(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooFdu3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooFdu3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooFdu3(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooFdu3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooFdu3.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooFdu3(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooFdu3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooUc6Z(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooUc6Z.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooUc6Z.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooUc6Z(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooUc6Z.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooUc6Z.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooUc6Z(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_ooUc6Z.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onkkzM(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onkkzM.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onkkzM.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onkkzM(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onkkzM.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onkkzM.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onkkzM(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_onkkzM.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op9zfX(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_op9zfX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_op9zfX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op9zfX(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_op9zfX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_op9zfX.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op9zfX(self):
        expected = get_data(
            path='contracts/KT1FU74GimCeEVRAEZGURb6TWU8jK1N6zFJy/parameter_op9zfX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
