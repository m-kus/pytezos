from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestediv_mutez_231(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_ediv_mutez_231(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/ediv_mutez.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 10 (Left 0)) (Left None)')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Left None)')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
