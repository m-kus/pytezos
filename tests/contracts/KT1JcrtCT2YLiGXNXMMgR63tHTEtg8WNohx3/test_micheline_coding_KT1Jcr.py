from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Jcr(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/code_KT1Jcr.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Jcr(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/storage_KT1Jcr.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opXBki(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opXBki.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo1W9F(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1W9F.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo1FDX(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1FDX.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oohTVV(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oohTVV.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opQZ7h(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opQZ7h.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opAmZ9(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opAmZ9.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oodNXi(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oodNXi.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
