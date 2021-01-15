from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1LiG(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1LiG(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/code_KT1LiG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/code_KT1LiG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1LiG(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/code_KT1LiG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/code_KT1LiG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1LiG(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/code_KT1LiG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1LiG(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/storage_KT1LiG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/storage_KT1LiG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1LiG(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/storage_KT1LiG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/storage_KT1LiG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1LiG(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/storage_KT1LiG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oobdt2(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_oobdt2.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_oobdt2.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oobdt2(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_oobdt2.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_oobdt2.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oobdt2(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_oobdt2.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op4Zwd(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_op4Zwd.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_op4Zwd.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op4Zwd(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_op4Zwd.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_op4Zwd.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op4Zwd(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_op4Zwd.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oneikC(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_oneikC.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_oneikC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oneikC(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_oneikC.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_oneikC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oneikC(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_oneikC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onrRt3(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_onrRt3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_onrRt3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onrRt3(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_onrRt3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_onrRt3.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onrRt3(self):
        expected = get_data(
            path='contracts/KT1LiGjQW3RZeurKpuuaMJyFG1P7Yje1BCb1/parameter_onrRt3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
