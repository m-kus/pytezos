from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestbig_map_magic_12(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_opcode_big_map_magic_12(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/big_map_magic.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Right (Right (Left (Pair { Pair "foo" "bar" } { Pair "gaz" "baz" }) ))) (Right Unit)')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Left (Pair 0 1))')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
        
        big_map_diff = [{'action': 'alloc', 'big_map': '1', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '1', 'key_hash': 'exprtft4mfpxnyufwZf17PQxf57VAyrwNM5mNwqCMkVRTfb5pALQpz', 'key': {'string': 'gaz'}, 'value': {'string': 'baz'}}, {'action': 'alloc', 'big_map': '0', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'expruTFUPVsqkuD5iwLMJuzoyGSFABnxLo7CZrgnS1czt1WbTwpVrJ', 'key': {'string': 'foo'}, 'value': {'string': 'bar'}}]
        self.assertCountEqual(big_map_diff, res['result']['big_map_diff'])
