from typing import List
from typing import Tuple
from typing import cast

from pytezos.context.abstract import AbstractContext
from pytezos.michelson.instructions.base import MichelsonInstruction
from pytezos.michelson.instructions.base import format_stdout
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import MichelsonType
from pytezos.michelson.types import NatType
from pytezos.michelson.types import OptionType
from pytezos.michelson.types import PairType
from pytezos.michelson.types import TicketType


class JoinTicketsInstruction(MichelsonInstruction, prim='JOIN_TICKETS'):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        pair = cast(PairType, stack.pop1())
        pair.assert_type_in(PairType)
        left, right = tuple(pair)
        assert isinstance(left, TicketType), f'expected ticket on the left, got {left.prim}'
        assert isinstance(right, TicketType), f'expected ticket on the right, got {right.prim}'
        res = TicketType.join(left, right)
        if res is None:
            res = OptionType.none(type(left))  # type: ignore
        else:
            res = OptionType.from_some(res)  # type: ignore
        stack.push(res)  # type: ignore
        stdout.append(format_stdout(cls.prim, [pair], [res]))  # type: ignore
        return cls(stack_items_added=1)


class ReadTicketInstruction(MichelsonInstruction, prim='READ_TICKET'):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        ticket = cast(TicketType, stack.pop1())
        ticket.assert_type_in(TicketType)
        res = ticket.to_comb()
        stack.push(ticket)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [ticket], [res, ticket]))  # type: ignore
        return cls(stack_items_added=2)


class SplitTicketInstruction(MichelsonInstruction, prim='SPLIT_TICKET'):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        ticket, amounts = cast(Tuple[TicketType, PairType], stack.pop2())
        ticket.assert_type_in(TicketType)
        amounts.assert_type_in(PairType)
        a, b = cast(Tuple[NatType, NatType], tuple(amounts))
        a.assert_type_equal(NatType)
        b.assert_type_equal(NatType)
        res = ticket.split(int(a), int(b))
        if res is None:
            res = OptionType.none(PairType.create_type(args=[type(ticket), type(ticket)]))  # type: ignore
        else:
            res = OptionType.from_some(PairType.from_comb(list(res)))  # type: ignore
        stack.push(res)  # type: ignore
        stdout.append(format_stdout(cls.prim, [ticket, amounts], [res]))  # type: ignore
        return cls(stack_items_added=1)


class TicketDeprecatedInstruction(MichelsonInstruction, prim='TICKET_DEPRECATED'):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        item, amount = cast(Tuple[MichelsonType, NatType], stack.pop2())
        amount.assert_type_equal(NatType)
        address = context.get_self_address()
        res = TicketType.create(address, item, int(amount))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [item, amount], [res]))  # type: ignore
        return cls(stack_items_added=1)


class TicketInstruction(MichelsonInstruction, prim='TICKET'):
    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        item, amount = cast(Tuple[MichelsonType, NatType], stack.pop2())
        amount.assert_type_equal(NatType)
        address = context.get_self_address()

        if int(amount) > 0:
            ticket = TicketType.create(address, item, int(amount))
            res = OptionType.from_some(ticket)
        else:
            ticket_ty = TicketType.create_type(args=[item.get_anon_type()])
            res = OptionType.none(ticket_ty)

        stack.push(res)
        stdout.append(format_stdout(cls.prim, [item, amount], [res]))  # type: ignore
        return cls(stack_items_added=1)
