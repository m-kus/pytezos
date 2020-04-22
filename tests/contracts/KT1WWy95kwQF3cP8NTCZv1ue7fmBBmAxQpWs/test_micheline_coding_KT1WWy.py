from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1WWy(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/code_KT1WWy.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1WWy(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/storage_KT1WWy.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onsEnb(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onsEnb.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onp1sJ(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_onp1sJ.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op8wwm(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op8wwm.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooT5FC(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_ooT5FC.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_op3ZxR(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_op3ZxR.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oo4hXL(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oo4hXL.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oopiMi(self):
        expected = get_data(
            path='contracts/KT1WWy95kwQF3cP8NTCZv1ue7fmBBmAxQpWs/parameter_oopiMi.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
