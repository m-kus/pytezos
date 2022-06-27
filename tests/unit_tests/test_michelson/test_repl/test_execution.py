from logging import DEBUG
from os.path import dirname, join
from unittest import TestCase

from parameterized import parameterized

from pytezos.logging import logger
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.repl import Interpreter

logger.setLevel(DEBUG)


class ExecutionTestCase(TestCase):
    @parameterized.expand(
        [
            ['florence_contract_#643_compare.tz', 'Unit', '0', {'int': '1'}],
            ['florence_contract_#643_with_%.tz', 'Unit', 'Unit', {'prim': 'Unit'}],
            ['florence_contract_#643_without_%.tz', 'Unit', 'Unit', {'prim': 'Unit'}],
        ]
    )
    def test_execution(self, filename, parameter, storage, result):
        with open(join(dirname(__file__), 'execution', filename)) as f:
            script = f.read()

        _, storage, lazy_diff, stdout, error = Interpreter.run_code(
            parameter=michelson_to_micheline(parameter),
            storage=michelson_to_micheline(storage),
            script=michelson_to_micheline(script),
        )
        self.assertIsNone(error)
        self.assertEqual(storage, result)
