from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTesthash_string_197(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_hash_string_197(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/hash_string.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "abcdefg" 0x00')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('0x46fdbcb4ea4eadad5615cdaa17d67f783e01e21149ce2b27de497600b4cd8f4e')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
