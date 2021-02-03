from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestlist_iter_140(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_list_iter_140(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/list_iter.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN { 10 ; 2 ; 1 } 0')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('20')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
