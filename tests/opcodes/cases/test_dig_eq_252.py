from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestdig_eq_252(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_dig_eq_252(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/dig_eq.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 2 (Pair 3 (Pair 12 (Pair 16 (Pair 10 (Pair 14 (Pair 19 (Pair 9 (Pair 18 (Pair 6 (Pair 8 (Pair 11 (Pair 4 (Pair 13 (Pair 15 (Pair 5 1)))))))))))))))) Unit')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('Unit')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
