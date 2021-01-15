from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1QMb(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1QMb(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/code_KT1QMb.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/code_KT1QMb.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1QMb(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/code_KT1QMb.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/code_KT1QMb.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1QMb(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/code_KT1QMb.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1QMb(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/storage_KT1QMb.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/storage_KT1QMb.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1QMb(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/storage_KT1QMb.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/storage_KT1QMb.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1QMb(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/storage_KT1QMb.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opV9Eg(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opV9Eg.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opV9Eg.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opV9Eg(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opV9Eg.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opV9Eg.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opV9Eg(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opV9Eg.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooA6bY(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooA6bY.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooA6bY.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooA6bY(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooA6bY.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooA6bY.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooA6bY(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooA6bY.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo8A7L(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_oo8A7L.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_oo8A7L.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo8A7L(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_oo8A7L.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_oo8A7L.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo8A7L(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_oo8A7L.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooh5VX(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooh5VX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooh5VX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooh5VX(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooh5VX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooh5VX.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooh5VX(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooh5VX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opSvca(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opSvca.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opSvca.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opSvca(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opSvca.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opSvca.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opSvca(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_opSvca.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onfEem(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_onfEem.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_onfEem.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onfEem(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_onfEem.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_onfEem.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onfEem(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_onfEem.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooeavH(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooeavH.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooeavH.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooeavH(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooeavH.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooeavH.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooeavH(self):
        expected = get_data(
            path='contracts/KT1QMbabsaiNNeEDD68or5RV7qWZTuguPPdo/parameter_ooeavH.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
