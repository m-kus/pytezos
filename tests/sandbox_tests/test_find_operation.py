from pytezos.sandbox.node import SandboxedNodeAutoBakeTestCase
from pytezos.sandbox.parameters import sandbox_addresses


class FindOperationTestCase(SandboxedNodeAutoBakeTestCase):

    def test_1_send_transaction_and_find_it(self) -> None:
        opg = self.client\
            .transaction(destination=sandbox_addresses['bootstrap3'], amount=1000)\
            .send(min_confirmations=1)

        self.client.shell.blocks[-10:0].find_operation(opg.opg_hash)
