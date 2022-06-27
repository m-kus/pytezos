import json
from unittest.case import TestCase
from unittest.mock import MagicMock

from pytezos.contract.interface import ContractInterface
from pytezos.contract.metadata import ContractMetadata
from pytezos.michelson.types.core import UnitType

TEST_VIEW_CONTRACT_MICHELSON = """
{ parameter unit ; storage unit ; code { CDR ; NIL operation ; PAIR } }
"""

TEST_VIEW_JSON = """
{
    "name": "my-simple-contract-metadata",
    "description": "This is fake metadata to use for unit testing",
    "version": "0.42.0",
    "license": {
      "name": "MIT",
      "details": "The MIT License"
    },
    "homepage": "https://gitlab.com/tezos/tezos",
    "interfaces": [
      "TZIP-16",
      "TZIP-12"
    ],
    "views": [
        {
            "name": "view_record_like",
            "implementations": [
                {
                    "michelsonStorageView": {
                        "parameter": {
                            "prim": "unit"
                        },
                        "returnType": {
                           "prim": "pair",
                            "args":
                              [ { "prim": "pair",
                                  "args":
                                    [ { "prim": "pair",
                                        "args": [ { "prim": "int" }, { "prim": "nat" } ],
                                        "annots": [ "%a_plain_tuple" ] },
                                      { "prim": "nat", "annots": [ "%my_first_nat" ] } ] },
                                { "prim": "pair",
                                  "args":
                                    [ { "prim": "int", "annots": [ "%my_first_number" ] },
                                      { "prim": "int", "annots": [ "%my_second_number" ] } ] }
                              ]
                        },
                        "code": [
                          { "prim": "DROP" },
                          { "prim": "PUSH", "args": [ { "prim": "int" }, { "int": "42" } ] },
                          { "prim": "ISNAT" },
                          { "prim": "IF_NONE",
                            "args":
                              [ [ { "prim": "PUSH",
                                    "args": [ { "prim": "string" }, { "string": "FAILURE" } ] },
                                  { "prim": "FAILWITH" } ], [] ] },
                          { "prim": "PUSH", "args": [ { "prim": "int" }, { "int": "2" } ] },
                          { "prim": "PUSH", "args": [ { "prim": "int" }, { "int": "1" } ] },
                          { "prim": "PAIR" }, { "prim": "SWAP" }, { "prim": "DUP" },
                          { "prim": "PUSH", "args": [ { "prim": "int" }, { "int": "3" } ] },
                          { "prim": "PAIR" }, { "prim": "PAIR" }, { "prim": "PAIR" }
                      ]
                    }
                }
            ]
      }
    ]
}
"""


class OffchainViewTest(TestCase):

    def test_view_return_type_regression_251(self) -> None:
        # Need to mock the shell for unit testing. Configuring it to always return a simple
        # value for the contract's current storage state
        contract = ContractInterface.from_michelson(TEST_VIEW_CONTRACT_MICHELSON)
        contract.context.storage_value = UnitType().to_micheline_value()
        meta = ContractMetadata.from_json(json.loads(TEST_VIEW_JSON), contract.context)

        expected_view_result = {"my_first_number": 1, "my_first_nat": 42, "my_second_number": 2, "a_plain_tuple": (3, 42)}
        actual_view_result = meta.viewRecordLike().storage_view()
        assert expected_view_result == actual_view_result, f"Expected: {expected_view_result} but got: {actual_view_result}"
