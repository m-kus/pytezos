from pytezos.rpc.shell import *
from pytezos.rpc.protocol import *
from pytezos.rpc.helpers import *
from pytezos.rpc.search import *
from pytezos.rpc.node import RpcNode, RpcMultiNode


class RpcProvider:

    def __init__(self, klass=RpcNode, **urls):
        self.urls = urls
        self.klass = klass

    @lru_cache(maxsize=None)
    def __getattr__(self, network) -> ShellQuery:
        return ShellQuery(node=self.klass(uri=self.urls[network], network=network))

    def __dir__(self):
        return list(super(RpcProvider, self).__dir__()) + list(self.urls.keys())

    def __repr__(self):
        res = [
            super(RpcProvider, self).__repr__(),
            '\nNetworks',
            *list(map(lambda x: f'.{x[0]}  # {x[1]}', self.urls.items()))
        ]
        return '\n'.join(res)


localhost = RpcProvider(
    sandboxnet='http://127.0.0.1:8732/',
    bbbox='http://flextesa:20000'
)
tzkt = RpcProvider(
    mainnet='https://rpc.tzkt.io/mainnet/',
    babylonnet='https://rpc.tzkt.io/babylonnet/',
    carthagenet='https://rpc.tzkt.io/carthagenet/',
    zeronet='https://rpc.tzkt.io/zeronet/'
)
giganode = RpcProvider(
    mainnet='https://mainnet-tezos.giganode.io/',
    carthagenet='https://testnet-tezos.giganode.io/',
    labnet='https://labnet-tezos.giganode.io/'
)
pool = RpcProvider(
    klass=RpcMultiNode,
    mainnet=[
        'https://rpc.tzkt.io/mainnet/',
        'https://tezos-prod.cryptonomic-infra.tech/',
        'https://rpc.tezrpc.me/',
        'https://api.tezos.org.ua/',
        'https://api.tez.ie/',

    ],
    babylonnet=[
        'https://rpc.tzkt.io/babylonnet/',
        'https://tezos-dev.cryptonomic-infra.tech/',
    ],
    carthagenet=[
        'https://rpc.tzkt.io/carthagenet/',
        'https://carthagenet.tezos.org.ua/',
    ]
)

mainnet = tzkt.mainnet
babylonnet = tzkt.babylonnet
carthagenet = tzkt.carthagenet
zeronet = tzkt.zeronet
labnet = giganode.labnet
