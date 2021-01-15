from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Saw(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Saw(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/code_KT1Saw.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/code_KT1Saw.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Saw(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/code_KT1Saw.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/code_KT1Saw.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Saw(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/code_KT1Saw.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Saw(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/storage_KT1Saw.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/storage_KT1Saw.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Saw(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/storage_KT1Saw.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/storage_KT1Saw.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Saw(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/storage_KT1Saw.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opJ4wD(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opJ4wD.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opJ4wD.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opJ4wD(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opJ4wD.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opJ4wD.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opJ4wD(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opJ4wD.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oogN9U(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oogN9U.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oogN9U.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oogN9U(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oogN9U.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oogN9U.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oogN9U(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oogN9U.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opYPFA(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYPFA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYPFA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opYPFA(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYPFA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYPFA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opYPFA(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYPFA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo6KsN(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oo6KsN.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oo6KsN.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo6KsN(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oo6KsN.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oo6KsN.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo6KsN(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_oo6KsN.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opYHZ8(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYHZ8.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYHZ8.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opYHZ8(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYHZ8.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYHZ8.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opYHZ8(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_opYHZ8.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onfaGG(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_onfaGG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_onfaGG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onfaGG(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_onfaGG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_onfaGG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onfaGG(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_onfaGG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooRTaE(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_ooRTaE.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_ooRTaE.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooRTaE(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_ooRTaE.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_ooRTaE.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooRTaE(self):
        expected = get_data(
            path='contracts/KT1SawqvsVdAbDzqc4KwPpaS1S1veuFgF9AN/parameter_ooRTaE.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
