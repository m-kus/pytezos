from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_value


class OpcodeTestmap_iter_174(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_map_iter_174(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/map_iter.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN { Elt 1 1 ; Elt 2 100 } (Pair 0 0)')
        self.assertTrue(res['success'])
        
        type_expr = self.i.ctx.stack[0].type_expr['args'][1]
        expected_expr = michelson_to_micheline('(Pair 3 101)')
        expected_val = parse_value(expected_expr, type_expr)
        self.assertEqual(expected_val, self.i.ctx.stack[0]._val[1])
