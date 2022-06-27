from os.path import dirname, join
from unittest import TestCase

from pytezos import ContractInterface


class Txr1ContractTest(TestCase):
    def test_txr1(self):
        contract = ContractInterface.from_file(join(dirname(__file__), 'contracts', 'txr1.tz'))
        res = contract.default(['KT1ENowZcfjAwYPSresbMBHnLMUhhuACWL7X', 'txr1YNMEtkj5Vkqsbdmt7xaxBTMRZjzS96UAi']).interpret()
        self.assertEqual(
            res.operations[0],
            {
                'kind': 'transaction',
                'source': 'KT1BEqzn5Wx8uJrZNvuS9DVHmLvG9td3fDLi',
                'destination': 'KT1ENowZcfjAwYPSresbMBHnLMUhhuACWL7X',
                'amount': '0',
                'parameters': {
                    'entrypoint': 'deposit',
                    'value': {
                        'prim': 'Pair',
                        'args': [
                            {
                                'prim': 'Pair',
                                'args': [
                                    {'string': 'KT1BEqzn5Wx8uJrZNvuS9DVHmLvG9td3fDLi'},
                                    {'prim': 'Unit'},
                                    {'int': '10'},
                                ],
                            },
                            {'string': 'txr1YNMEtkj5Vkqsbdmt7xaxBTMRZjzS96UAi'},
                        ],
                    },
                },
            },
        )
