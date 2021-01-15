from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter


class OpcodeTestpackunpack_0(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=False)  # disable exceptions

    def test_opcode_packunpack_0(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/packunpack.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair (Pair (Pair "toto" {3;7;9;1}) {1;2;3}) 0x05070707070100000004746f746f020000000800030007000900010200000006000100020003) Unit')
        self.assertEqual(True, res['success'])
