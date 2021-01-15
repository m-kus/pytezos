from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1AxG(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1AxG(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/code_KT1AxG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/code_KT1AxG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1AxG(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/code_KT1AxG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/code_KT1AxG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1AxG(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/code_KT1AxG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1AxG(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/storage_KT1AxG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/storage_KT1AxG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1AxG(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/storage_KT1AxG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/storage_KT1AxG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1AxG(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/storage_KT1AxG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op81ij(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_op81ij.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_op81ij.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op81ij(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_op81ij.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_op81ij.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op81ij(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_op81ij.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onyNJA(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onyNJA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onyNJA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onyNJA(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onyNJA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onyNJA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onyNJA(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onyNJA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ont4Rq(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ont4Rq.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ont4Rq.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ont4Rq(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ont4Rq.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ont4Rq.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ont4Rq(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ont4Rq.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opSFzK(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_opSFzK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_opSFzK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opSFzK(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_opSFzK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_opSFzK.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opSFzK(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_opSFzK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onx2eB(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onx2eB.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onx2eB.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onx2eB(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onx2eB.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onx2eB.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onx2eB(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_onx2eB.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooySE4(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooySE4.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooySE4.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooySE4(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooySE4.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooySE4.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooySE4(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooySE4.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooGd3B(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooGd3B.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooGd3B.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooGd3B(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooGd3B.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooGd3B.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooGd3B(self):
        expected = get_data(
            path='contracts/KT1AxGnZL9YzmXZh1Lc4dHhznAeJAQCfML25/parameter_ooGd3B.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
