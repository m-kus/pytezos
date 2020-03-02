from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestsub_timestamp_delta_216(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_sub_timestamp_delta_216(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/sub_timestamp_delta.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 100 -100) 111')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('"1970-01-01T00:03:20Z"')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
