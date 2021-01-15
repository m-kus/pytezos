from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter


class OpcodeTestslices_4(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=False)  # disable exceptions

    def test_opcode_slices_4(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/slices.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair 0xe009ab79e8b84ef0 "spsig1PPUFZucuAQybs5wsqsNQ68QNgFaBnVKMFaoZZfi1BtNnuCAWnmL9wVy5HfHkR6AeodjVGxpBVVSYcJKyMURn6K1yknYLm") "sppk7dBPqMPjDjXgKbb5f7V3PuKUrA4Zuwc3c3H7XqQerqPUWbK7Hna"')
        self.assertEqual(False, res['success'])
