import re
from copy import deepcopy
from pprint import pformat
from typing import List

from pytezos.crypto import blake2b
from pytezos.encoding import base58_encode
from pytezos.repl.types import StackItem, assert_stack_item
from pytezos.michelson.converter import micheline_to_michelson
from pytezos.repl.big_map import BigMapPool


class DummyGen:

    def __init__(self):
        self.index = 0
        self.self = self.get_fresh_address()

    def get_fresh_address(self):
        nonce = b'\x00' * 32 + self.index.to_bytes(4, 'big')
        nonce_hash = blake2b(data=nonce, digest_size=20).digest()
        res = base58_encode(nonce_hash, b'KT1').decode()
        self.index += 1
        return res


class Context:

    def __init__(self):
        self.stack = []
        self.meta = {}
        self.dummy_gen = DummyGen()
        self.big_maps = BigMapPool()
        self.debug = True
        self.stdout = list()
        self.protected = 0
        self.pushed = 0

    def __deepcopy__(self, memodict={}):
        ctx = Context()
        ctx.stack = deepcopy(self.stack)
        ctx.meta = deepcopy(self.meta)
        ctx.dummy_gen = deepcopy(self.dummy_gen)
        ctx.big_maps = deepcopy(self.big_maps)
        ctx.debug = self.debug
        ctx.protected = self.protected
        ctx.pushed = self.pushed
        return ctx

    def spawn(self, stack):
        ctx = Context()
        ctx.stack = stack
        ctx.meta = self.meta
        ctx.dummy_gen = self.dummy_gen
        ctx.big_maps = self.big_maps
        ctx.debug = self.debug
        ctx.stdout = self.stdout
        return ctx

    def reset(self):
        self.stdout = []
        self.pushed = False

    def protect(self, count: int):
        assert len(self.stack) >= count, f'got {len(self.stack)} items, wanted to protect {count}'
        self.protected += count
        self.print(f'protect {count} item(s)')

    def restore(self, count: int):
        assert self.protected >= count, f'wanted to restore {count}, only {self.protected} protected'
        self.print(f'restore {count} item(s)')
        self.protected -= count

    def push(self, item: StackItem, annots=None, move=False):
        assert_stack_item(item)
        self.stack.insert(self.protected, item if move else item.rename(annots))
        self.pushed = True
        self.print(f'push {repr(item)}')

    def peek(self):
        assert len(self.stack) > 0, 'stack is empty'
        return self.stack[self.protected]

    def pop(self, count: int) -> List[StackItem]:
        assert len(self.stack) - self.protected >= count, \
            f'got {len(self.stack) - self.protected} items, requested {count} '
        res = [self.stack.pop(self.protected) for _ in range(count)]
        if count <= 3:
            body = ', '.join(map(repr, res))  # TODO: restrict line length
        else:
            body = f'{count} items'
        self.print(f'pop {body}')
        return res

    def pop1(self):
        res = self.pop(count=1)
        return res[0]

    def pop2(self):
        return tuple(self.pop(count=2))

    def pop3(self):
        return tuple(self.pop(count=3))

    def get(self, key, default=None):
        return self.meta.get(key, default)

    def set(self, key, value):
        self.meta[key] = value
        if key in ['parameter', 'storage', 'code', 'STORAGE']:
            self.print(micheline_to_michelson({"prim": key, "args": [value]}, inline=True))
        else:
            self.print(f'set {key}={repr(value)}')

    def unset(self, key):
        if key in self.meta:
            del self.meta[key]
            self.print(f'unset {key}')

    def drop_all(self):
        self.stack.clear()
        self.protected = 0
        self.print(f'drop all')

    def dump(self, count: int):
        if len(self.stack) > 0:
            count = min(count, len(self.stack))
            return self.stack[:count]

    def print(self, message):
        if self.debug:
            self.stdout.append({'action': 'event', 'text': message})

    def printf(self, template: str):
        def format_stack_item(match):
            i = int(match.groups()[0])
            assert i < len(self.stack), f'requested {i}th element, got only {len(self.stack)} items'
            return repr(self.stack[i])

        message = re.sub(r'\{(\d+)\}', format_stack_item, template)
        self.stdout.append({'action': 'message', 'text': message})

    def begin(self, prim=None):
        self.pushed = False
        if self.debug:
            self.stdout.append({'action': 'begin', 'prim': prim})

    def end(self):
        if self.debug:
            self.stdout.append({'action': 'end'})

    def __len__(self) -> int:
        return len(self.stack)

    def __repr__(self):
        return pformat(self.stack)
