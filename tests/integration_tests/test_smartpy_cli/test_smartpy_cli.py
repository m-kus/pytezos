import json
from unittest import TestCase
from unittest import skip

import pytest
from click.testing import CliRunner

from pytezos.cli.cli import cli

TEST_SCRIPT_CONTENT = """# SmartPy Code
import smartpy as sp

class StoreValue(sp.Contract):
  def __init__(self, value):
      self.init(storedValue = value)

  @sp.entry_point
  def replace(self, value):
      self.data.storedValue = value

  @sp.entry_point
  def double(self):
      self.data.storedValue *= 2

@sp.add_test(name = "StoreValue")
def test():
  scenario = sp.test_scenario()
  scenario.h1("Store Value")
  contract = StoreValue(1)
  scenario += contract
  scenario += contract.replace(2)
  scenario += contract.double()
"""


@skip('FIXME')
class TestSmartPyCLIContainer(TestCase):
    def setUp(self):
        super().setUp()
        self.runner = CliRunner()

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog, tmp_path):
        self._caplog = caplog
        self._tmp_path = tmp_path

    def test_update_smartpy(self):
        result = self.runner.invoke(cli, ['update-smartpy'])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue('Pulling from bakingbad/smartpy-cli' in self._caplog.records[1].message)
        self.assertEqual(self._caplog.records[-1].message, 'Pulled SmartPy CLI image successfully!')

    def test_run_smartpy(self):
        result = self.runner.invoke(cli, ['update-smartpy'])
        self.assertEqual(result.exit_code, 0)

        output_dir = self._tmp_path / "smartpy-output"
        output_dir.mkdir()
        script_file = self._tmp_path / "smartpy-test-script.py"
        script_file.write_text(TEST_SCRIPT_CONTENT)
        print(script_file, output_dir)
        result = self.runner.invoke(
            cli,
            [
                'smartpy-compile',
                '--script',
                str(script_file),
                '--output-directory',
                str(output_dir),
            ],
        )

        self.assertEqual(result.exit_code, 0)

        for filename in ['script_init.py', 'script_pure.py']:
            tmp_file = output_dir / filename
            self.assertEqual(tmp_file.read_text(), TEST_SCRIPT_CONTENT)
