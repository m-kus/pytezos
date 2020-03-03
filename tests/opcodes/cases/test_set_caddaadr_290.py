from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestset_caddaadr_290(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_set_caddaadr_290(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/set_caddaadr.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN 3000000 (Pair (Pair 1 (Pair 2 (Pair (Pair (Pair 3 0) 4) 5))) 6)')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Pair (Pair 1 (Pair 2 (Pair (Pair (Pair 3 3000000) 4) 5))) 6)')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
