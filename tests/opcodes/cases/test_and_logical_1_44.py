from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestand_logical_1_44(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_and_logical_1_44(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/and_logical_1.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair False False) False')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('False')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
