from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Suf(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Suf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/code_KT1Suf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/code_KT1Suf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Suf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/code_KT1Suf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/code_KT1Suf.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Suf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/code_KT1Suf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Suf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/storage_KT1Suf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/storage_KT1Suf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Suf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/storage_KT1Suf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/storage_KT1Suf.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Suf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/storage_KT1Suf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo3zPe(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_oo3zPe.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_oo3zPe.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo3zPe(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_oo3zPe.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_oo3zPe.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo3zPe(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_oo3zPe.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opJtR2(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJtR2.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJtR2.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opJtR2(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJtR2.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJtR2.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opJtR2(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJtR2.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooa5iW(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooa5iW.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooa5iW.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooa5iW(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooa5iW.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooa5iW.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooa5iW(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooa5iW.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooASVX(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooASVX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooASVX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooASVX(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooASVX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooASVX.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooASVX(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooASVX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opJh9L(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJh9L.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJh9L.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opJh9L(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJh9L.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJh9L.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opJh9L(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_opJh9L.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooKbwJ(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooKbwJ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooKbwJ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooKbwJ(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooKbwJ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooKbwJ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooKbwJ(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_ooKbwJ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op6Brf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_op6Brf.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_op6Brf.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op6Brf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_op6Brf.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_op6Brf.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op6Brf(self):
        expected = get_data(
            path='contracts/KT1SufMDx6d2tuVe3n6tSYUBNjtV9GgaLgtV/parameter_op6Brf.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
