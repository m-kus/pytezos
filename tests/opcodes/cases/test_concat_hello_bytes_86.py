from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestconcat_hello_bytes_86(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_concat_hello_bytes_86(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/concat_hello_bytes.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN { 0xcd } {}')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('{ 0xffcd }')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
