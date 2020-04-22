from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1G39(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/code_KT1G39.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1G39(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/storage_KT1G39.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ong4Gv(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ong4Gv.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooqEHd(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooqEHd.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onynir(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onynir.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onn4pk(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_onn4pk.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooYJ85(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooYJ85.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooDRnz(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_ooDRnz.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oophVz(self):
        expected = get_data(
            path='contracts/KT1G393LjojNshvMdf68XQD24Hwjn7xarzNe/parameter_oophVz.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
