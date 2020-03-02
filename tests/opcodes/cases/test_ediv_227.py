from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestediv_227(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_ediv_227(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/ediv.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 10 0) (Pair None (Pair None (Pair None None)))')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Pair None (Pair None (Pair None None)))')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
