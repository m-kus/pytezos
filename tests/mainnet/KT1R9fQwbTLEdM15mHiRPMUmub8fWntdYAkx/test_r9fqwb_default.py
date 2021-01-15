from unittest import TestCase
from os.path import dirname, join
from pprint import pprint
import json

from pytezos.types import StorageType, ParameterType
from pytezos.types.big_map import big_map_diff_to_lazy_diff
from pytezos.types.base import get_script_section

folder = 'dexter_usdtz_xtz'
entrypoint = 'removeLiquidity'


class MainnetOperationTestCaseR9FQWB(TestCase):

    @classmethod
    def setUpClass(cls):
        with open(join(dirname(__file__), f'', '__script__.json')) as f:
            script = json.loads(f.read())

        cls.parameter_type = ParameterType.match(get_script_section(script, 'parameter'))
        cls.storage_type = StorageType.match(get_script_section(script, 'storage'))

        with open(join(dirname(__file__), f'', f'default.json')) as f:
            operation = json.loads(f.read())

        cls.entrypoint = f'default'
        cls.operation = operation
        # cls.maxDiff = None

    def test_parameters_r9fqwb(self):
        original_params = self.parameter_type.from_parameters(self.operation['parameters'])
        py_obj = original_params.to_python_object()
        # pprint(py_obj)
        readable_params = self.parameter_type.from_parameters(original_params.to_parameters(mode='readable'))
        self.assertEqual(py_obj, readable_params.to_python_object())

    def test_lazy_storage_r9fqwb(self):
        storage = self.storage_type.from_micheline_value(self.operation['storage'])
        lazy_diff = big_map_diff_to_lazy_diff(self.operation['big_map_diff'])
        extended_storage = storage.merge_lazy_diff(lazy_diff)
        py_obj = extended_storage.to_python_object(try_unpack=True, lazy_diff=True)
        # pprint(py_obj)
