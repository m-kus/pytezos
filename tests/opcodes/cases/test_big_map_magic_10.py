from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTestbig_map_magic_10(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_opcode_big_map_magic_10(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/big_map_magic.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Right (Left (Left (Pair { Elt "3" "three" } { Elt "4" "four" })))) (Left (Pair { Elt "1" "one" } { Elt "2" "two" }))')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Left (Pair 0 1))')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
        
        big_map_diff = [{'action': 'alloc', 'big_map': '1', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '1', 'key_hash': 'exprttiwE7dpYJ8Xjp28uMZzcC3Bwh4xAEF7GT7FutVwVoskMZYExx', 'key': {'string': '4'}, 'value': {'string': 'four'}}, {'action': 'alloc', 'big_map': '0', 'key_type': {'prim': 'string'}, 'value_type': {'prim': 'string'}}, {'action': 'update', 'big_map': '0', 'key_hash': 'exprtzN2y9qBiaf7A14AbS1SveJWXpMdJQztXFgiGzG5yu43tem2he', 'key': {'string': '3'}, 'value': {'string': 'three'}}]
        self.assertCountEqual(big_map_diff, res['result']['big_map_diff'])
