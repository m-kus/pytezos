from copy import copy
from typing import List, Optional, Type

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline, MichelineLiteral, MichelineSequence, parse_micheline_literal
from pytezos.michelson.types.base import MichelsonType


class SaplingTransactionType(MichelsonType, prim='sapling_transaction', args_len=1):
    pass


class SaplingStateType(MichelsonType, prim='sapling_state', args_len=1):

    def __init__(self, ptr: Optional[int] = None):
        super(SaplingStateType, self).__init__()
        self.ptr = ptr
        self.context: Optional[AbstractContext] = None

    def __repr__(self):
        if self.ptr:
            return f'<{self.ptr}>'
        else:
            return '{}'

    @staticmethod
    def empty(memo_size: int):
        cls = SaplingStateType.create_type(args=[MichelineLiteral.create(memo_size)])
        return cls()

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'SaplingStateType':
        if isinstance(val_expr, dict):
            ptr = parse_micheline_literal(val_expr, {'int': int})
            return cls(ptr=ptr)
        elif isinstance(val_expr, list):
            return cls()
        else:
            assert False, f'unexpected value {val_expr}'

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if lazy_diff:
            return []
        else:
            assert self.ptr is not None, f'Sapling_state id is not defined'
            return {'int': str(self.ptr)}

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        assert not comparable, f'{self.prim} is not comparable'
        if self.ptr is not None:
            return self.ptr
        else:
            return []

    def to_literal(self) -> Type[Micheline]:
        if self.ptr is not None:
            return MichelineLiteral.create(self.ptr)
        else:
            return MichelineSequence.create_type(args=[])

    def attach_context(self, context: AbstractContext, big_map_copy=False):
        self.context = context
        self.ptr = context.get_tmp_sapling_state_id()

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        return copy(self)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable') -> 'MichelsonType':
        assert self.ptr is not None, f'Sapling_state ID is not defined'
        if self.context:
            dst_ptr, _ = self.context.get_sapling_state_diff()
        else:
            dst_ptr = self.ptr
        return type(self)(dst_ptr)
