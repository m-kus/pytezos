from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestadd_timestamp_delta_209(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_add_timestamp_delta_209(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/add_timestamp_delta.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 100 100) None')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Some "1970-01-01T00:03:20Z")')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
