from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface, NonFungibleTokenImpl, MichelsonRuntimeError


class NftContractTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.nft = ContractInterface.create_from(join(dirname(__file__), 'nft.tz'), factory=NonFungibleTokenImpl)

    def test_mint(self):
        res = self.nft \
            .mint(token_id=42, owner='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq') \
            .result(storage={})
        self.assertDictEqual({42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, res.context)

    def test_mint_existing(self):
        res = self.nft \
            .mint(token_id=42, owner='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq') \
            .result(storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'})
        self.assertDictEqual({42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, res.context)

    def test_transfer_skip(self):
        res = self.nft \
            .transfer(token_id=42, destination='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq') \
            .result(storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'})
        self.assertDictEqual({42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, res.context)

    def test_transfer_non_existing(self):
        with self.assertRaises(MichelsonRuntimeError):
            self.nft \
                .transfer(token_id=42, destination='tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu') \
                .result(storage={}, source='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq')

    def test_transfer_unwanted(self):
        res = self.nft \
            .transfer(token_id=42, destination='tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu') \
            .result(storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'})
        self.assertDictEqual({42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, res.context)

    def test_transfer(self):
        res = self.nft \
            .transfer(token_id=42, destination='tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu') \
            .result(storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'},
                    source='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq')
        self.assertDictEqual({42: 'tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu'}, res.context)

    def test_burn_unwanted(self):
        res = self.nft \
            .burn(42) \
            .result(storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'})
        self.assertDictEqual({42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'}, res.context)

    def test_burn_non_existing(self):
        with self.assertRaises(MichelsonRuntimeError):
            self.nft.burn(42).result(storage={})

    def test_burn(self):
        res = self.nft \
            .burn(42) \
            .result(storage={42: 'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq'},
                    source='tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq')
        self.assertDictEqual({}, res.context)
