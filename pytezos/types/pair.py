from typing import Generator, Tuple, List, Union

from pytezos.types.base import MichelsonType, undefined
from pytezos.types.schema import TypeSchema


class PairType(MichelsonType, prim='pair', args_len=None):

    @classmethod
    def construct_type(cls, field_name, type_name, type_args):
        if len(type_args) == 2:
            pass
        elif len(type_args) > 2:  # comb
            type_args = [type_args[0], cls.construct_type(None, None, type_args[1:])]
        else:
            assert False, f'unexpected number of args: {len(type_args)}'
        return cls(value=undefined(), field_name=field_name, type_name=type_name, type_args=type_args)

    def assert_value_defined(self):
        assert isinstance(self.value, tuple), f'expected tuple, got {type(self.value).__name__}'
        assert len(self.value) == 2, f'expected 2 args, got {len(self.value)}'

    def assert_item_defined(self, idx: int, arg: MichelsonType):
        assert isinstance(arg, type(self.type_args[idx])),  \
            f'expected {type(self.type_args[idx]).__name__}, got {type(arg).__name__}'

    def __iter__(self) -> Generator[MichelsonType, None, None]:
        for i, item in enumerate(self.value):
            self.assert_item_defined(i, item)
            yield item

    def parse_micheline_value(self, val_expr):
        if isinstance(val_expr, dict):
            prim, args = val_expr.get('prim'), val_expr.get('args', [])
            assert prim == 'Pair', f'expected Pair, got {prim}'
        elif isinstance(val_expr, list):
            args = val_expr
        else:
            assert False, f'either dict(prim) or list expected, got {type(val_expr).__name__}'

        if len(args) == 2:
            value = [self.type_args[i].parse_micheline_value(arg)
                     for i, arg in enumerate(args)]
        elif len(args) > 2:
            value = [self.type_args[0].parse_micheline_value(args[0]),
                     self.type_args[1].parse_micheline_value(args[1:])]
        else:
            assert False, f'at least two args expected, got {len(args)}'
        return self.spawn(tuple(value))

    def iter_comb(self) -> Generator[MichelsonType, None, None]:
        for i, item in enumerate(self):
            if i == 1 and isinstance(item, PairType) and item.field_name is None and item.type_name is None:
                yield from item.iter_comb()
            else:
                yield item

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        args = [arg.to_micheline_value(mode=mode, lazy_diff=lazy_diff) for arg in self.iter_comb()]
        if mode == 'readable':
            return {'prim': 'Pair', 'args': args}
        elif mode == 'optimized':
            if len(args) == 2:
                return {'prim': 'Pair', 'args': args}
            elif len(args) == 3:
                return {'prim': 'Pair', 'args': [args[0], {'prim': 'Pair', 'args': args[1:]}]}
            elif len(args) >= 4:
                return args
            else:
                assert False, f'unexpected args len {len(args)}'
        else:
            assert False, f'unsupported mode {mode}'

    def iter_type_args(self, path='') -> Generator[Tuple[str, MichelsonType], None, None]:
        for i, arg in enumerate(self.type_args):
            if isinstance(arg, PairType) and arg.field_name is None and arg.type_name is None:
                yield from arg.iter_type_args(path + str(i))
            else:
                yield path + str(i), arg

    def iter_values(self, path='') -> Generator[Tuple[str, MichelsonType], None, None]:
        for i, arg in enumerate(self):
            if isinstance(arg, PairType) and arg.field_name is None and arg.type_name is None:
                yield from arg.iter_values(path + str(i))
            elif isinstance(arg, MichelsonType):
                yield path + str(i), arg
            else:
                assert arg is None, f'unexpected arg {arg}'

    def parse_python_object(self, py_obj):
        if isinstance(py_obj, list):
            py_obj = tuple(py_obj)

        if isinstance(py_obj, tuple) and len(py_obj) == 2:
            value = tuple(self.type_args[i].parse_python_object(item) for i, item in enumerate(py_obj))
            return self.spawn(value)
        else:
            schema = TypeSchema.from_flat_args(self.prim, list(self.iter_type_args()))
            return self.parse_python_object(schema.normalize_python_object(py_obj))

    def to_python_object(self, lazy_diff=False) -> Union[dict, tuple]:
        schema = TypeSchema.from_flat_args(self.prim, list(self.iter_type_args()))
        flat_values = [(path, arg.to_python_object(lazy_diff=lazy_diff)) for path, arg in self.iter_values()]
        if schema.is_named():
            return {schema.get_name(path): arg for path, arg in flat_values}
        else:
            return tuple(arg for _, arg in flat_values)

    def generate_pydoc(self, definitions: list, inferred_name=None):
        name = self.field_name or self.type_name or inferred_name or f'{self.prim}_{len(definitions)}'
        flat_args = list(self.iter_type_args())
        schema = TypeSchema.from_flat_args(self.prim, flat_args)
        if schema.is_named():
            fields = [
                (schema.get_name(path), arg.generate_pydoc(definitions, inferred_name=schema.get_name(path)))
                for path, arg in flat_args
            ]
            doc = '{\n' + ',\n'.join(f'\t  "{name}": {arg_doc}' for name, arg_doc in fields) + '\n\t}'
        else:
            items = [
                arg.generate_pydoc(definitions, inferred_name=f'{arg.prim}_{i}')
                for i, (_, arg) in enumerate(flat_args)
            ]
            if all(arg.prim in ['pair', 'or'] or not arg.type_args for _, arg in flat_args):
                return f'( {", ".join(items)} )'
            else:
                doc = '(\n' + ',\n'.join(f'\t  {arg_doc}' for arg_doc in items) + '\n\t)'
        definitions.insert(0, (name, doc))
        return f'${name}'

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MichelsonType':
        value = tuple(item.merge_lazy_diff(lazy_diff) for item in self)
        return self.spawn(value)

    def aggregate_lazy_diff(self, lazy_diff: List[dict]):
        for item in self:
            item.aggregate_lazy_diff(lazy_diff)

    def __getitem__(self, name: Union[int, str]) -> MichelsonType:
        self.assert_value_defined()
        if isinstance(name, int) and 0 <= name <= 1:
            return self.value[name]
        else:
            schema = TypeSchema.from_flat_args(self.prim, list(self.iter_type_args()))
            key_path = schema.get_path(name)
            return next(arg for path, arg in self.iter_values() if path == key_path)
