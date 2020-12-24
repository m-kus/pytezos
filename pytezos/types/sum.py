from typing import Generator, Tuple, Optional, List

from pytezos.types.base import MichelsonType, parse_micheline_value
from pytezos.types.schema import TypeSchema


class OrType(MichelsonType, prim='or', args_len=2):

    def assert_value_defined(self):
        assert isinstance(self.value, tuple), f'value is undefined'
        assert len(self.value) == 2, f'expected 2 args, got {len(self.value)}'

    def __iter__(self) -> Generator[Optional[MichelsonType], None, None]:
        self.assert_value_defined()
        for i, item in enumerate(self.value):
            assert item is None or isinstance(item, type(self.type_args[i])),  \
                f'expected None or {type(self.type_args[i])}, got {type(item).__name__}'
            yield item

    def parse_micheline_value(self, val_expr) -> 'OrType':
        value = parse_micheline_value(val_expr, {
            ('Left', 1): lambda x: (self.type_args[0].parse_micheline_value(x), None),
            ('Right', 1): lambda x: (None, self.type_args[1].parse_micheline_value(x))
        })
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        self.assert_value_defined()
        for i, prim in enumerate(['Left', 'Right']):
            if isinstance(self.value[i], MichelsonType):
                return {'prim': prim, 'args': [self.value[i].to_micheline_type(mode=mode, lazy_diff=lazy_diff)]}
        assert False, f'unexpected value {self.value}'

    def iter_type_args(self, path='') -> Generator[Tuple[str, MichelsonType], None, None]:
        for i, arg in enumerate(self.type_args):
            if isinstance(arg, OrType):
                yield from arg.iter_type_args(path + str(i))
            else:
                yield path + str(i), arg

    def iter_values(self, path='') -> Generator[Tuple[str, MichelsonType], None, None]:
        self.assert_value_defined()
        for i, arg in enumerate(self.value):
            if isinstance(arg, OrType):
                yield from arg.iter_values(path + str(i))
            elif isinstance(arg, MichelsonType):
                yield path + str(i), arg
            else:
                assert arg is None, f'unexpected arg {arg}'

    def parse_python_object(self, py_obj) -> 'OrType':
        if isinstance(py_obj, tuple):
            assert len(py_obj) == 2, f'expected 2 args, got {len(py_obj)}'
            assert len([x for x in py_obj if x is None]) == 1, f'only single variant allowed'
            value = tuple(
                item if item is None else self.type_args[i].parse_python_object(item)
                for i, item in enumerate(py_obj)
            )
            return self.spawn(value)
        elif isinstance(py_obj, dict):
            schema = TypeSchema.from_flat_args(self.prim, list(self.iter_type_args()))
            return self.parse_python_object(schema.normalize_python_object(py_obj))
        else:
            assert False, f'expected tuple or dict, got {type(py_obj).__name__}'

    def to_python_object(self, lazy_diff=False):
        schema = TypeSchema.from_flat_args(self.prim, list(self.iter_type_args()))
        bin_path, value = next(self.iter_values())
        entry_point = schema.get_name(bin_path)
        return {entry_point: value.to_python_object(lazy_diff=lazy_diff)}

    def generate_pydoc(self, definitions: list, inferred_name=None):
        flat_args = list(self.iter_type_args())
        schema = TypeSchema.from_flat_args(self.prim, flat_args)
        variants = [
            (schema.get_name(path), arg.generate_pydoc(definitions, inferred_name=schema.get_name(path)))
            for path, arg in flat_args
        ]
        doc = ' ||\n\t'.join(f'{{ "{entry_point}": {arg_doc} }}' for entry_point, arg_doc in variants)
        name = self.field_name or self.type_name or inferred_name or f'{self.prim}_{len(definitions)}'
        definitions.insert(0, (name, doc))
        return f'${name}'

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        value = tuple(item.merge_lazy_diff(lazy_diff) if item else None for item in self)
        return self.spawn(value)

    def aggregate_lazy_diff(self, lazy_diff: List[dict]):
        for item in self:
            if item is not None:
                item.aggregate_lazy_diff(lazy_diff)

    def __getitem__(self, entry_point: str):
        schema = TypeSchema.from_flat_args(self.prim, list(self.iter_type_args()))
        key_path = schema.get_path(entry_point)
        return next(arg for path, arg in self.iter_values() if path == key_path)
