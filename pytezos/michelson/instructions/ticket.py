from typing import List, cast, Tuple

from pytezos.michelson.instructions.base import format_stdout, MichelsonInstruction
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import PairType, TicketType, OptionType, NatType, MichelsonType
from pytezos.context.abstract import AbstractContext


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
            res = OptionType.none(type(left))
        else:
            res = OptionType.from_some(res)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [pair], [res]))
        return cls()


class ReadTicketInstruction(MichelsonInstruction, prim='READ_TICKET'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        ticket = cast(TicketType, stack.pop1())
        ticket.assert_type_in(TicketType)
        res = ticket.to_comb()
        stack.push(ticket)
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [ticket], [res, ticket]))
        return cls()


class SplitTicketInstruction(MichelsonInstruction, prim='SPLIT_TICKET'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        ticket, amounts = cast(Tuple[TicketType, PairType], stack.pop2())
        ticket.assert_type_in(TicketType)
        amounts.assert_type_in(PairType)
        a, b = tuple(amounts)  # type: NatType, NatType
        a.assert_type_equal(NatType)
        b.assert_type_equal(NatType)
        res = ticket.split(int(a), int(b))
        if res is None:
            res = OptionType.none(PairType.create_type(args=[type(ticket), type(ticket)]))
        else:
            res = OptionType.from_some(PairType.from_comb(list(res)))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [ticket, amounts], [res]))
        return cls()


class TicketInstruction(MichelsonInstruction, prim='TICKET'):

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        item, amount = cast(Tuple[MichelsonType, NatType], stack.pop2())
        amount.assert_type_equal(NatType)
        address = context.get_self_address()
        res = TicketType.init(address, item, int(amount))
        stack.push(res)
        stdout.append(format_stdout(cls.prim, [item, amount], [res]))
        return cls()
