# SmartPy Code
import smartpy as sp


class StoreValue(sp.Contract):
    def __init__(self, value):
        self.init(storedValue=value)

    @sp.entry_point
    def replace(self, value):
        self.data.storedValue = value

    @sp.entry_point
    def double(self):
        self.data.storedValue *= 2


@sp.add_test(name="StoreValue")
def test():
    scenario = sp.test_scenario()
    scenario.h1("Store Value")
    contract = StoreValue(1)
    scenario += contract
    scenario += contract.replace(2)
    scenario += contract.double()
