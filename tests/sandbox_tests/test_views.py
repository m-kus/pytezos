from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos import ContractInterface
from pytezos.operation.result import OperationResult

# This contract updates his storage with number provided to default and allow
# to view this number using getValue view:
code = """
{
    parameter nat ;
    storage nat ;
    code { CAR ; NIL operation ; PAIR } ;
    view "getValue" unit nat { CDR }
}
"""


class ViewTestCase(SandboxedNodeTestCase):
    def originate_contract(self, storage):
        ci = ContractInterface.from_michelson(code).using(
            shell=self.client.shell,
            key=self.client.key
        )
        res = ci.originate(initial_storage=storage).send()
        self.bake_block()

        opg = self.client.shell.blocks['head':].find_operation(res.hash())
        address = OperationResult.originated_contracts(opg)[0]
        contract = self.client.contract(address)
        return contract

    def test_check_view_should_be_updated(self):

        # originating contract with value 12:
        contract = self.originate_contract(12)
        self.assertEqual(contract.getValue().storage_view(), 12)

        # updating value to 33:
        contract.default(33).send()
        self.bake_block()
        self.assertEqual(contract.getValue().storage_view(), 33)
