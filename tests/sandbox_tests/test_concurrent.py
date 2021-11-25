from pytezos.sandbox.node import SandboxedNodeAutoBakeTestCase
from pytezos import ContractInterface
from pytezos.operation.result import OperationResult

code = """
parameter (or (int %decrement) (int %increment));
storage int;
code { UNPAIR ; IF_LEFT { SWAP ; SUB } { ADD } ; NIL operation ; PAIR }
"""


class ConcurrentTransactionsTestCase(SandboxedNodeAutoBakeTestCase):

    def get_contract(self) -> ContractInterface:
        for address in self.client.shell.contracts():
            if address.startswith('KT1'):
                contract = self.client.contract(address)
                if 'increment' in contract.entrypoints:
                    return contract
        assert False

    def test_1_originate_contract(self) -> None:
        ci = ContractInterface.from_michelson(code)
        res = self.client.origination(ci.script()).autofill().sign().inject(
            time_between_blocks=self.TIME_BETWEEN_BLOCKS,
            min_confirmations=1
        )
        self.assertEqual(1, len(OperationResult.originated_contracts(res)))

    def test_2_batch_multiple_calls(self) -> None:
        contract = self.get_contract()
        txs = [contract.increment(i) for i in range(10)]
        opg = self.client.bulk(*txs).autofill()
        opg.sign().inject(
            time_between_blocks=self.TIME_BETWEEN_BLOCKS,
            min_confirmations=1
        )
        self.assertEqual(45, int(contract.storage()))

    def test_3_send_multiple_calls(self) -> None:
        contract = self.get_contract()
        value_before = int(contract.storage())
        counter = self.client.context.get_counter()
        self.client.context.chain_id = self.client.context.get_chain_id()
        self.client.context.protocol = self.client.context.get_protocol()
        txs = [
            contract.increment(i).send_async(
                ttl=120,
                counter=counter + idx,
                storage_limit=10,
                gas_limit=50000,
            )
            for idx, i in enumerate(range(50))
        ]
        self.client.wait(
            *txs,
            time_between_blocks=self.TIME_BETWEEN_BLOCKS,
            min_confirmations=1
        )
        self.assertEqual(1225, int(contract.storage() - value_before))
