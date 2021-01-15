from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import michelson_to_micheline
from pytezos.michelson.format import micheline_to_michelson


class MichelsonCodingTestKT1NpC(TestCase):
    
    def setUp(self):
        self.maxDiff = None

    def test_michelson_parse_code_KT1NpC(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/code_KT1NpC.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/code_KT1NpC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_code_KT1NpC(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/code_KT1NpC.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/code_KT1NpC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_code_KT1NpC(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/code_KT1NpC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_storage_KT1NpC(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/storage_KT1NpC.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/storage_KT1NpC.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_storage_KT1NpC(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/storage_KT1NpC.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/storage_KT1NpC.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_storage_KT1NpC(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/storage_KT1NpC.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oofSXx(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oofSXx.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oofSXx.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oofSXx(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oofSXx.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oofSXx.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oofSXx(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oofSXx.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opCGFQ(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opCGFQ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opCGFQ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opCGFQ(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opCGFQ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opCGFQ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opCGFQ(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opCGFQ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_oojsnQ(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oojsnQ.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oojsnQ.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_oojsnQ(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oojsnQ.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oojsnQ.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_oojsnQ(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_oojsnQ.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooKXTr(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooKXTr.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooKXTr.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooKXTr(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooKXTr.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooKXTr.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooKXTr(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooKXTr.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooxskv(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooxskv.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooxskv.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooxskv(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooxskv.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooxskv.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooxskv(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooxskv.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_ooAm3B(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooAm3B.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooAm3B.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_ooAm3B(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooAm3B.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooAm3B.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_ooAm3B(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_ooAm3B.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)

    def test_michelson_parse_parameter_opF6CW(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opF6CW.json')
        actual = michelson_to_micheline(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opF6CW.tz'))
        self.assertEqual(expected, actual)

    def test_michelson_format_parameter_opF6CW(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opF6CW.tz')
        actual = micheline_to_michelson(get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opF6CW.json'), 
            inline=True)
        self.assertEqual(expected, actual)

    def test_michelson_inverse_parameter_opF6CW(self):
        expected = get_data(
            path='contracts/KT1NpCh6tNQDmbmAVbGLxwRBx8jJD4rEFnmC/parameter_opF6CW.json')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
