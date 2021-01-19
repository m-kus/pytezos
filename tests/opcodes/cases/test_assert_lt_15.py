from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter


class OpcodeTestassert_lt_15(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=False)  # disable exceptions

    def test_opcode_assert_lt_15(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/assert_lt.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair 0 0) Unit')
        self.assertEqual(False, res['success'])
