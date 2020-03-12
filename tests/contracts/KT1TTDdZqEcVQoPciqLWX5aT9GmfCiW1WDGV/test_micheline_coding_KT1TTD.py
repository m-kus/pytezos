from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1TTD(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/code_KT1TTD.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1TTD(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/storage_KT1TTD.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooySj1(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooySj1.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ontKCo(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ontKCo.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooJ4W9(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_ooJ4W9.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op2cp1(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_op2cp1.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onxPie(self):
        expected = get_data(
            path='contracts/KT1TTDdZqEcVQoPciqLWX5aT9GmfCiW1WDGV/parameter_onxPie.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
