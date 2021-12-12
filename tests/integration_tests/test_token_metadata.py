from unittest import TestCase, skip

from pytezos import pytezos


class TestTokenMetadata(TestCase):

    def test_from_storage(self):
        contract = pytezos.using('mainnet').contract('KT1RJ6PbjHpwc3M5rw5s2Nbmefwbuwbdxton')
        token_metadata = contract.token_metadata[24552]
        self.assertEqual('Ordo Ad Chaos', token_metadata.name)

    def test_from_view(self):
        contract = pytezos.using('mainnet').contract('KT1REEb5VxWRjcHm5GzDMwErMmNFftsE5Gpf')
        token_metadata = contract.token_metadata[0]
        self.assertEqual('Stably USD', token_metadata.name)
