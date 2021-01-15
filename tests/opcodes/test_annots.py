from unittest import TestCase

from tests import abspath

from pytezos.michelson.repl import Interpreter, MichelsonRuntimeError


class OpcodeTestAnnotations(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_map_map_annots(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/map_map_annots.tz")}"')
        self.assertTrue(res['success'])

        try:
            self.i.execute("""
                RUN Unit (Pair
                  { Elt "tz1daj8qHeMtJ1XPCLGYRguH8BeNJc7YQ4ym" (Pair {} 30000000000000000000) ;
                    Elt "tz1euqMMX8dhf21M921UEq3f1EKy98FSYqTX" (Pair {} 30000000000000000000) ;
                    Elt "tz1fWUkzMvnz4dmRn4kQMytahG6R4MMoobwp" (Pair {} 30000000000000000000) }
                  90000000000000000000)
                """)
        except MichelsonRuntimeError as e:
            self.assertEquals({'tz1daj8qHeMtJ1XPCLGYRguH8BeNJc7YQ4ym': 30000000000000000000,
                               'tz1euqMMX8dhf21M921UEq3f1EKy98FSYqTX': 30000000000000000000,
                               'tz1fWUkzMvnz4dmRn4kQMytahG6R4MMoobwp': 30000000000000000000},
                              e.data._val)

    def test_type_annots_mismatch(self):
        res = self.i.execute("""
        parameter (pair (nat :a) (nat :b)) ;
        storage (pair (nat :c) (nat :d)) ;
        code {
            CAR ;
            NIL operation ;
            PAIR ;
        }
        """)
        self.assertTrue(res['success'])

        with self.assertRaises(MichelsonRuntimeError):
            self.i.execute("RUN (Pair 1 2) (Pair 3 4)")
