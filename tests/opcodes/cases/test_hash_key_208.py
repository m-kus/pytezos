from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTesthash_key_208(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_hash_key_208(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/hash_key.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "edpkuJqtDcA2m2muMxViSM47MPsGQzmyjnNTawUPqR8vZTAMcx61ES" None')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Some "tz1XPTDmvT3vVE5Uunngmixm7gj7zmdbPq6k")')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
