from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestadd_delta_timestamp_214(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_add_delta_timestamp_214(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/add_delta_timestamp.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 0 "1970-01-01T00:00:00Z") None')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Some "1970-01-01T00:00:00Z")')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
