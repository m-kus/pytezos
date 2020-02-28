from pprint import pformat
from copy import deepcopy

from pytezos.michelson.converter import micheline_to_michelson
from pytezos.encoding import is_pkh, is_kt, is_chain_id
from pytezos.repl.parser import parse_value, parse_prim_expr, assert_expr_equal, assert_comparable, \
    expr_equal, assert_type, get_prim_args, get_int


def assert_stack_item(item: 'StackItem'):
    assert isinstance(item, StackItem), f'expected StackItem, got {type(item).__name__}'


def assert_stack_type(item: 'StackItem', item_type):
    if not isinstance(item_type, list):
        item_type = [item_type]
    expected = ' or '.join(map(lambda x: x.__name__, item_type))
    assert type(item) in item_type, f'expected {expected}, got {type(item).__name__}: {item}'


def dispatch_type_map(a, b, mapping):
    assert (type(a), type(b)) in mapping, \
        f'unsupported argument types {type(a).__name__} and {type(b).__name__}'
    return mapping[(type(a), type(b))]


def assert_equal_types(a, b):
    assert type(a) == type(b), f'different types {type(a).__name__} and {type(b).__name__}'


class StackItem:
    prim = ''
    __cls__ = {}

    def __init__(self, *args, val_expr, type_expr, **kwargs):
        self.val_expr = val_expr
        self.type_expr = type_expr
        self.val_annot = kwargs.get('val_annot')
        self._val = kwargs['val'] if 'val' in kwargs else parse_value(val_expr, type_expr)
        self._ctx = kwargs.get('ctx')

    @staticmethod
    def _get_type(type_expr):
        prim, args = parse_prim_expr(type_expr)
        assert prim in StackItem.__cls__, f'{prim}: unknown type primitive'
        item_cls, args_len = StackItem.__cls__[type_expr['prim']]
        assert len(args) == args_len, f'{prim}: expected {args_len} arg(s), got {len(args)}'
        return item_cls

    @staticmethod
    def parse(val_expr, type_expr, **kwargs):
        return StackItem._get_type(type_expr)(val_expr=val_expr, type_expr=type_expr, **kwargs)

    def _parse(self, val_expr, type_expr):
        return self.parse(val_expr, type_expr, ctx=self._ctx)

    @classmethod
    def __init_subclass__(cls, prim='', args_len=0, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__cls__[prim] = cls, args_len
        cls.prim = prim

    def __cmp__(self, other: 'StackItem') -> int:
        assert_stack_item(other)
        assert_expr_equal(self.type_expr, other.type_expr)
        if self._val > other._val:
            return 1
        elif self._val < other._val:
            return -1
        else:
            return 0

    def __eq__(self, other: 'StackItem'):
        assert_stack_item(other)
        assert_expr_equal(self.type_expr, other.type_expr)
        return expr_equal(self.val_expr, other.val_expr)

    def __int__(self):
        assert_type(self._val, int)
        return self._val

    def __str__(self):
        assert_type(self._val, str)
        return self._val

    def __bytes__(self):
        assert_type(self._val, bytes)
        return self._val

    def __bool__(self):
        assert_type(self._val, bool)
        return self._val

    def __len__(self):
        return len(self._val)

    def __repr__(self):
        return pformat(self._val, compact=True)

    def _modify(self, cache_val=False, **kwargs):
        param = dict(
            val_expr=kwargs.get('val_expr', deepcopy(self.val_expr)),
            val_annot=kwargs.get('val_annot', self.val_annot),
            type_expr=deepcopy(self.type_expr),
            ctx=self._ctx
        )
        if 'val' in kwargs or cache_val:
            param['val'] = kwargs.get('val', deepcopy(self._val))
        return type(self)(**param)

    def __deepcopy__(self, memodict={}):
        return self._modify(cache_val=True)

    def rename(self, annots: list):
        return self._modify(cache_val=True,
                            val_annot=next(filter(lambda x: x.startswith('@'), annots or []), None))


class String(StackItem, prim='string'):

    def __init__(self, val='', val_expr=None, type_expr=None, **kwargs):
        assert isinstance(val, str)
        super(String, self).__init__(
            val_expr=val_expr or {'string': val},
            type_expr=type_expr or {'prim': self.prim}, **kwargs)

    def __getitem__(self, item):
        assert_type(item, slice)
        return type(self)(self._val[item.start:item.stop])


class Int(StackItem, prim='int'):

    def __init__(self, val=0, val_expr=None, type_expr=None, **kwargs):
        assert_type(val, int)
        assert isinstance(val, int)
        super(Int, self).__init__(
            val_expr=val_expr or {'int': str(val)},
            type_expr=type_expr or {'prim': self.prim}, **kwargs)


class Bytes(StackItem, prim='bytes'):

    def __init__(self, val=b'', type_expr=None, val_expr=None, **kwargs):
        assert_type(val, bytes)
        super(Bytes, self).__init__(
            val_expr=val_expr or {'bytes': val.hex()},
            type_expr=type_expr or {'prim': self.prim}, **kwargs)

    def __getitem__(self, item):
        assert_type(item, slice)
        return type(self)(self._val[item.start:item.stop])

    def __repr__(self):
        return self._val.hex()


class Nat(Int, prim='nat'):

    def __init__(self, val=0, val_expr=None, type_expr=None, **kwargs):
        assert_type(val, int)
        assert val >= 0, 'expected non-negative val'
        super(Nat, self).__init__(val, val_expr=val_expr, type_expr=type_expr, **kwargs)


class Bool(StackItem, prim='bool'):

    def __init__(self, val=False, val_expr=None, type_expr=None, **kwargs):
        assert_type(val, bool)
        super(Bool, self).__init__(
            val_expr=val_expr or {'prim': str(val)},
            type_expr=type_expr or {'prim': self.prim}, **kwargs)


class Unit(StackItem, prim='unit'):

    def __init__(self, val_expr=None, type_expr=None, **kwargs):
        super(Unit, self).__init__(
            val_expr=val_expr or {'prim': 'Unit'},
            type_expr=type_expr or {'prim': self.prim}, **kwargs)


class List(StackItem, prim='list', args_len=1):

    def __iter__(self):
        for item in self.val_expr:
            yield self._parse(val_expr=item, type_expr=self.type_expr['args'][0])

    def prepend(self, item: StackItem) -> 'List':
        self.assert_val_type(item)
        return self._parse(val_expr=[item.val_expr] + self.val_expr, type_expr=self.type_expr)

    def cut_head(self):
        assert len(self._val) > 0, f'must be non-empty list'
        head = self._parse(val_expr=self.val_expr[0], type_expr=self.type_expr['args'][0])
        tail = self._modify(val_expr=self.val_expr[1:])
        return head, tail

    @classmethod
    def empty(cls, v_type_expr):
        return cls(val_expr=[], type_expr={'prim': cls.prim, 'args': [v_type_expr]})

    @classmethod
    def new(cls, items: list):
        assert isinstance(items, list) and len(items) > 0, f'expected non-empty list'
        val_expr = [assert_stack_item(x) or x.val_expr for x in items]
        return cls(val_expr=val_expr, type_expr={'prim': cls.prim, 'args': [items[0].type_expr]})

    def assert_val_type(self, item: StackItem):
        assert_stack_item(item)
        assert_expr_equal(self.type_expr['args'][0], item.type_expr)

    def val_type(self):
        return self._get_type(self.type_expr['args'][0])


class Pair(StackItem, prim='pair', args_len=2):

    @classmethod
    def new(cls, left: StackItem, right: StackItem):
        assert_stack_item(left)
        assert_stack_item(right)
        return cls(
            type_expr={'prim': cls.prim, 'args': [left.type_expr, right.type_expr]},
            val_expr={'prim': 'Pair', 'args': [left.val_expr, right.val_expr]})

    def get_element(self, idx: int):
        return self._parse(val_expr=self.val_expr['args'][idx], type_expr=self.type_expr['args'][idx])


class Option(StackItem, prim='option', args_len=1):

    @classmethod
    def some(cls, item: StackItem):
        assert_stack_item(item)
        return cls(
            type_expr={'prim': cls.prim, 'args': [item.type_expr]},
            val_expr={'prim': 'Some', 'args': [item.val_expr]})

    @classmethod
    def none(cls, type_expr):
        return cls(
            type_expr={'prim': cls.prim, 'args': [type_expr]},
            val_expr={'prim': 'None'})

    def is_none(self):
        return self._val is None

    def get_some(self):
        return self._parse(val_expr=self.val_expr['args'][0],
                           type_expr=self.type_expr['args'][0])


class Or(StackItem, prim='or', args_len=2):

    @classmethod
    def left(cls, r_type_expr, item: StackItem):
        assert_stack_item(item)
        return cls(type_expr={'prim': cls.prim, 'args': [item.type_expr, r_type_expr]},
                   val_expr={'prim': 'Left', 'args': [item.val_expr]})

    @classmethod
    def right(cls, l_type_expr, item: StackItem):
        assert_stack_item(item)
        return cls(type_expr={'prim': cls.prim, 'args': [l_type_expr, item.type_expr]},
                   val_expr={'prim': 'Right', 'args': [item.val_expr]})

    def is_left(self):
        prim, _ = parse_prim_expr(self.val_expr)
        return prim == 'Left'

    def get_some(self):
        idx = 0 if self.is_left() else 1
        return self._parse(val_expr=self.val_expr['args'][0],
                           type_expr=self.type_expr['args'][idx])


class Set(StackItem, prim='set', args_len=1):

    def __iter__(self):
        for item in self.val_expr:
            yield self._parse(val_expr=item, type_expr=self.type_expr['args'][0])

    @classmethod
    def empty(cls, k_type_expr):
        assert_comparable(k_type_expr)
        return cls(type_expr={'prim': cls.prim, 'args': [k_type_expr]}, val_expr=[])

    @classmethod
    def new(cls, items: list):
        assert isinstance(items, list) and len(items) > 0, f'expected non-empty list'
        assert len(set(items)) == len(items), f'duplicate keys found'
        val_expr = [assert_stack_item(x) or x.val_expr for x in items]
        return cls(val_expr=val_expr, type_expr={'prim': cls.prim, 'args': [items[0].type_expr]})

    def __contains__(self, item: StackItem):
        self.assert_key_type(item)
        return item._val in self._val

    def add(self, item: StackItem) -> 'Set':
        self.assert_key_type(item)
        if item._val in self._val:
            return self
        return self._modify(val_expr=[item.val_expr] + self.val_expr)  # TODO: sort

    def remove(self, item: StackItem) -> 'Set':
        self.assert_key_type(item)
        val_expr = list(filter(lambda x: not expr_equal(x, item.val_expr), self.val_expr))
        return self._modify(val_expr=val_expr)

    def assert_key_type(self, item: StackItem):
        assert_stack_item(item)
        assert_expr_equal(self.type_expr['args'][0], item.type_expr)


class Map(StackItem, prim='map', args_len=2):

    def __iter__(self):
        for elt in self.val_expr:
            yield tuple(self._parse(val_expr=elt['args'][i], type_expr=self.type_expr['args'][i]) for i in [0, 1])

    @classmethod
    def empty(cls, k_type_expr, v_type_expr):
        assert_comparable(k_type_expr)
        return cls(type_expr={'prim': cls.prim, 'args': [k_type_expr, v_type_expr]}, val_expr=[])

    @classmethod
    def new(cls, items: list):
        assert isinstance(items, list) and len(items) > 0, f'expected non-empty list'
        _ = [assert_stack_item(x) for kv in items for x in kv]
        val_expr = [{'prim': 'Elt', 'args': [k.val_expr, v.val_expr]} for k, v in items]
        k0, v0 = items[0]
        return cls(val_expr=val_expr, type_expr={'prim': cls.prim, 'args': [k0.type_expr, v0.type_expr]})

    def __contains__(self, item: StackItem):
        self.assert_key_type(item)
        return item._val in self._val

    def add(self, key: StackItem, val: StackItem) -> 'Map':
        self.assert_key_type(key)
        self.assert_val_type(val)
        if key._val in self._val:
            return self
        elt = {'prim': 'Elt', 'args': [key.val_expr, val.val_expr]}
        return self._modify(val_expr=self.val_expr + [elt])  # TODO: sort

    def remove(self, key: StackItem) -> 'Map':
        self.assert_key_type(key)
        val_expr = list(filter(lambda elt: not expr_equal(elt['args'][0], key.val_expr), self.val_expr))
        return self._modify(val_expr=val_expr)

    def find(self, key: StackItem) -> 'StackItem':
        self.assert_key_type(key)
        val_expr = next(elt['args'][1] for elt in self.val_expr if expr_equal(elt['args'][0], key.val_expr))
        return self._parse(val_expr=val_expr, type_expr=self.type_expr['args'][1])

    def assert_key_type(self, item: StackItem):
        assert_stack_item(item)
        assert_expr_equal(self.type_expr['args'][0], item.type_expr)

    def assert_val_type(self, item: StackItem):
        assert_stack_item(item)
        assert_expr_equal(self.type_expr['args'][1], item.type_expr)

    def val_type_expr(self):
        return self.type_expr['args'][1]


class BigMap(StackItem, prim='big_map', args_len=2):

    def __init__(self, *args, val_expr, type_expr, **kwargs):
        assert self._ctx, f'context is not initialized'
        if isinstance(val_expr, list):
            big_map_id = self._ctx.alloc(Map(val_expr=val_expr, type_expr=type_expr))
            self._ctx.big_map_diff.append({
                'action': 'alloc',
                'big_map': big_map_id,
                'key_type': type_expr['args'][0],
                'value_type': type_expr['args'][1]
            })
        else:
            src_id = get_int(val_expr)
            big_map_id = self._ctx.alloc(src_id)
            self._ctx.big_map_diff.append({
                'action': 'copy',
                'source_big_map': src_id,
                'destination_big_map': big_map_id
            })
        kwargs['val'] = big_map_id
        val_expr = {'int': big_map_id}
        super(BigMap, self).__init__(*args, val_expr, type_expr, **kwargs)

    @classmethod
    def empty(cls, k_type_expr, v_type_expr, **kwargs):
        return cls(val_expr=[], type_expr={'prim': cls.prim, 'args': [k_type_expr, v_type_expr]}, **kwargs)

    def __contains__(self, item: StackItem):
        return item in self._ctx.big_maps[self._val]

    def _update(self, key, val=None) -> 'BigMap':
        self._ctx.big_map_diff.append({
            'action': 'update',
            'big_map': self._val,
            'key_hash': '',  # TODO
            'key': key.val_expr,
            'value': val.val_expr if val else None
        })
        return self

    def add(self, key: StackItem, val: StackItem) -> 'BigMap':
        self._ctx.big_maps[self._val] = self._ctx.big_maps[self._val].add(key, val)
        return self._update(key, val)

    def remove(self, key: StackItem) -> 'BigMap':
        self._ctx.big_maps[self._val] = self._ctx.big_maps[self._val].remove(key)
        return self._update(key)

    def find(self, key: StackItem) -> 'StackItem':
        return self._ctx.big_maps[self._val].find(key)

    def val_type_expr(self):
        return self.type_expr['args'][1]


class Timestamp(Int, prim='timestamp'):
    pass


class Mutez(Nat, prim='mutez'):
    pass


class Address(String, prim='address'):

    @classmethod
    def new(cls, address):
        assert is_pkh(address) or is_kt(address), f'expected address, got {address}'
        return cls(val=address,
                   val_expr={'string': address},
                   type_expr={'prim': cls.prim})


class Contract(StackItem, prim='contract', args_len=1):

    @classmethod
    def new(cls, contract, type_expr):
        assert is_pkh(contract[:36]) or is_kt(contract[:36]), f'expected contract, got {contract}'
        if len(contract) > 36:
            assert contract[36] == '%', f'expected contract, got {contract}'
        return cls(val=contract,
                   val_expr={'string': contract},
                   type_expr={'prim': cls.prim, 'args': [type_expr]})

    def assert_param_type(self, item: StackItem):
        assert_stack_item(item)
        assert_expr_equal(self.type_expr['args'][0], item.type_expr)

    def get_address(self):
        return self._val[:36]

    def get_entrypoint(self):
        annot = self._val[36:] or '%default'
        return annot[1:]


class Key(StackItem, prim='key'):
    pass


class KeyHash(String, prim='key_hash'):

    @classmethod
    def new(cls, key_hash):
        assert is_pkh(key_hash), f'expected key hash, got {key_hash}'
        return cls(val=key_hash,
                   val_expr={'string': key_hash},
                   type_expr={'prim': cls.prim})


class Signature(StackItem, prim='signature'):
    pass


class ChainID(String, prim='chain_id'):

    def __init__(self, val, val_expr=None, type_expr=None, **kwargs):
        assert is_chain_id(val), f'expected chain_id, got {val}'
        super(ChainID, self).__init__(val, val_expr=val_expr, type_expr=type_expr, **kwargs)


class Lambda(StackItem, prim='lambda', args_len=2):

    @classmethod
    def new(cls, p_type_expr, r_type_expr, code):
        return cls(
            val_expr={'prim': 'Lambda', 'args': [code]},
            type_expr={'prim': 'lambda', 'args': [p_type_expr, r_type_expr]})

    def assert_param_type(self, item: StackItem):
        assert_stack_item(item)
        assert_expr_equal(self.type_expr['args'][0], item.type_expr)

    def assert_ret_type(self, item: StackItem):
        assert_stack_item(item)
        assert_expr_equal(self.type_expr['args'][1], item.type_expr)

    @property
    def code(self):
        return self._val

    def partial_apply(self, item: StackItem):
        l_type_expr, r_type_expr = get_prim_args(self.type_expr['args'][0], prim='pair', args_len=2)
        assert_equal_types(l_type_expr, item.type_expr)
        push = {'prim': 'PUSH', 'args': [item.type_expr, item.val_expr]}
        pair = {'prim': 'PAIR'}
        code = self.val_expr['args'][0]
        assert_type(code, list), f'expected instruction sequence, got {code}'
        return type(self)(
            val_expr={'prim': 'Lambda', 'args': [[push, pair] + code]},
            type_expr={'prim': 'lambda', 'args': [r_type_expr, self.type_expr['args'][1]]}
        )

    def __repr__(self):
        return micheline_to_michelson(self._val, inline=True)


class Operation(StackItem, prim='operation'):

    @classmethod
    def new(cls, content):
        return cls(val=content,
                   val_expr={'prim': 'Unit'},
                   type_expr={'prim': cls.prim, 'annots': [f':{content["kind"]}']})
