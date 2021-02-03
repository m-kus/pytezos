from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestself_with_entrypoint_256(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_self_with_entrypoint_256(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/self_with_entrypoint.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Left (Left 0)) Unit')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('Unit')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
