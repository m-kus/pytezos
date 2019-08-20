from os.path import exists, expanduser

from pytezos.rpc import ShellQuery, RpcNode, mainnet, alphanet, zeronet
from pytezos.crypto import Key
from pytezos.encoding import is_key
from pytezos.tools.docstring import InlineDocstring

default_shell = 'alphanet'
default_key = 'edsk33N474hxzA4sKeWVM6iuGNGDpX2mGwHNxEA4UbWS8sW3Ta3NKH'  # please, use responsibly


class Interop(metaclass=InlineDocstring):

    def __repr__(self):
        res = [
            super(Interop, self).__repr__(),
            '\nProperties',
            f'.key  # {self.key.public_key_hash()}',
            f'.shell  # {self.shell.node.uri} ({self.shell.node.network})'
        ]
        return '\n'.join(res)

    def __init__(self, shell=None, key=None):
        if shell is None:
            shell = default_shell

        if isinstance(shell, str):
            networks = {
                'mainnet': mainnet,
                'alphanet': alphanet,
                'zeronet': zeronet
            }
            if shell in networks:
                self.shell = networks[shell]
            else:
                self.shell = ShellQuery(node=RpcNode(uri=shell))
        elif isinstance(shell, ShellQuery):
            self.shell = shell
        else:
            raise NotImplementedError(shell)

        if key is None:
            key = default_key

        if isinstance(key, str):
            if is_key(key):
                self.key = Key.from_encoded_key(key)
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
        """
        Change current rpc endpoint and account (private key)
        :param shell: one of 'alphanet', 'mainnet', 'zeronet', or RPC node uri, or instance of `ShellQuery`
        :param key: base58 encoded key, path to the faucet file, alias from tezos-client, or instance of `Key`
        :return: A copy of current object with changes applied
        """
        return self._spawn(shell=shell, key=key)
