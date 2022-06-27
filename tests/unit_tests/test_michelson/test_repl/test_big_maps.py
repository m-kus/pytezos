from os.path import dirname, join
from typing import Generator, List
from unittest import TestCase

from parameterized import parameterized

from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.repl import Interpreter


def iter_lazy_diff(lazy_diff: List[dict]) -> Generator[List[str], None, None]:
    for item in lazy_diff:
        if item['kind'] == 'big_map':
            ptr = item['id']
            diff = item['diff']
            if diff['action'] == 'alloc':
                key_type = micheline_to_michelson(diff['key_type'], wrap=True)
                val_type = micheline_to_michelson(diff['value_type'], wrap=True)
                yield [f'New map({ptr}) of type (big_map {key_type} {val_type})']
            for update in diff.get('updates', []):
                key = micheline_to_michelson(update['key'], wrap=True)
                if 'value' in update:
                    val = micheline_to_michelson(update['value'], wrap=True)
                    yield [f'Set map({ptr})[{key}] to {val}']
                else:
                    yield [f'Unset map({ptr})[{key}]']


class BigMapsTestCase(TestCase):
    @parameterized.expand(
        [
            # FORMAT: assert_output contract_file storage input expected_result
            #         expected_diffs
            # Get the value stored at the given key in the big map
            (
                'get_big_map_value.tz',
                '(Pair { Elt "hello" "hi" } None)',
                '"hello"',
                '(Pair 0 (Some "hi"))',
                [
                    ["New map(0) of type (big_map string string)"],
                    ['Set map(0)["hello"] to "hi"'],
                ],
            ),
            (
                'get_big_map_value.tz',
                '(Pair { Elt "hello" "hi" } None)',
                '""',
                '(Pair 0 None)',
                [
                    ["New map(0) of type (big_map string string)"],
                    ['Set map(0)["hello"] to "hi"'],
                ],
            ),
            (
                'get_big_map_value.tz',
                '(Pair { Elt "1" "one" ; Elt "2" "two" } None)',
                '"1"',
                '(Pair 0 (Some "one"))',
                [
                    ["New map(0) of type (big_map string string)"],
                    ['Set map(0)["1"] to "one"'],
                    ['Set map(0)["2"] to "two"'],
                ],
            ),
            # Test updating big maps
            (
                'update_big_map.tz',
                '(Pair { Elt "1" "one" ; Elt "2" "two" } Unit)',
                '{}',
                '(Pair 0 Unit)',
                [
                    ["New map(0) of type (big_map string string)"],
                    ['Set map(0)["1"] to "one"'],
                    ['Set map(0)["2"] to "two"'],
                ],
            ),
            (
                'update_big_map.tz',
                '(Pair { Elt "1" "one" ; Elt "2" "two" } Unit)',
                '{ Elt "1" (Some "two") }',
                '(Pair 0 Unit)',
                [
                    ["New map(0) of type (big_map string string)"],
                    ['Set map(0)["1"] to "two"'],
                    ['Set map(0)["2"] to "two"'],
                ],
            ),
            (
                'update_big_map.tz',
                '(Pair { Elt "1" "one" ; Elt "2" "two" } Unit)',
                '{ Elt "3" (Some "three") }',
                '(Pair 0 Unit)',
                [
                    ["New map(0) of type (big_map string string)"],
                    ['Set map(0)["1"] to "one"'],
                    ['Set map(0)["2"] to "two"'],
                    ['Set map(0)["3"] to "three"'],
                ],
            ),
            # TODO:
            # (
            #     'update_big_map.tz',
            #     '(Pair { Elt "1" "one" ; Elt "2" "two" } Unit)',
            #     '{ Elt "3" None }',
            #     '(Pair 0 Unit)',
            #     [
            #         ["New map(0) of type (big_map string string)"],
            #         ['Set map(0)["1"] to "one"'],
            #         ['Set map(0)["2"] to "two"'],
            #         ['Unset map(0)["3"]'],
            #     ],
            # ),
            (
                'update_big_map.tz',
                '(Pair { Elt "1" "one" ; Elt "2" "two" } Unit)',
                '{ Elt "2" None }',
                '(Pair 0 Unit)',
                [
                    ["New map(0) of type (big_map string string)"],
                    ['Set map(0)["1"] to "one"'],
                    ['Unset map(0)["2"]'],
                ],
            ),
            (
                'update_big_map.tz',
                '(Pair { Elt "1" "one" ; Elt "2" "two" } Unit)',
                '{ Elt "1" (Some "two") }',
                '(Pair 0 Unit)',
                [
                    ["New map(0) of type (big_map string string)"],
                    ['Set map(0)["1"] to "two"'],
                    ['Set map(0)["2"] to "two"'],
                ],
            ),
            # test the GET_AND_UPDATE instruction on big maps
            # Get and update the value stored at the given key in the map
            # TODO:
            # (
            #     'get_and_update_big_map.tz',
            #     '(Pair None {})',
            #     '"hello"',
            #     '(Pair None 0)',
            #     [
            #         ["New map(0) of type (big_map string nat)"],
            #         ['Unset map(0)["hello"]'],
            #     ],
            # ),
            # TODO:
            # (
            #     'get_and_update_big_map.tz',
            #     '(Pair (Some 4) {})',
            #     '"hello"',
            #     '(Pair None 0)',
            #     [
            #         ["New map(0) of type (big_map string nat)"],
            #         ['Set map(0)["hello"] to 4'],
            #     ],
            # ),
            (
                'get_and_update_big_map.tz',
                '(Pair None { Elt "hello" 4 })',
                '"hello"',
                '(Pair (Some 4) 0)',
                [
                    ["New map(0) of type (big_map string nat)"],
                    ['Unset map(0)["hello"]'],
                ],
            ),
            (
                'get_and_update_big_map.tz',
                '(Pair (Some 5) { Elt "hello" 4 })',
                '"hello"',
                '(Pair (Some 4) 0)',
                [
                    ["New map(0) of type (big_map string nat)"],
                    ['Set map(0)["hello"] to 5'],
                ],
            ),
            (
                'get_and_update_big_map.tz',
                '(Pair (Some 5) { Elt "hello" 4 })',
                '"hi"',
                '(Pair None 0)',
                [
                    ["New map(0) of type (big_map string nat)"],
                    ['Set map(0)["hello"] to 4'],
                    ['Set map(0)["hi"] to 5'],
                ],
            ),
            (
                'get_and_update_big_map.tz',
                '(Pair None { Elt "1" 1 ; Elt "2" 2 })',
                '"1"',
                '(Pair (Some 1) 0)',
                [
                    ["New map(0) of type (big_map string nat)"],
                    ['Unset map(0)["1"]'],
                    ['Set map(0)["2"] to 2'],
                ],
            ),
            (
                'get_and_update_big_map.tz',
                '(Pair None { Elt "1" 1 ; Elt "2" 2 })',
                '"1"',
                '(Pair (Some 1) 0)',
                [
                    ["New map(0) of type (big_map string nat)"],
                    ['Unset map(0)["1"]'],
                    ['Set map(0)["2"] to 2'],
                ],
            ),
            # MAGIC
            (
                'big_map_magic.tz',
                '(Left (Pair { Elt "1" "one" } { Elt "2" "two" }))',
                '(Left Unit)',
                '(Left (Pair 0 1))',
                [
                    ['New map(1) of type (big_map string string)'],
                    ['Set map(1)["1"] to "one"'],
                    ['New map(0) of type (big_map string string)'],
                    ['Set map(0)["2"] to "two"'],
                ],
            ),
            # test reset with new map
            (
                'big_map_magic.tz',
                '(Left (Pair { Elt "1" "one" } { Elt "2" "two" }))',
                '(Right (Left (Left (Pair { Elt "3" "three" } ' + '{ Elt "4" "four" }))))',
                '(Left (Pair 0 1))',
                [
                    ['New map(1) of type (big_map string string)'],
                    ['Set map(1)["4"] to "four"'],
                    ['New map(0) of type (big_map string string)'],
                    ['Set map(0)["3"] to "three"'],
                ],
            ),
            # test reset to unit
            (
                'big_map_magic.tz',
                '(Left (Pair { Elt "1" "one" } { Elt "2" "two" }))',
                '(Right (Left (Right Unit)))',
                '(Right Unit)',
                [],
            ),
            # test import to big_map
            (
                'big_map_magic.tz',
                '(Right Unit)',
                '(Right (Right (Left (Pair { Pair "foo" "bar" } ' + '{ Pair "gaz" "baz" }) )))',
                '(Left (Pair 0 1))',
                [
                    ['New map(1) of type (big_map string string)'],
                    ['Set map(1)["gaz"] to "baz"'],
                    ['New map(0) of type (big_map string string)'],
                    ['Set map(0)["foo"] to "bar"'],
                ],
            ),
            # test add to big_map
            (
                'big_map_magic.tz',
                '(Left (Pair { Elt "1" "one" } { Elt "2" "two" }) )',
                '(Right (Right (Right (Left { Pair "3" "three" }))))',
                '(Left (Pair 0 1))',
                [
                    ['New map(1) of type (big_map string string)'],
                    ['Set map(1)["2"] to "two"'],
                    ['New map(0) of type (big_map string string)'],
                    ['Set map(0)["1"] to "one"'],
                    ['Set map(0)["3"] to "three"'],
                ],
            ),
            # test remove from big_map
            (
                'big_map_magic.tz',
                '(Left (Pair { Elt "1" "one" } { Elt "2" "two" }))',
                '(Right (Right (Right (Right { "1" }))))',
                '(Left (Pair 0 1))',
                [
                    ['New map(1) of type (big_map string string)'],
                    ['Set map(1)["2"] to "two"'],
                    ['New map(0) of type (big_map string string)'],
                    ['Unset map(0)["1"]'],
                ],
            ),
        ]
    )
    def test_big_map_opcodes(self, filename, storage, parameter, result, big_map_log):
        with open(join(dirname(__file__), 'opcodes', filename)) as f:
            script = f.read()

        _, storage, lazy_diff, stdout, error = Interpreter.run_code(
            parameter=michelson_to_micheline(parameter),
            storage=michelson_to_micheline(storage),
            script=michelson_to_micheline(script),
            output_mode='optimized',
        )
        if error:
            print('\n'.join(stdout))
            raise error
        self.assertEqual(michelson_to_micheline(result), storage)
        log = list(iter_lazy_diff(lazy_diff))
        self.assertEqual(sorted(big_map_log), sorted(log))
