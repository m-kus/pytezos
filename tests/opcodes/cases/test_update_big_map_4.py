from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestupdate_big_map_4(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_opcode_update_big_map_4(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/update_big_map.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN { Elt "1" (Some "two") } (Pair { Elt "1" "one" ; Elt "2" "two" } Unit)')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Pair 0 Unit)')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
        
        big_map_diff = [{'action': 'alloc', 'big_map': '0', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'exprvHK69NiDmfXXw2Gx5x9meBfRp3CBMZ1QjM3UdqoNfUzK3nSpnL', 'key': {'string': '1'}, 'value': {'string': 'two'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'exprtaPfHX9A3HW7vujsuarwHDXwJYu9hJZvuqUCyoeHLRLPXyDQjW', 'key': {'string': '2'}, 'value': {'string': 'two'}}]
        self.assertCountEqual(big_map_diff, res['result']['big_map_diff'])
