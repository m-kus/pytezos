from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestsub_timestamp_delta_217(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_sub_timestamp_delta_217(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/sub_timestamp_delta.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 100 2000000000000000000) 111')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('-1999999999999999900')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
