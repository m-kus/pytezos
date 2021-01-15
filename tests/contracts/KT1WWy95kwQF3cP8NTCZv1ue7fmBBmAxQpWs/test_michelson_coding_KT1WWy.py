from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1WWy(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1WWy(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/code_KT1WWy.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/code_KT1WWy.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1WWy(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/code_KT1WWy.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/code_KT1WWy.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1WWy(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/code_KT1WWy.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1WWy(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/storage_KT1WWy.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/storage_KT1WWy.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1WWy(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/storage_KT1WWy.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/storage_KT1WWy.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1WWy(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/storage_KT1WWy.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onsEnb(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onsEnb.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onsEnb.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onsEnb(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onsEnb.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onsEnb.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onsEnb(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onsEnb.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onp1sJ(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onp1sJ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onp1sJ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onp1sJ(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onp1sJ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onp1sJ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onp1sJ(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onp1sJ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op8wwm(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op8wwm.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op8wwm.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op8wwm(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op8wwm.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op8wwm.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op8wwm(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op8wwm.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooT5FC(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_ooT5FC.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_ooT5FC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooT5FC(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_ooT5FC.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_ooT5FC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooT5FC(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_ooT5FC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_op3ZxR(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op3ZxR.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op3ZxR.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_op3ZxR(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op3ZxR.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op3ZxR.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_op3ZxR(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op3ZxR.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo4hXL(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oo4hXL.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oo4hXL.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo4hXL(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oo4hXL.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oo4hXL.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo4hXL(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oo4hXL.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oopiMi(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oopiMi.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oopiMi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oopiMi(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oopiMi.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oopiMi.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oopiMi(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oopiMi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
