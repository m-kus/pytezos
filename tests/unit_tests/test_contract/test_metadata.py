import json
from os import listdir
from os.path import join, dirname
from pytezos.contract.metadata import ContractMetadata
from unittest import TestCase


class MetadataTest(TestCase):
    metadata_path = join(dirname(__file__), 'metadata')

    def test_from_json(self):
        for filename in listdir(self.metadata_path):
            with self.subTest(filename):
                with open(join(self.metadata_path, filename)) as file:
                    metadata_json = json.load(file)
                    ContractMetadata.from_json(metadata_json)
