from unittest import TestCase, skip

from pytezos import pytezos


class TestMetadata(TestCase):

    @skip
    def test_usds_all_tokens_view(self):
        usds = pytezos.using('mainnet').contract('KT1REEb5VxWRjcHm5GzDMwErMmNFftsE5Gpf')
        res = usds.metadata.allTokens().storage_view()
        self.assertEqual([0], res)

    @skip
    def test_1(self):
        client = pytezos.using('florencenet')
        contract = client.contract("KT1PPL3svzkumTQfq4aXm9LfPnocAMCYQN2w")
        balance = contract.metadata.getBalance(("tz1bpuUfhPj9Vo3RqY6KfCdkpFJt9VNC3aHQ", 1)).storage_view()
        assert int(balance) > 0
