from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestbuild_list_262(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_build_list_262(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/build_list.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN 10 {}')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('{ 0 ; 1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7 ; 8 ; 9 ; 10 }')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
