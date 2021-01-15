from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTesthash_string_197(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_hash_string_197(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/hash_string.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "abcdefg" 0x00')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('0x46fdbcb4ea4eadad5615cdaa17d67f783e01e21149ce2b27de497600b4cd8f4e')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
