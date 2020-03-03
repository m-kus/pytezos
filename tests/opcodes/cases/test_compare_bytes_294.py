from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestcompare_bytes_294(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_compare_bytes_294(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/compare_bytes.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair 0x33 0x33) {}')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('{ True ; False ; False ; True ; True }')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
