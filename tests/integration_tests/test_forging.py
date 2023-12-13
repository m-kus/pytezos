from unittest import TestCase

from pytezos import pytezos
from pytezos.block.forge import forge_block_header
from pytezos.block.forge import forge_protocol_data


class TestForging(TestCase):
    def test_forge_header(self) -> None:
        header = {
            'context': 'CoWJDoPwD4JzbkQtxbNLQYXeNt2VYMNue6kTtZhpsgsMHvopD1Nv',
            'fitness': ['02', '00000002', '', 'ffffffff', '00000000'],
            'level': 2,
            'operations_hash': 'LLoa7bxRTKaQN2bLYoitYB6bU2DvLnBAqrVjZcvJ364cTcX2PZYKU',
            'predecessor': 'BMHbhkJb2urryvEt6rskJBmUSL6KdoCd6H7S7rGBNULYVJucbvc',
            'proto': 1,
            'protocol_data': '0d23a240e9a8481c10c7a8474a52b2697533755621fb727a9fc989a154d9baba0000000000000000000000010000',
            'timestamp': '1970-01-01T00:00:02Z',
            'validation_pass': 4,
        }
        actual = forge_block_header(header).hex()
        expected = pytezos.shell.head.helpers.forge_block_header.post(header)
        self.assertEqual(expected['block'], actual)

    def test_forge_protocol_data(self) -> None:
        # https://rpc.tzkt.io/ithacanet/chains/main/blocks/10001/header/protocol_data
        protocol_data = {
            "protocol": "Psithaca2MLRFYargivpo7YvUr7wUDqyxrdhC5CQq78mRvimz6A",
            "payload_hash": "vh2UTuqLs3Tf1Tr9HV51QJjvFHskzLydH1pNn3BfHdRiy8E5sDMf",
            "payload_round": 1,
            "proof_of_work_nonce": "7985fafeccd00d00",
            "liquidity_baking_escape_vote": False,
        }
        actual = forge_protocol_data(protocol_data).hex()
        expected = '6939439d683b0d8258522f6c0c37a495776ed804ac68a04cf69292aaa6cc98d5000000017985fafeccd00d000000'
        self.assertEqual(expected, actual)
