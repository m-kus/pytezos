from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter


class OpcodeTestmul_overflow_8(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=False)  # disable exceptions

    def test_opcode_mul_overflow_8(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/mul_overflow.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Left Unit) Unit')
        self.assertEqual(False, res['success'])
