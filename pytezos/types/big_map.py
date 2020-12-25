from copy import copy
from typing import Generator, Optional, Tuple, List, Union

from pytezos.types.base import MichelsonType, parse_micheline_literal, undefined, LazyStorage
from pytezos.types.map import MapType
from pytezos.michelson.pack import get_key_hash


class BigMapType(MapType, prim='big_map', args_len=2):

    def __init__(self, ptr: Optional[int],
                 items: List[Tuple[MichelsonType, MichelsonType]],
                 removed_keys: List[MichelsonType]):
        super(BigMapType, self).__init__(items=items)
        self.ptr = ptr
        self.removed_keys = removed_keys
        self.storage: Optional[LazyStorage] = None

    def __len__(self):
        return len(self.items) + len(self.removed_keys)

    def __iter__(self) -> Generator[Tuple[MichelsonType, Optional[MichelsonType]], None, None]:
        yield from iter(self.items)
        for key in self.removed_keys:
            yield key, None

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
            return cls(ptr=ptr, items=[], removed_keys=[])
        else:
            items = super(BigMapType, cls).parse_micheline_value(val_expr)
            return cls(ptr=None, items=items, removed_keys=[])

    @classmethod
    def from_python_object(cls, py_obj: Union[int, dict]) -> 'BigMapType':
        if isinstance(py_obj, int):
            return cls(ptr=py_obj, items=[], removed_keys=[])
        else:
            items = super(BigMapType, cls).parse_python_object(py_obj)
            return cls(ptr=None, items=items, removed_keys=[])

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

    def get_key_hash(self, key_obj):
        key = self.type_args[0].from_python_object(key_obj)
        return get_key_hash(val_expr=key.to_micheline_value(),
                            type_expr=self.type_args[0].get_micheline_type())

    def __getitem__(self, key_obj) -> Optional[MichelsonType]:
        key = self.type_args[0].from_python_object(key_obj)
        val = next((v for k, v in self if k == key), undefined())
        if isinstance(val, undefined):
            assert self.storage, f'lazy storage is not attached'
            key_hash = get_key_hash(val_expr=key.to_micheline_value(),
                                    type_expr=self.type_args[0].get_micheline_type())
            val_expr = self.storage.get_big_map_value(key_hash)
            if val_expr is None:
                return None
            else:
                return self.type_args[1].from_micheline_value(val_expr)
        else:
            return val
