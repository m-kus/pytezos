from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestmap_id_96(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_map_id_96(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/map_id.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN { Elt 0 0 } {}')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('{ Elt 0 0 }')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
