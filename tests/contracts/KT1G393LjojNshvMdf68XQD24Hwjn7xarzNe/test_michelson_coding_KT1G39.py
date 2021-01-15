from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1G39(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1G39(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/code_KT1G39.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/code_KT1G39.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1G39(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/code_KT1G39.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/code_KT1G39.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1G39(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/code_KT1G39.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1G39(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/storage_KT1G39.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/storage_KT1G39.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1G39(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/storage_KT1G39.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/storage_KT1G39.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1G39(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/storage_KT1G39.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ong4Gv(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ong4Gv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ong4Gv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ong4Gv(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ong4Gv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ong4Gv.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ong4Gv(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ong4Gv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooqEHd(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooqEHd.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooqEHd.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooqEHd(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooqEHd.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooqEHd.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooqEHd(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooqEHd.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onynir(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onynir.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onynir.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onynir(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onynir.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onynir.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onynir(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onynir.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onn4pk(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onn4pk.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onn4pk.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onn4pk(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onn4pk.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onn4pk.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onn4pk(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onn4pk.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooYJ85(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooYJ85.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooYJ85.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooYJ85(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooYJ85.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooYJ85.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooYJ85(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooYJ85.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooDRnz(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooDRnz.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooDRnz.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooDRnz(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooDRnz.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooDRnz.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooDRnz(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooDRnz.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oophVz(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_oophVz.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_oophVz.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oophVz(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_oophVz.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_oophVz.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oophVz(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_oophVz.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
