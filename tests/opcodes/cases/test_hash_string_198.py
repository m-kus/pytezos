from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTesthash_string_198(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_hash_string_198(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/hash_string.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "12345" 0x00')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('0xb4c26c20de52a4eaf0d8a340db47ad8cb1e74049570859c9a9a3952b204c772f')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
