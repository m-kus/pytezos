import logging
from time import sleep

from pytezos.logging import logger
from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import sandbox_addresses

logger.setLevel(logging.DEBUG)


# NOTE: Node won't be wiped between tests so alphabetical order of method names matters
class SandboxTestCase(SandboxedNodeTestCase):
    def test_1_activate_protocol(self) -> None:
        # Arrange
        client = self.get_client().using(key='dictator')

        # Act
        op = client.activate_protocol('PtEdo2Zk')
        op.fill().sign().inject()
        sleep(1)

        # Assert
        block = client.shell.block()
        self.assertIsNotNone(block['header'].get('content'))

    def test_2_bake_empty_block(self) -> None:
        # Arrange
        client = self.get_client().using(key='bootstrap1')

        # Act
        op = client.bake_block()
        op.fill().work().sign().inject()
        sleep(1)

        # Assert
        ...

    def test_3_create_transaction(self) -> None:
        # Arrange
        client = self.get_client().using(key='bootstrap1')

        # Act
        op = client.transaction(
            destination=sandbox_addresses['bootstrap2'],
            amount=42,
        )

        op.fill(branch_offset=1).sign().inject()
        sleep(1)

        # Assert
        ...

    def test_4_bake_block(self) -> None:
        # Arrange
        client = self.get_client()
        client.loglevel = 'DEBUG'

        # Act
        op = client.using(key='bootstrap1').bake_block()
        op.fill().work().sign().inject()

        # Assert
        ...
