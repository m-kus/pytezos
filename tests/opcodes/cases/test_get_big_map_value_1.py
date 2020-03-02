from unittest import TestCase

from tests import abspath

#from pytezos import pytezos, Contract
from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestget_big_map_value_1(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_opcode_get_big_map_value_1(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/get_big_map_value.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN "" (Pair { Elt "hello" "hi" } None)')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Pair 0 None)')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
        
        big_map_diff = [{'action': 'alloc', 'big_map': '0', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'exprtsjEVVZk3Gm82U9wEs8kvwRiQwUT7zipJwvCeFMNsApe2tQ15s', 'key': {'string': 'hello'}, 'value': {'string': 'hi'}}]
        self.assertCountEqual(big_map_diff, res['result'][2])
