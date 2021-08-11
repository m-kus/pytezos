from pytezos.sandbox.node import SandboxedNodeAutoBakeTestCase
from pytezos.sandbox.parameters import sandbox_addresses
from pytezos.operation.result import OperationResult


class FindOperationTestCase(SandboxedNodeAutoBakeTestCase):

    def test_1_send_transaction_and_find_it(self) -> None:
        opg = self.client\
            .transaction(destination=sandbox_addresses['bootstrap3'], amount=1000)\
            .send(min_confirmations=1)

        self.client.shell.blocks[-10:0].find_operation(opg.opg_hash)

    def test_2_sleep(self) -> None:
        level_from = self.client.shell.head.level()
        self.client.sleep(2)
        level_to = self.client.shell.head.level()
        self.assertEqual(2, level_to - level_from)

    def test_3_consumed_gas(self) -> None:
        opg = self.client \
            .transaction(destination=sandbox_addresses['bootstrap3'], amount=1000)\
            .send(min_confirmations=1)

        consumed_gas = OperationResult.consumed_gas(opg.opg_result)
        self.assertGreater(consumed_gas, 0)
