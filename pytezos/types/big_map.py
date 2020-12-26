from copy import copy
from typing import Generator, Optional, Tuple, List, Union, Type

from pytezos.types.base import MichelsonType, parse_micheline_literal, undefined, LazyStorage
from pytezos.types.map import MapType
from pytezos.michelson.pack import get_key_hash


class BigMapType(MapType, prim='big_map', args_len=2):

    def __init__(self, items: List[Tuple[MichelsonType, MichelsonType]],
                 ptr: Optional[int] = None,
                 removed_keys: Optional[List[MichelsonType]] = None):
        super(BigMapType, self).__init__(items=items)
        self.ptr = ptr
        self.removed_keys = removed_keys or []
        self.storage: Optional[LazyStorage] = None

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
        cls = BigMapType.construct_type(type_args=[key_type, val_type])
        return cls(items=[])

    @staticmethod
    def from_items(items: List[Tuple[MichelsonType, MichelsonType]]):
        assert False, 'forbidden'

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None):
        name = cls.field_name or cls.type_name or inferred_name
        arg_names = [f'{name}_key', f'{name}_value'] if name else [None, None]
        key, val = [arg.generate_pydoc(definitions, inferred_name=arg_names[i]) for i, arg in enumerate(cls.type_args)]
        return f'{{ {key}: {val}, ... }} || int /* Big_map ID */'

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

    def to_python_object(self, lazy_diff=False):
        if lazy_diff:
            res = super(BigMapType, self).to_python_object()
            removals = {key.to_python_object(): None for key in self.removed_keys}
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
                key = self.type_args[0].from_micheline_value(update['key'])
                if update.get('value'):
                    value = self.type_args[1].from_micheline_value(update['value'])
                    items.append((key, value))
                else:
                    removed_keys.append(key)
            return type(self)(ptr=self.ptr, items=items, removed_keys=removed_keys)
        else:
            return copy(self)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        assert self.ptr is not None, f'Big_map id is not defined'
        ptr, action = self.storage.get_big_map_diff() if self.storage else (self.ptr, 'alloc')
        key_type, val_type = [arg.get_micheline_type() for arg in self.type_args]

        def make_update(key: MichelsonType, val: Optional[MichelsonType]) -> dict:
            key_expr = key.to_micheline_value(mode=mode)
            update = {
                'key': key_expr,
                'key_hash': get_key_hash(key_expr, key_type)
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

        lazy_diff.append({
            'kind': 'big_map',
            'id': str(ptr),
            'diff': diff
        })

    def attach_lazy_storage(self, storage: LazyStorage, action: str):
        if self.ptr is None:
            self.ptr = storage.get_tmp_big_map_id()
        else:
            storage.register_big_map(self.ptr, action)

    def get(self, key: MichelsonType, check_dup=True) -> Optional[MichelsonType]:
        self.type_args[0].assert_equal_types(type(key))
        val = next((v for k, v in self if k == key), undefined())
        if isinstance(val, undefined):
            if self.is_allocated():
                assert self.storage, f'lazy storage is not attached'
                key_hash = get_key_hash(val_expr=key.to_micheline_value(),
                                        type_expr=self.type_args[0].get_micheline_type())
                val_expr = self.storage.get_big_map_value(key_hash)
                if val_expr is None:
                    return None
                else:
                    return self.type_args[1].from_micheline_value(val_expr)
            else:
                return None
        else:
            return val

    def update(self, key: MichelsonType, val: Optional[MichelsonType]) -> Tuple[Optional[MichelsonType], MichelsonType]:
        removed_keys = set(self.removed_keys)
        prev_val = self.get(key, check_dup=False)
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
        key = self.type_args[0].from_python_object(key_obj)
        return get_key_hash(val_expr=key.to_micheline_value(),
                            type_expr=self.type_args[0].get_micheline_type())

    def __getitem__(self, key_obj) -> Optional[MichelsonType]:
        key = self.type_args[0].from_python_object(key_obj)
        return self.get(key, check_dup=False)
