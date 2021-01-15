from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Qde(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Qde(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/code_KT1Qde.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/code_KT1Qde.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Qde(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/code_KT1Qde.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/code_KT1Qde.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Qde(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/code_KT1Qde.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Qde(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/storage_KT1Qde.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/storage_KT1Qde.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Qde(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/storage_KT1Qde.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/storage_KT1Qde.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Qde(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/storage_KT1Qde.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo3Zu4(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo3Zu4.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo3Zu4.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo3Zu4(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo3Zu4.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo3Zu4.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo3Zu4(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo3Zu4.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooTYSp(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooTYSp.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooTYSp.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooTYSp(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooTYSp.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooTYSp.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooTYSp(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooTYSp.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oovxpk(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oovxpk.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oovxpk.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oovxpk(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oovxpk.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oovxpk.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oovxpk(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oovxpk.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooWRVq(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooWRVq.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooWRVq.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooWRVq(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooWRVq.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooWRVq.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooWRVq(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooWRVq.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooDitX(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooDitX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooDitX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooDitX(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooDitX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooDitX.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooDitX(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_ooDitX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo7BsA(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo7BsA.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo7BsA.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo7BsA(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo7BsA.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo7BsA.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo7BsA(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_oo7BsA.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_onncXB(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_onncXB.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_onncXB.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_onncXB(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_onncXB.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_onncXB.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_onncXB(self):
        expected = get_data(
            path='contracts/KT1QdevirZq7PpMgVFWP6QVRSGbSsdHEUjgt/parameter_onncXB.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
