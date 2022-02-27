from unittest import TestCase, skip

from pytezos import pytezos


class TestMetadata(TestCase):

    def test_usds_all_tokens_view(self):
        usds = pytezos.using('mainnet').contract('KT1REEb5VxWRjcHm5GzDMwErMmNFftsE5Gpf')
        res = usds.metadata.allTokens().storage_view()
        self.assertEqual([0], res)

    def test_1(self):
        client = pytezos.using('kaizen')
        contract = client.contract("KT1Tg6WFuTU47Z8rPeBhDbgx1DmX1SWCZcZq")
        balance = contract.metadata.getBalance(("tz1WkYQMi1LSvge2ksaWtx5t4eqqLqgEskUM", 0)).storage_view()
        assert int(balance) > 0

    def test_domains(self):
        td = pytezos.using('mainnet').contract('KT1GBZmSxmnKJXGMdMLbugPfLyUPmuLSMwKS')
        res = td.metadata.resolveAddress('tz1PN9FWDGoASBTvgppaQbbPdGhkrnTNmcVz').storage_view()
        self.assertEqual('tz1PN9FWDGoASBTvgppaQbbPdGhkrnTNmcVz', res['address'])
