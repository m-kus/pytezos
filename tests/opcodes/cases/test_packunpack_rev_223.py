from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestpackunpack_rev_223(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_packunpack_rev_223(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/packunpack_rev.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair -1  (Pair 1 (Pair "foobar" (Pair 0x00AABBCC (Pair 1000 (Pair False (Pair "tz1cxcwwnzENRdhe2Kb8ZdTrdNy4bFNyScx5" (Pair "2019-09-09T08:35:33Z" "tz1cxcwwnzENRdhe2Kb8ZdTrdNy4bFNyScx5")))))))) Unit')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('Unit')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
