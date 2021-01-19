from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestpair_id_28(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_pair_id_28(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/pair_id.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair True False) None')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Some (Pair True False))')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
