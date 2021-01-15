from typing import List, Type, Optional, Tuple, cast
from copy import copy
from pprint import pformat

from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.types.pair import PairType
from pytezos.michelson.types.domain import NatType, AddressType


class TicketType(MichelsonType, prim='ticket', args_len=1):
    type_impl: Type[PairType] = None

    def __init__(self, ticketer: str, item: MichelsonType, amount: int):
        super(TicketType, self).__init__()
        self.ticketer = ticketer
        self.item = item
        self.amount = amount

    def __copy__(self):
        assert False, 'forbidden'

    def __deepcopy__(self, memodict={}):
        assert False, 'forbidden'

    def __repr__(self):
        return pformat((self.ticketer, repr(self.item), self.amount))

    @classmethod
    def from_comb(cls, comb: PairType) -> 'TicketType':
        ticketer, item, amount = tuple(comb.iter_comb())  # type: AddressType, MichelsonType, NatType
        return cls(item=item,
                   ticketer=str(ticketer),
                   amount=int(amount))

    @staticmethod
    def join(left: 'TicketType', right: 'TicketType') -> Optional['TicketType']:
        if left.ticketer != right.ticketer or left.item != right.item:
            return None
        else:
            return TicketType(ticketer=left.ticketer, item=left.item, amount=left.amount + right.amount)

    @classmethod
    def construct_type(cls, type_args: List[Type['MichelsonType']],
                       field_name: Optional[str] = None,
                       type_name: Optional[str] = None,
                       type_params: Optional[list] = None, **kwargs) -> Type['TicketType']:
        type_impl = PairType.construct_type(type_args=[AddressType, type_args[0], NatType])
        type_class = super(TicketType, cls).construct_type(type_args=type_args,
                                                           field_name=field_name,
                                                           type_name=type_name,
                                                           type_impl=type_impl)
        return cast(Type['TicketType'], type_class)

    @classmethod
    def generate_pydoc(cls, definitions: List[Tuple[str, str]], inferred_name=None) -> str:
        name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
        item_doc = cls.type_args[0].generate_pydoc(definitions, inferred_name=f'{name}_value')
        doc = f'(\n\t  address  /* ticketer */\n\t  {item_doc}\n\t  nat  /* amount */\n\t)'
        definitions.insert(0, (name, doc))
        return f'${name}'

    @classmethod
    def dummy(cls):
        assert False, 'forbidden'

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'TicketType':
        comb = cls.type_impl.from_micheline_value(val_expr)
        return cls.from_comb(comb)

    @classmethod
    def from_python_object(cls, py_obj) -> 'MichelsonType':
        comb = cls.type_impl.from_python_object(py_obj)
        return cls.from_comb(comb)

    def to_comb(self) -> PairType:
        return self.type_impl.init(items=[AddressType(self.ticketer), self.item, NatType(self.amount)])

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return self.to_comb().to_micheline_value(mode=mode)

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.ticketer, self.item.to_python_object(try_unpack=try_unpack), self.amount

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        return self

    def split(self, amount_left: int, amount_right: int) -> Optional[Tuple['TicketType', 'TicketType']]:
        if amount_left + amount_right != self.amount:
            return None
        else:
            left = TicketType(ticketer=self.ticketer, item=copy(self.item), amount=amount_left)
            right = TicketType(ticketer=self.ticketer, item=copy(self.item), amount=amount_right)
            return left, right
