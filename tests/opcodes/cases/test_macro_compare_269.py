from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestmacro_compare_269(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_macro_compare_269(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/macro_compare.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 1000000 2000000) {}')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('{ False ; False ; True ; False ; True }')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
