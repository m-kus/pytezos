from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestget_map_value_170(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_get_map_value_170(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/get_map_value.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "hello" (Pair None { Elt "hello" "hi" })')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Pair (Some "hi") { Elt "hello" "hi" })')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
