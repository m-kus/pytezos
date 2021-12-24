import logging

from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import FLORENCE

logging.getLogger().setLevel(0)


class TransactionCounterTestCase(SandboxedNodeTestCase):

    def test_endorsement(self):
        self.bake_block()

        client = self.get_client(key='bootstrap1')
        level = client.shell.head.level()
        endorsement_with_slot = client.endorsement(level).fill().sign().with_slot()

        endorsement_with_slot.forge(True)  # validate
        endorsement_with_slot.inject()
