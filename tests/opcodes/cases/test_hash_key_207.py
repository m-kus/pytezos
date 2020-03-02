from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTesthash_key_207(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_hash_key_207(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/hash_key.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "edpkuBknW28nW72KG6RoHtYW7p12T6GKc7nAbwYX5m8Wd9sDVC9yav" None')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Some "tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx")')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
