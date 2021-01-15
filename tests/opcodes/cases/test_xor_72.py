from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestxor_72(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_xor_72(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/xor.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Right (Pair 42 63)) None')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Some (Right 21))')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
