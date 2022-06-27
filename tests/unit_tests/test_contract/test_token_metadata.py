import json
from os import listdir
from os.path import join, dirname
from pytezos.contract.token_metadata import ContractTokenMetadata
from unittest import TestCase


class TokenMetadataTest(TestCase):
    token_metadata_path = join(dirname(__file__), 'token_metadata')

    def test_from_json(self):
        for filename in listdir(self.token_metadata_path):
            with self.subTest(filename):
                with open(join(self.token_metadata_path, filename)) as file:
                    metadata_json = json.load(file)
                    ContractTokenMetadata.from_json(metadata_json)
