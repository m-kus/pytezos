from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestsplit_bytes_259(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_split_bytes_259(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/split_bytes.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN 0xddeeff { 0xaa ; 0xbb ; 0xcc }')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('{ 0xaa ; 0xbb ; 0xcc ; 0xdd ; 0xee ; 0xff }')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
