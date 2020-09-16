from pytezos.rpc.shell import *
from pytezos.rpc.protocol import *
from pytezos.rpc.helpers import *
from pytezos.rpc.search import *
from pytezos.rpc.node import RpcNode, RpcMultiNode


def is_public_network(network):
    return network in ['mainnet', 'carthagenet', 'delphinet', 'dalphanet']


class RpcProvider:

    def __init__(self, klass=RpcNode, **urls):
        self.urls = urls
        self.klass = klass

    @lru_cache(maxsize=None)
    def __getattr__(self, network) -> ShellQuery:
        return ShellQuery(node=self.klass(
            uri=self.urls[network],
            network=network,
            caching=is_public_network(network)))

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
    carthagenet='https://rpc.tzkt.io/carthagenet/',
    dalphanet='https://rpc.tzkt.io/dalphanet/',
    delphinet='https://rpc.tzkt.io/delphinet/',
)
giganode = RpcProvider(
    mainnet='https://mainnet-tezos.giganode.io/',
    carthagenet='https://testnet-tezos.giganode.io/',
    labnet='https://labnet-tezos.giganode.io/',
    dalphanet='https://dalphanet-tezos.giganode.io/'
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
    carthagenet=[
        'https://rpc.tzkt.io/carthagenet/',
        'https://carthagenet.tezos.org.ua/',
    ]
)

mainnet = tzkt.mainnet
carthagenet = tzkt.carthagenet
labnet = giganode.labnet
dalphanet = tzkt.dalphanet
delphinet = tzkt.delphinet
