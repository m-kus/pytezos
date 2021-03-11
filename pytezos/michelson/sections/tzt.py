from typing import List
from typing import Type

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline


# FIXME: CodeSection copypaste
class InputSection(Micheline, prim='input', args_len=1):

    @staticmethod
    def match(input_expr) -> Type['InputSection']:
        cls = Micheline.match(input_expr)
        if not issubclass(cls, InputSection):
            cls = InputSection.create_type(args=[cls])
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_input_expr(cls.as_micheline_expr())
        stdout.append('input: updated')


# FIXME: CodeSection copypaste
class OutputSection(Micheline, prim='output', args_len=1):

    @staticmethod
    def match(output_expr) -> Type['OutputSection']:
        cls = Micheline.match(output_expr)
        if not issubclass(cls, OutputSection):
            cls = OutputSection.create_type(args=[cls])
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_output_expr(cls.as_micheline_expr())
        stdout.append('output: updated')


# FIXME: CodeSection copypaste
class SenderSection(Micheline, prim='sender', args_len=1):

    @staticmethod
    def match(output_expr) -> Type['SenderSection']:
        cls = Micheline.match(output_expr)
        if not issubclass(cls, SenderSection):
            cls = SenderSection.create_type(args=[cls])
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_sender_expr(cls.as_micheline_expr())
        stdout.append('sender: updated')

# FIXME: CodeSection copypaste
class BalanceSection(Micheline, prim='balance', args_len=1):

    @staticmethod
    def match(output_expr) -> Type['BalanceSection']:
        cls = Micheline.match(output_expr)
        if not issubclass(cls, BalanceSection):
            cls = BalanceSection.create_type(args=[cls])
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_balance_expr(cls.as_micheline_expr())
        stdout.append('balance: updated')

# FIXME: CodeSection copypaste
class AmountSection(Micheline, prim='amount', args_len=1):

    @staticmethod
    def match(output_expr) -> Type['AmountSection']:
        cls = Micheline.match(output_expr)
        if not issubclass(cls, AmountSection):
            cls = AmountSection.create_type(args=[cls])
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_amount_expr(cls.as_micheline_expr())
        stdout.append('amount: updated')


# FIXME: CodeSection copypaste
class SelfSection(Micheline, prim='self', args_len=1):

    @staticmethod
    def match(output_expr) -> Type['SelfSection']:
        cls = Micheline.match(output_expr)
        if not issubclass(cls, SelfSection):
            cls = SelfSection.create_type(args=[cls])
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_self_expr(cls.as_micheline_expr())
        stdout.append('self: updated')


# FIXME: CodeSection copypaste
class NowSection(Micheline, prim='now', args_len=1):

    @staticmethod
    def match(output_expr) -> Type['NowSection']:
        cls = Micheline.match(output_expr)
        if not issubclass(cls, NowSection):
            cls = NowSection.create_type(args=[cls])
        return cls  # type: ignore

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_now_expr(cls.as_micheline_expr())
        stdout.append('now: updated')
