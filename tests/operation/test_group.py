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
            "branch_offset_sandboxed": [5, None, True, -5],
            "branch_offset_not_sandboxed": [5, None, False, -5],
            "ttl_sandboxed": [None, 5, True, -55],
            "ttl_not_sandboxed": [None, 5, False, -55],
            "ttl_sandboxed_default": [None, None, True, 0],
            "ttl_not_sandboxed_default": [None, None, False, -50],
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

    # FIXME: This test is super ugly. Rewrite as soon as .inject() will be splitted to multiple functions
    @patch(
        "pytezos.context.impl.ExecutionContext.constants",
        MagicMock(return_value=DEFAULT_CONSTANTS),
    )
    @patch("pytezos.context.impl.ExecutionContext.sandboxed", Mock(return_value=True))
    @patch("pytezos.context.impl.ExecutionContext.get_counter", Mock(return_value=1))
    @patch("pytezos.rpc.protocol.BlockQuery.level", Mock(return_value=1))
    @patch(
        "pytezos.operation.group.OperationGroup.forge",
        Mock(
            return_value="385912772f07a5fb73888ef142c50307f3ca6be040e67710cadd074ae476796c6c006f89a145d19ed05ffa5f3268ad854e454e2756f78b0200c801640000006f89a145d19ed05ffa5f3268ad854e454e2756f700"
        ),
    )
    @patch("pytezos.rpc.query.RpcQuery._post")
    def test_inject(self, query_mock) -> None:
        # Arrange
        client = PyTezosClient()
        inject_result = {
            "branch": "BL96fhbju22fMhejZ4ftvS9M45gdcU8HPurtc3N8oXQDK5WLf9A",
            "chain_id": {},
            "contents": [
                {
                    "amount": "0",
                    "counter": "0",
                    "destination": "tz1Vona7MnADxXVFugpHohxSTFmah5Aj5xBM",
                    "fee": "267",
                    "gas_limit": "200",
                    "kind": "transaction",
                    "source": "tz1Vona7MnADxXVFugpHohxSTFmah5Aj5xBM",
                    "storage_limit": "100",
                }
            ],
            "hash": {
                "branch": "BL96fhbju22fMhejZ4ftvS9M45gdcU8HPurtc3N8oXQDK5WLf9A",
                "contents": [
                    {
                        "amount": "0",
                        "counter": "0",
                        "destination": "tz1Vona7MnADxXVFugpHohxSTFmah5Aj5xBM",
                        "fee": "267",
                        "gas_limit": "200",
                        "kind": "transaction",
                        "source": "tz1Vona7MnADxXVFugpHohxSTFmah5Aj5xBM",
                        "storage_limit": "100",
                    }
                ],
            },
            "protocol": "PtEdo2ZkT9oKpimTah6x2embF25oss54njMuPzkJTEi5RqfdZFA",
            "signature": "sigb2PfzL9y7C5etwBTkZMyFTa5v7cMNGewtXR296caeSetgHhBe6iPSstWF39C576ip514m4MAzL7jNG86j8bDHhd7ib3Jg",
        }
        testmap = {
            "async_true": [
                True,
                1,
                2,
            ],
        }
        query_mock.return_value = {
            "contents": [
                {
                    "kind": "transaction",
                    "source": "tz1Vona7MnADxXVFugpHohxSTFmah5Aj5xBM",
                    "destination": "tz1Vona7MnADxXVFugpHohxSTFmah5Aj5xBM",
                    "fee": "0",
                    "counter": "0",
                    "gas_limit": "0",
                    "storage_limit": "0",
                    "amount": "0",
                    "metadata": {},
                }
            ],
            "branch": "BL96fhbju22fMhejZ4ftvS9M45gdcU8HPurtc3N8oXQDK5WLf9A",
        }

        for name, data in testmap.items():
            with self.subTest(name):
                _async, min_confirmations, query_call_count = data

                with patch("pytezos.rpc.query.RpcQuery.__call__") as rpc_mock:
                    rpc_mock.return_value = {}

                    # Act
                    op = client.transaction(
                        destination="tz1Vona7MnADxXVFugpHohxSTFmah5Aj5xBM", amount="100"
                    )
                    op.protocol = "PtEdo2ZkT9oKpimTah6x2embF25oss54njMuPzkJTEi5RqfdZFA"
                    op.branch = "BL96fhbju22fMhejZ4ftvS9M45gdcU8HPurtc3N8oXQDK5WLf9A"
                    result = (
                        op.autofill()
                        .sign()
                        .inject(
                            preapply=False,
                            _async=_async,
                            min_confirmations=min_confirmations,
                        )
                    )

                    # Assert
                    self.assertEqual(inject_result, result)
                    self.assertEqual(query_call_count, query_mock.call_count)