from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestaddress_238(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_address_238(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/address.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "tz1cxcwwnzENRdhe2Kb8ZdTrdNy4bFNyScx5" None')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Some "tz1cxcwwnzENRdhe2Kb8ZdTrdNy4bFNyScx5")')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
