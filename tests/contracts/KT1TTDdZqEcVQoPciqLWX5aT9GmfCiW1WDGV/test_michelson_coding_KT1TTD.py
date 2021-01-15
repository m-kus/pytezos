from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1TTD(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1TTD(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/code_KT1TTD.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/code_KT1TTD.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1TTD(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/code_KT1TTD.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/code_KT1TTD.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1TTD(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/code_KT1TTD.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1TTD(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/storage_KT1TTD.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/storage_KT1TTD.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1TTD(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/storage_KT1TTD.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/storage_KT1TTD.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1TTD(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/storage_KT1TTD.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooySj1(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooySj1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooySj1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooySj1(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooySj1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooySj1.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooySj1(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooySj1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ontKCo(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ontKCo.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ontKCo.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ontKCo(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ontKCo.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ontKCo.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ontKCo(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ontKCo.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooJ4W9(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooJ4W9.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooJ4W9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooJ4W9(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooJ4W9.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooJ4W9.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooJ4W9(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooJ4W9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op2cp1(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_op2cp1.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_op2cp1.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op2cp1(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_op2cp1.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_op2cp1.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op2cp1(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_op2cp1.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onxPie(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_onxPie.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_onxPie.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onxPie(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_onxPie.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_onxPie.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onxPie(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_onxPie.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
