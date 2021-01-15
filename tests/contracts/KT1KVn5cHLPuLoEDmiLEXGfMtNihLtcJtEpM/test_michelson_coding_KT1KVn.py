from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1KVn(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1KVn(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/code_KT1KVn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/code_KT1KVn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1KVn(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/code_KT1KVn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/code_KT1KVn.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1KVn(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/code_KT1KVn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1KVn(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/storage_KT1KVn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/storage_KT1KVn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1KVn(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/storage_KT1KVn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/storage_KT1KVn.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1KVn(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/storage_KT1KVn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oodpad(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oodpad.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oodpad.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oodpad(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oodpad.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oodpad.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oodpad(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oodpad.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op5JXz(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_op5JXz.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_op5JXz.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op5JXz(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_op5JXz.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_op5JXz.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op5JXz(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_op5JXz.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opWTsh(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opWTsh.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opWTsh.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opWTsh(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opWTsh.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opWTsh.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opWTsh(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opWTsh.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oovB4n(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oovB4n.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oovB4n.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oovB4n(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oovB4n.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oovB4n.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oovB4n(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_oovB4n.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opVpjK(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opVpjK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opVpjK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opVpjK(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opVpjK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opVpjK.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opVpjK(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opVpjK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooSTG6(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_ooSTG6.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_ooSTG6.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooSTG6(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_ooSTG6.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_ooSTG6.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooSTG6(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_ooSTG6.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opPcx1(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opPcx1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opPcx1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opPcx1(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opPcx1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opPcx1.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opPcx1(self):
        expected = get_data(
            path='contracts/KT1KVn5cHLPuLoEDmiLEXGfMtNihLtcJtEpM/parameter_opPcx1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
