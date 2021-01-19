from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestget_big_map_value_0(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_opcode_get_big_map_value_0(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/get_big_map_value.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN "hello" (Pair { Elt "hello" "hi" } None)')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Pair 0 (Some "hi"))')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
        
        big_map_diff = [{'action': 'alloc', 'big_map': '0', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'exprtsjEVVZk3Gm82U9wEs8kvwRiQwUT7zipJwvCeFMNsApe2tQ15s', 'key': {'string': 'hello'}, 'value': {'string': 'hi'}}]
        self.assertCountEqual(big_map_diff, res['result']['big_map_diff'])
