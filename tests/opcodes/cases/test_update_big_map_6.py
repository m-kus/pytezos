from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestupdate_big_map_6(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_opcode_update_big_map_6(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/update_big_map.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN { Elt "3" None } (Pair { Elt "1" "one" ; Elt "2" "two" } Unit)')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Pair 0 Unit)')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
        
        big_map_diff = [{'action': 'alloc', 'big_map': '0', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'exprvHK69NiDmfXXw2Gx5x9meBfRp3CBMZ1QjM3UdqoNfUzK3nSpnL', 'key': {'string': '1'}, 'value': {'string': 'one'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'exprtaPfHX9A3HW7vujsuarwHDXwJYu9hJZvuqUCyoeHLRLPXyDQjW', 'key': {'string': '2'}, 'value': {'string': 'two'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'exprtzN2y9qBiaf7A14AbS1SveJWXpMdJQztXFgiGzG5yu43tem2he', 'key': {'string': '3'}}]
        self.assertCountEqual(big_map_diff, res['result'][2])
