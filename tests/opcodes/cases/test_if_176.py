from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestif_176(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_if_176(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/if.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN False None')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Some False)')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
