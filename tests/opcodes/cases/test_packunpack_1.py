from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter


class OpcodeTestpackunpack_1(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=False)  # disable exceptions

    def test_opcode_packunpack_1(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/packunpack.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair (Pair (Pair "toto" {3;7;9;1}) {1;2;3}) 0x05070707070100000004746f746f0200000008000300070009000102000000060001000200030004) Unit')
        self.assertEqual(False, res['success'])
