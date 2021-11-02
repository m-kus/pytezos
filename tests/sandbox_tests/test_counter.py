import logging
from pprint import pprint

from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import sandbox_addresses

logging.basicConfig(level=logging.DEBUG)


class TransactionCounterTestCase(SandboxedNodeTestCase):

    def test_1_send_multiple_transactions_non_batched(self) -> None:
        client = self.client
        for _ in range(3):
            client.transaction(destination=sandbox_addresses['bootstrap3'], amount=42) \
                .autofill() \
                .sign() \
                .inject(min_confirmations=0)

        pending_operations = client.shell.mempool.pending_operations()
        self.assertEqual(3, len(pending_operations['applied']))

    def test_2_send_zero_fee_transaction_and_bake(self) -> None:
        self.client.transaction(destination=sandbox_addresses['bootstrap3'], amount=42) \
            .autofill(fee=0) \
            .sign() \
            .inject(min_confirmations=0)

        self.bake_block(min_fee=1)

        pending_operations = self.client.shell.mempool.pending_operations()
        self.assertEqual(1, len(pending_operations['applied']))

    def test_3_send_another_transaction_and_bake(self) -> None:
        self.client.transaction(destination=sandbox_addresses['bootstrap3'], amount=42) \
            .autofill() \
            .sign() \
            .inject(min_confirmations=0)

        self.bake_block(min_fee=1)
        pending_operations = self.client.shell.mempool.pending_operations()
        self.assertEqual(1, len(pending_operations['applied']))
        self.assertEqual(1, len(pending_operations['branch_delayed']))

    def test_4_reuse_counter(self) -> None:
        self.client.transaction(destination=sandbox_addresses['bootstrap3'], amount=13) \
            .send_async(ttl=60, counter=5, gas_limit=15000, storage_limit=0)  # override delayed tx
        pending_operations = self.client.shell.mempool.pending_operations()
        self.assertEqual(2, len(pending_operations['applied']))
        self.assertEqual(1, len(pending_operations['branch_delayed']))

    def test_5_force_bake(self) -> None:
        self.bake_block(min_fee=0)
        pending_operations = self.client.shell.mempool.pending_operations()
        self.assertEqual(1, len(pending_operations['branch_refused']))
