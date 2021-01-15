from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1XRw(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1XRw(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/code_KT1XRw.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/code_KT1XRw.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1XRw(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/code_KT1XRw.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/code_KT1XRw.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1XRw(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/code_KT1XRw.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1XRw(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/storage_KT1XRw.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/storage_KT1XRw.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1XRw(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/storage_KT1XRw.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/storage_KT1XRw.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1XRw(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/storage_KT1XRw.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opAqc9(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opAqc9.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opAqc9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opAqc9(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opAqc9.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opAqc9.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opAqc9(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opAqc9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooZibz(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooZibz.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooZibz.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooZibz(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooZibz.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooZibz.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooZibz(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooZibz.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oodMWj(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_oodMWj.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_oodMWj.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oodMWj(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_oodMWj.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_oodMWj.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oodMWj(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_oodMWj.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooVH4y(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooVH4y.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooVH4y.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooVH4y(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooVH4y.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooVH4y.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooVH4y(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooVH4y.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opVkzg(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opVkzg.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opVkzg.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opVkzg(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opVkzg.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opVkzg.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opVkzg(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opVkzg.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooh2Qs(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooh2Qs.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooh2Qs.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooh2Qs(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooh2Qs.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooh2Qs.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooh2Qs(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooh2Qs.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooTejB(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooTejB.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooTejB.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooTejB(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooTejB.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooTejB.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooTejB(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooTejB.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
