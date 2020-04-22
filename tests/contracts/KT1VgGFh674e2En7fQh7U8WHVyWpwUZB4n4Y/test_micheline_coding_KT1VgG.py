from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1VgG(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/code_KT1VgG.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1VgG(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/storage_KT1VgG.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onq1Fe(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onq1Fe.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opNjir(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opNjir.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooAJnK(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooAJnK.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooiPCb(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooiPCb.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_onzfvH(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onzfvH.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opQFws(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opQFws.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooArK7(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooArK7.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
