from hashlib import blake2b
from typing import List

from pytezos.crypto.encoding import base58_decode
from pytezos.crypto.encoding import base58_encode


def _hash_tuple(left: bytes = b'', right: bytes = b'') -> bytes:
    return blake2b(left + right, digest_size=32).digest()


def _reduce_operation_hashes(hashes: List[bytes]) -> bytes:
    a: List[bytes] = []

    def step(n: int) -> bytes:
        nonlocal a
        m = (n + 1) // 2
        for i in range(m):
            a[i] = _hash_tuple(a[2 * i], a[2 * i + 1])
        a[m] = _hash_tuple(a[n], a[n])
        if m == 1:
            return a[0]
        elif m % 2 == 0:
            return step(m)
        else:
            a[m + 1] = a[m]
            return step(m + 1)

    if len(hashes) == 0:
        return _hash_tuple()
    elif len(hashes) == 1:
        return _hash_tuple(hashes[0])
    else:
        res = list(map(lambda x: _hash_tuple(x), hashes))
        a = res + [res[-1]]
        return step(len(hashes))


def operation_list_hash(operation_hashes: List[str]) -> str:
    raw_items = list(map(lambda x: base58_decode(x.encode()), operation_hashes))
    res = _reduce_operation_hashes(raw_items)
    return base58_encode(res, b'Lo').decode()


def operation_list_list_hash(operations_hashes: List[List[str]]) -> str:
    lo_hashes = list(map(operation_list_hash, operations_hashes))
    raw_items = list(map(lambda x: base58_decode(x.encode()), lo_hashes))
    res = _reduce_operation_hashes(raw_items)
    return base58_encode(res, b'LLo').decode()


def block_payload_hash(predecessor: str, payload_round: int, operation_hashes: List[str]) -> str:
    """Calculate payload hash
    For each level, Tenderbake proceeds in rounds. Each round represents an attempt by the validators to agree on the
    content of the block for the current level, that is, on the sequence of non-consensus operations the block contains.
    We call this sequence the block’s payload.
    :param predecessor: block hash (base58 encoded) of the previous block
    :param payload_round: round number (int32)
    :param operation_hashes: flat list of non-consensus (validation pass > 0) operation hashes
    """
    # https://gitlab.com/tezos/tezos/-/blob/master/src/proto_alpha/lib_delegate/block_forge.ml#L166
    # https://gitlab.com/tezos/tezos/-/blob/master/src/proto_012_Psithaca/lib_protocol/block_payload_repr.ml#L41
    payload = [
        base58_decode(predecessor.encode()),
        payload_round.to_bytes(4, 'big'),
        _reduce_operation_hashes([base58_decode(x.encode()) for x in operation_hashes]),
    ]
    res = blake2b(b''.join(payload), digest_size=32).digest()
    return base58_encode(res, b'vh').decode()
