import io
from pathlib import Path
from unittest import TestCase

from parameterized import parameterized  # type: ignore

from pytezos import ContractInterface

asset_directory = Path(__file__).parent.joinpath('contracts')


class TestDataConversion(TestCase):
    michelson_contract: str

    @classmethod
    def setUpClass(cls) -> None:
        contract_path = asset_directory.joinpath('contract_for_data_conversion_test.tz')
        with io.open(contract_path, 'r') as contract_input:
            cls.michelson_contract = contract_input.read()

    @parameterized.expand([('storage_for_data_conversion_test.tz',), ('storage_for_data_conversion_test_ptr.tz',)])
    def test_decode_from_michelson(self, file_name):
        """
        Ensure that a valid Michelson contract with valid storage can be instantiated in Python
        """
        storage_path = asset_directory.joinpath(file_name)
        with io.open(storage_path, 'r') as contract_data_input:
            michelson_storage = contract_data_input.read()

        contract_interface = ContractInterface.from_michelson(self.michelson_contract)
        python_storage = contract_interface.contract.storage.decode(michelson_storage)
        self.assertIsNotNone(python_storage, msg="Why couldn't the valid storage be decoded from Michelson?")
        contract_interface.contract.storage_from_michelson(michelson_storage)

        micheline_storage = contract_interface.contract.storage.encode(python_storage)
        self.assertIsNotNone(
            micheline_storage,
            msg="Why couldn't python_storage (the result of decoding) be submitted " "for encoding?",
        )
