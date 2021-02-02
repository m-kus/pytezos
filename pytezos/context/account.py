from os.path import exists, expanduser

from pytezos.rpc import ShellQuery, RpcNode, RpcMultiNode
from pytezos.crypto.key import Key, is_installed
from pytezos.crypto.encoding import is_public_key, is_pkh
from pytezos.jupyter import InlineDocstring

default_shell = 'delphinet'
default_key = 'edsk33N474hxzA4sKeWVM6iuGNGDpX2mGwHNxEA4UbWS8sW3Ta3NKH'  # please, use responsibly
default_key_hash = 'tz1cnQZXoznhduu4MVWfJF6GSyP6mMHMbbWa'

alice_key = 'edsk3QoqBuvdamxouPhin7swCvkQNgq4jP5KZPbwWNnwdZpSpJiEbq'
alice_key_hash = 'tz1VSUr8wwNhLAzempoch5d6hLRiTh8Cjcjb'

nodes = {
    'mainnet': ['https://mainnet-tezos.giganode.io/',
                'https://rpc.tzkt.io/mainnet/',
                'https://api.tez.ie/',
                'https://tezos-prod.cryptonomic-infra.tech/chains/main/blocks/head'],
    'sandboxnet': ['http://127.0.0.1:8732/'],
    'delphinet': ['https://rpc.tzkt.io/delphinet/'],
    'edonet': ['https://rpc.tzkt.io/delphinet/']
}


class KeyHash(Key):

    def __init__(self, public_key_hash):
        super(KeyHash, self).__init__(0)
        self._pkh = public_key_hash

    def __repr__(self):
        res = [
            super(Key, self).__repr__(),
            f'\nPublic key hash',
            self.public_key_hash()
        ]
        return '\n'.join(res)

    def public_key_hash(self):
        return self._pkh

    def public_key(self):
        raise NotImplementedError

    def secret_key(self, passphrase=None, ed25519_seed=True):
        raise NotImplementedError

    def sign(self, message, generic=False):
        raise NotImplementedError

    def verify(self, signature, message):
        raise NotImplementedError


class AccountContext(metaclass=InlineDocstring):
    """ Mixin for blockchain interaction, stores node connection and key object.
    """

    def __repr__(self):
        res = [
            super(AccountContext, self).__repr__(),
            '\nProperties',
            f'.key  # {self.key.public_key_hash()}',
            f'.shell  # {self.shell.node.uri} ({self.shell.node.network})'
        ]
        return '\n'.join(res)

    def __init__(self, shell=None, key=None):
        if shell is None:
            shell = default_shell

        if isinstance(shell, str):
            if shell.endswith('.pool'):
                shell = shell.split('.')[0]
                assert shell in nodes, f'unknown network {shell}'
                self.shell = ShellQuery(node=RpcMultiNode(uri=nodes[shell], network=shell))
            elif shell in nodes:
                caching = 'sandbox' not in shell
                self.shell = ShellQuery(node=RpcNode(uri=nodes[shell], network=shell, caching=caching))
            else:
                self.shell = ShellQuery(node=RpcNode(uri=shell))
        elif isinstance(shell, ShellQuery):
            self.shell = shell
        else:
            raise NotImplementedError(shell)

        if key is None:
            key = default_key if is_installed() else default_key_hash

        if isinstance(key, str):
            keys = {
                'alice': alice_key
            }
            if key in keys:
                self.key = Key.from_encoded_key(keys[key])
            elif is_public_key(key):
                self.key = Key.from_encoded_key(key)
            elif is_pkh(key):
                self.key = KeyHash(key)
            elif exists(expanduser(key)):
                self.key = Key.from_faucet(key)
            else:
                self.key = Key.from_alias(key)
        elif isinstance(key, Key):
            self.key = key
        else:
            raise NotImplementedError(key)

    def _spawn(self, **kwargs):
        raise NotImplementedError

    def using(self, shell: ShellQuery = None, key: Key = None):
        """ Change current rpc endpoint and account (private key).

        :param shell: one of 'mainnet', '***net', or RPC node uri, or instance of `ShellQuery`
        :param key: base58 encoded key, path to the faucet file, alias from tezos-client, or instance of `Key`
        :returns: A copy of current object with changes applied
        """
        return self._spawn(shell=shell, key=key)
