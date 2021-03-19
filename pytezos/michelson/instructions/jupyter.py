import re
from functools import wraps
from typing import List, Type, cast

from pytezos.context.abstract import AbstractContext
from pytezos.context.mixin import nodes
from pytezos.jupyter import is_interactive
from pytezos.michelson.instructions.base import MichelsonInstruction, format_stdout
from pytezos.michelson.micheline import MichelineLiteral
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types.base import MichelsonType


def jupyter_only(fn):
    @wraps(fn)
    def wrapper(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        # if not is_interactive():
        #     raise Exception(f'`{cls.__name__}` instruction could be used only in Jupyter notebooks')
        return fn(cls, stack, stdout, context)
    return wrapper


class DumpAllInstruction(MichelsonInstruction, prim='DUMP'):

    @classmethod
    @jupyter_only
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        print(stack)
        stack.push(stack.items[:])  # type: ignore
        return cls()


class DumpInstruction(MichelsonInstruction, prim='DUMP', args_len=1):

    @classmethod
    @jupyter_only
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        literal: Type[MichelineLiteral] = cls.args[0]  # type: ignore

        count = cast(int, literal.literal)
        if len(stack) > 0:
            count = min(count, len(stack))
            stack.push(stack.items[:count])  # type: ignore

        return cls()


class PrintInstruction(MichelsonInstruction, prim='PRINT', args_len=1):

    @classmethod
    @jupyter_only
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
    @jupyter_only
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        literal = cls.args[0]
        debug = bool(literal.get_int())  # type: ignore
        context.debug = debug  # type: ignore
        return cls()


class DropAllInstruction(MichelsonInstruction, prim='DROP_ALL'):

    @classmethod
    @jupyter_only
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        stack.items = []
        return cls()


class PatchInstruction(MichelsonInstruction, prim='PATCH', args_len=1):

    allowed_primitives = ['AMOUNT', 'BALANCE', 'CHAIN_ID', 'SENDER', 'SOURCE', 'NOW']

    @classmethod
    @jupyter_only
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
            raise Exception(f'Expected one of {cls.allowed_primitives}, got {res_type.prim}')
        return cls()


class PatchValueInstruction(MichelsonInstruction, prim='PATCH', args_len=2):

    allowed_primitives = ['AMOUNT', 'BALANCE', 'CHAIN_ID', 'SENDER', 'SOURCE', 'NOW']

    @classmethod
    @jupyter_only
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
            # FIXME: Both formats?
            context.now = literal.get_int()  # type: ignore
        else:
            raise Exception(f'Expected one of {cls.allowed_primitives}, got {res_type.prim}')
        return cls()


class ResetInstruction(MichelsonInstruction, prim='RESET'):

    @classmethod
    @jupyter_only
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        context.network = None  # type: ignore
        context.chain_id = None  # type: ignore
        context.big_maps = {}  # type: ignore
        stack.items = []
        return cls()


class ResetValueInstruction(MichelsonInstruction, prim='RESET', args_len=1):

    @classmethod
    @jupyter_only
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
