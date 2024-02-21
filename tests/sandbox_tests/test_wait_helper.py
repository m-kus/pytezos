import logging

from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import sandbox_addresses

logging.basicConfig(level=logging.DEBUG)


class WaitHelpersTestCase(SandboxedNodeTestCase):
    def test_1_send_multiple_transactions(self) -> None:
        client = self.client
        operations = [
            self.get_client(key)
            .transaction(
                destination=sandbox_addresses['bootstrap5'],
                amount=1000,
            )
            .send()
            for key in ['bootstrap1', 'bootstrap2']
        ]
        with self.assertRaises(TimeoutError):
            client.wait(
                *operations,
                num_blocks_wait=1,
                time_between_blocks=1,
                block_timeout=2,
            )

        self.bake_block()

        operations.extend(
            [
                self.get_client(key)
                .transaction(
                    destination=sandbox_addresses['bootstrap5'],
                    amount=1000,
                )
                .send()
                for key in ['bootstrap3', 'bootstrap4']
            ]
        )
        with self.assertRaises(TimeoutError):
            client.wait(
                *operations,
                num_blocks_wait=1,
                time_between_blocks=1,
                block_timeout=2,
            )

        head_hash = client.shell.head.hash()
        self.bake_block()

        client.wait(
            *operations,
            num_blocks_wait=1,
            time_between_blocks=1,
            prev_hash=head_hash,
        )
        bootstrap5 = self.client.shell.contracts[sandbox_addresses['bootstrap5']]()
        self.assertEqual('3800000004000', bootstrap5['balance'])
