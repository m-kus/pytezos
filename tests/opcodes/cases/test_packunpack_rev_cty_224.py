from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestpackunpack_rev_cty_224(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_packunpack_rev_cty_224(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/packunpack_rev_cty.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN (Pair "edpkuBknW28nW72KG6RoHtYW7p12T6GKc7nAbwYX5m8Wd9sDVC9yav" (Pair Unit (Pair "edsigthTzJ8X7MPmNeEwybRAvdxS1pupqcM5Mk4uCuyZAe7uEk68YpuGDeViW8wSXMrCi5CwoNgqs8V2w8ayB5dMJzrYCHhD8C7" (Pair (Some "edsigthTzJ8X7MPmNeEwybRAvdxS1pupqcM5Mk4uCuyZAe7uEk68YpuGDeViW8wSXMrCi5CwoNgqs8V2w8ayB5dMJzrYCHhD8C7") (Pair { Unit }  (Pair { True }  (Pair (Pair 19 10) (Pair (Left "tz1cxcwwnzENRdhe2Kb8ZdTrdNy4bFNyScx5") (Pair { Elt 0 "foo" ; Elt 1 "bar" }  { PACK } ))))))))) Unit')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('Unit')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
