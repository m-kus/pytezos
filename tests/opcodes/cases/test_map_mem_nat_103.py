from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestmap_mem_nat_103(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_map_mem_nat_103(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/map_mem_nat.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN 3 (Pair { Elt 1 4 ; Elt 2 11 } None)')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Pair { Elt 1 4 ; Elt 2 11 } (Some False))')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
