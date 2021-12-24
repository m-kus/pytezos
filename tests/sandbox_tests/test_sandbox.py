from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import sandbox_addresses, LATEST


# NOTE: Node won't be wiped between tests so alphabetical order of method names matters
class SandboxTestCase(SandboxedNodeTestCase):

    def test_1_activate_protocol(self) -> None:
        header = self.client.shell.head.header()
        self.assertIsNotNone(header.get('content'))

    def test_2_bake_empty_block(self) -> None:
        self.bake_block()

    def test_3_create_transaction(self) -> None:
        opg = self.client.transaction(
            destination=sandbox_addresses['bootstrap3'],
            amount=42,
        ).fill().sign().inject(min_confirmations=0)
        self.assertIsNotNone(self.client.shell.mempool.pending_operations[opg['hash']])

    def test_4_bake_block(self) -> None:
        self.bake_block()
        bootstrap3 = self.client.shell.contracts[sandbox_addresses['bootstrap3']]()
        self.assertEqual('4000000000042', bootstrap3['balance'])

    def test_5_rollback(self) -> None:
        self.activate(LATEST, reset=True)
        bootstrap3 = self.client.shell.contracts[sandbox_addresses['bootstrap3']]()
        self.assertEqual('4000000000000', bootstrap3['balance'])
