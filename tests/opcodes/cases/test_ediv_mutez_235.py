from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestediv_mutez_235(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_ediv_mutez_235(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/ediv_mutez.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 5 (Right 10)) (Left None)')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Right (Some (Pair 0 5)))')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
