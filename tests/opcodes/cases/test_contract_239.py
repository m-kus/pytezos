from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestcontract_239(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_contract_239(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/contract.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "tz1cxcwwnzENRdhe2Kb8ZdTrdNy4bFNyScx5" Unit')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('Unit')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
