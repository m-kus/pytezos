from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestbig_map_magic_9(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_opcode_big_map_magic_9(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/big_map_magic.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Left Unit) (Left (Pair { Elt "1" "one" } { Elt "2" "two" }))')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Left (Pair 0 1))')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
        
        big_map_diff = [{'action': 'alloc', 'big_map': '1', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '1', 'key_hash': 'exprvHK69NiDmfXXw2Gx5x9meBfRp3CBMZ1QjM3UdqoNfUzK3nSpnL', 'key': {'string': '1'}, 'value': {'string': 'one'}}, {'action': 'alloc', 'big_map': '0', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'exprtaPfHX9A3HW7vujsuarwHDXwJYu9hJZvuqUCyoeHLRLPXyDQjW', 'key': {'string': '2'}, 'value': {'string': 'two'}}]
        self.assertCountEqual(big_map_diff, res['result']['big_map_diff'])
