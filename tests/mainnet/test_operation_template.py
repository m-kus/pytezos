from unittest import TestCase
from os.path import dirname, join
import json

from pytezos.types import StorageType, ParameterType, MichelsonType

folder = 'tzbtc'
entrypoint = 'transfer'


class MainnetOperationTestCaseTemplate(TestCase):

    @classmethod
    def setUpClass(cls):
        with open(join(dirname(__file__), f'{folder}/script.json')) as f:
            script = json.loads(f.read())

        cls.parameter_type = ParameterType.match(script['code'][0])
        cls.storage_type = StorageType.match(script['code'][1])

        with open(join(dirname(__file__), f'{folder}/{entrypoint}.json')) as f:
            operation = json.loads(f.read())

        cls.entrypoint = f'{entrypoint}'
        cls.operation = operation
        # cls.maxDiff = None

    def test_parameters_template(self):
        params = self.parameter_type.from_parameters(self.operation['parameters'])
        print(params.to_python_object())

    def test_lazy_storage_template(self):
        storage = self.storage_type.from_micheline_value(self.operation['storage'])
        