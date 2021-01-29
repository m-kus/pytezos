import sha3
from hashlib import sha256, sha512
from typing import List, Tuple, Callable, cast, Any, Type

from pytezos.crypto.key import blake2b_32, Key

from pytezos.michelson.interpreter.stack import MichelsonStack
from pytezos.michelson.types import BytesType, KeyType, SignatureType, BoolType, KeyHashType, SaplingStateType
from pytezos.michelson.micheline import parse_micheline_literal
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.context.base import NodeContext


def execute_hash(prim: str, stack: MichelsonStack, stdout: List[str], hash_digest: Callable[[bytes], bytes]):
    a = cast(BytesType, stack.pop1())
    a.assert_equal_types(BytesType)
    res = BytesType.unpack(hash_digest(bytes(a)))
    stack.push(res)
    stdout.append(format_stdout(prim, [a], [res]))


class Blake2bInstruction(MichelsonInstruction, prim='BLAKE2B'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_hash(cls.prim, stack, stdout, lambda x: blake2b_32(bytes(x)).digest())
        return cls()


class Sha256Instruction(MichelsonInstruction, prim='SHA256'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_hash(cls.prim, stack, stdout, lambda x: sha256(bytes(x)).digest())
        return cls()


class Sha512Instruction(MichelsonInstruction, prim='SHA512'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_hash(cls.prim, stack, stdout, lambda x: sha512(bytes(x)).digest())
        return cls()


class Sha3Instruction(MichelsonInstruction, prim='SHA3'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_hash(cls.prim, stack, stdout, lambda x: sha3.sha3_256(bytes(x)).digest())
        return cls()


class KeccakInstruction(MichelsonInstruction, prim='KECCAK'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        execute_hash(cls.prim, stack, stdout, lambda x: sha3.keccak_256(bytes(x)).digest())
        return cls()


class CheckSignatureInstruction(MichelsonInstruction, prim='CHECK_SIGNATURE'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
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
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        a = cast(KeyType, stack.pop1())
        a.assert_equal_types(KeyType)
        key = Key.from_encoded_key(str(a))
        res = KeyHashType.from_value(key.public_key_hash())
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [a], [res]))
        return cls()


class PairingCheckInstruction(MichelsonInstruction, prim='PAIRING_CHECK'):
    pass


class SaplingEmptyStateInstruction(MichelsonInstruction, prim='SAPLING_EMPTY_STATE', args_len=1):

    @classmethod
    def create_type(cls, args: List[Any], **kwargs) -> Type['SaplingEmptyStateInstruction']:
        res = type(cls.__name__, (cls,), dict(args=[parse_micheline_literal(args[0], {'int': int})], **kwargs))
        return cast(Type['SaplingEmptyStateInstruction'], res)

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        res = SaplingStateType.empty(cls.args[0])
        res.attach_context(context)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [], [res]))
        return cls()


class SaplingVerifyUpdateInstruction(MichelsonInstruction, prim='SAPLING_VERIFY_UPDATE'):
    pass
