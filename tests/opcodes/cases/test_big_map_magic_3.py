from unittest import TestCase

from tests import abspath

#from pytezos import pytezos, Contract
from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestbig_map_magic_3(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_opcode_big_map_magic_3(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/big_map_magic.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Right (Right (Left (Pair { Pair "foo" "bar" } { Pair "gaz" "baz" }) ))) (Right Unit)')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Left (Pair 0 1))')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
        
        big_map_diff = [{'action': 'alloc', 'big_map': '1', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '1', 'key_hash': 'exprtft4mfpxnyufwZf17PQxf57VAyrwNM5mNwqCMkVRTfb5pALQpz', 'key': {'string': 'gaz'}, 'value': {'string': 'baz'}}, {'action': 'alloc', 'big_map': '0', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'expruTFUPVsqkuD5iwLMJuzoyGSFABnxLo7CZrgnS1czt1WbTwpVrJ', 'key': {'string': 'foo'}, 'value': {'string': 'bar'}}]
        self.assertCountEqual(big_map_diff, res['result'][2])
