from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestset_id_132(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_set_id_132(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/set_id.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN {} {}')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('{}')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
