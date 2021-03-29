from unittest import TestCase

from pytezos import pytezos


class TestMetadata(TestCase):

    def test_usds_all_tokens_view(self):
        usds = pytezos.using('mainnet').contract('KT1REEb5VxWRjcHm5GzDMwErMmNFftsE5Gpf')
        res = usds.metadata.allTokens().storage_view()
        self.assertEqual([0], res)
