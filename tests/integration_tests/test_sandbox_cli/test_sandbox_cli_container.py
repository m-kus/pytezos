import pytest
from unittest import TestCase

from click.testing import CliRunner

from pytezos.cli.cli import cli


class TestSandboxCLIContainer(TestCase):
    def setUp(self):
        super().setUp()
        self.runner = CliRunner()

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog):
        self._caplog = caplog

    def test_run_sandbox(self):        
        result = self.runner.invoke(cli, ['sandbox', '--n-blocks', 10])

        self.assertEqual(result.exit_code, 0)
        self.assertTrue('Giving node 5 seconds to start.' in self._caplog.text)
        for idx in range(10):
            self.assertTrue(f'Baking block {idx}...' in self._caplog.text)
        self.assertTrue('Baked block: ' in self._caplog.text)
