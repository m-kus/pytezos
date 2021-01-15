from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestif_some_199(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_if_some_199(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/if_some.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Some "hello") "?"')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('"hello"')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
