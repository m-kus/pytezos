from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestslice_17(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_slice_17(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/slice.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 0 10) (Some "Foo")')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('None')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
