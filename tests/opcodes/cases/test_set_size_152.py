from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestset_size_152(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_set_size_152(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/set_size.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN { 1 ; 2 ; 3 ; 4 ; 5 ; 6 } 111')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('6')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
