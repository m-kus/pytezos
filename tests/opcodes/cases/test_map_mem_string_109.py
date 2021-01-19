from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestmap_mem_string_109(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_map_mem_string_109(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/map_mem_string.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "baz" (Pair { Elt "bar" 4 ; Elt "foo" 11 } None)')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Pair { Elt "bar" 4 ; Elt "foo" 11 } (Some False))')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
