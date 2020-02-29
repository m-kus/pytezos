from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_value


class OpcodeTesttez_add_sub_185(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_tez_add_sub_185(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/tez_add_sub.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 2310000 1010000) None')
        self.assertTrue(res['success'])
        
        type_expr = self.i.ctx.stack[0].type_expr['args'][1]
        expected_expr = michelson_to_micheline('(Some (Pair 3320000 1300000))')
        expected_val = parse_value(expected_expr, type_expr)
        self.assertEqual(expected_val, self.i.ctx.stack[0]._val[1])
