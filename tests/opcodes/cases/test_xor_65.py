from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestxor_65(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_xor_65(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/xor.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Left (Pair True False)) None')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Some (Left True))')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
