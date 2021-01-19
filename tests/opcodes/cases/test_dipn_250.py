from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestdipn_250(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_dipn_250(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/dipn.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair (Pair (Pair (Pair 1 2) 3) 4) 5) 0')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('6')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
