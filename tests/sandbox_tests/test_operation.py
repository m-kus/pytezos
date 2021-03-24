from time import sleep

from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import sandbox_addresses, sandbox_params


class TransactionCounterTestCase(SandboxedNodeTestCase):

    @classmethod
    def _create_stalled_transactions(cls, client) -> None:
        op = client.transaction(destination=sandbox_addresses['bootstrap3'], amount=42).autofill().sign()
        op.contents[0]['fee'] = "0"
        op.sign().inject(min_confirmations=0)

    def test_1_stalled_transaction_same_client(self) -> None:
        for _ in range(3):
            client = self.get_client().using(key='bootstrap2')
            self._create_stalled_transactions(client)
            sleep(1)

    def test_2_stalled_transaction_new_client(self) -> None:
        for _ in range(3):
            client = self.create_client().using(key='bootstrap2')
            self._create_stalled_transactions(client)
            sleep(1)

    def test_3_bake_block(self) -> None:
        self.bake_block()

    def test_4_stalled_transaction_same_client(self) -> None:
        for _ in range(3):
            client = self.get_client().using(key='bootstrap2')
            self._create_stalled_transactions(client)
            sleep(1)

    def test_5_stalled_transaction_new_client(self) -> None:
        for _ in range(3):
            client = self.create_client().using(key='bootstrap2')
            self._create_stalled_transactions(client)
            sleep(1)

    def test_6_assert(self) -> None:
        self.assertEqual(
            {
                'applied': [
                    {
                        'branch': 'BMD1TC8F7nx7VYSfgEL7qpuxBLwMvBNkbhpX2j2XjaMs9q1W2rB',
                        'contents': [
                            {
                                'amount': '42',
                                'counter': '7',
                                'destination': 'tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU',
                                'fee': '0',
                                'gas_limit': '1627',
                                'kind': 'transaction',
                                'source': 'tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN',
                                'storage_limit': '100',
                            }
                        ],
                        'hash': 'opCjgDZKXfrtyQr1mdL24wSkvsJCM9NoNHNQDaX3YhNi4gFkFcW',
                        'signature': 'sigbQ9sCsvdByqiodMWtmpvAQMYQeTjotMw6tApvXYqjboMiUUBm35w2vb383sdcq3EtipWC4NDJ5snBSNg2VcLzkptu9Hg2',
                    },
                    {
                        'branch': 'BMD1TC8F7nx7VYSfgEL7qpuxBLwMvBNkbhpX2j2XjaMs9q1W2rB',
                        'contents': [
                            {
                                'amount': '42',
                                'counter': '8',
                                'destination': 'tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU',
                                'fee': '0',
                                'gas_limit': '1627',
                                'kind': 'transaction',
                                'source': 'tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN',
                                'storage_limit': '100',
                            }
                        ],
                        'hash': 'oo53WT43yzbauR3a57miTyL6gZQPwu9iS6fJ6XPmmEpnCqPs81G',
                        'signature': 'sige9bLaeGFeaKX2fnQCtbsX5VPYwhehTv9Hzck4rnbWcP8S4SvVa5kainJgxLekmKvA7HocigBu4DnYavbBNmzBKXwAcdo1',
                    },
                    {
                        'branch': 'BMD1TC8F7nx7VYSfgEL7qpuxBLwMvBNkbhpX2j2XjaMs9q1W2rB',
                        'contents': [
                            {
                                'amount': '42',
                                'counter': '9',
                                'destination': 'tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU',
                                'fee': '0',
                                'gas_limit': '1627',
                                'kind': 'transaction',
                                'source': 'tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN',
                                'storage_limit': '100',
                            }
                        ],
                        'hash': 'ooVLY6oKKvkF8Enyq3gvCEgDc1jSizvdnsQP4sc4yGTuLEvuirt',
                        'signature': 'sigpCJouYM6DtZ9SyPZgL9gtPShcX6xAeTW5ANdDm5Zix4kwVxQ1ftX76NDtGRuypAu8xGXQHN7pgCAbDhfQMbhG2zjwDEuh',
                    },
                    {
                        'branch': 'BMD1TC8F7nx7VYSfgEL7qpuxBLwMvBNkbhpX2j2XjaMs9q1W2rB',
                        'contents': [
                            {
                                'amount': '42',
                                'counter': '10',
                                'destination': 'tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU',
                                'fee': '0',
                                'gas_limit': '1627',
                                'kind': 'transaction',
                                'source': 'tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN',
                                'storage_limit': '100',
                            }
                        ],
                        'hash': 'op7rkdqCqRMhg7E36NM8jaCicSYtMUMGevSVckn2jQKsRLBDKR7',
                        'signature': 'sigacukWKZUZVwmH2EAAM25fmjRYEMa3XqUZQU7DkUzbnQNv81BrfsF6KVhbHLd5deQ1GA9t5gTMsrHxrMezpsK2dCoUqBfK',
                    },
                    {
                        'branch': 'BMD1TC8F7nx7VYSfgEL7qpuxBLwMvBNkbhpX2j2XjaMs9q1W2rB',
                        'contents': [
                            {
                                'amount': '42',
                                'counter': '11',
                                'destination': 'tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU',
                                'fee': '0',
                                'gas_limit': '1627',
                                'kind': 'transaction',
                                'source': 'tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN',
                                'storage_limit': '100',
                            }
                        ],
                        'hash': 'ooguYSGCKx6fFEtrqUYGHh4YEaQWwNWZzACyJFNKCBbhtgVjT9R',
                        'signature': 'siguwiDVsHL1Xj8sv5KBLdT1gb1m5Tfvd5BDGZsiDYxWhvdyrnLh1xyAZuvgwJptc19nTxRTMxkkuWk8jW3QHrrDPQhsBzNV',
                    },
                    {
                        'branch': 'BMD1TC8F7nx7VYSfgEL7qpuxBLwMvBNkbhpX2j2XjaMs9q1W2rB',
                        'contents': [
                            {
                                'amount': '42',
                                'counter': '12',
                                'destination': 'tz1faswCTDciRzE4oJ9jn2Vm2dvjeyA9fUzU',
                                'fee': '0',
                                'gas_limit': '1627',
                                'kind': 'transaction',
                                'source': 'tz1gjaF81ZRRvdzjobyfVNsAeSC6PScjfQwN',
                                'storage_limit': '100',
                            }
                        ],
                        'hash': 'op66shHirheZgp9KQwJidvsFKDJZ5hNUdpgDYiEkPs9guDYuLeg',
                        'signature': 'sigWk3jiJeu5yRRjTHQLoCwd1QzdT3thL51JsAeuZv8dTFuw22zQZ8FHuj4EsuoZPxMGrBcGunhC7t7MBM1tLX1t4kAizvc2',
                    },
                ],
                'branch_delayed': [],
                'branch_refused': [],
                'refused': [],
                'unprocessed': [],
            },
            self.client.shell.mempool.pending_operations(),
        )
