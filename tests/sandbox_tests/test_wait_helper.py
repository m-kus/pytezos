import logging
from unittest.mock import patch

from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import sandbox_addresses

logging.basicConfig(level=logging.DEBUG)


class WaitHelpersTestCase(SandboxedNodeTestCase):

    def test_1_send_multiple_transactions(self) -> None:
        client = self.client
        operations = [
            client.transaction(destination=sandbox_addresses['bootstrap3'], amount=1000).send()
            for _ in range(2)
        ]
        with self.assertRaises(StopIteration):
            client.wait(*operations, num_blocks_wait=1, time_between_blocks=1)

        self.bake_block()

        operations.extend([
            client.transaction(destination=sandbox_addresses['bootstrap3'], amount=1000).send()
            for _ in range(2)
        ])
        with self.assertRaises(StopIteration):
            client.wait(*operations, num_blocks_wait=1, time_between_blocks=1)

        head_hash = client.shell.head.hash()
        self.bake_block()

        client.wait(*operations, num_blocks_wait=1, time_between_blocks=1, prev_hash=head_hash)
        bootstrap3 = self.client.shell.contracts[sandbox_addresses['bootstrap3']]()
        self.assertEqual('4000000004000', bootstrap3['balance'])
