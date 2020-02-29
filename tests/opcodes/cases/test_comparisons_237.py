from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_value


class OpcodeTestcomparisons_237(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_comparisons_237(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/comparisons.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN { -9999999; -1 ; 0 ; 1 ; 9999999 } {}')
        self.assertTrue(res['success'])
        
        type_expr = self.i.ctx.stack[0].type_expr['args'][1]
        expected_expr = michelson_to_micheline('{ { False ; False ; False ; True ; True } ;     { False ; False ; True ; True ; True } ;     { True ; True ; False ; False ; False } ;     { True ; True ; True ; False ; False } ;     { True ; True ; False ; True ; True } ;     { False ; False ; True ; False ; False } }')
        expected_val = parse_value(expected_expr, type_expr)
        self.assertEqual(expected_val, self.i.ctx.stack[0]._val[1])
