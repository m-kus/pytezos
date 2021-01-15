from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1VgG(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1VgG(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/code_KT1VgG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/code_KT1VgG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1VgG(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/code_KT1VgG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/code_KT1VgG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1VgG(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/code_KT1VgG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1VgG(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/storage_KT1VgG.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/storage_KT1VgG.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1VgG(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/storage_KT1VgG.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/storage_KT1VgG.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1VgG(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/storage_KT1VgG.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onq1Fe(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onq1Fe.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onq1Fe.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onq1Fe(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onq1Fe.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onq1Fe.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onq1Fe(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onq1Fe.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opNjir(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opNjir.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opNjir.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opNjir(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opNjir.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opNjir.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opNjir(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opNjir.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooAJnK(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooAJnK.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooAJnK.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooAJnK(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooAJnK.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooAJnK.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooAJnK(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooAJnK.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooiPCb(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooiPCb.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooiPCb.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooiPCb(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooiPCb.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooiPCb.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooiPCb(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooiPCb.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onzfvH(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onzfvH.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onzfvH.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onzfvH(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onzfvH.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onzfvH.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onzfvH(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_onzfvH.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opQFws(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opQFws.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opQFws.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opQFws(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opQFws.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opQFws.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opQFws(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_opQFws.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooArK7(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooArK7.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooArK7.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooArK7(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooArK7.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooArK7.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooArK7(self):
        expected = get_data(
            path='contracts/KT1VgGFh674e2En7fQh7U8WHVyWpwUZB4n4Y/parameter_ooArK7.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
