from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1WQA(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/code_KT1WQA.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1WQA(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/storage_KT1WQA.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onjMGH(self):
        expected = get_data(
            path='contracts/KT1WQAW1sRaykMPYEPpqiL4nrYvdnb8SWTV7/parameter_onjMGH.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
