from pytezos.rpc.shell import ShellQuery
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from pytezos.context.impl import ExecutionContext


class TestContext(TestCase):
    def test_sandboxed(self) -> None:
        # Arrange
        # TODO: Update with florencenet response
        public_version_response = {
            "version": {"major": 8, "minor": 2, "additional_info": "release"},
            "network_version": {"chain_name": "TEZOS_EDO2NET_2021-02-11T14:00:00Z", "distributed_db_version": 1, "p2p_version": 1},
            "commit_info": {"commit_hash": "6102c808a21b32e732ab9bb1825761cd056f3e86", "commit_date": "2021-02-10 22:57:06 +0100"},
        }
        sandboxed_version_response = {
            "version": {"major": 8, "minor": 2, "additional_info": "release"},
            "network_version": {"chain_name": "SANDBOXED_TEZOS", "distributed_db_version": 1, "p2p_version": 1},
            "commit_info": {"commit_hash": "6102c808a21b32e732ab9bb1825761cd056f3e86", "commit_date": "2021-02-10 22:57:06 +0100"},
        }

        # Act
        with patch("pytezos.rpc.query.RpcQuery.__call__") as rpc_mock:
            rpc_mock.return_value = public_version_response
            public_result = ExecutionContext(shell=ShellQuery(None)).sandboxed

        with patch("pytezos.rpc.query.RpcQuery.__call__") as rpc_mock:
            rpc_mock.return_value = sandboxed_version_response
            sandboxed_result = ExecutionContext(shell=ShellQuery(None)).sandboxed

        # Assert
        self.assertFalse(public_result)
        self.assertTrue(sandboxed_result)
