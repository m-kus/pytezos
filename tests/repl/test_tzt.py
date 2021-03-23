import logging
from os.path import dirname
from os.path import join
from os import listdir
from unittest.case import TestCase

from pytezos.logging import logger
from pytezos.michelson.parse import MichelsonParser
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.repl import Interpreter

logger.setLevel(logging.DEBUG)


class TztTest(TestCase):
    path = join(dirname(__file__), "tzt")
    exclude = [
        ".git",
        "LICENSE",
        # NOTE: unknown primitive `MutezOverflow`
        "add_mutez-mutez_01.tzt",
        # NOTE: unknown primitive `Contract`
        "address_00.tzt",
        "address_01.tzt",
        "address_02.tzt",
        # NOTE: unknown primitive Contract
        "contract_00.tzt",
        "contract_01.tzt",
        "contract_02.tzt",
        "contract_03.tzt",
        "contract_04.tzt",
        "contract_05.tzt",
        # NOTE: failed to parse expression LexToken(_,'_',1,658)
        "createcontract_00.tzt",
        "createcontract_01.tzt",
        # NOTE: unknown primitive `Failed`
        "failwith_00.tzt",
        # NOTE: unknown primitive `GeneralOverflow`
        "lsl_01.tzt",
        # NOTE: unknown primitive `GeneralOverflow`
        "lsr_01.tzt",
        # NOTE: unknown primitive `MutezOverflow`
        "mul_mutez-nat_01.tzt",
        # NOTE: unknown primitive `MutezOverflow
        "mul_nat-mutez_01.tzt",
        # NOTE: parameter type is not defined
        "self_00.tzt",
        # NOTE: failed to parse expression LexToken(_,'_',1,199)
        "setdelegate_00.tzt",
        # NOTE: ('SLICE', 'string is empty')
        "slice_string_05.tzt",
        # NOTE: unknown primitive `MutezUnderflow`
        "sub_mutez-mutez_01.tzt",
        # NOTE: failed to parse expression LexToken(_,'_',1,238)
        "transfertokens_00.tzt",
        "transfertokens_01.tzt",
    ]

    def test_tzt(self) -> None:
        parser = MichelsonParser()
        for filename in listdir(self.path):
            if filename in self.exclude:
                continue
            with self.subTest(filename):
                filename = join(self.path, filename)
                with open(filename) as file:
                    script = michelson_to_micheline(
                        file.read(),
                        parser=parser,
                    )

                    Interpreter.run_tzt(script=script)
