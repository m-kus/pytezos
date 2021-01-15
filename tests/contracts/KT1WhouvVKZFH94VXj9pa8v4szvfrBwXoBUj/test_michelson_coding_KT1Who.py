from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Who(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Who(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/code_KT1Who.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/code_KT1Who.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Who(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/code_KT1Who.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/code_KT1Who.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Who(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/code_KT1Who.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Who(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/storage_KT1Who.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/storage_KT1Who.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Who(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/storage_KT1Who.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/storage_KT1Who.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Who(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/storage_KT1Who.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oozD2D(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oozD2D.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oozD2D.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oozD2D(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oozD2D.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oozD2D.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oozD2D(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oozD2D.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opECec(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opECec.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opECec.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opECec(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opECec.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opECec.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opECec(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opECec.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooaH79(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooaH79.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooaH79.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooaH79(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooaH79.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooaH79.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooaH79(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooaH79.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oonu1M(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oonu1M.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oonu1M.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oonu1M(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oonu1M.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oonu1M.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oonu1M(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_oonu1M.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onvCMZ(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_onvCMZ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_onvCMZ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onvCMZ(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_onvCMZ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_onvCMZ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onvCMZ(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_onvCMZ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooqB2A(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooqB2A.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooqB2A.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooqB2A(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooqB2A.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooqB2A.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooqB2A(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_ooqB2A.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opGvHd(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opGvHd.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opGvHd.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opGvHd(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opGvHd.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opGvHd.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opGvHd(self):
        expected = get_data(
            path='contracts/KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj/parameter_opGvHd.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
