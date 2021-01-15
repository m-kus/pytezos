from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.instructions import parse_expression


class OpcodeTesthash_key_208(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_hash_key_208(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/hash_key.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "edpkuJqtDcA2m2muMxViSM47MPsGQzmyjnNTawUPqR8vZTAMcx61ES" None')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('(Some "tz1XPTDmvT3vVE5Uunngmixm7gj7zmdbPq6k")')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
