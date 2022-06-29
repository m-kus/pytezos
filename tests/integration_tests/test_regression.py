from unittest import TestCase
from unittest import skip

from pytezos import pytezos


class TestRegression(TestCase):
    def test_tzbtc_get_balance_view(self):
        tzbtc = pytezos.using('mainnet').contract('KT1PWx2mnDueood7fEmfbBDKx1D9BAnnXitn')
        res = tzbtc.getBalance(owner='tz1QwZgNgPc3fFCCNLbrmjfB3Czms4qaobyA', contract_1=None).view()
        self.assertIsNotNone(res)

    def test_kusd_get_balance_view(self):
        kusd = pytezos.using('mainnet').contract('KT1K9gCRgaLRFKTErYt1wVxA3Frb9FjasjTV')
        res = kusd.getBalance('KT1SorR4UFBkUJeYVbtXZBNivUV1cQM6AqRR', None).view()
        self.assertIsNotNone(res)

    def test_branch_offset_overflow(self):
        bh = pytezos.using('mainnet').shell.blocks[-1000000000].hash()
        self.assertEqual("BLockGenesisGenesisGenesisGenesisGenesisf79b5d1CoW2", bh)
