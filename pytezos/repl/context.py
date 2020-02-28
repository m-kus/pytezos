import re
from copy import deepcopy
from pprint import pformat
from typing import List

from pytezos.repl.types import StackItem, assert_stack_item
from pytezos.michelson.converter import micheline_to_michelson


class Context:

    def __init__(self, stack=None, meta=None, big_maps=None, debug=True):
        self.stack = stack or []
        self.meta = meta or {}
        self.big_maps = big_maps or {}
        self.big_map_id = 0
        self.big_map_diff = []
        self.protected = 0
        self.exec_depth = 0
        self.debug = debug
        self.stdout = list()
        self.pushed = 0

    def reset(self):
        self.stdout.clear()
        self.pushed = False

    def alloc(self, item):
        big_map_id = self.big_map_id
        self.big_map_id += 1
        if isinstance(item, StackItem):
            self.big_maps[big_map_id] = item
        elif isinstance(item, int):
            assert item in self.big_maps, f'big map #{item} is not found'
            self.big_maps[big_map_id] = deepcopy(self.big_maps[item])
        else:
            assert False, f'expected stack item or big map id, got {item}'
        self._print(f' big map #{big_map_id} allocated;')
        return big_map_id

    def protect(self, count: int):
        assert len(self.stack) >= count, f'got {len(self.stack)} items, wanted to protect {count}'
        self.protected += count
        self._print(f' protect {count} item(s);')

    def restore(self, count: int):
        assert self.protected >= count, f'wanted to restore {count}, only {self.protected} protected'
        self._print(f' restore {count} item(s);')
        self.protected -= count

    def push(self, item: StackItem, annots=None):
        assert_stack_item(item)
        self.stack.insert(self.protected, item.rename(annots))
        self.pushed = True
        self._print(f' push {repr(item)};')

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
        self._print(f' pop {body};')
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
        if key in ['parameter', 'storage', 'code']:
            val = micheline_to_michelson(value, inline=True)
        else:
            val = repr(value)
        self._print(f' set {key}={val};')

    def unset(self, key):
        del self.meta[key]
        self._print(f' unset {key};')

    def drop_all(self):
        self.stack.clear()
        self._print(f' drop all;')

    def dump(self, count: int):
        if len(self.stack) > 0:
            count = min(count, len(self.stack))
            return self.stack[:count]
        else:
            return 'stack is empty'

    def _print(self, message):
        if self.debug:
            self.stdout.append(message)

    def printf(self, template: str):
        def format_stack_item(match):
            i = int(match.groups()[0])
            assert i < len(self.stack), f'requested {i}th element, got only {len(self.stack)} items'
            return repr(self.stack[i])

        message = re.sub(r'\{(\d+)\}', format_stack_item, template)
        self.stdout.append(message)

    def begin(self, prim=None):
        self.pushed = False
        if prim:
            indent = '  ' * self.exec_depth
            self._print(f'\n{indent}{prim}:')
        self.exec_depth += 1

    def end(self):
        self.exec_depth -= 1

    def __len__(self) -> int:
        return len(self.stack)

    def __repr__(self):
        return pformat(self.stack)

    def __deepcopy__(self, memodict={}):
        ctx = Context(stack=deepcopy(self.stack),
                      meta=deepcopy(self.meta),
                      debug=self.debug)
        ctx.protected = self.protected
        ctx.exec_depth = self.exec_depth
        return ctx
