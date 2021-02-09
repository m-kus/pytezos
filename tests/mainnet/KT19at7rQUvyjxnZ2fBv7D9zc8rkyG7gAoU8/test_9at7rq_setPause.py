from unittest import TestCase
from os.path import dirname, join
import json

from pytezos.michelson.program import MichelsonProgram
from pytezos.michelson.types.big_map import big_map_diff_to_lazy_diff

folder = 'dexter_usdtz_xtz'
entrypoint = 'removeLiquidity'


class MainnetOperationTestCase9AT7RQ(TestCase):

    @classmethod
    def setUpClass(cls):
        with open(join(dirname(__file__), f'', '__script__.json')) as f:
            script = json.loads(f.read())

        cls.program = MichelsonProgram.match(script['code'])

        with open(join(dirname(__file__), f'', f'setPause.json')) as f:
            operation = json.loads(f.read())

        cls.entrypoint = f'setPause'
        cls.operation = operation
        # cls.maxDiff = None

    def test_parameters_9at7rq(self):
        original_params = self.program.parameter.from_parameters(self.operation['parameters'])
        py_obj = original_params.to_python_object()
        # pprint(py_obj)
        readable_params = self.program.parameter.from_parameters(original_params.to_parameters(mode='readable'))
        # optimized_params = self.parameter_type.from_parameters(original_params.to_parameters(mode='optimized'))
        self.assertEqual(py_obj, readable_params.to_python_object())
        self.program.parameter.from_python_object(py_obj)

    def test_lazy_storage_9at7rq(self):
        storage = self.program.storage.from_micheline_value(self.operation['storage'])
        lazy_diff = big_map_diff_to_lazy_diff(self.operation['big_map_diff'])
        extended_storage = storage.merge_lazy_diff(lazy_diff)
        py_obj = extended_storage.to_python_object(try_unpack=True, lazy_diff=True)
        # pprint(py_obj)
