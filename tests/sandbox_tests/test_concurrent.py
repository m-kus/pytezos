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
        address = next(a for a in self.client.shell.contracts() if a.startswith('KT1'))
        return self.client.contract(address)

    def test_1_originate_contract(self) -> None:
        ci = ContractInterface.from_michelson(code)
        res = self.client.origination(ci.script()).autofill().sign().inject(
            time_between_blocks=self.TIME_BETWEEN_BLOCKS,
            min_confirmations=1
        )
        self.assertEqual(1, len(OperationResult.originated_contracts(res)))

    def test_2_batch_multiple_calls(self) -> None:
        contract = self.get_contract()
        txs = [contract.increment(i) for i in range(100)]
        self.client.bulk(*txs).autofill().sign().inject(
            time_between_blocks=self.TIME_BETWEEN_BLOCKS,
            min_confirmations=1
        )
        self.assertEqual(4950, int(contract.storage()))

    def test_3_send_multiple_calls(self) -> None:
        contract = self.get_contract()
        counter = self.client.context.get_counter()
        self.client.context.chain_id = self.client.context.get_chain_id()
        self.client.context.protocol = self.client.context.get_protocol()
        txs = [
            contract.increment(i).send_async(
                ttl=60,
                counter=counter + idx,
                storage_limit=10,
                gas_limit=50000,
            )
            for idx, i in enumerate(range(100))
        ]
        self.client.wait(
            *txs,
            time_between_blocks=self.TIME_BETWEEN_BLOCKS,
            min_confirmations=1
        )
        self.assertEqual(9900, int(contract.storage()))
