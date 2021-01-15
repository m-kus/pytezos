from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1PF3(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1PF3(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/code_KT1PF3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/code_KT1PF3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1PF3(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/code_KT1PF3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/code_KT1PF3.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1PF3(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/code_KT1PF3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1PF3(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/storage_KT1PF3.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/storage_KT1PF3.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1PF3(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/storage_KT1PF3.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/storage_KT1PF3.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1PF3(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/storage_KT1PF3.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oom6TD(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oom6TD.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oom6TD.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oom6TD(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oom6TD.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oom6TD.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oom6TD(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oom6TD.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oog5Rn(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oog5Rn.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oog5Rn.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oog5Rn(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oog5Rn.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oog5Rn.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oog5Rn(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oog5Rn.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oofw5X(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oofw5X.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oofw5X.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oofw5X(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oofw5X.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oofw5X.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oofw5X(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_oofw5X.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opTCKd(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_opTCKd.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_opTCKd.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opTCKd(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_opTCKd.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_opTCKd.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opTCKd(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_opTCKd.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooAUgp(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooAUgp.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooAUgp.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooAUgp(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooAUgp.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooAUgp.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooAUgp(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooAUgp.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooDrNz(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooDrNz.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooDrNz.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooDrNz(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooDrNz.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooDrNz.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooDrNz(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_ooDrNz.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onr1XX(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_onr1XX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_onr1XX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onr1XX(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_onr1XX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_onr1XX.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onr1XX(self):
        expected = get_data(
            path='contracts/KT1PF3SoynnYGUw3diCjETSbTSEZ1LJMXK9F/parameter_onr1XX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
