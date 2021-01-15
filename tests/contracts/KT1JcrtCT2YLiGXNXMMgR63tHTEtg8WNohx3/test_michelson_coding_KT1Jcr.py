from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1Jcr(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1Jcr(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/code_KT1Jcr.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/code_KT1Jcr.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1Jcr(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/code_KT1Jcr.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/code_KT1Jcr.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1Jcr(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/code_KT1Jcr.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1Jcr(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/storage_KT1Jcr.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/storage_KT1Jcr.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1Jcr(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/storage_KT1Jcr.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/storage_KT1Jcr.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1Jcr(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/storage_KT1Jcr.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opXBki(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opXBki.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opXBki.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opXBki(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opXBki.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opXBki.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opXBki(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opXBki.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo1W9F(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1W9F.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1W9F.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo1W9F(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1W9F.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1W9F.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo1W9F(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1W9F.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oo1FDX(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1FDX.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1FDX.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oo1FDX(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1FDX.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1FDX.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oo1FDX(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oo1FDX.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oohTVV(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oohTVV.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oohTVV.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oohTVV(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oohTVV.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oohTVV.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oohTVV(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oohTVV.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opQZ7h(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opQZ7h.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opQZ7h.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opQZ7h(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opQZ7h.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opQZ7h.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opQZ7h(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opQZ7h.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opAmZ9(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opAmZ9.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opAmZ9.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opAmZ9(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opAmZ9.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opAmZ9.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opAmZ9(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_opAmZ9.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oodNXi(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oodNXi.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oodNXi.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oodNXi(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oodNXi.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oodNXi.json'),
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oodNXi(self):
        expected = get_data(
            path='contracts/KT1JcrtCT2YLiGXNXMMgR63tHTEtg8WNohx3/parameter_oodNXi.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
