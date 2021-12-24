import logging

from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import sandbox_addresses, sandbox_commitment

logging.basicConfig(level=logging.DEBUG)


class TransactionCounterTestCase(SandboxedNodeTestCase):

    def test_1_activate_account(self) -> None:
        client = self.get_client(key=sandbox_commitment)
        client.activate_account().autofill().sign().inject()
        self.bake_block()
        self.assertEqual('100500000000', client.account()['balance'])

    def test_2_reveal_pk_and_send_tez(self) -> None:
        client = self.get_client(key=sandbox_commitment)
        client.reveal().transaction(destination=sandbox_addresses['bootstrap2'], amount=42) \
            .autofill().sign().inject()
        self.bake_block()
        bootstrap2 = client.shell.contracts[sandbox_addresses['bootstrap2']]()
        self.assertEqual('4000000000042', bootstrap2['balance'])
