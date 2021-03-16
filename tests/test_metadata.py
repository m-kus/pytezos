import cattr
import json
from os import listdir
from os.path import join, dirname
from pytezos.contract.metadata import ContractMetadata
from unittest import TestCase
from pytezos.client import PyTezosClient

class MetadataTest(TestCase):
    metadata_path = join(dirname(__file__), 'metadata')

    def test_from_json(self):
        for filename in listdir(self.metadata_path):
            with self.subTest(filename):
                with open(join(self.metadata_path, filename)) as file:
                    metadata_json = json.load(file)
                    ContractMetadata.from_json(metadata_json)

    def test_run_storage_view(self):
        contract = PyTezosClient().using('delphinet').contract('KT1RyihALYEsVCcKP7Ya6teCHs9ii5ZHQxvj')
        view_entrypoint = contract.metadata.call_view('multiply-the-nat-in-storage', contract.code[1])
        view_entrypoint(7).run_code()