from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter


class OpcodeTestcheck_signature_2(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=False)  # disable exceptions

    def test_opcode_check_signature_2(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/check_signature.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN "edpkuBknW28nW72KG6RoHtYW7p12T6GKc7nAbwYX5m8Wd9sDVC9yav" (Pair "edsigu3QszDjUpeqYqbvhyRxMpVFamEnvm9FYnt7YiiNt9nmjYfh8ZTbsybZ5WnBkhA7zfHsRVyuTnRsGLR6fNHt1Up1FxgyRtF" "hello")')
        self.assertEqual(True, res['success'])
