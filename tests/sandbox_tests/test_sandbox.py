from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import sandbox_addresses, sandbox_commitment


# NOTE: Node won't be wiped between tests so alphabetical order of method names matters
class SandboxTestCase(SandboxedNodeTestCase):
    def test_1_activate_protocol(self) -> None:
        header = self.client.shell.head.header()
        self.assertIsNotNone(header.get('content'))

    def test_2_bake_empty_block(self) -> None:
        self.bake_block()

    def test_3_create_transaction(self) -> None:
        bootstrap3 = self.client.shell.contracts[sandbox_addresses['bootstrap3']]()
        print(bootstrap3['balance'])
        opg = (
            self.client.transaction(
                destination=sandbox_addresses['bootstrap3'],
                amount=42,
            )
            .autofill()
            .sign()
            .inject(min_confirmations=0)
        )
        assert self.client.shell.mempool.pending_operations()['applied'][0]['hash'] == opg['hash']

    def test_4_bake_block(self) -> None:
        self.bake_block()
        bootstrap3 = self.client.shell.contracts[sandbox_addresses['bootstrap3']]()
        self.assertEqual(3_800_000_333_333 + 42, int(bootstrap3['balance']))
        # 200_000_000_000 frozen deposits + 333333 block rewards

    def test_5_activate_account(self) -> None:
        client = self.get_client(key=sandbox_commitment)
        client.activate_account().autofill().sign().inject()
        self.bake_block()
        self.assertEqual('100500000000', client.account()['balance'])

    def test_6_reveal_pk_and_send_tez(self) -> None:
        client = self.get_client(key=sandbox_commitment)
        res = client.reveal().transaction(destination=sandbox_addresses['bootstrap4'], amount=1000).autofill().sign().inject()
        balance_change = sum(int(op.get('amount', 0)) + int(op['fee']) for op in res['contents'])
        self.bake_block()
        self.assertEqual(100500000000 - balance_change, int(client.account()['balance']))

    def test_7_register_constant(self):
        self.client.register_global_constant({'int': '12345'}).autofill().sign().inject()
        self.bake_block()
