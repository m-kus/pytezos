from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestor_40(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_or_40(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/or.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair False False) None')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Some False)')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
