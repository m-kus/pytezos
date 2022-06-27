from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface, Unit
from pytezos.jupyter import is_interactive


class TestInterfaces(TestCase):
    def test_concat(self):
        concat = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'default_entrypoint.tz'))
        res = concat.default('bar').interpret(storage='foo')
        self.assertEqual('foobar', res.storage)

    def test_increment(self):
        counter = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'counter.tz'))
        res = counter.default('deadbeef').interpret(storage=[{}, 0])
        self.assertEqual(1, res.storage[1])
        self.assertIn(bytes.fromhex('deadbeef'), res.storage[0])

    def test_mint(self):
        token_v3 = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'token.tz'))
        alice = "tz1ibMpWS6n6MJn73nQHtK5f4ogyYC1z9T9z"
        res = token_v3.mint(mintOwner=alice, mintValue=3).interpret(
            storage={"admin": alice, "balances": {}, "paused": False, "shareType": "APPLE", "totalSupply": 0}, source=alice
        )
        self.assertEqual(3, res.storage['balances'][alice])

    def test_increment_decrement(self):
        counter = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'macro_counter.tz'))
        res = counter.increaseCounterBy(5).interpret(storage=0)
        self.assertEqual(res.storage, 5)

        res = counter.decreaseCounterBy(5).interpret(storage=0)
        self.assertEqual(res.storage, -5)

    def test_none_vs_unit(self):
        ci = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'none_vs_unit.tz'))
        res = ci.callAnotherContract().interpret(storage=None)
        self.assertEqual(0, len(res.operations))

        res = ci.callAnotherContract('KT1VG2WtYdSWz5E7chTeAdDPZNy2MpP8pTfL').interpret(storage=None)
        self.assertEqual(1, len(res.operations))

        res = ci.doNothing().interpret(storage=None)
        self.assertEqual(Unit, res.storage)

    def test_docstring(self):
        ci = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'macro_counter.tz'))
        print(ci.increaseCounterBy)
        self.assertTrue(is_interactive())

    def test_top_field_annot(self):
        ci = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'top_field_annot.tz'))
        print(ci.buyTicket)

    def test_or_entry(self):
        ci = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'or_entry.tz'))
        ci.collect(collectRequest=dict(swap_id=0, token_amount=0))
