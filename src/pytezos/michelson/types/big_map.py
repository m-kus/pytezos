from copy import copy, deepcopy
from typing import Dict, Generator, List, Optional, Tuple, Type, Union

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.forge import forge_script_expr
from pytezos.michelson.micheline import Micheline, MichelineLiteral, MichelineSequence, parse_micheline_literal
from pytezos.michelson.types.base import MichelsonType, Undefined
from pytezos.michelson.types.map import EltLiteral, MapType


def big_map_diff_to_lazy_diff(big_map_diff: List[dict]):
    lazy_diff = dict()
    for diff in big_map_diff:
        if diff['action'] in ['copy', 'remove']:
            continue
        ptr = diff['big_map']
        if ptr not in lazy_diff:
            lazy_diff[ptr] = {
                'kind': 'big_map',
                'id': ptr,
                'diff': {'action': 'update', 'updates': []}
            }
        if diff['action'] == 'alloc':
            lazy_diff[ptr]['diff']['action'] = diff['action']
            lazy_diff[ptr]['diff']['key_type'] = diff['key_type']
            lazy_diff[ptr]['diff']['value_type'] = diff['value_type']
        elif diff['action'] == 'update':
            item = {'key': diff['key'], 'key_hash': diff['key_hash']}
            if diff.get('value'):
                item['value'] = diff['value']
            lazy_diff[ptr]['diff']['updates'].append(item)
        else:
            raise NotImplementedError(diff['action'])
    return list(lazy_diff.values())


class BigMapType(MapType, prim='big_map', args_len=2):

    def __init__(self,
                 items: List[Tuple[MichelsonType, MichelsonType]],
                 ptr: Optional[int] = None,
                 removed_keys: Optional[List[MichelsonType]] = None):
        super(BigMapType, self).__init__(items=items)
        self.ptr = ptr
        self.removed_keys = removed_keys or []
        self.context: Optional[AbstractContext] = None

    def __len__(self):
        return len(self.items) + len(self.removed_keys)

    def __iter__(self) -> Generator[Tuple[MichelsonType, Optional[MichelsonType]], None, None]:  # type: ignore
        yield from iter(self.items)
        for key in self.removed_keys:
            yield key, None

    def __repr__(self):
        if self.context:
            return f'<{self.ptr}>'
        else:
            elements = [f'{repr(k)}: {repr(v)}' for k, v in self]
            return f'{{{", ".join(elements)}}}'

    def __deepcopy__(self, memodict={}):
        return self.duplicate()

    def __getitem__(self, key_obj) -> Optional[MichelsonType]:  # type: ignore
        key = self.args[0].from_python_object(key_obj)
        return self.get(key, dup=False)

    @staticmethod
    def empty(key_type: Type[MichelsonType], val_type: Type[MichelsonType]) -> 'BigMapType':
        cls = BigMapType.create_type(args=[key_type, val_type])
        return cls(items=[])  # type: ignore

    @staticmethod
    def from_items(items: List[Tuple[MichelsonType, MichelsonType]]):
        assert False, 'forbidden'

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None, comparable=False):
        doc = super(BigMapType, cls).generate_pydoc(definitions, inferred_name=inferred_name)
        return f'{doc} || int /* Big_map ID */'

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'BigMapType':
        return cls(items=[])

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'BigMapType':
        if isinstance(val_expr, dict):
            ptr = parse_micheline_literal(val_expr, {'int': int})
            return cls(items=[], ptr=ptr)
        else:
            items = super(BigMapType, cls).parse_micheline_value(val_expr)
            return cls(items=items)

    @classmethod
    def from_python_object(cls, py_obj: Union[int, dict]) -> 'BigMapType':
        if isinstance(py_obj, int):
            return cls(items=[], ptr=py_obj)
        else:
            items = super(BigMapType, cls).parse_python_object(py_obj)
            return cls(items=items)

    def to_literal(self) -> Type[Micheline]:
        if self.ptr is not None:
            return MichelineLiteral.create(self.ptr)
        else:
            return MichelineSequence.create_type(args=[
                EltLiteral.create_type(args=[k.to_literal(), v.to_literal()])
                for k, v in self.items
            ])

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if lazy_diff:
            return super(BigMapType, self).to_micheline_value(mode=mode)
        else:
            assert self.ptr is not None, f'Big_map id is not defined'
            return {'int': str(self.ptr)}

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False):
        if lazy_diff:
            assert not comparable, f'big_map is not comparable'
            res = super(BigMapType, self).to_python_object(try_unpack=try_unpack)
            removals = {key.to_python_object(try_unpack=try_unpack, comparable=True): None
                        for key in self.removed_keys}
            return {**res, **removals}
        else:
            assert self.ptr is not None, f'Big_map id is not defined'
            return self.ptr

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'BigMapType':
        assert self.ptr is not None, f'Big_map id is not defined'
        assert isinstance(lazy_diff, list), f'expected list, got {type(lazy_diff).__name__}'
        diff = next((item for item in lazy_diff
                     if item['kind'] == 'big_map' and item['id'] == str(self.ptr)), None)
        if diff:
            items: List[Tuple[MichelsonType, MichelsonType]] = []
            removed_keys: List[MichelsonType] = []
            for update in diff['diff'].get('updates', []):
                key = self.args[0].from_micheline_value(update['key'])
                if update.get('value'):
                    value = self.args[1].from_micheline_value(update['value'])
                    items.append((key, value))
                else:
                    removed_keys.append(key)
            res = type(self)(ptr=self.ptr, items=items, removed_keys=removed_keys)
            res.context = self.context
            return res
        else:
            return copy(self)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable') -> 'BigMapType':
        assert self.ptr is not None, f'Big_map ID is not defined'
        if self.context:
            src_ptr, dst_ptr, action = self.context.get_big_map_diff(self.ptr)
        else:
            src_ptr, dst_ptr, action = self.ptr, self.ptr, 'update'

        def make_update(key: MichelsonType, val: Optional[MichelsonType]) -> dict:
            update = {
                'key': key.to_micheline_value(mode=mode),
                'key_hash': forge_script_expr(key.pack(legacy=True))
            }
            if val is not None:
                update['value'] = val.to_micheline_value(mode=mode)
            return update

        diff = {
            'action': action,
            'updates': [make_update(key, val) for key, val in self]
        }
        if action == 'alloc':
            key_type, val_type = [arg.as_micheline_expr() for arg in self.args]
            diff['key_type'] = key_type
            diff['value_type'] = val_type
        elif action == 'copy':
            pass  # TODO:

        lazy_diff.append({
            'kind': 'big_map',
            'id': str(dst_ptr),
            'diff': diff
        })
        res = type(self)(items=[], ptr=dst_ptr)
        res.context = self.context
        return res

    def attach_context(self, context: AbstractContext, big_map_copy=False):
        assert self.context is None, f'context already attached'
        self.context = context
        if self.ptr is None:
            self.ptr = context.get_tmp_big_map_id()
        else:
            self.ptr = context.register_big_map(self.ptr, copy=big_map_copy)
        if context.tzt:  # type: ignore
            context.tzt_big_maps[self.ptr] = self  # type: ignore

    def get(self, key: MichelsonType, dup=True) -> Optional[MichelsonType]:
        self.args[0].assert_type_equal(type(key))
        val = next((v for k, v in self if k == key), Undefined)  # search in diff
        if val is Undefined:
            assert self.context, f'context is not attached'
            key_hash = forge_script_expr(key.pack(legacy=True))
            val_expr = self.context.get_big_map_value(self.ptr, key_hash)  # type: ignore
            if val_expr is None:
                return None
            else:
                return self.args[1].from_micheline_value(val_expr)
        else:
            return val  # type: ignore

    def update(self, key: MichelsonType, val: Optional[MichelsonType]) -> Tuple[Optional[MichelsonType], MichelsonType]:
        removed_keys = set(self.removed_keys)
        prev_val = self.get(key, dup=False)
        if prev_val is not None:
            if val is not None:
                items = [(k, v if k != key else val) for k, v in self]
            else:  # remove
                items = [(k, v) for k, v in self if k != key]
                removed_keys.add(key)
        else:
            if val is not None:
                items = list(sorted(self.items + [(key, val)], key=lambda x: x[0]))
                if key in removed_keys:
                    removed_keys.remove(key)
            else:  # do nothing
                items = self.items  # type: ignore
        res = type(self)(items=items, ptr=self.ptr, removed_keys=list(removed_keys))  # type: ignore
        res.context = self.context
        return prev_val, res

    def get_key_hash(self, key_obj):
        key = self.args[0].from_python_object(key_obj)
        return forge_script_expr(key.pack(legacy=True))

    def duplicate(self):
        res = type(self)(items=deepcopy(self.items),
                         ptr=self.ptr,
                         removed_keys=deepcopy(self.removed_keys))
        res.context = self.context
        return res

