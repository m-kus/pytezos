from unittest import TestCase
from os.path import dirname, join
from pprint import pprint
import json

from pytezos.types import StorageType, ParameterType
from pytezos.types.big_map import big_map_diff_to_lazy_diff

folder = 'tzbtc'
entrypoint = 'transfer'


class MainnetOperationTestCaseHARBINGER_ORACLE__COINBASE_STORAGE(TestCase):

    @classmethod
    def setUpClass(cls):
        with open(join(dirname(__file__), f'', '__script__.json')) as f:
            script = json.loads(f.read())

        cls.parameter_type = ParameterType.match(script['code'][0])
        cls.storage_type = StorageType.match(script['code'][1])

        with open(join(dirname(__file__), f'', f'push.json')) as f:
            operation = json.loads(f.read())

        cls.entrypoint = f'push'
        cls.operation = operation
        # cls.maxDiff = None

    def test_parameters_harbinger_oracle__coinbase_storage(self):
        params = self.parameter_type.from_parameters(self.operation['parameters'])
        py_obj = params.to_python_object()
        # pprint(py_obj)
        param_expr = params.to_parameters(mode='optimized')
        self.assertEqual(self.operation['parameters'], param_expr)

    def test_lazy_storage_harbinger_oracle__coinbase_storage(self):
        storage = self.storage_type.from_micheline_value(self.operation['storage'])
        lazy_diff = big_map_diff_to_lazy_diff(self.operation['big_map_diff'])
        extended_storage = storage.merge_lazy_diff(lazy_diff)
        py_obj = extended_storage.to_python_object(try_unpack=True, lazy_diff=True)
        # pprint(py_obj[0])
