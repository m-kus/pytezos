from unittest import TestCase

from tests import abspath

from pytezos.michelson.interpreter.repl import Interpreter


class OpcodeTestBigMapCommit(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_big_map_gen(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/big_map_mem.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair 0 False) (Pair { Elt 1 Unit ; Elt 2 Unit ; Elt 3 Unit } Unit)')
        self.assertTrue(res['success'])

        with self.assertRaises(Exception):
            self.i.execute('RUN (Pair 0 True) (Pair 0 Unit)')

        res = self.i.execute('RUN (Pair 0 False) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        with self.assertRaises(Exception):
            self.i.execute('RUN (Pair 0 True) (Pair 0 Unit)')

        res = self.i.execute('RUN (Pair 1 True) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        with self.assertRaises(Exception):
            self.i.execute('RUN (Pair 1 False) (Pair 0 Unit)')

        res = self.i.execute('RUN (Pair 2 True) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        with self.assertRaises(Exception):
            self.i.execute('RUN (Pair 2 False) (Pair 0 Unit)')

        res = self.i.execute('RUN (Pair 3 True) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        with self.assertRaises(Exception):
            self.i.execute('RUN (Pair 3 False) (Pair 0 Unit)')

        res = self.i.execute('RUN (Pair 4 False) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        with self.assertRaises(Exception):
            self.i.execute('RUN (Pair 4 True) (Pair 0 Unit)')

    def test_big_map_get_add(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/big_map_get_add.tz")}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair (Pair 200 (Some 2)) (Pair 200 (Some 2))) ' +
                             '(Pair { Elt 0 1 ; Elt 1 2 ; Elt 2 3 } Unit)')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair (Pair 200 (Some 2)) (Pair 200 (Some 2))) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair (Pair 200 None) (Pair 200 None)) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair (Pair 200 None) (Pair 300 None)) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair (Pair 1 None) (Pair 200 None)) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair (Pair 1 (Some 2)) (Pair 0 (Some 1))) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair (Pair 400 (Some 1232)) (Pair 400 (Some 1232))) (Pair 0 Unit)')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN (Pair (Pair 401 (Some 0)) (Pair 400 (Some 1232))) (Pair 0 Unit)')
        self.assertTrue(res['success'])
