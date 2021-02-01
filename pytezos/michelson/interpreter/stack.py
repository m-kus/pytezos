from typing import List, Tuple, Optional
from pprint import pformat

from pytezos.michelson.types.base import MichelsonType


class MichelsonStack:

    def __init__(self, items: Optional[List[MichelsonType]] = None):
        self.items = items or []
        self.protected = 0

    @classmethod
    def from_items(cls, items: List[MichelsonType]):
        return cls(items)

    def protect(self, count: int):
        assert len(self.items) >= count, f'got {len(self.items)} items, wanted to protect {count}'
        self.protected += count

    def restore(self, count: int):
        assert self.protected >= count, f'wanted to restore {count}, only {self.protected} protected'
        self.protected -= count

    def push(self, item: MichelsonType):
        assert item.is_pushable(), f'{item.prim} is not pushable'
        self.items.insert(self.protected, item)

    def peek(self) -> MichelsonType:
        assert len(self.items) > 0, 'stack is empty'
        return self.items[self.protected]

    def pop(self, count: int) -> List[MichelsonType]:
        assert len(self.items) - self.protected >= count, \
            f'got {len(self.items) - self.protected} items, requested {count} '
        return [self.items.pop(self.protected) for _ in range(count)]

    def pop1(self) -> MichelsonType:
        a, = self.pop(count=1)
        return a

    def pop2(self) -> Tuple[MichelsonType, MichelsonType]:
        a, b = self.pop(count=2)
        return a, b

    def pop3(self) -> Tuple[MichelsonType, MichelsonType, MichelsonType]:
        a, b, c = self.pop(count=3)
        return a, b, c

    def clear(self):
        self.items.clear()
        self.protected = 0

    def dump(self, count: int):
        if len(self.items) > 0:
            count = min(count, len(self.items))
            return self.items[:count]

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self):
        return pformat(self.items)
