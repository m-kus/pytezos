from typing import List, Tuple, Optional, Dict, Union

from pytezos.types.base import MichelsonType


class TypeSchema:

    def __init__(self, prim, path_to_key: Optional[Dict[str, str]], key_to_path: Dict[Union[str, int], str]):
        self.prim = prim
        self.path_to_key = path_to_key
        self.key_to_path = key_to_path

    def is_named(self):
        return self.path_to_key is not None

    def get_name(self, path):
        assert self.is_named(), f'{self.prim} is not named'
        assert path in self.path_to_key, f'cannot resolve path {path}'
        return self.path_to_key[path]

    def get_path(self, key):
        if isinstance(key, str):
            assert self.is_named(), f'{self.prim} is not named'
        else:
            assert isinstance(key, int), f'expected int or string, got {type(key).__name__}'
        assert key in self.key_to_path, f'cannot find key {key}'
        return self.key_to_path[key]

    def make_nested_pairs(self, py_obj) -> tuple:
        assert self.prim == 'pair', f'works for "pair" only'
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

    def make_nested_ors(self, py_obj) -> tuple:
        assert self.prim == 'or', f'works for "or" only'
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
            return self.make_nested_pairs(py_obj)
        elif self.prim == 'or':
            return self.make_nested_ors(py_obj)
        else:
            assert False

    @classmethod
    def from_flat_args(cls, prim, flat_args: List[Tuple[str, MichelsonType]]) -> 'TypeSchema':
        assert prim in ['pair', 'or'], f'expected "pair" or "or", got {prim}'
        reserved_names = set()
        names = {}
        for i, (bin_path, arg) in enumerate(flat_args):
            name = arg.field_name or (arg.type_name if prim == 'pair' else None)
            if name is not None and name not in reserved_names:
                reserved_names.add(name)
                names[bin_path] = name
            else:
                names[bin_path] = f'{arg.prim}_{i}'

        if not reserved_names and prim == 'pair':
            paths = {i: path for i, path in enumerate(names)}
            names = None
        else:
            paths = {name: path for path, name in names.items()}

        return cls(prim, names, paths)
