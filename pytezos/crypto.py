import hashlib
import binascii
import json
from os.path import expanduser, join, abspath
from getpass import getpass
from pyblake2 import blake2b
from mnemonic import Mnemonic

from pytezos.encoding import scrub_input, base58_decode, base58_encode
from pytezos.tools.docstring import InlineDocstring, get_class_docstring


class CryptoExtraFallback:

    def __getattr__(self, item):
        raise NotImplementedError(
            "Please, install packages libsodium-dev, libsecp256k1-dev, and libgmp-dev, "
            "and Python libraries pysodium, secp256k1, and fastecdsa")

    def __call__(self, *args, **kwargs):
        self.__getattr__('throw')


try:
    import pysodium
    import secp256k1
    import fastecdsa.ecdsa
    import fastecdsa.keys
    import fastecdsa.curve
    import fastecdsa.encoding.sec1
    from fastecdsa.encoding.util import bytes_to_int
except ImportError as e:
    pysodium = CryptoExtraFallback()
    secp256k1 = CryptoExtraFallback()
    fastecdsa = CryptoExtraFallback()
    bytes_to_int = CryptoExtraFallback()
    __crypto__ = False
else:
    __crypto__ = True


def is_installed():
    return __crypto__


def blake2b_32(v=b''):
    """ Get a BLAKE2B hash of bytes
    """
    return blake2b(scrub_input(v), digest_size=32)


def validate_mnemonic(mnemonic, language='english'):
    m = Mnemonic(language)
    mnemonic = m.normalize_string(mnemonic).split(' ')
    if len(mnemonic) not in [12, 15, 18, 21, 24]:
        raise ValueError(
            'Number of words must be one of the following: [12, 15, 18, 21, 24], but it is not (%d).' % len(mnemonic))

    idx = map(lambda x: bin(m.wordlist.index(x))[2:].zfill(11), mnemonic)
    b = ''.join(idx)
    l = len(b)
    d = b[:l // 33 * 32]
    h = b[-l // 33:]
    nd = binascii.unhexlify(hex(int(d, 2))[2:].rstrip('L').zfill(l // 33 * 8))
    nh = bin(int(hashlib.sha256(nd).hexdigest(), 16))[2:].zfill(256)[:l // 33]
    if h != nh:
        raise ValueError('Failed checksum.')


class Key(metaclass=InlineDocstring):
    """ Represents a public or secret key for Tezos. Ed25519, Secp256k1 and P256
    are supported.
    """
    def __init__(self, public_point, secret_exponent=None, curve=b'ed', activation_code=None):
        self.public_point = public_point
        self.secret_exponent = secret_exponent
        self.curve = curve
        self.activation_code = activation_code

    def __repr__(self):
        res = [
            super(Key, self).__repr__(),
            f'\nPublic key hash',
            self.public_key_hash(),
            '\nHelpers',
            get_class_docstring(self.__class__)
        ]
        return '\n'.join(res)

    @property
    def is_secret(self):
        return self.secret_exponent is not None

    @classmethod
    def from_secret_exponent(cls, secret_exponent: bytes, curve=b'ed', activation_code=None):
        """ Creates a key object from a secret exponent.

        :param secret_exponent: secret exponent or seed
        :param curve: b'sp' for Secp251k1, b'p2' for P256/Secp256r1, b'ed' for Ed25519 (default)
        :param activation_code: secret for initializing account balance
        """
        # Ed25519
        if curve == b'ed':
            # Dealing with secret exponent or seed?
            if len(secret_exponent) == 64:
                public_point = pysodium.crypto_sign_sk_to_pk(sk=secret_exponent)
            else:
                public_point, secret_exponent = pysodium.crypto_sign_seed_keypair(seed=secret_exponent)
        # Secp256k1
        elif curve == b'sp':
            sk = secp256k1.PrivateKey(secret_exponent)
            public_point = sk.pubkey.serialize()
        # P256
        elif curve == b'p2':
            pk = fastecdsa.keys.get_public_key(bytes_to_int(secret_exponent), curve=fastecdsa.curve.P256)
            public_point = fastecdsa.encoding.sec1.SEC1Encoder.encode_public_key(pk)
        else:
            assert False

        return cls(public_point, secret_exponent, curve=curve, activation_code=activation_code)

    @classmethod
    def from_public_point(cls, public_point: bytes, curve=b'ed'):
        """ Creates a key object from a public elliptic point.

        :param public_point: elliptic point in the compressed format (see https://tezos.stackexchange.com/a/623/309)
        :param curve: b'sp' for secp251k1, b'p2' for P256/secp256r1, b'ed' for Ed25519 (default)
        """
        return cls(public_point, curve=curve)

    @classmethod
    def from_encoded_key(cls, key, passphrase=''):
        """ Creates a key object from a base58 encoded key.

        :param key: a public or secret key in base58 encoding
        :param passphrase: the passphrase used if the key provided is an encrypted private key
        """
        key = scrub_input(key)

        curve = key[:2]  # "sp", "p2" "ed"
        if curve not in [b'sp', b'p2', b'ed']:
            raise ValueError("Invalid prefix for a key encoding.")
        if not len(key) in [54, 55, 88, 98]:
            raise ValueError("Invalid length for a key encoding.")

        encrypted = (key[2:3] == b'e')
        public_or_secret = key[3:5] if encrypted else key[2:4]
        if public_or_secret not in [b'pk', b'sk']:
            raise Exception("Invalid prefix for a key encoding.")

        key = base58_decode(key)
        is_secret = (public_or_secret == b'sk')
        if not is_secret:
            return cls.from_public_point(key, curve)

        if encrypted:
            if not passphrase:
                raise ValueError("Encrypted key provided without a passphrase.")

            salt, encrypted_sk = key[:8], key[8:]
            encryption_key = hashlib.pbkdf2_hmac(
                hash_name="sha512",
                password=scrub_input(passphrase),
                salt=salt,
                iterations=32768,
                dklen=32
            )
            key = pysodium.crypto_secretbox_open(
                c=encrypted_sk, nonce=b'\000' * 24, k=encryption_key)
            del passphrase

        return cls.from_secret_exponent(key, curve)

    @classmethod
    def generate(cls, passphrase='', curve=b'ed', strength=128, language='english', export=True):
        """ Generates new key.

        :param passphrase: optional password
        :param curve: b'sp' for secp251k1, b'p2' for P256/secp256r1, b'ed' for Ed25519 (default)
        :param strength: mnemonic strength, default is 128
        :param language: mnemonic language, default is english
        :param export: export as json file in the current folder, default is True
        :rtype: Key
        """
        mnemonic = Mnemonic(language).generate(strength)
        key = cls.from_mnemonic(mnemonic, passphrase, curve=curve)

        if export:
            pkh = key.public_key_hash()
            data = {
                'mnemonic': mnemonic.split(),
                'pkh': pkh,
                'password': passphrase
            }
            with open(abspath(f'./{pkh}.json'), 'w+') as f:
                f.write(json.dumps(data))

        return key

    @classmethod
    def from_mnemonic(cls, mnemonic, passphrase='', email='', validate=True, curve=b'ed', activation_code=None):
        """ Creates a key object from a bip39 mnemonic.

        :param mnemonic: a 15 word bip39 english mnemonic
        :param passphrase: a mnemonic password or a fundraiser key
        :param email: email used if a fundraiser key is passed
        :param validate: whether to check mnemonic or not
        :param curve: b'sp' for secp251k1, b'p2' for P256/secp256r1, b'ed' for Ed25519 (default)
        :param activation_code: secret for initializing account balance
        :rtype: Key
        """
        if isinstance(mnemonic, list):
            mnemonic = ' '.join(mnemonic)

        if validate:
            validate_mnemonic(mnemonic)

        seed = Mnemonic.to_seed(mnemonic, passphrase=email + passphrase)

        if curve == b'ed':
            _, secret_exponent = pysodium.crypto_sign_seed_keypair(seed=seed[:32])
        elif curve == b'sp':
            secret_exponent = seed[:32]
        elif curve == b'p2':
            secret_exponent = seed[:32]
        else:
            assert False

        return cls.from_secret_exponent(secret_exponent, curve=curve, activation_code=activation_code)

    @classmethod
    def from_faucet(cls, path):
        """ Import key from a faucet file: https://faucet.tzalpha.net/

        :param path: path to the json file
        :rtype: Key
        """
        with open(expanduser(path), 'r') as f:
            data = json.loads(f.read())

        key = cls.from_mnemonic(
            mnemonic=data['mnemonic'],
            passphrase=data.get('password', ''),
            email=data.get('email', ''),
            activation_code=data['secret']
        )
        if key.public_key_hash() != data['pkh']:
            raise ValueError('Failed to import')

        return key

    @classmethod
    def from_alias(cls, alias, passphrase='', tezos_client_dir='~/.tezos-client'):
        """ Import secret key from tezos-client keychain.

        :param alias: key alias
        :param passphrase: if key is encrypted (optional)
        :param tezos_client_dir: path to the tezos client directory (default is `~/.tezos-client`)
        :rtype: Key
        """
        path = expanduser(join(tezos_client_dir, 'secret_keys'))
        with open(path, 'r') as f:
            data = json.loads(f.read())

        value = next(x['value'] for x in data if x['name'] == alias)
        prefix, sk = value.split(':', maxsplit=1)

        if prefix == 'encrypted':
            if not passphrase:
                passphrase = getpass(f'Please, enter passphrase for `{alias}`:\n')
            key = cls.from_encoded_key(sk, passphrase=passphrase)
            del passphrase
        else:
            key = cls.from_encoded_key(sk)

        return key

    def public_key(self):
        """ Creates base58 encoded public key representation.

        :returns: the public key associated with the private key
        """
        return base58_encode(self.public_point, self.curve + b'pk').decode()

    def secret_key(self, passphrase=None, ed25519_seed=True):
        """ Creates base58 encoded private key representation.

        :param passphrase: encryption phrase for the private key
        :param ed25519_seed: encode seed rather than full key for ed25519 curve (True by default)
        :returns: the secret key associated with this key, if available
        """
        if not self.secret_exponent:
            raise ValueError("Secret key not known.")

        if self.curve == b'ed' and ed25519_seed:
            key = pysodium.crypto_sign_sk_to_seed(self.secret_exponent)
        else:
            key = self.secret_exponent

        if passphrase:
            if not ed25519_seed:
                raise NotImplementedError

            salt = pysodium.randombytes(8)
            encryption_key = hashlib.pbkdf2_hmac(
                hash_name="sha512",
                password=scrub_input(passphrase),
                salt=salt,
                iterations=32768,
                dklen=32
            )
            encrypted_sk = pysodium.crypto_secretbox(
                msg=key, nonce=b'\000' * 24, k=encryption_key)
            key = salt + encrypted_sk  # we have to combine salt and encrypted key in order to decrypt later
            prefix = self.curve + b'esk'
        else:
            prefix = self.curve + b'sk'

        return base58_encode(key, prefix).decode()

    def public_key_hash(self):
        """ Creates base58 encoded public key hash for this key.

        :returns: the public key hash for this key
        """
        pkh = blake2b(data=self.public_point, digest_size=20).digest()
        prefix = {b'ed': b'tz1', b'sp': b'tz2', b'p2': b'tz3'}[self.curve]
        return base58_encode(pkh, prefix).decode()

    def sign(self, message, generic=False):
        """ Sign a raw sequence of bytes.

        :param message: sequence of bytes, raw format or hexadecimal notation
        :param generic: do not specify elliptic curve if set to True
        :returns: signature in base58 encoding
        """
        message = scrub_input(message)

        if not self.secret_exponent:
            raise ValueError("Cannot sign without a secret key.")

        # Ed25519
        if self.curve == b"ed":
            digest = pysodium.crypto_generichash(message)
            signature = pysodium.crypto_sign_detached(digest, self.secret_exponent)
        # Secp256k1
        elif self.curve == b"sp":
            pk = secp256k1.PrivateKey(self.secret_exponent)
            signature = pk.ecdsa_serialize_compact(
                pk.ecdsa_sign(message, digest=blake2b_32))
        # P256
        elif self.curve == b"p2":
            r, s = fastecdsa.ecdsa.sign(msg=message, d=bytes_to_int(self.secret_exponent), hashfunc=blake2b_32)
            signature = r.to_bytes(32, 'big') + s.to_bytes(32, 'big')
        else:
            assert False

        if generic:
            prefix = b'sig'
        else:
            prefix = self.curve + b'sig'

        return base58_encode(signature, prefix).decode()

    def verify(self, signature, message):
        """ Verify signature, raise exception if it is not valid.

        :param message: sequance of bytes, raw format or hexadecimal notation
        :param signature: a signature in base58 encoding
        :raises: ValueError if signature is not valid
        """
        signature = scrub_input(signature)
        message = scrub_input(message)

        if not self.public_point:
            raise ValueError("Cannot verify without a public key")

        if signature[:3] != b'sig':  # not generic
            if self.curve != signature[:2]:  # "sp", "p2" "ed"
                raise ValueError("Signature and public key curves mismatch.")

        signature = base58_decode(signature)

        # Ed25519
        if self.curve == b"ed":
            digest = pysodium.crypto_generichash(message)
            try:
                pysodium.crypto_sign_verify_detached(signature, digest, self.public_point)
            except ValueError:
                raise ValueError('Signature is invalid.')
        # Secp256k1
        elif self.curve == b"sp":
            pk = secp256k1.PublicKey(self.public_point, raw=True)
            sig = pk.ecdsa_deserialize_compact(signature)
            if not pk.ecdsa_verify(message, sig, digest=blake2b_32):
                raise ValueError('Signature is invalid.')
        # P256
        elif self.curve == b"p2":
            pk = fastecdsa.encoding.sec1.SEC1Encoder.decode_public_key(self.public_point, curve=fastecdsa.curve.P256)
            r, s = bytes_to_int(signature[:32]), bytes_to_int(signature[32:])
            if not fastecdsa.ecdsa.verify(sig=(r, s), msg=message, Q=pk, hashfunc=blake2b_32):
                raise ValueError('Signature is invalid.')
        else:
            assert False
