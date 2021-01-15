from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1TEy(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1TEy(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/code_KT1TEy.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/code_KT1TEy.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1TEy(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/code_KT1TEy.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/code_KT1TEy.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1TEy(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/code_KT1TEy.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1TEy(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/storage_KT1TEy.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/storage_KT1TEy.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1TEy(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/storage_KT1TEy.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/storage_KT1TEy.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1TEy(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/storage_KT1TEy.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooSJeE(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_ooSJeE.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_ooSJeE.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooSJeE(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_ooSJeE.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_ooSJeE.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooSJeE(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_ooSJeE.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opKSUG(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_opKSUG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_opKSUG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opKSUG(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_opKSUG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_opKSUG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opKSUG(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_opKSUG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ootApt(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_ootApt.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_ootApt.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ootApt(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_ootApt.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_ootApt.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ootApt(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_ootApt.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo7dXA(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_oo7dXA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_oo7dXA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo7dXA(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_oo7dXA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_oo7dXA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo7dXA(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_oo7dXA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opJMM9(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_opJMM9.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_opJMM9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opJMM9(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_opJMM9.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_opJMM9.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opJMM9(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_opJMM9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op6KiD(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_op6KiD.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_op6KiD.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op6KiD(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_op6KiD.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_op6KiD.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op6KiD(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_op6KiD.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onkFnb(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_onkFnb.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_onkFnb.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onkFnb(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_onkFnb.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_onkFnb.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onkFnb(self):
        expected = get_data(
            path='contracts/KT1TEyRcaJi39jgj4Uuz7VD6Jmn6CDDADv4x/parameter_onkFnb.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
