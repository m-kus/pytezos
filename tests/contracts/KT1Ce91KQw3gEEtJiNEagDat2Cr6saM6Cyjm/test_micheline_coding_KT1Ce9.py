from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Ce9(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/code_KT1Ce9.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Ce9(self):
        expected = get_data(
            path='contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/storage_KT1Ce9.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooxrXG(self):
        expected = get_data(
            path='contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooxrXG.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oopaer(self):
        expected = get_data(
            path='contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_oopaer.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opEbxt(self):
        expected = get_data(
            path='contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opEbxt.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooYaRG(self):
        expected = get_data(
            path='contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooYaRG.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ony5uQ(self):
        expected = get_data(
            path='contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ony5uQ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooWRdi(self):
        expected = get_data(
            path='contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_ooWRdi.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opZvXV(self):
        expected = get_data(
            path='contracts/KT1Ce91KQw3gEEtJiNEagDat2Cr6saM6Cyjm/parameter_opZvXV.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
