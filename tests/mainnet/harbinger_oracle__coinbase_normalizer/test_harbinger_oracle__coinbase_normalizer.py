from unittest import TestCase
from os.path import dirname, join
import json

from pytezos.types import StorageType, ParameterType, MichelsonType

folder = 'tzbtc'


class MainnetContractTestCaseHARBINGER_ORACLE__COINBASE_NORMALIZER(TestCase):

    @classmethod
    def setUpClass(cls):
        with open(join(dirname(__file__), f'', '__script__.json')) as f:
            script = json.loads(f.read())

        cls.parameter_type = ParameterType.match(script['code'][0])
        cls.storage_type = StorageType.match(script['code'][1])
        cls.script = script

        with open(join(dirname(__file__), f'', '__entrypoints__.json')) as f:
            entrypoints = json.loads(f.read())

        cls.entrypoints = entrypoints
        # cls.maxDiff = None

    def test_parameter_type_harbinger_oracle__coinbase_normalizer(self):
        type_expr = self.parameter_type.get_micheline_type()
        self.assertEqual(self.script['code'][0], type_expr, 'micheline -> type -> micheline')

    def test_entrypoints_harbinger_oracle__coinbase_normalizer(self):
        ep_types = self.parameter_type.list_entry_points()
        self.assertEqual(len(self.entrypoints['entrypoints']) + 1, len(ep_types))
        for name, ep_type in ep_types.items():
            if name not in ['default', 'root']:
                expected_type = MichelsonType.match(self.entrypoints['entrypoints'][name])
                expected_type.assert_equal_types(ep_type)

    def test_storage_type_harbinger_oracle__coinbase_normalizer(self):
        type_expr = self.storage_type.get_micheline_type()
        self.assertEqual(self.script['code'][1], type_expr, 'micheline -> type -> micheline')

    def test_storage_encoding_harbinger_oracle__coinbase_normalizer(self):
        val = self.storage_type.from_micheline_value(self.script['storage'])
        val_expr = val.to_micheline_value(mode='optimized')
        self.assertEqual(self.script['storage'], val_expr, 'micheline -> value -> micheline')

        val_ = self.storage_type.from_python_object(val.to_python_object())
        val_expr_ = val_.to_micheline_value(mode='optimized')
        self.assertEqual(self.script['storage'], val_expr_, 'value -> pyobj -> value -> micheline')
