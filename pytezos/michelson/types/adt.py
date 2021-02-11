from typing import List, Tuple, Optional, Dict, Union, Type, Iterable, cast, Generator

from pytezos.michelson.types.base import MichelsonType, Undefined


def iter_type_args(nested_type: Type[MichelsonType], ignore_annots=False, force_recurse=False, path='') \
        -> Generator[Tuple[str, Type[MichelsonType]], None, None]:
    for i, arg in enumerate(nested_type.args):
        if arg.prim == nested_type.prim:
            name = arg.field_name or arg.type_name
            if not ignore_annots and name:
                yield path + str(i), arg
            if force_recurse or ignore_annots or not name:
                yield from iter_type_args(arg,
                                          ignore_annots=ignore_annots,
                                          force_recurse=force_recurse,
                                          path=path + str(i))
        else:
            yield path + str(i), arg


def iter_values(prim: str, nested_item: Iterable[MichelsonType], ignore_annots=False, allow_nones=False, path='') \
        -> Generator[Tuple[str, MichelsonType], None, None]:
    for i, arg in enumerate(nested_item):
        if arg is Undefined:
            assert allow_nones, f'Nones are not allowed for {prim} args'
        elif arg.prim == prim:
            name = arg.field_name or arg.type_name
            if not ignore_annots and name:
                yield path + str(i), arg
            else:
                arg = cast(Iterable[MichelsonType], arg)
                yield from iter_values(prim, arg,
                                       ignore_annots=ignore_annots,
                                       allow_nones=allow_nones,
                                       path=path + str(i))
        else:
            assert isinstance(arg, MichelsonType), f'unexpected arg {arg}'
            yield path + str(i), arg


def get_type_layout(flat_args: List[Tuple[str, Type[MichelsonType]]], force_named=False) \
        -> Tuple[Optional[Dict[str, str]], Optional[Dict[str, str]], Dict[int, str]]:
    reserved = set()
    path_to_key = {}
    for i, (bin_path, arg) in enumerate(flat_args):
        key = arg.field_name or arg.type_name
        if key is not None and key not in reserved:
            reserved.add(key)
            path_to_key[bin_path] = key
        else:
            path_to_key[bin_path] = f'{arg.prim}_{i}'

    idx_to_path = {i: path for i, path in enumerate(path_to_key)}
    if not reserved and not force_named:
        path_to_key = None
        key_to_path = None
    else:
        key_to_path = {name: path for path, name in path_to_key.items()}
    return path_to_key, key_to_path, idx_to_path


class Nested:

    def __init__(self, *args):
        self.args = args

    def __getitem__(self, item: int):
        return self.args[item]


class ADT:

    def __init__(self,
                 prim: str,
                 path_to_key: Optional[Dict[str, str]],
                 key_to_path: Optional[Dict[str, str]],
                 idx_to_path: Dict[int, str]):
        self.prim = prim
        self.path_to_key = path_to_key
        self.key_to_path = key_to_path
        self.idx_to_path = idx_to_path

    def __len__(self):
        return len(self.idx_to_path)

    def is_named(self):
        return self.path_to_key is not None

    def get_name(self, path):
        assert path in self.path_to_key, f'cannot resolve path {path}'
        return self.path_to_key[path]

    def get_path(self, key):
        if isinstance(key, str):
            assert self.is_named(), f'{self.prim} is not named'
            assert key in self.key_to_path, f'cannot find key `{key}`'
            return self.key_to_path[key]
        elif isinstance(key, int):
            assert key in self.idx_to_path, f'cannot find key `{key}`'
            return self.idx_to_path[key]
        else:
            assert isinstance(key, int), f'expected int or string, got {type(key).__name__}'

    def has_path(self, key) -> bool:
        return self.is_named() and key in self.key_to_path

    @classmethod
    def get_flat_args(cls, nested_type: Type[MichelsonType], force_tuple=False,
                      ignore_annots=False, force_named=False, force_recurse=False, fields_only=False) \
            -> Union[Dict[str, Type[MichelsonType]], List[Type[MichelsonType]]]:
        flat_args = list(iter_type_args(nested_type, ignore_annots=ignore_annots, force_recurse=force_recurse))
        if not force_tuple:
            path_to_key, _, _ = get_type_layout(flat_args, force_named=force_named)
            if path_to_key:
                return {
                    path_to_key[path]: arg
                    for path, arg in flat_args
                    if not fields_only or arg.field_name
                }
        return [arg for _, arg in flat_args]

    @classmethod
    def from_nested_type(cls, nested_type: Type[MichelsonType],
                         ignore_annots=False, force_named=False, force_recurse=False) -> 'ADT':
        flat_args = list(iter_type_args(nested_type, ignore_annots=ignore_annots, force_recurse=force_recurse))
        path_to_key, key_to_path, idx_to_path = get_type_layout(flat_args, force_named=force_named)
        return cls(prim=nested_type.prim,
                   path_to_key=path_to_key,
                   key_to_path=key_to_path,
                   idx_to_path=idx_to_path)

    def make_nested_pair(self, py_obj) -> Nested:
        if isinstance(py_obj, dict):
            assert self.is_named(), f'cannot parse dict into unnamed pair'
            values = {self.key_to_path[name]: value for name, value in py_obj.items()}
        elif isinstance(py_obj, tuple):  # can be both named and unnamed
            values = {self.idx_to_path[i]: value for i, value in enumerate(py_obj)}
        else:
            assert False, f'expected dict or tuple, got {type(py_obj).__name__}'

        def wrap_pair(path='') -> Nested:
            items = [values[subpath] if subpath in values else wrap_pair(subpath)
                     for subpath in [path + '0', path + '1']]
            return Nested(*items)

        assert len(self) == len(values), f'expected {len(self)} items, got {len(values)}'
        return wrap_pair()

    def make_nested_or(self, py_obj) -> Nested:
        assert self.is_named(), f'unnamed sum types are not allowed (in the scope of PyTezos)'
        assert isinstance(py_obj, dict), f'expected dict, got {py_obj}'
        assert len(py_obj) == 1, f'single key expected, got {len(py_obj)}'
        entrypoint = next(iter(py_obj))
        assert entrypoint in self.key_to_path, f'unknown entrypoint {entrypoint}'

        def wrap_or(obj, path) -> Nested:
            if len(path) == 0:
                return obj
            elif path[0] == '0':
                return Nested(wrap_or(obj, path[1:]), Undefined)
            elif path[0] == '1':
                return Nested(Undefined, wrap_or(obj, path[1:]))
            else:
                assert False, path

        return wrap_or(py_obj[entrypoint], self.key_to_path[entrypoint])

    def normalize_python_object(self, py_obj) -> Nested:
        if self.prim == 'pair':
            return self.make_nested_pair(py_obj)
        elif self.prim == 'or':
            return self.make_nested_or(py_obj)
        else:
            assert False

    def normalize_micheline_value(self, entrypoint, val_expr):
        assert self.prim == 'or'
        assert self.is_named(), f'sum type has to be named'
        assert entrypoint in self.key_to_path, f'unknown entrypoint {entrypoint}'

        def wrap_expr(expr, path):
            if len(path) == 0:
                return expr
            elif path[0] == '0':
                return {'prim': 'Left', 'args': [wrap_expr(expr, path[1:])]}
            elif path[0] == '1':
                return {'prim': 'Right', 'args': [wrap_expr(expr, path[1:])]}
            else:
                assert False, path

        return wrap_expr(val_expr, self.get_path(entrypoint))

    def get_flat_values(self, nested_item: Iterable[MichelsonType], force_unnamed=False,
                        ignore_annots=False, allow_nones=False, fields_only=False) \
            -> Union[Dict[str, MichelsonType], List[MichelsonType]]:
        flat_values = list(iter_values(self.prim, nested_item,
                                       ignore_annots=ignore_annots,
                                       allow_nones=allow_nones))
        if not force_unnamed and self.is_named():
            return {
                self.get_name(path): arg
                for path, arg in flat_values
                if arg is not None and (not fields_only or arg.field_name)
            }
        else:
            return [arg for _, arg in flat_values]

    def get_value(self, nested_item: Iterable[MichelsonType], key: Union[str, int],
                  ignore_annots=False, allow_nones=False) -> MichelsonType:
        key_path = self.get_path(key)
        return next(
            arg for path, arg in iter_values(self.prim, nested_item, ignore_annots, allow_nones)
            if path == key_path)
