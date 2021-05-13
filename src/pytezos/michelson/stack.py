from pprint import pformat
from typing import List, Optional, Tuple

from pytezos.michelson.types.base import MichelsonType


class MichelsonStack:
    def __init__(self, items: Optional[List[MichelsonType]] = None) -> None:
        self.items = items or []
        self.protected = 0

    @classmethod
    def from_items(cls, items: List[MichelsonType]) -> 'MichelsonStack':
        return cls(items)

    def protect(self, count: int) -> None:
        if len(self.items) < count:
            raise Exception(f'got {len(self.items)} items on the stack, want to protect {count}')
        self.protected += count

    def restore(self, count: int) -> None:
        if self.protected < count:
            raise Exception(f'want to restore {count} items, but only {self.protected} are protected')
        self.protected -= count

    def push(self, item: MichelsonType):
        self.items.insert(self.protected, item)

    def peek(self) -> MichelsonType:
        if not self.items:
            raise Exception('stack is empty')
        return self.items[self.protected]

    def pop(self, count: int) -> List[MichelsonType]:
        if len(self.items) - self.protected < count:
            raise Exception(f'got {len(self.items) - self.protected} items on the stack, want to pop {count}')
        return [self.items.pop(self.protected) for _ in range(count)]

    def pop1(self) -> MichelsonType:
        (a,) = self.pop(count=1)
        return a

    def pop2(self) -> Tuple[MichelsonType, MichelsonType]:
        a, b = self.pop(count=2)
        return a, b

    def pop3(self) -> Tuple[MichelsonType, MichelsonType, MichelsonType]:
        a, b, c = self.pop(count=3)
        return a, b, c

    def clear(self) -> None:
        self.items.clear()
        self.protected = 0

    def dump(self, count: int) -> Optional[List[MichelsonType]]:
        if not self.items:
            return None
        count = min(count, len(self.items))
        return self.items[:count]

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        return pformat(self.items)
