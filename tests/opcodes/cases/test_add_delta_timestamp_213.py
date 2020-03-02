from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestadd_delta_timestamp_213(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_add_delta_timestamp_213(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/add_delta_timestamp.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair -100 100) None')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Some "1970-01-01T00:00:00Z")')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
