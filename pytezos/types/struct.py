from typing import List, Tuple, Optional, Dict, Union, Type, Iterable, cast, Generator, Any

from pytezos.types.base import MichelsonType


class Struct:

    def __init__(self, prim: str, path_to_key: Optional[Dict[str, str]], key_to_path: Dict[Union[str, int], str]):
        self.prim = prim
        self.path_to_key = path_to_key
        self.key_to_path = key_to_path

    def is_named(self):
        return self.path_to_key is not None

    def get_name(self, path):
        assert path in self.path_to_key, f'cannot resolve path {path}'
        return self.path_to_key[path]

    def get_path(self, key):
        if isinstance(key, str):
            assert self.is_named(), f'{self.prim} is not named'
        else:
            assert isinstance(key, int), f'expected int or string, got {type(key).__name__}'
        assert key in self.key_to_path, f'cannot find key {key}'
        return self.key_to_path[key]

    @staticmethod
    def iter_type_args(nested_type: Type[MichelsonType], ignore_annots=False, path='') \
            -> Generator[Tuple[str, Type[MichelsonType]], None, None]:
        for i, arg in enumerate(nested_type.type_args):
            if arg.prim == nested_type.prim:
                if not ignore_annots and (arg.field_name or arg.type_name):
                    yield path + str(i), arg
                else:
                    yield from Struct.iter_type_args(arg, ignore_annots, path=path + str(i))
            else:
                yield path + str(i), arg

    @staticmethod
    def iter_values(prim: str, nested_item: Iterable[MichelsonType], ignore_annots=False, allow_nones=False, path='') \
            -> Generator[Tuple[str, MichelsonType], None, None]:
        for i, arg in enumerate(nested_item):
            if arg.prim == prim:
                if not ignore_annots and (arg.field_name or arg.type_name):
                    yield path + str(i), arg
                else:
                    arg = cast(Iterable[MichelsonType], arg)
                    yield from Struct.iter_values(prim, arg, ignore_annots, allow_nones, path + str(i))
            elif isinstance(arg, MichelsonType):
                yield path + str(i), arg
            elif arg is None:
                assert allow_nones, f'Nones are not allowed for {prim} args'
            else:
                assert False, f'unexpected arg {arg}'

    @staticmethod
    def get_type_layout(flat_args: List[Tuple[str, Type[MichelsonType]]], force_named=False) \
            -> Tuple[Optional[Dict[str, str]], Dict[Union[str, int], str]]:
        reserved = set()
        keys = {}
        for i, (bin_path, arg) in enumerate(flat_args):
            key = arg.field_name or arg.type_name
            if key is not None and key not in reserved:
                reserved.add(key)
                keys[bin_path] = key
            else:
                keys[bin_path] = f'{arg.prim}_{i}'

        if not reserved and not force_named:
            paths = {i: path for i, path in enumerate(keys)}
            keys = None
        else:
            paths = {name: path for path, name in keys.items()}
        return keys, paths

    @classmethod
    def get_flat_args(cls, nested_type: Type[MichelsonType], ignore_annots=False, force_named=False) \
            -> Union[Dict[str, Type[MichelsonType]], List[Type[MichelsonType]]]:
        flat_args = list(cls.iter_type_args(nested_type, ignore_annots=ignore_annots))
        keys, _ = cls.get_type_layout(flat_args, force_named=force_named)
        if keys:
            return {keys[path]: arg for path, arg in flat_args}
        else:
            return [arg for _, arg in flat_args]

    @classmethod
    def from_nested_type(cls, nested_type: Type[MichelsonType], ignore_annots=False, force_named=False) -> 'Struct':
        flat_args = list(cls.iter_type_args(nested_type, ignore_annots=ignore_annots))
        keys, paths = cls.get_type_layout(flat_args, force_named=force_named)
        return cls(prim=nested_type.prim, path_to_key=keys, key_to_path=paths)

    def make_nested_pair(self, py_obj) -> tuple:
        if self.is_named():
            assert isinstance(py_obj, dict), f'expected dict, got {type(py_obj).__name__}'
            values = {self.key_to_path[name]: value for name, value in py_obj.items()}
        else:
            assert isinstance(py_obj, tuple), f'expected tuple, got {type(py_obj).__name__})'
            values = {self.key_to_path[i]: value for i, value in enumerate(py_obj)}

        def wrap_tuple(path=''):
            return tuple(
                values[subpath] if subpath in values else wrap_tuple(subpath)
                for subpath in [path + '0', path + '1']
            )

        assert len(self.key_to_path) == len(values), f'expected {len(self.key_to_path)} items, got {len(values)}'
        return wrap_tuple()

    def make_nested_or(self, py_obj) -> tuple:
        assert self.is_named(), f'sum type has to be named'
        assert isinstance(py_obj, dict), f'expected dict, got {type(py_obj).__name__}'
        assert len(py_obj) == 1, f'single key expected, got {len(py_obj)}'

        entry_point = next(py_obj)
        assert entry_point in self.key_to_path, f'unknown entrypoint {entry_point}'

        def wrap_tuple(obj, path):
            if len(path) == 0:
                return obj
            elif path[0] == '0':
                return wrap_tuple(obj, path[1:]), None
            elif path[1] == '1':
                return None, wrap_tuple(obj, path[1:])
            else:
                assert False, path

        return wrap_tuple(py_obj, self.key_to_path[entry_point])

    def normalize_python_object(self, py_obj):
        if self.prim == 'pair':
            return self.make_nested_pair(py_obj)
        elif self.prim == 'or':
            return self.make_nested_or(py_obj)
        else:
            assert False

    def normalize_micheline_value(self, entry_point, val_expr):
        assert self.prim == 'or'
        assert self.is_named(), f'sum type has to be named'
        assert entry_point in self.key_to_path, f'unknown entrypoint {entry_point}'

        def wrap_expr(expr, path):
            if len(path) == 0:
                return expr
            elif path[0] == '0':
                return {'prim': 'Left', 'args': [wrap_expr(expr, path[1:])]}
            elif path[1] == '1':
                return {'prim': 'Right', 'args': [wrap_expr(expr, path[1:])]}
            else:
                assert False, path

        return wrap_expr(val_expr, self.get_path(entry_point))

    def get_flat_values(self, nested_item: Iterable[MichelsonType], ignore_annots=False, allow_nones=False) \
            -> Union[Dict[str, MichelsonType], List[MichelsonType, ...]]:
        flat_values = list(self.iter_values(self.prim, nested_item, ignore_annots, allow_nones))
        if self.is_named():
            return {self.get_name(path): arg for path, arg in flat_values if arg is not None}
        else:
            return [arg for _, arg in flat_values]

    def get_value(self, nested_item: Iterable[MichelsonType], key: Union[str, int],
                  ignore_annots=False, allow_nones=False) -> MichelsonType:
        key_path = self.get_path(key)
        return next(
            arg for path, arg in self.iter_values(self.prim, nested_item, ignore_annots, allow_nones)
            if path == key_path)
