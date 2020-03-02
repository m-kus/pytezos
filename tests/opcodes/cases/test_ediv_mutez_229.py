from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestediv_mutez_229(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_ediv_mutez_229(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/ediv_mutez.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 10 (Left 10)) (Left None)')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Left (Some (Pair 1 0)))')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
