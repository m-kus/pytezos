from copy import copy
from typing import Generator, Optional, Tuple, List, Union, Type

from pytezos.michelson.types.base import MichelsonType, undefined
from pytezos.michelson.micheline import parse_micheline_literal
from pytezos.context.execution import ExecutionContext
from pytezos.michelson.types.map import MapType
from pytezos.michelson.forge import forge_script_expr


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

    def __init__(self, items: List[Tuple[MichelsonType, MichelsonType]],
                 ptr: Optional[int] = None,
                 removed_keys: Optional[List[MichelsonType]] = None):
        super(BigMapType, self).__init__(items=items)
        self.ptr = ptr
        self.removed_keys = removed_keys or []
        self.storage: Optional[ExecutionContext] = None

    def __len__(self):
        return len(self.items) + len(self.removed_keys)

    def __iter__(self) -> Generator[Tuple[MichelsonType, Optional[MichelsonType]], None, None]:
        yield from iter(self.items)
        for key in self.removed_keys:
            yield key, None

    def is_allocated(self) -> bool:
        return self.ptr and self.ptr >= 0

    @staticmethod
    def empty(key_type: Type[MichelsonType], val_type: Type[MichelsonType]) -> 'BigMapType':
        cls = BigMapType.create_type(args=[key_type, val_type])
        return cls(items=[])

    @staticmethod
    def from_items(items: List[Tuple[MichelsonType, MichelsonType]]):
        assert False, 'forbidden'

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None):
        name = cls.field_name or cls.type_name or inferred_name
        arg_names = [f'{name}_key', f'{name}_value'] if name else [None, None]
        key, val = [arg.generate_pydoc(definitions, inferred_name=arg_names[i]) for i, arg in enumerate(cls.args)]
        return f'{{ {key}: {val}, ... }} || int /* Big_map ID */'

    @classmethod
    def dummy(cls, context: ExecutionContext) -> 'BigMapType':
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
            return cls(ptr=py_obj, items=[])
        else:
            items = super(BigMapType, cls).parse_python_object(py_obj)
            return cls(items=items)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if lazy_diff:
            return super(BigMapType, self).to_micheline_value(mode=mode)
        else:
            assert self.ptr is not None, f'Big_map id is not defined'
            return {'int': str(self.ptr)}

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        if lazy_diff:
            res = super(BigMapType, self).to_python_object(try_unpack=try_unpack)
            removals = {key.to_python_object(try_unpack=try_unpack): None for key in self.removed_keys}
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
            return type(self)(ptr=self.ptr, items=items, removed_keys=removed_keys)
        else:
            return copy(self)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        assert self.ptr is not None, f'Big_map id is not defined'
        if self.storage:
            src_ptr, dst_ptr, action = self.storage.get_big_map_diff(self.ptr)
        else:
            src_ptr, dst_ptr, action = self.ptr, self.ptr, 'update'
        key_type, val_type = [arg.as_micheline_expr() for arg in self.args]

        def make_update(key: MichelsonType, val: Optional[MichelsonType]) -> dict:
            update = {
                'key': key.to_micheline_value(mode=mode),
                'key_hash': forge_script_expr(key.pack())
            }
            if val is not None:
                update['value'] = val.to_micheline_value(mode=mode)
            return update

        diff = {
            'action': action,
            'updates': [make_update(key, val) for key, val in self]
        }
        if action == 'alloc':
            diff['key_type'] = key_type
            diff['value_type'] = val_type
        elif action == 'copy':
            pass  # TODO:

        lazy_diff.append({
            'kind': 'big_map',
            'id': str(dst_ptr),
            'diff': diff
        })

    def attach_context(self, context: ExecutionContext, big_map_copy=False):
        if self.ptr is None:
            self.ptr = context.get_tmp_big_map_id()
        else:
            self.ptr = context.register_big_map(self.ptr, copy=big_map_copy)

    def get(self, key: MichelsonType, dup=True) -> Optional[MichelsonType]:
        self.args[0].assert_equal_types(type(key))
        val = next((v for k, v in self if k == key), undefined())  # search in diff
        if isinstance(val, undefined):
            assert self.storage, f'lazy storage is not attached'
            key_hash = forge_script_expr(key.pack())
            val_expr = self.storage.get_big_map_value(self.ptr, key_hash)
            if val_expr is None:
                return None
            else:
                return self.args[1].from_micheline_value(val_expr)
        else:
            return val

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
                removed_keys.remove(key)
            else:  # do nothing
                items = self.items
        return prev_val, type(self)(items=items, ptr=self.ptr, removed_keys=list(removed_keys))

    def get_key_hash(self, key_obj):
        key = self.args[0].from_python_object(key_obj)
        return forge_script_expr(key.pack())

    def __getitem__(self, key_obj) -> Optional[MichelsonType]:
        key = self.args[0].from_python_object(key_obj)
        return self.get(key, dup=False)
