from unittest import TestCase

from pytezos import pytezos


class CallbackViewTestCase(TestCase):

    def test_balance_of(self):
        usds = pytezos.using('mainnet').contract('KT1REEb5VxWRjcHm5GzDMwErMmNFftsE5Gpf')
        res = usds.balance_of(requests=[
            {'owner': 'tz1PNsHbJRejCnnYzbsQ1CR8wUdEQqVjWen1', 'token_id': 0},
            {'owner': 'tz1i2tE6hic2ASe9Kvy85ar5hGSSc58bYejT', 'token_id': 0},
            {'owner': 'tz2QegZQXyz8b74iTdaqKsGRF7YQb88Wu9CS', 'token_id': 0}
        ], callback=None).callback_view()
        print(res)
