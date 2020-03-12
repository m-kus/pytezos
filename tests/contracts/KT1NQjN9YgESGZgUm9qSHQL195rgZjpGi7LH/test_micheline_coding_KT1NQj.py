from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1NQj(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/code_KT1NQj.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1NQj(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/storage_KT1NQj.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooeA7c(self):
        expected = get_data(
            path='contracts/KT1NQjN9YgESGZgUm9qSHQL195rgZjpGi7LH/parameter_ooeA7c.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
