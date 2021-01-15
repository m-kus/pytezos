from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1MUt(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1MUt(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/code_KT1MUt.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/code_KT1MUt.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1MUt(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/code_KT1MUt.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/code_KT1MUt.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1MUt(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/code_KT1MUt.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1MUt(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/storage_KT1MUt.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/storage_KT1MUt.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1MUt(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/storage_KT1MUt.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/storage_KT1MUt.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1MUt(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/storage_KT1MUt.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooaeRJ(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooaeRJ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooaeRJ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooaeRJ(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooaeRJ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooaeRJ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooaeRJ(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooaeRJ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op6E1L(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op6E1L.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op6E1L.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op6E1L(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op6E1L.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op6E1L.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op6E1L(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op6E1L.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op16Ra(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op16Ra.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op16Ra.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op16Ra(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op16Ra.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op16Ra.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op16Ra(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_op16Ra.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onnwwM(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_onnwwM.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_onnwwM.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onnwwM(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_onnwwM.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_onnwwM.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onnwwM(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_onnwwM.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ookN7L(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ookN7L.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ookN7L.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ookN7L(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ookN7L.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ookN7L.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ookN7L(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ookN7L.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooqMbo(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooqMbo.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooqMbo.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooqMbo(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooqMbo.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooqMbo.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooqMbo(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ooqMbo.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ongS8k(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ongS8k.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ongS8k.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ongS8k(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ongS8k.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ongS8k.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ongS8k(self):
        expected = get_data(
            path='contracts/KT1MUtNy8bVdwXXaiH2qPAvB6R7Nq9k8BtZg/parameter_ongS8k.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
