import json
from os.path import dirname, join
from unittest import TestCase

from pytezos.michelson.forge import forge_micheline, unforge_micheline
from pytezos.michelson.program import MichelsonProgram

folder = 'typed_minter'
entrypoint = 'mint_TYPED'


class MainnetOperationTestCaseCTEZ_TEZ_PNLP_FARM(TestCase):
    @classmethod
    def setUpClass(cls):
        with open(join(dirname(__file__), f'', '__script__.json')) as f:
            script = json.loads(f.read())

        cls.program = MichelsonProgram.match(script['code'])

        with open(join(dirname(__file__), f'', f'stake.json')) as f:
            operation = json.loads(f.read())

        cls.entrypoint = f'stake'
        cls.operation = operation
        # cls.maxDiff = None

    def test_parameters_ctez_tez_pnlp_farm(self):
        original_params = self.program.parameter.from_parameters(self.operation['parameters'])
        py_obj = original_params.to_python_object()
        # pprint(py_obj)
        readable_params = self.program.parameter.from_parameters(original_params.to_parameters(mode='readable'))
        self.assertEqual(py_obj, readable_params.to_python_object())
        self.program.parameter.from_python_object(py_obj)

    def test_lazy_storage_ctez_tez_pnlp_farm(self):
        storage = self.program.storage.from_micheline_value(self.operation['storage'])
        lazy_storage_diff = self.operation['lazy_storage_diff']

        extended_storage = storage.merge_lazy_diff(lazy_storage_diff)
        py_obj = extended_storage.to_python_object(try_unpack=True, lazy_diff=True)
        # pprint(py_obj)

    def test_parameters_forging(self):
        expected = self.operation['parameters'].get('value', {'prim': 'Unit'})
        actual = unforge_micheline(forge_micheline(expected))
        self.assertEqual(expected, actual)
