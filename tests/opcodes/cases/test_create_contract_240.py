from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestcreate_contract_240(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_create_contract_240(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/create_contract.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN Unit None')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Some "KT1Mjjcb6tmSsLm7Cb3DSQszePjfchPM4Uxm")')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
