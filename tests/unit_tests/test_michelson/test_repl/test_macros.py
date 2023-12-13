from os.path import dirname
from os.path import join
from unittest import TestCase

from parameterized import parameterized  # type: ignore

from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.repl import Interpreter


class MacrosTestCase(TestCase):
    @parameterized.expand(
        [
            # FORMAT: assert_output contract_file storage input expected_result
            # Build list
            ('build_list.tz', '{}', '0', '{ 0 }'),
            ('build_list.tz', '{}', '3', '{ 0 ; 1 ; 2 ; 3 }'),
            (
                'build_list.tz',
                '{}',
                '10',
                '{ 0 ; 1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7 ; 8 ; 9 ; 10 }',
            ),
            # Find maximum int in list -- returns None if not found
            ('max_in_list.tz', 'None', '{}', 'None'),
            ('max_in_list.tz', 'None', '{ 1 }', '(Some 1)'),
            ('max_in_list.tz', 'None', '{ -1 }', '(Some -1)'),
            (
                'max_in_list.tz',
                'None',
                '{ 10 ; -1 ; -20 ; 100 ; 0 }',
                '(Some 100)',
            ),
            (
                'max_in_list.tz',
                'None',
                '{ 10 ; -1 ; -20 ; 100 ; 0 }',
                '(Some 100)',
            ),
            (
                'max_in_list.tz',
                'None',
                '{ -10 ; -1 ; -20 ; -100 }',
                '(Some -1)',
            ),
            # Test comparisons on tez { EQ ; GT ; LT ; GE ; LE }
            (
                'compare.tz',
                '{}',
                '(Pair 1000000 2000000)',
                '{ False ; False ; True ; False ; True }',
            ),
            (
                'compare.tz',
                '{}',
                '(Pair 2000000 1000000)',
                '{ False ; True ; False ; True ; False }',
            ),
            (
                'compare.tz',
                '{}',
                '(Pair 2370000 2370000)',
                '{ True ; False ; False ; True ; True }',
            ),
            # Test ASSERT
            ('assert.tz', 'Unit', 'True', 'Unit'),
            # ASSERT_{OP}
            ('assert_eq.tz', 'Unit', '(Pair -1 -1)', 'Unit'),
            ('assert_eq.tz', 'Unit', '(Pair -1 -1)', 'Unit'),
            ('assert_neq.tz', 'Unit', '(Pair 0 -1)', 'Unit'),
            ('assert_lt.tz', 'Unit', '(Pair -1 0)', 'Unit'),
            ('assert_le.tz', 'Unit', '(Pair 0 0)', 'Unit'),
            ('assert_le.tz', 'Unit', '(Pair -1 0)', 'Unit'),
            ('assert_gt.tz', 'Unit', '(Pair 0 -1)', 'Unit'),
            ('assert_ge.tz', 'Unit', '(Pair 0 0)', 'Unit'),
            ('assert_ge.tz', 'Unit', '(Pair 0 -1)', 'Unit'),
            # ASSERT_CMP{OP}
            ('assert_cmpeq.tz', 'Unit', '(Pair -1 -1)', 'Unit'),
            ('assert_cmpneq.tz', 'Unit', '(Pair 0 -1)', 'Unit'),
            ('assert_cmplt.tz', 'Unit', '(Pair -1 0)', 'Unit'),
            ('assert_cmple.tz', 'Unit', '(Pair -1 0)', 'Unit'),
            ('assert_cmple.tz', 'Unit', '(Pair 0 0)', 'Unit'),
            ('assert_cmpgt.tz', 'Unit', '(Pair 0 -1)', 'Unit'),
            ('assert_cmpge.tz', 'Unit', '(Pair 0 -1)', 'Unit'),
            ('assert_cmpge.tz', 'Unit', '(Pair 0 0)', 'Unit'),
            # Tests the SET_CAR and SET_CDR instructions
            (
                'set_caddaadr.tz',
                '(Pair (Pair 1 2 (Pair (Pair 3 0) 4) 5) 6)',
                '3000000',
                '(Pair (Pair 1 2 (Pair (Pair 3 3000000) 4) 5) 6)',
            ),
            (
                'map_caddaadr.tz',
                '(Pair (Pair 1 2 (Pair (Pair 3 0) 4) 5) 6)',
                'Unit',
                '(Pair (Pair 1 2 (Pair (Pair 3 1000000) 4) 5) 6)',
            ),
            # Test comparisons on bytes { EQ ; GT ; LT ; GE ; LE }
            (
                'compare_bytes.tz',
                '{}',
                '(Pair 0x33 0x34)',
                '{ False ; False ; True ; False ; True }',
            ),
            (
                'compare_bytes.tz',
                '{}',
                '(Pair 0x33 0x33aa)',
                '{ False ; False ; True ; False ; True }',
            ),
            (
                'compare_bytes.tz',
                '{}',
                '(Pair 0x33 0x33)',
                '{ True ; False ; False ; True ; True }',
            ),
            (
                'compare_bytes.tz',
                '{}',
                '(Pair 0x34 0x33)',
                '{ False ; True ; False ; True ; False }',
            ),
            # EXTRA
            ('pair_macro.tz', 'Unit', 'Unit', 'Unit'),
            ('unpair_macro.tz', 'Unit', 'Unit', 'Unit'),
            # TODO:
            # (
            #     'carn_and_cdrn.tz',
            #     'Unit',
            #     'Pair 1 2 3 Unit',
            #     'Unit'
            # )
        ]
    )
    def test_macros(self, filename, storage, parameter, result):
        with open(join(dirname(__file__), 'macros', filename)) as f:
            script = f.read()

        _, storage, _, stdout, error = Interpreter.run_code(
            parameter=michelson_to_micheline(parameter),
            storage=michelson_to_micheline(storage),
            script=michelson_to_micheline(script),
        )
        if error:
            print('\n'.join(stdout))
            raise error
        self.assertEqual(michelson_to_micheline(result), storage)

    @parameterized.expand(
        [
            # FORMAT: assert_output contract_file storage input expected_result
            ('assert.tz', 'Unit', 'False'),
            ('assert_eq.tz', 'Unit', '(Pair 0 -1)'),
            ('assert_eq.tz', 'Unit', '(Pair 0 -1)'),
            ('assert_neq.tz', 'Unit', '(Pair -1 -1)'),
            ('assert_lt.tz', 'Unit', '(Pair 0 -1)'),
            ('assert_lt.tz', 'Unit', '(Pair 0 0)'),
            ('assert_le.tz', 'Unit', '(Pair 0 -1)'),
            ('assert_gt.tz', 'Unit', '(Pair -1 0)'),
            ('assert_gt.tz', 'Unit', '(Pair 0 0)'),
            ('assert_ge.tz', 'Unit', '(Pair -1 0)'),
            ('assert_cmpeq.tz', 'Unit', '(Pair 0 -1)'),
            ('assert_cmpneq.tz', 'Unit', '(Pair -1 -1)'),
            ('assert_cmplt.tz', 'Unit', '(Pair 0 0)'),
            ('assert_cmplt.tz', 'Unit', '(Pair 0 -1)'),
            ('assert_cmple.tz', 'Unit', '(Pair 0 -1)'),
            ('assert_cmpgt.tz', 'Unit', '(Pair 0 0)'),
            ('assert_cmpgt.tz', 'Unit', '(Pair -1 0)'),
            ('assert_cmpge.tz', 'Unit', '(Pair -1 0)'),
            ('fail.tz', 'Unit', 'Unit'),
        ]
    )
    def test_failed_macros(self, filename, storage, parameter):
        with open(join(dirname(__file__), 'macros', filename)) as f:
            script = f.read()

        _, _, _, _, error = Interpreter.run_code(
            parameter=michelson_to_micheline(parameter),
            storage=michelson_to_micheline(storage),
            script=michelson_to_micheline(script),
        )
        self.assertIsNotNone(error)
