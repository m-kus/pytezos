from unittest import TestCase
from os.path import dirname, join
import json

from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.interpreter.program import MichelsonProgram

folder = 'dexter_usdtz_xtz'


class MainnetContractTestCaseTemplate(TestCase):

    @classmethod
    def setUpClass(cls):
        with open(join(dirname(__file__), f'{folder}', '__script__.json')) as f:
            script = json.loads(f.read())

        cls.program = MichelsonProgram.match(script['code'])
        cls.script = script

        with open(join(dirname(__file__), f'{folder}', '__entrypoints__.json')) as f:
            entrypoints = json.loads(f.read())

        cls.entrypoints = entrypoints
        # cls.maxDiff = None

    def test_parameter_type_template(self):
        type_expr = self.program.parameter.as_micheline_expr()
        self.assertEqual(self.script['code'][0], type_expr, 'micheline -> type -> micheline')

    def test_entrypoints_template(self):
        ep_types = self.program.parameter.list_entry_points()
        self.assertEqual(len(self.entrypoints['entrypoints']) + 1, len(ep_types))
        for name, ep_type in ep_types.items():
            if name not in ['default', 'root']:
                expected_type = MichelsonType.match(self.entrypoints['entrypoints'][name])
                expected_type.assert_equal_types(ep_type)

    def test_storage_type_template(self):
        type_expr = self.program.storage.as_micheline_expr()
        self.assertEqual(self.script['code'][1], type_expr, 'micheline -> type -> micheline')

    def test_storage_encoding_template(self):
        val = self.program.storage.from_micheline_value(self.script['storage'])
        val_expr = val.to_micheline_value(mode='optimized')
        self.assertEqual(self.script['storage'], val_expr, 'micheline -> value -> micheline')

        val_ = self.program.storage.from_python_object(val.to_python_object())
        val_expr_ = val_.to_micheline_value(mode='optimized')
        self.assertEqual(self.script['storage'], val_expr_, 'value -> pyobj -> value -> micheline')
