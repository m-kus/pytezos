from contextlib import suppress
from pytezos.operation.fees import DEFAULT_CONSTANTS
from pytezos.client import PyTezosClient
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch


class TestOperationGroup(TestCase):
    maxDiff = None

    @patch("pytezos.rpc.protocol.BlocksQuery.__getitem__")
    def test_fill(self, rpc_mock):
        # Arrange
        testmap = {
            "branch_offset_sandboxed": [5, None, True, 'head-5'],
            "branch_offset_not_sandboxed": [5, None, False, 'head-5'],
            "ttl_sandboxed": [None, 10, True, 'head-50'],
            "ttl_not_sandboxed": [None, 10, False, 'head-50'],
            "ttl_sandboxed_default": [None, None, True, 'head-0'],
            "ttl_not_sandboxed_default": [None, None, False, 'head-55'],
        }

        client = PyTezosClient()
        op = client.transaction(destination="")

        for name, (branch_offset, ttl, sandboxed, mock_call) in testmap.items():
            with self.subTest(name):
                # Act
                op.context._sandboxed = sandboxed
                with suppress(Exception):
                    op.fill(branch_offset=branch_offset, ttl=ttl)

                # Assert
                rpc_mock.assert_called_with(mock_call)
