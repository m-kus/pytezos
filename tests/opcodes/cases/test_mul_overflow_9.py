from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestmul_overflow_9(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=False)  # disable exceptions

    def test_opcode_mul_overflow_9(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/mul_overflow.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Right Unit) Unit')
        self.assertEqual(False, res['success'])
