from typing import Dict, Generator, List, Optional, Tuple, Type, Union

from pytezos.michelson.types.base import MichelsonType, Undefined


def get_type_layout(flat_args: List[Tuple[str, Type[MichelsonType]]],
                    infer_names: bool = False, entrypoints: bool = False) \
        -> Tuple[Optional[Dict[str, str]], Optional[Dict[str, str]], Dict[int, str]]:
    reserved = set()
    path_to_key = {}
    for i, (bin_path, arg) in enumerate(flat_args):
        key = arg.field_name
        if key is None and not entrypoints:
            key = arg.type_name
        if key is not None and key not in reserved:
            reserved.add(key)
            path_to_key[bin_path] = key
        else:
            assert entrypoints is False, f'duplicate key {key}'
            path_to_key[bin_path] = f'{arg.prim}_{i}'

    idx_to_path = {i: path for i, path in enumerate(path_to_key)}
    if len(reserved) == 0 and infer_names is False and entrypoints is False:
        path_to_key = None  # type: ignore
        key_to_path = None
    else:
        key_to_path = {name: path for path, name in path_to_key.items()}
    return path_to_key, key_to_path, idx_to_path


class Nested:

    def __init__(self, *args):
        self.args = args

    def __getitem__(self, item: int):
        return self.args[item]


def wrap_or(obj, path) -> Nested:
    if len(path) == 0:
        return obj
    elif path[0] == '0':
        return Nested(wrap_or(obj, path[1:]), Undefined)
    elif path[0] == '1':
        return Nested(Undefined, wrap_or(obj, path[1:]))
    else:
        assert False, path


def wrap_pair(obj: dict, path='') -> Nested:
    if all(not x.startswith(path) for x in obj):
        raise KeyError(path)

    items = [
        obj[subpath] if subpath in obj else wrap_pair(obj, subpath)
        for subpath
        in [path + '0', path + '1']
    ]
    return Nested(*items)


def wrap_parameters(expr, path):
    if len(path) == 0:
        return expr
    elif path[0] == '0':
        return {'prim': 'Left', 'args': [wrap_parameters(expr, path[1:])]}
    elif path[0] == '1':
        return {'prim': 'Right', 'args': [wrap_parameters(expr, path[1:])]}
    else:
        assert False, path


class ADTMixin:

    @classmethod
    def iter_type_args(cls, entrypoints: bool = False, path='') -> Generator[Tuple[str, Type[MichelsonType]], None, None]:
        raise NotImplementedError

    @classmethod
    def get_flat_args(cls, infer_names: bool = False, force_tuple: bool = False, entrypoints: bool = False) \
            -> Union[Dict[str, Type[MichelsonType]], List[Type[MichelsonType]]]:
        flat_args = list(cls.iter_type_args(entrypoints=entrypoints))
        if force_tuple is False:
            path_to_key, _, _ = get_type_layout(flat_args, infer_names=infer_names, entrypoints=entrypoints)
            if isinstance(path_to_key, dict):
                return {path_to_key[path]: arg for path, arg in flat_args}
        return [arg for _, arg in flat_args]

    @classmethod
    def get_type_layout(cls, infer_names: bool = False, entrypoints: bool = False) \
            -> Tuple[Optional[Dict[str, str]], Optional[Dict[str, str]], Dict[int, str]]:
        flat_args = list(cls.iter_type_args(entrypoints=entrypoints))
        return get_type_layout(flat_args, infer_names=infer_names, entrypoints=entrypoints)

    def iter_values(self, path='') -> Generator[Tuple[str, MichelsonType], None, None]:
        raise NotImplementedError

    def get_flat_values(self, infer_names: bool = False, force_tuple: bool = False, entrypoints: bool = False) \
            -> Union[Dict[str, MichelsonType], List[MichelsonType]]:
        path_to_key, _, _ = self.get_type_layout(infer_names=infer_names, entrypoints=entrypoints)
        flat_values = list(self.iter_values())
        if force_tuple is False and isinstance(path_to_key, dict):
            return {path_to_key[path]: arg for path, arg in flat_values}
        else:
            return [arg for _, arg in flat_values]

    def get_value(self, key: Union[str, int], infer_names: bool = False):
        _, key_to_path, idx_to_path = self.get_type_layout(infer_names=infer_names)
        if isinstance(key, str):
            assert key_to_path, f'type is not named'
            path = key_to_path[key]
        elif isinstance(key, int):
            path = idx_to_path[key]
        else:
            assert False, f'expected string or int, got {key}'
        return next(v for p, v in self.iter_values() if p == path)
