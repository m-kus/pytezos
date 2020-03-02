from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestfirst_195(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_first_195(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/first.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN { 1 ; 2 ; 3 ; 4 } 111')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('1')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
