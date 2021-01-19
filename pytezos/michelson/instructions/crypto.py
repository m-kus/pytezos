from hashlib import sha256, sha512
from typing import List, Tuple, Callable, cast

from pytezos.crypto.key import blake2b_32, Key

from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import BytesType, KeyType, SignatureType, BoolType, KeyHashType
from pytezos.michelson.instructions.base import MichelsonInstruction, dispatch_types, format_stdout


def execute_hash(prim: str, stack: MichelsonStack, stdout: List[str], hash_digest: Callable[[bytes], bytes]):
    a = cast(BytesType, stack.pop1())
    a.assert_equal_types(BytesType)
    res = BytesType.from_bytes(hash_digest(bytes(a)))
    stack.push(res)
    stdout.append(format_stdout(prim, [a], [res]))


class Blake2bInstruction(MichelsonInstruction, prim='BLAKE2B'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        execute_hash(cls.prim, stack, stdout, lambda x: blake2b_32(bytes(x)).digest())
        return cls()


class Sha256Instruction(MichelsonInstruction, prim='SHA256'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        execute_hash(cls.prim, stack, stdout, lambda x: sha256(bytes(x)).digest())
        return cls()


class Sha512Instruction(MichelsonInstruction, prim='SHA512'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        execute_hash(cls.prim, stack, stdout, lambda x: sha512(bytes(x)).digest())
        return cls()


class CheckSignatureInstruction(MichelsonInstruction, prim='CHECK_SIGNATURE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        pk, sig, msg = cast(Tuple[KeyType, SignatureType, BytesType], stack.pop3())
        pk.assert_equal_types(KeyType)
        sig.assert_equal_types(SignatureType)
        msg.assert_equal_types(BytesType)
        key = Key.from_encoded_key(str(pk))
        try:
            key.verify(signature=str(sig), message=bytes(msg))
        except ValueError:
            res = BoolType(False)
        else:
            res = BoolType(True)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [pk, sig, msg], [res]))
        return cls()


class HashKeyInstruction(MichelsonInstruction, prim='HASH_KEY'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        a = cast(KeyType, stack.pop1())
        a.assert_equal_types(KeyType)
        key = Key.from_encoded_key(str(a))
        res = KeyHashType.from_value(key.public_key_hash())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))
        return cls()
