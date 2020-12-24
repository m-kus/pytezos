from typing import Generator, Optional, Tuple, List

from pytezos.types.base import MichelsonType, parse_micheline_literal, undefined
from pytezos.types.map import MapType
from pytezos.types.lazy import LazyStorage
from pytezos.michelson.pack import get_key_hash


class BigMap:

    def __init__(self, ptr: Optional[int], updates: List[Tuple[MichelsonType, Optional[MichelsonType]]]):
        self.ptr = ptr
        self.updates = updates
        self.storage = None  # type: Optional[LazyStorage]

    @property
    def upserts(self) -> List[Tuple[MichelsonType, MichelsonType]]:
        return [(k, v) for k, v in self.updates if v is not None]

    def attach(self, storage: LazyStorage):
        self.storage = storage
        if self.ptr is None:
            self.ptr = storage.allocate_big_map_id()
        else:
            storage.register_big_map_id(self.ptr)


class BigMapType(MichelsonType, prim='big_map', args_len=2):

    def assert_value_defined(self):
        assert isinstance(self.value, BigMap), f'expected BigMap, got {type(self.value).__name__}'

    def assert_id_allocated(self):
        self.assert_value_defined()
        assert self.value.ptr is not None, f'Big_map ID is not allocated'

    def assert_storage_attached(self):
        self.assert_value_defined()
        assert self.value.storage is not None, f'lazy storage is not attached'

    def __len__(self):
        self.assert_value_defined()
        return len(self.value.updates)

    def __iter__(self) -> Generator[Tuple[MichelsonType, Optional[MichelsonType]], None, None]:
        self.assert_value_defined()
        yield from iter(self.value.updates)

    def parse_micheline_value(self, val_expr) -> 'BigMapType':
        if isinstance(val_expr, dict):
            ptr = parse_micheline_literal(val_expr, {'int': int})
            return self.spawn(BigMap(ptr=ptr, updates=[]))
        else:
            plain_map = MapType(type_args=self.type_args).parse_micheline_value(val_expr)
            return self.spawn(BigMap(ptr=None, updates=plain_map.value))

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        if lazy_diff:
            plain_map = MapType(value=self.value.upserts, type_args=self.type_args)
            return plain_map.to_micheline_value(mode=mode)
        else:
            self.assert_id_allocated()
            return {'int': str(self.value)}

    def parse_python_object(self, py_obj) -> 'BigMapType':
        if isinstance(py_obj, int):
            return self.spawn(BigMap(ptr=py_obj, updates=[]))
        else:
            plain_map = MapType(type_args=self.type_args).parse_python_object(py_obj)
            return self.spawn(BigMap(ptr=None, updates=plain_map.value))

    def to_python_object(self, lazy_diff=False):
        if lazy_diff:
            plain_map = MapType(value=self.value.upserts, type_args=self.type_args)
            return plain_map.to_python_object()
        else:
            self.assert_id_allocated()
            return self.value.ptr

    def generate_pydoc(self, definitions: list, inferred_name=None):
        name = self.field_name or self.type_name or inferred_name
        arg_names = [f'{name}_key', f'{name}_value'] if name else [None, None]
        key, val = [arg.generate_pydoc(definitions, inferred_name=arg_names[i]) for i, arg in enumerate(self.type_args)]
        return f'{{ {key}: {val}, ... }} || int /* Big_map ID */'

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'BigMapType':
        self.assert_id_allocated()
        assert isinstance(lazy_diff, list), f'expected list, got {type(lazy_diff).__name__}'
        res = []
        for diff in lazy_diff:
            assert isinstance(diff, dict), f'expected dict, got {type(diff).__name__}'
            if diff.get('kind') != 'big_map' or diff.get('id') != str(self.value.ptr):
                continue
            updates = diff.get('diff', {}).get('updates', [])
            for update in updates:
                key = self.type_args[0].parse_micheline_value(update['key'])
                if update.get('value'):
                    value = self.type_args[1].parse_micheline_value(update['value'])
                else:
                    value = None
                res.append((key, value))
        return self.spawn(BigMap(ptr=self.value.ptr, updates=res))

    def aggregate_lazy_diff(self, lazy_diff: List[dict]):
        raise NotImplementedError

    def attach_lazy_storage(self, storage: LazyStorage):
        self.assert_value_defined()
        self.value.attach(storage)

    def get_key_hash(self, key_obj):
        key = self.type_args[0].parse_python_object(key_obj)
        return get_key_hash(val_expr=key.to_micheline_value(),
                            type_expr=self.type_args[0].get_micheline_type())

    def __getitem__(self, key_obj) -> Optional[MichelsonType]:
        key = self.type_args[0].parse_python_object(key_obj)
        val = next((v for k, v in self.value.updates if k == key), undefined())
        if isinstance(val, undefined):
            self.assert_storage_attached()
            key_hash = get_key_hash(val_expr=key.to_micheline_value(),
                                    type_expr=self.type_args[0].get_micheline_type())
            val_expr = self.value.storage.get_big_map_value(key_hash)
            if val_expr is None:
                return None
            else:
                return self.type_args[1].parse_micheline_value(val_expr)
        else:
            return val
