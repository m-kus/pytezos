from dataclasses import dataclass
from os.path import dirname, join
from typing import Any, List
from pytezos.michelson.parse import MichelsonParser, michelson_to_micheline
from pytezos.michelson.repl import Interpreter
from unittest.case import TestCase

# TZT_FIELD_EXPR = r'^[^ ]+'


# @dataclass
# class TztTestCase:
#     code: str
#     input: List[str]
#     output: List[str]
#     big_maps: Any

#     @classmethod
#     def from_file(cls, filename: str) -> 'TztTestCase':
#         kwargs = {}

#             # for line in f.readlines():
#             #     if not line:
#             #         continue
#             #     try:
#             #         field, code = line.split()
#             #         kwargs



class TztTest(TestCase):
    include = ['abs_00.tzt']

    def test_tzt(self) -> None:
        parser = MichelsonParser(extra_primitives=('Stack_elt',))
        for filename in self.include:
            with self.subTest(filename):
                filename = join(dirname(__file__), 'tzt', filename)
                with open(filename) as file:
                    micheline = michelson_to_micheline(file.read().replace('Stack_elt', 'PUSH'), parser=parser,)

                # tzt_test_case = TztTestCase.from_file()
                # _, _, _, _, error = Interpreter.run_code(
                #     parameter=None,
                #     storage=None,
                #     script=michelson_to_micheline(tzt_test_case.code)
                # )
                # self.assertIsNotNone(error)
