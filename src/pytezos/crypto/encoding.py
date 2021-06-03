from typing import Union

import base58  # type: ignore


def tb(l):
    return b''.join(map(lambda x: x.to_bytes(1, 'big'), l))


base58_encodings = [
    #    Encoded   |               Decoded             |
    # prefix | len | prefix                      | len | Data type
    (b"B",     51,   tb([1, 52]),                  32,   u"block hash"),
    (b"o",     51,   tb([5, 116]),                 32,   u"operation hash"),
    (b"Lo",    52,   tb([133, 233]),               32,   u"operation list hash"),
    (b"LLo",   53,   tb([29, 159, 109]),           32,   u"operation list list hash"),
    (b"P",     51,   tb([2, 170]),                 32,   u"protocol hash"),
    (b"Co",    52,   tb([79, 199]),                32,   u"context hash"),

    (b"tz1",   36,   tb([6, 161, 159]),            20,   u"ed25519 public key hash"),
    (b"tz2",   36,   tb([6, 161, 161]),            20,   u"secp256k1 public key hash"),
    (b"tz3",   36,   tb([6, 161, 164]),            20,   u"p256 public key hash"),
    (b"KT1",   36,   tb([2, 90, 121]),             20,   u"originated address"),

    (b"id",    30,   tb([153, 103]),               16,   u"cryptobox public key hash"),

    (b'expr',  54,   tb([13, 44, 64, 27]),         32,   u'script expression'),
    (b"edsk",  54,   tb([13, 15, 58, 7]),          32,   u"ed25519 seed"),
    (b"edpk",  54,   tb([13, 15, 37, 217]),        32,   u"ed25519 public key"),
    (b"spsk",  54,   tb([17, 162, 224, 201]),      32,   u"secp256k1 secret key"),
    (b"p2sk",  54,   tb([16, 81, 238, 189]),       32,   u"p256 secret key"),

    (b"edesk", 88,   tb([7, 90, 60, 179, 41]),     56,   u"ed25519 encrypted seed"),
    (b"spesk", 88,   tb([9, 237, 241, 174, 150]),  56,   u"secp256k1 encrypted secret key"),
    (b"p2esk", 88,   tb([9, 48, 57, 115, 171]),    56,   u"p256_encrypted_secret_key"),

    (b"sppk",  55,   tb([3, 254, 226, 86]),        33,   u"secp256k1 public key"),
    (b"p2pk",  55,   tb([3, 178, 139, 127]),       33,   u"p256 public key"),
    (b"SSp",   53,   tb([38, 248, 136]),           33,   u"secp256k1 scalar"),
    (b"GSp",   53,   tb([5, 92, 0]),               33,   u"secp256k1 element"),

    (b"edsk",  98,   tb([43, 246, 78, 7]),         64,   u"ed25519 secret key"),
    (b"edsig", 99,   tb([9, 245, 205, 134, 18]),   64,   u"ed25519 signature"),
    (b"spsig", 99,   tb([13, 115, 101, 19, 63]),   64,   u"secp256k1 signature"),
    (b"p2sig", 98,   tb([54, 240, 44, 52]),        64,   u"p256 signature"),
    (b"sig",   96,   tb([4, 130, 43]),             64,   u"generic signature"),

    (b'Net',   15,   tb([87, 82, 0]),              4,    u"chain id"),
    (b'nce',   53,   tb([69, 220, 169]),           32,   u'seed nonce hash'),
    (b'btz1',  37,   tb([1, 2, 49, 223]),          20,   u'blinded public key hash'),
]

operation_tags = {
    'endorsement': 0,
    'seed_nonce_revelation': 1,
    'double_endorsement_evidence': 2,
    'double_baking_evidence': 3,
    'account_activation': 4,
    'proposals': 5,
    'ballot': 6,
    'reveal': 7,
    'transaction': 8,
    'origination': 9,
    'delegation': 10
}


def scrub_input(v: Union[str, bytes]) -> bytes:
    if isinstance(v, bytes):
        pass
    elif isinstance(v, str):
        try:
            _ = int(v, 16)
        except ValueError:
            v = v.encode('ascii')
        else:
            if v.startswith('0x'):
                v = v[2:]
            v = bytes.fromhex(v)
    else:
        raise TypeError(
            "a bytes-like object is required (also str), not '%s'" %
            type(v).__name__)
    return v


def base58_decode(v: bytes) -> bytes:
    """ Decode data using Base58 with checksum + validate binary prefix against known kinds and cut in the end.

    :param v: Array of bytes (use string.encode())
    :returns: bytes
    """
    try:
        prefix_len = next(
            len(encoding[2])
            for encoding in base58_encodings
            if len(v) == encoding[1] and v.startswith(encoding[0])
        )
    except StopIteration as e:
        raise ValueError('Invalid encoding, prefix or length mismatch.') from e

    return base58.b58decode_check(v)[prefix_len:]


def base58_encode(v: bytes, prefix: bytes) -> bytes:
    """ Encode data using Base58 with checksum and add an according binary prefix in the end.

    :param v: Array of bytes
    :param prefix: Human-readable prefix (use b'') e.g. b'tz', b'KT', etc
    :returns: bytes (use string.decode())
    """
    try:
        encoding = next(
            encoding
            for encoding in base58_encodings
            if len(v) == encoding[3] and prefix == encoding[0]
        )
    except StopIteration as e:
        raise ValueError('Invalid encoding, prefix or length mismatch.') from e

    return base58.b58encode_check(encoding[2] + v)


def _validate(v: Union[str, bytes], prefixes: list):
    if isinstance(v, str):
        v = v.encode()
    v = scrub_input(v)
    if any(map(v.startswith, prefixes)):
        base58_decode(v)
    else:
        raise ValueError('Unknown prefix.')


def validate_pkh(v: Union[str, bytes]):
    """ Ensure parameter is a public key hash (starts with b'tz1', b'tz2', b'tz3')

    :param v: string or bytes
    :raises ValueError: if parameter is not a public key hash
    """
    return _validate(v, prefixes=[b'tz1', b'tz2', b'tz3'])


def validate_sig(v: Union[str, bytes]):
    """ Ensure parameter is a signature (starts with b'edsig', b'spsig', b'p2sig', b'sig')

    :param v: string or bytes
    :raises ValueError: if parameter is not a signature
    """
    return _validate(v, prefixes=[b'edsig', b'spsig', b'p2sig', b'sig'])


def is_pkh(v: Union[str, bytes]) -> bool:
    """ Check if value is a public key hash.
    """
    try:
        validate_pkh(v)
    except (ValueError, TypeError):
        return False
    return True


def is_sig(v: Union[str, bytes]) -> bool:
    """ Check if value is a signature.
    """
    try:
        validate_sig(v)
    except (ValueError, TypeError):
        return False
    return True


def is_bh(v: Union[str, bytes]) -> bool:
    """ Check if value is a block hash.
    """
    try:
        _validate(v, prefixes=[b'B'])
    except (ValueError, TypeError):
        return False
    return True


def is_ogh(v) -> bool:
    """ Check if value is an operation group hash.
    """
    try:
        _validate(v, prefixes=[b'o'])
    except (ValueError, TypeError):
        return False
    return True


def is_kt(v: Union[str, bytes]) -> bool:
    """ Check if value is a KT address.
    """
    try:
        _validate(v, prefixes=[b'KT1'])
    except (ValueError, TypeError):
        return False
    return True


def is_public_key(v: Union[str, bytes]) -> bool:
    """ Check if value is a public key.
    """
    try:
        _validate(v, prefixes=[b"edsk", b"edpk", b"spsk", b"p2sk", b"sppk", b"p2pk"])
    except (ValueError, TypeError):
        return False
    return True


def is_chain_id(v: Union[str, bytes]) -> bool:
    """ Check if value is a chain id.
    """
    try:
        _validate(v, prefixes=[b'Net'])
    except (ValueError, TypeError):
        return False
    return True


def is_address(v: Union[str, bytes]) -> bool:
    """ Check if value is a tz/KT address
    """
    if isinstance(v, bytes):
        v = v.decode()
    address = v.split('%')[0]
    return is_kt(address) or is_pkh(address)
