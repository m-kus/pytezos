from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1RV1(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1RV1(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/code_KT1RV1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/code_KT1RV1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1RV1(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/code_KT1RV1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/code_KT1RV1.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1RV1(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/code_KT1RV1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1RV1(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/storage_KT1RV1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/storage_KT1RV1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1RV1(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/storage_KT1RV1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/storage_KT1RV1.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1RV1(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/storage_KT1RV1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op6A3j(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op6A3j.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op6A3j.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op6A3j(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op6A3j.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op6A3j.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op6A3j(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op6A3j.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onoZj3(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onoZj3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onoZj3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onoZj3(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onoZj3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onoZj3.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onoZj3(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onoZj3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooDZxK(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooDZxK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooDZxK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooDZxK(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooDZxK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooDZxK.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooDZxK(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooDZxK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opFUTY(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_opFUTY.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_opFUTY.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opFUTY(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_opFUTY.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_opFUTY.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opFUTY(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_opFUTY.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onj3Qf(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onj3Qf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onj3Qf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onj3Qf(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onj3Qf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onj3Qf.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onj3Qf(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_onj3Qf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op3Rex(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op3Rex.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op3Rex.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op3Rex(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op3Rex.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op3Rex.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op3Rex(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_op3Rex.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooK1di(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooK1di.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooK1di.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooK1di(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooK1di.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooK1di.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooK1di(self):
        expected = get_data(
            path='contracts/KT1RV1EidsuGckfgLFtDjStSdgbRtyf44jTn/parameter_ooK1di.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
