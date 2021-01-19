from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTesthash_string_198(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_hash_string_198(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/hash_string.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "12345" 0x00')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('0xb4c26c20de52a4eaf0d8a340db47ad8cb1e74049570859c9a9a3952b204c772f')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
