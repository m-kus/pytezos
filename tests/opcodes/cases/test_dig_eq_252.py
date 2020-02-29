from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_value


class OpcodeTestdig_eq_252(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_dig_eq_252(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/dig_eq.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 2 (Pair 3 (Pair 12 (Pair 16 (Pair 10 (Pair 14 (Pair 19 (Pair 9 (Pair 18 (Pair 6 (Pair 8 (Pair 11 (Pair 4 (Pair 13 (Pair 15 (Pair 5 1)))))))))))))))) Unit')
        self.assertTrue(res['success'])
        
        type_expr = self.i.ctx.stack[0].type_expr['args'][1]
        expected_expr = michelson_to_micheline('Unit')
        expected_val = parse_value(expected_expr, type_expr)
        self.assertEqual(expected_val, self.i.ctx.stack[0]._val[1])
