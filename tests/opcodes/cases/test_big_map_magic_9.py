from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestbig_map_magic_9(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_opcode_big_map_magic_9(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/big_map_magic.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Left Unit) (Left (Pair { Elt "1" "one" } { Elt "2" "two" }))')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Left (Pair 0 1))')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
        
        big_map_diff = [{'action': 'alloc', 'big_map': '1', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '1', 'key_hash': 'exprvHK69NiDmfXXw2Gx5x9meBfRp3CBMZ1QjM3UdqoNfUzK3nSpnL', 'key': {'string': '1'}, 'value': {'string': 'one'}}, {'action': 'alloc', 'big_map': '0', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'exprtaPfHX9A3HW7vujsuarwHDXwJYu9hJZvuqUCyoeHLRLPXyDQjW', 'key': {'string': '2'}, 'value': {'string': 'two'}}]
        self.assertCountEqual(big_map_diff, res['result'][2])
