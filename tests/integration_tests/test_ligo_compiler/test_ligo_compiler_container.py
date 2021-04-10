import pytest
from unittest import TestCase

from click.testing import CliRunner

from pytezos.cli.cli import cli

TEST_CONTRACT_TEXT = """// variant defining pseudo multi-entrypoint actions
type action is
| Increment of int
| Decrement of int

function add (const a : int ; const b : int) : int is
  block { skip } with a + b

function subtract (const a : int ; const b : int) : int is
  block { skip } with a - b

// real entrypoint that re-routes the flow based
// on the action provided
function main (const p : action ; const s : int) :
  (list(operation) * int) is
  block { skip } with ((nil : list(operation)),
  case p of
  | Increment(n) -> add(s, n)
  | Decrement(n) -> subtract(s, n)
  end)
"""

TEST_CONTRACT_COMPILATION_RESULT = """{ parameter (or (int %decrement) (int %increment)) ;
  storage int ;
  code { UNPAIR ; IF_LEFT { SWAP ; SUB } { ADD } ; NIL operation ; PAIR } }

"""


class TestLigoCompiler(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog, tmp_path):
        self._caplog = caplog
        self._tmp_path = tmp_path

    def test_update_ligo(self):
        result = self.runner.invoke(cli, ['update-ligo'])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(self._caplog.records[0].message.startswith('Pulling ligolang/ligo'))
        self.assertEqual(self._caplog.records[-1].message, 'Pulled Ligo compiler image successfully!')

    def test_compile_contract(self):
        contract_tmp_file = self._tmp_path / "contract.ligo"
        contract_tmp_file.write_text(TEST_CONTRACT_TEXT)

        # Must update image first because order of tests is not defined
        result = self.runner.invoke(cli, ['update-ligo'])
        self.assertEqual(result.exit_code, 0)

        result = self.runner.invoke(
            cli,
            [
                'ligo-compile-contract',
                f'--path={str(self._tmp_path / "contract.ligo")}',
                '--entry-point=main'
            ]
        )
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, TEST_CONTRACT_COMPILATION_RESULT)
