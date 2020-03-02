from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestdign_247(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_dign_247(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/dign.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair (Pair (Pair (Pair 1 2) 3) 4) 5) 0')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('5')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
