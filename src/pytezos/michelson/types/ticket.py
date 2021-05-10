from copy import copy
from pprint import pformat
from typing import List, Optional, Tuple, Type, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.micheline import Micheline
from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.types.domain import AddressType, NatType
from pytezos.michelson.types.pair import PairType


class TicketType(MichelsonType, prim='ticket', args_len=1):

    def __init__(self, ticketer: str, item: MichelsonType, amount: int):
        super(TicketType, self).__init__()
        self.ticketer = ticketer
        self.item = item
        self.amount = amount

    def __copy__(self):
        assert False, 'forbidden'

    def __repr__(self):
        return pformat((self.ticketer, repr(self.item), self.amount))

    @staticmethod
    def create(ticketer: str, item: MichelsonType, amount: int) -> 'TicketType':
        cls = TicketType.create_type(args=[item.get_anon_type()])
        return cls(ticketer, item, amount)  # type: ignore

    @classmethod
    def from_comb(cls, comb: PairType) -> 'TicketType':
        ticketer, item, amount = cast(Tuple[AddressType, MichelsonType, NatType], tuple(comb.iter_comb()))
        return cls(
            item=item,
            ticketer=str(ticketer),
            amount=int(amount),
        )

    @staticmethod
    def join(left: 'TicketType', right: 'TicketType') -> Optional['TicketType']:
        left.assert_type_equal(type(right))
        if left.ticketer != right.ticketer or left.item != right.item:
            return None
        else:
            return TicketType(ticketer=left.ticketer, item=left.item, amount=left.amount + right.amount)

    @classmethod
    def generate_pydoc(cls, definitions: List[Tuple[str, str]], inferred_name=None, comparable=False) -> str:
        super(TicketType, cls).generate_pydoc(definitions)
        param_expr = micheline_to_michelson(cls.args[0].as_micheline_expr())
        if cls.args[0].args:
            name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
            param_name = f'{name}_param'
            definitions.insert(0, (param_name, param_expr))
            return f'ticket (${param_name})'
        else:
            return f'ticket ({param_expr})'

    @classmethod
    def dummy(cls, context: AbstractContext):
        assert False, 'forbidden'

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'TicketType':
        type_impl = PairType.create_type(args=[AddressType, cls.args[0], NatType])
        comb = type_impl.from_micheline_value(val_expr)
        return cls.from_comb(comb)

    @classmethod
    def from_python_object(cls, py_obj) -> 'MichelsonType':
        type_impl = PairType.create_type(args=[AddressType, cls.args[0], NatType])
        comb = type_impl.from_python_object(py_obj)
        return cls.from_comb(comb)

    def to_comb(self) -> PairType:
        return PairType.from_comb(items=[AddressType(self.ticketer), self.item, NatType(self.amount)])

    def to_literal(self) -> Type[Micheline]:
        return self.to_comb().to_literal()

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return self.to_comb().to_micheline_value(mode=mode)

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        assert not comparable, f'{self.prim} is not comparable'
        return self.ticketer, self.item.to_python_object(try_unpack=try_unpack, comparable=True), self.amount

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        return self

    def split(self, amount_left: int, amount_right: int) -> Optional[Tuple['TicketType', 'TicketType']]:
        if amount_left + amount_right != self.amount:
            return None
        else:
            left = TicketType(ticketer=self.ticketer, item=copy(self.item), amount=amount_left)
            right = TicketType(ticketer=self.ticketer, item=copy(self.item), amount=amount_right)
            return left, right
