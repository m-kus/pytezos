import re
from typing import List, Type, cast

import strict_rfc3339  # type: ignore

from pytezos.context.abstract import AbstractContext
from pytezos.context.mixin import nodes
from pytezos.michelson.instructions.base import MichelsonInstruction
from pytezos.michelson.micheline import MichelineLiteral, MichelsonRuntimeError
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types.base import MichelsonType


class DumpAllInstruction(MichelsonInstruction, prim='DUMP'):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        stdout.append(str(stack))
        # FIXME: Should not modify stack, just return value
        stack.push(stack.items[:])  # type: ignore
        return cls()


class DumpInstruction(MichelsonInstruction, prim='DUMP', args_len=1):
    def __init__(self, items: List[MichelsonType]):
        super().__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        literal: Type[MichelineLiteral] = cls.args[0]  # type: ignore

        count = cast(int, literal.literal)
        count = min(count, len(stack))

        return cls(stack.items[:count])


class PrintInstruction(MichelsonInstruction, prim='PRINT', args_len=1):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        literal: Type[MichelineLiteral] = cls.args[0]  # type: ignore

        template = literal.get_string()

        def format_stack_item(match):
            i = int(match.groups()[0])
            assert i < len(stack), f'requested {i}th element, got only {len(stack)} items'
            return repr(stack.items[i])

        message = re.sub(r'{(\d+)}', format_stack_item, template)
        stdout.append(message)
        return cls()


class DebugInstruction(MichelsonInstruction, prim='DEBUG', args_len=1):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        literal = cls.args[0]
        debug = bool(literal.get_int())  # type: ignore
        context.debug = debug  # type: ignore
        return cls()


class DropAllInstruction(MichelsonInstruction, prim='DROP_ALL'):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        stack.items = []
        return cls()


class PatchInstruction(MichelsonInstruction, prim='PATCH', args_len=1):

    allowed_primitives = ['AMOUNT', 'BALANCE', 'CHAIN_ID', 'SENDER', 'SOURCE', 'NOW']

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):

        res_type: MichelsonType
        res_type = cls.args[0]  # type: ignore

        if res_type.prim == 'AMOUNT':
            context.amount = None  # type: ignore
        elif res_type.prim == 'BALANCE':
            context.balance = None  # type: ignore
        elif res_type.prim == 'CHAIN_ID':
            context.chain_id = None  # type: ignore
        elif res_type.prim == 'SENDER':
            context.sender = None  # type: ignore
        elif res_type.prim == 'SOURCE':
            context.source = None  # type: ignore
        elif res_type.prim == 'NOW':
            context.now = None  # type: ignore
        else:
            raise ValueError(f'Expected one of {cls.allowed_primitives}, got {res_type.prim}')
        return cls()


class PatchValueInstruction(MichelsonInstruction, prim='PATCH', args_len=2):

    allowed_primitives = ['AMOUNT', 'BALANCE', 'CHAIN_ID', 'SENDER', 'SOURCE', 'NOW']

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        res_type: MichelsonType
        literal: Type[MichelineLiteral]
        res_type, literal = cls.args  # type: ignore

        if res_type.prim == 'AMOUNT':
            context.amount = literal.get_int()  # type: ignore
        elif res_type.prim == 'BALANCE':
            context.balance = literal.get_int()  # type: ignore
        elif res_type.prim == 'CHAIN_ID':
            context.chain_id = literal.get_string()  # type: ignore
        elif res_type.prim == 'SENDER':
            context.sender = literal.get_string()  # type: ignore
        elif res_type.prim == 'SOURCE':
            context.source = literal.get_string()  # type: ignore
        elif res_type.prim == 'NOW':
            try:
                context.now = literal.get_int()  # type: ignore
            # FIXME: Why does TypeError appear to be wrapped?
            except (TypeError, MichelsonRuntimeError):
                context.now = int(strict_rfc3339.rfc3339_to_timestamp(literal.get_string()))  # type: ignore
        else:
            raise ValueError(f'Expected one of {cls.allowed_primitives}, got {res_type.prim}')
        return cls()


class ResetInstruction(MichelsonInstruction, prim='RESET'):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        context.network = None  # type: ignore
        context.chain_id = None  # type: ignore
        context.big_maps = {}  # type: ignore
        stack.items = []
        return cls()


class ResetValueInstruction(MichelsonInstruction, prim='RESET', args_len=1):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        literal: Type[MichelineLiteral]
        literal = cls.args[0]  # type: ignore

        network = literal.get_string()
        if network not in nodes:
            raise Exception(f'Expected one of {nodes}, got {network}')

        context.network = network  # type: ignore
        context.chain_id = context.shell.chains.main.chain_id()  # type: ignore
        context.big_maps = {}  # type: ignore
        stack.items = []
        return cls()
