from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface, MichelsonRuntimeError


class NftContractTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nft = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'nft.tz'))

    def test_mint(self):
        res = self.nft.mint(nftToMintId=42, nftToMint='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq').interpret(storage={})
        self.assertDictEqual({42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, res.storage)

    def test_mint_existing(self):
        res = self.nft.mint(nftToMintId=42, nftToMint='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq').interpret(
            storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}
        )
        self.assertDictEqual({42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, res.storage)

    def test_transfer_skip(self):
        res = self.nft.transfer(nftToTransfer=42, destination='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq').interpret(
            storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}
        )
        self.assertDictEqual({42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, res.storage)

    def test_transfer_non_existing(self):
        with self.assertRaises(MichelsonRuntimeError):
            self.nft.transfer(nftToTransfer=42, destination='tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu').interpret(
                storage={}, source='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'
            )

    def test_transfer_unwanted(self):
        res = self.nft.transfer(nftToTransfer=42, destination='tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu').interpret(
            storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}
        )
        self.assertDictEqual({42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, res.storage)

    def test_transfer(self):
        res = self.nft.transfer(nftToTransfer=42, destination='tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu').interpret(
            storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, source='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'
        )
        self.assertDictEqual({42: 'tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu'}, res.storage)

    def test_burn_unwanted(self):
        res = self.nft.burn(42).interpret(storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'})
        self.assertDictEqual({42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, res.storage)

    def test_burn_non_existing(self):
        with self.assertRaises(MichelsonRuntimeError):
            self.nft.burn(42).interpret(storage={})

    def test_burn(self):
        res = self.nft.burn(42).interpret(
            storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, source='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'
        )
        self.assertDictEqual({}, res.storage)
