from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestbig_map_mem_nat_117(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_big_map_mem_nat_117(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/big_map_mem_nat.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN 2 (Pair { Elt 1 4 ; Elt 2 11 } None)')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Pair 0 (Some True))')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
