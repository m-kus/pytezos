import requests
import simplejson as json
from functools import lru_cache
from binascii import hexlify
from datetime import datetime
from time import sleep

from pytezos.encoding import base58_decode
from pytezos.rpc.query import RpcQuery
from pytezos.tools.docstring import get_attr_docstring
from pytezos.rpc.search import CyclesQuery, VotingPeriodsQuery


def make_operation_result(**kwargs):
    return {'metadata': {'operation_result': kwargs}}


class ShellQuery(RpcQuery, path=''):

    @property
    def blocks(self):
        return self.chains.main.blocks

    @property
    def head(self):
        return self.blocks.head

    @property
    @lru_cache(maxsize=None)
    def block(self):
        """
        Cached head block, useful if you just want to explore things.
        """
        return self.blocks[self.head.hash()]

    @property
    def cycles(self):
        """
        Operate on cycles rather than blocks.
        """
        return CyclesQuery(
            node=self.node,
            path=self._wild_path + '/chains/{}/blocks',
            params=self._params + ['main']
        )

    @property
    def voting_periods(self):
        """
        Operate on voting periods rather than blocks.
        """
        return VotingPeriodsQuery(
            node=self.node,
            path=self._wild_path + '/chains/{}/blocks',
            params=self._params + ['main']
        )

    @property
    def contracts(self):
        return self.head.context.contracts

    @property
    def mempool(self):
        return self.chains.main.mempool

    def wait_next_block(self, block_hash=None):
        block_time = int(self.block.context.constants()["time_between_blocks"][0])
        header = self.head.header()
        if block_hash is None:
            block_hash = header['hash']

        prev_block_dt = datetime.strptime(header['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
        elapsed_sec = (datetime.utcnow() - prev_block_dt).seconds
        delay_sec = 0 if elapsed_sec > block_time else block_time - elapsed_sec
        print(f'Wait {delay_sec} seconds until block {block_hash} is finalized')
        sleep(delay_sec)

        for i in range(block_time):
            current_block_hash = self.head.hash()
            if current_block_hash == block_hash:
                sleep(1)
            else:
                return current_block_hash
        assert False


class ChainQuery(RpcQuery, path='/chains/{}'):

    def watermark(self):
        """
        Chain watermark, hex encoded
        """
        data = self.chain_id()
        return hexlify(base58_decode(data.encode())).decode()


class InvalidBlockQuery(RpcQuery, path='/chains/{}/invalid_blocks/{}'):

    def delete(self):
        return self._delete()


class MempoolQuery(RpcQuery, path='/chains/{}/mempool'):

    def post(self, configuration):
        """
        Set operation filter rules.
        :param configuration: a JSON dictionary, known keys are `minimal_fees`, `minimal_nanotez_per_gas_unit`,
        `minimal_nanotez_per_byte`
        """
        return self._post(json=configuration)


class PendingOperationsQuery(RpcQuery, path='/chains/{}/mempool/pending_operations'):

    def __getitem__(self, item):
        """
        Search for operation in node's mempool by hash.
        :param item: operation group hash (base58)
        """
        operations_dict = self()
        for status, operations in operations_dict.items():
            for operation in operations:
                if isinstance(operation, dict):
                    if operation['hash'] == item:
                        return {**make_operation_result(status=status), **operation}
                elif isinstance(operation, list):
                    if operation[0] == item:
                        errors = operation[1].pop1('error', default=[])
                        return {**make_operation_result(status=status, errors=errors), **operation[1]}
                else:
                    assert False, operation
        raise StopIteration

    def __repr__(self):
        res = [
            super(PendingOperationsQuery, self).__repr__(),
            '[]' + get_attr_docstring(self.__class__, '__getitem__')
        ]
        return '\n'.join(res)


class DescribeQuery(RpcQuery, path='/describe'):

    def __call__(self, recurse=True):
        """
        Get RPCs documentation and input/output schema.
        :param recurse: Show information for child elements, default is True.
        In some cases doesn't work without this flag.
        """
        return super(DescribeQuery, self).__call__(recurse=recurse)

    def __repr__(self):
        res = [
            super(DescribeQuery, self).__repr__(),
            f'(){get_attr_docstring(DescribeQuery, "__call__")}',
            'Can be followed by any path:\n.chains\n.network.connections\netc\n'
        ]
        return '\n'.join(res)


class BlockInjectionQuery(RpcQuery, path='/injection/block'):

    def post(self, block, _async=False, force=False, chain=None):
        """
        Inject a block in the node and broadcast it.
        The `operations` embedded in `blockHeader` might be pre-validated using a contextual RPCs from the latest block
        (e.g. '/blocks/head/context/preapply').
        :param block: Json input:
        {
            "data": <hex-encoded block header>,
            "operations": [ [ {
                "branch": <block_hash>,
                "data": <hex-encoded operation>
            } ... ] ... ]
        }
        :param _async: By default, the RPC will wait for the block to be validated before answering,
        set True if you don't want to.
        :param force:
        :param chain: Optionally you can specify the chain
        :return: ID of the block
        """
        return self._post(
            params={
                'async': _async,
                'force': force,
                'chain': chain
            },
            json=block
        )


class OperationInjectionQuery(RpcQuery, path='/injection/operation'):

    def post(self, operation, _async=False, chain=None):
        """
        Inject an operation in node and broadcast it.
        The `signedOperationContents` should be constructed using a contextual RPCs from the latest block
        and signed by the client.
        :param operation: Hex-encoded operation data or bytes
        :param _async: By default, the RPC will wait for the operation to be (pre-)validated before answering,
        set True if you don't want to.
        :param chain: Optionally you can specify the chain
        :return: ID of the operation
        """
        if isinstance(operation, bytes):
            operation = operation.hex()

        return self._post(
            params={
                'async': _async,
                'chain': chain
            },
            json=operation
        )


class ProtocolInjectionQuery(RpcQuery, path='/injection/protocol'):

    def post(self, protocol, _async=False, force=False):
        """
        Inject a protocol in node.
        :param protocol: Json input:
        {
            "expected_env_version": <integer>,
            "components": [{
                "name": <unistring>,
                "interface"?: <hex-encoded data>,
                "implementation": <hex-encoded data> }
                 ...
            ]}
        }
        :param _async:
        :param force:
        :return: ID of the protocol
        """
        return self._post(
            params={
                'async': _async,
                'force': force
            },
            json=protocol
        )


class ResponseGenerator:

    def __init__(self, res: requests.Response):
        self._lines = res.iter_lines()

    def __iter__(self):
        for line in self._lines:
            yield json.loads(line.decode())


class MonitorQuery(RpcQuery, path=['/monitor/active_chains',
                                   '/monitor/bootstrapped',
                                   '/monitor/commit_hash',
                                   '/monitor/heads/{}',
                                   '/monitor/protocols',
                                   '/monitor/valid_blocks']):

    def __call__(self, *args, **kwargs):
        return ResponseGenerator(self.node.request(
            method='GET',
            path=self.path,
            params=kwargs,
            stream=True
        ))

    def __repr__(self):
        res = [
            super(MonitorQuery, self).__repr__(),
            'NOTE: Returned object is a generator.'
        ]
        return '\n'.join(res)


class ConnectionQuery(RpcQuery, path='/network/connections/{}'):

    def delete(self, wait=False):
        return self._delete(params=dict(wait=wait))


class NetworkItems(RpcQuery, path=['/network/peers', '/network/points']):

    def __call__(self, _filter=None):
        return self._get(params={'filter': _filter})


class NetworkLogQuery(RpcQuery, path=['/network/peers/{}/log', '/network/points/{}/log']):

    def __call__(self, monitor=False):
        if monitor:
            return ResponseGenerator(self.node.request(
                method='GET',
                path=self.path,
                stream=True
            ))
        else:
            return self._get()
