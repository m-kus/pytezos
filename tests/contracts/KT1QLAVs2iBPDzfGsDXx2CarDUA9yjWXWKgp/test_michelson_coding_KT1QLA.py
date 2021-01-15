from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1QLA(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1QLA(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/code_KT1QLA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/code_KT1QLA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1QLA(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/code_KT1QLA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/code_KT1QLA.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1QLA(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/code_KT1QLA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1QLA(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/storage_KT1QLA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/storage_KT1QLA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1QLA(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/storage_KT1QLA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/storage_KT1QLA.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1QLA(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/storage_KT1QLA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opNpQp(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opNpQp.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opNpQp.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opNpQp(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opNpQp.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opNpQp.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opNpQp(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opNpQp.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opQLA4(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opQLA4.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opQLA4.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opQLA4(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opQLA4.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opQLA4.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opQLA4(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_opQLA4.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooK7pF(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooK7pF.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooK7pF.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooK7pF(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooK7pF.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooK7pF.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooK7pF(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooK7pF.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oohjwZ(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_oohjwZ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_oohjwZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oohjwZ(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_oohjwZ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_oohjwZ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oohjwZ(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_oohjwZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooCesN(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooCesN.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooCesN.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooCesN(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooCesN.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooCesN.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooCesN(self):
        expected = get_data(
            path='contracts/KT1QLAVs2iBPDzfGsDXx2CarDUA9yjWXWKgp/parameter_ooCesN.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
