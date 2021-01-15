from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1DMB(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1DMB(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/code_KT1DMB.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/code_KT1DMB.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1DMB(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/code_KT1DMB.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/code_KT1DMB.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1DMB(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/code_KT1DMB.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1DMB(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/storage_KT1DMB.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/storage_KT1DMB.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1DMB(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/storage_KT1DMB.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/storage_KT1DMB.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1DMB(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/storage_KT1DMB.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo2fTZ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oo2fTZ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oo2fTZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo2fTZ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oo2fTZ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oo2fTZ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo2fTZ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oo2fTZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op5cVM(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_op5cVM.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_op5cVM.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op5cVM(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_op5cVM.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_op5cVM.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op5cVM(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_op5cVM.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooxMFE(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooxMFE.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooxMFE.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooxMFE(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooxMFE.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooxMFE.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooxMFE(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooxMFE.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oot462(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oot462.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oot462.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oot462(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oot462.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oot462.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oot462(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_oot462.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opWUQQ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_opWUQQ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_opWUQQ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opWUQQ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_opWUQQ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_opWUQQ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opWUQQ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_opWUQQ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooi5HZ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooi5HZ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooi5HZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooi5HZ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooi5HZ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooi5HZ.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooi5HZ(self):
        expected = get_data(
            path='contracts/KT1DMBFZ4f6PUHoG3Du5VXEW4XqKfBfoeWJs/parameter_ooi5HZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
