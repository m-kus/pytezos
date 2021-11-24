from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import sandbox_addresses
from pytezos.operation.result import OperationResult


class HangzhouFeaturesTestCase(SandboxedNodeTestCase):

    def test_register_constant(self):
        self.client.register_global_constant({'int': '12345'}).autofill().sign().inject()
        self.bake_block()
