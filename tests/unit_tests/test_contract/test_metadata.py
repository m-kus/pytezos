import json
from os import listdir
from os.path import dirname
from os.path import join
from unittest import TestCase

from pytezos.contract.metadata import ContractMetadata


class MetadataTest(TestCase):
    metadata_path = join(dirname(__file__), 'metadata')

    def test_from_json(self):
        for filename in listdir(self.metadata_path):
            with self.subTest(filename), open(join(self.metadata_path, filename)) as file:
                metadata_json = json.load(file)
                ContractMetadata.from_json(metadata_json)
