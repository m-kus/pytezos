from typing import List, Type, cast, Dict, Any

from pytezos.types.base import MichelsonType, LazyStorage
from pytezos.types.sum import OrType
from pytezos.types.struct import Struct


class SectionType(MichelsonType):

    def __init__(self, item: MichelsonType):
        super(SectionType, self).__init__()
        self.item = item

    def __repr__(self):
        return repr(self.item)

    @staticmethod
    def match(type_expr) -> Type['SectionType']:
        return cast(Type['SectionType'], MichelsonType.match(type_expr))

    @classmethod
    def generate_pydoc(cls, definitions=None, inferred_name=None):
        definitions = []
        res = cls.type_args[0].generate_pydoc(definitions, inferred_name or cls.prim)
        if res != f'${cls.prim}':
            definitions.insert(0, (cls.prim, res))
        return '\n'.join(f'${var}:\n\t{doc}\n' for var, doc in definitions)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'MichelsonType':
        item = cls.type_args[0].from_micheline_value(val_expr)
        return cls(item)

    @classmethod
    def from_python_object(cls, py_obj) -> 'MichelsonType':
        item = cls.type_args[0].from_python_object(py_obj)
        return cls(item)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return self.item.to_micheline_value(mode=mode, lazy_diff=lazy_diff)

    def to_python_object(self, lazy_diff=False):
        return self.item.to_python_object(lazy_diff=lazy_diff)

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        item = self.item.merge_lazy_diff(lazy_diff)
        return type(self)(item)

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action: str):
        self.item.attach_lazy_storage(lazy_storage, action=action)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        self.item.aggregate_lazy_diff(lazy_diff, mode=mode)

    def __getitem__(self, key):
        assert hasattr(self.item, '__getitem__'), f'index access is not implemented for {self.item.prim}'
        return self.item[key]


class ParameterType(SectionType, prim='parameter', args_len=1):

    @staticmethod
    def match(type_expr) -> Type['ParameterType']:
        return cast(Type['ParameterType'], MichelsonType.match(type_expr))

    @classmethod
    def list_entry_points(cls) -> Dict[str, Type[MichelsonType]]:
        entry_points = dict(default=cls.type_args[0])
        if cls.type_args[0].prim == 'or':
            flat_args = Struct.get_flat_args(cls.type_args[0], force_recurse=True)
            if isinstance(flat_args, dict):
                for name, arg in flat_args.items():
                    entry_points[name] = arg.get_anon_type()
        return entry_points

    @classmethod
    def from_parameters(cls, parameters: Dict[str, Any]) -> 'MichelsonType':
        assert isinstance(parameters, dict) and list(parameters.keys()) == ['entrypoint', 'value'], \
            f'expected {{entrypoint, value}}, got {parameters}'
        entry_point = parameters['entrypoint']
        if cls.type_args[0].prim == 'or':
            struct = Struct.from_nested_type(cls.type_args[0], force_recurse=True)
            if struct.get_path(entry_point):
                val_expr = struct.normalize_micheline_value(entry_point, parameters['value'])
                item = cls.type_args[0].from_micheline_value(val_expr)
                return cls(item)
        assert entry_point == 'default', f'unexpected entrypoint {entry_point}'
        return cls.from_micheline_value(parameters['value'])

    def to_parameters(self, mode='readable') -> Dict[str, Any]:
        entry_point, item = 'default', self.item
        if isinstance(self.item, OrType):
            struct = Struct.from_nested_type(self.type_args[0], force_recurse=True)
            if struct.is_named():
                flat_values = struct.get_flat_values(self.item.items, force_recurse=True, allow_nones=True)
                assert isinstance(flat_values, dict) and len(flat_values) == 1
                entry_point, item = next(iter(flat_values.items()))
        return {'entrypoint': entry_point,
                'value': item.to_micheline_value(mode=mode)}

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action='copy'):
        super(ParameterType, self).attach_lazy_storage(lazy_storage, action)


class StorageType(SectionType, prim='storage', args_len=1):

    @staticmethod
    def match(type_expr) -> Type['StorageType']:
        return cast(Type['StorageType'], MichelsonType.match(type_expr))

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action='remove'):
        super(StorageType, self).attach_lazy_storage(lazy_storage, action)
