import io

from pathlib import Path
from unittest import TestCase

from pytezos import ContractInterface


class TestDataConversion(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        asset_directory = Path(__file__).parent.joinpath('contracts')
        contract_path = asset_directory.joinpath('contract_for_data_conversion_test.tz')
        with io.open(contract_path, 'r') as contract_input:
            cls.michelson_contract = contract_input.read()
        storage_path = asset_directory.joinpath('storage_for_data_conversion_test.tz')
        with io.open(storage_path, 'r') as contract_data_input:
            cls.michelson_storage = contract_data_input.read()

    def test_decode_from_michelson(self):
        """
        Ensure that a valid Michelson contract with valid storage can be instantiated in Python
        """
        contract_interface = ContractInterface.from_michelson(self.michelson_contract)
        python_storage = contract_interface.contract.storage.decode(self.michelson_storage)
        self.assertIsNotNone(python_storage, msg="Why couldn't the valid storage be decoded from Michelson?")
        contract_interface.contract.storage_from_michelson(self.michelson_storage)

        micheline_storage = contract_interface.contract.storage.encode(python_storage)
        self.assertIsNotNone(micheline_storage, msg="Why couldn't python_storage (the result of decoding) be submitted "
                                                    "for encoding?")
