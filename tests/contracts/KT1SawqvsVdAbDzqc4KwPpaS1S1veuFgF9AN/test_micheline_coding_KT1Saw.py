from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Saw(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/code_KT1Saw.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Saw(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/storage_KT1Saw.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opJ4wD(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opJ4wD.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oogN9U(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oogN9U.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opYPFA(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYPFA.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo6KsN(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oo6KsN.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opYHZ8(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYHZ8.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onfaGG(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_onfaGG.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooRTaE(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_ooRTaE.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
