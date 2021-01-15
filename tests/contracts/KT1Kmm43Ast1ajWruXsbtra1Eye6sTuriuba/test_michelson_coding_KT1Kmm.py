from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Kmm(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Kmm(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/code_KT1Kmm.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/code_KT1Kmm.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Kmm(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/code_KT1Kmm.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/code_KT1Kmm.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Kmm(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/code_KT1Kmm.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Kmm(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/storage_KT1Kmm.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/storage_KT1Kmm.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Kmm(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/storage_KT1Kmm.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/storage_KT1Kmm.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Kmm(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/storage_KT1Kmm.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oon1yX(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oon1yX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oon1yX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oon1yX(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oon1yX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oon1yX.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oon1yX(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oon1yX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooZyyN(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooZyyN.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooZyyN.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooZyyN(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooZyyN.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooZyyN.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooZyyN(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooZyyN.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op8NAr(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_op8NAr.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_op8NAr.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op8NAr(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_op8NAr.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_op8NAr.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op8NAr(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_op8NAr.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo1zTK(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo1zTK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo1zTK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo1zTK(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo1zTK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo1zTK.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo1zTK(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo1zTK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo9EBk(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo9EBk.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo9EBk.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo9EBk(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo9EBk.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo9EBk.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo9EBk(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_oo9EBk.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooksLV(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooksLV.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooksLV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooksLV(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooksLV.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooksLV.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooksLV(self):
        expected = get_data(
            path='contracts/KT1Kmm43Ast1ajWruXsbtra1Eye6sTuriuba/parameter_ooksLV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
