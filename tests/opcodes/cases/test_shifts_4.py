from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter


class OpcodeTestshifts_4(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=False)  # disable exceptions

    def test_opcode_shifts_4(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/shifts.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Left (Pair 1 257)) None')
        self.assertEqual(False, res['success'])
