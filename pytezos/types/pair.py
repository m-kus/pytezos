from typing import Generator, Tuple, List, Union, Type, Optional, cast

from pytezos.types.base import MichelsonType, LazyStorage
from pytezos.types.struct import Struct


class PairType(MichelsonType, prim='pair', args_len=None):

    def __init__(self, items: Tuple[MichelsonType, ...]):
        super(PairType, self).__init__()
        self.items = items

    def __iter__(self) -> Generator[MichelsonType, None, None]:
        yield from iter(self.items)

    @staticmethod
    def from_items(items: List[MichelsonType]):
        assert len(items) == 2, f'expected two items, got {len(items)}'
        cls = PairType.construct_type(type_args=[type(item) for item in items])
        return cls(items=tuple(items))

    @classmethod
    def construct_type(cls, type_args: List[Type['MichelsonType']],
                       field_name: Optional[str] = None, type_name: Optional[str] = None) -> Type['PairType']:
        if len(type_args) > 2:  # comb
            type_args = [type_args[0], PairType.construct_type(type_args=type_args[1:])]
        else:
            assert len(type_args) == 2, f'unexpected number of args: {len(type_args)}'
        type_class = super(PairType, cls).construct_type(type_args=type_args,
                                                         field_name=field_name,
                                                         type_name=type_name)
        return cast(Type['PairType'], type_class)

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None):
        name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
        flat_args = Struct.get_flat_args(cls)
        if isinstance(flat_args, dict):
            fields = [
                (name, arg.generate_pydoc(definitions, inferred_name=name))
                for name, arg in flat_args.items()
            ]
            doc = '{\n' + ',\n'.join(f'\t  "{name}": {arg_doc}' for name, arg_doc in fields) + '\n\t}'
        else:
            items = [
                arg.generate_pydoc(definitions, inferred_name=f'{arg.prim}_{i}')
                for i, arg in enumerate(flat_args)
            ]
            if all(arg.prim in ['pair', 'or'] or not arg.type_args for arg in flat_args):
                return f'( {", ".join(items)} )'
            else:
                doc = '(\n' + ',\n'.join(f'\t  {arg_doc}' for arg_doc in items) + '\n\t)'
        definitions.insert(0, (name, doc))
        return f'${name}'

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'PairType':
        if isinstance(val_expr, dict):
            prim, args = val_expr.get('prim'), val_expr.get('args', [])
            assert prim == 'Pair', f'expected Pair, got {prim}'
        elif isinstance(val_expr, list):
            args = val_expr
        else:
            assert False, f'either dict(prim) or list expected, got {type(val_expr).__name__}'

        if len(args) == 2:
            value = tuple(cls.type_args[i].from_micheline_value(arg) for i, arg in enumerate(args))
        elif len(args) > 2:
            value = cls.type_args[0].from_micheline_value(args[0]), cls.type_args[1].from_micheline_value(args[1:])
        else:
            assert False, f'at least two args expected, got {len(args)}'
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'PairType':
        if isinstance(py_obj, list):
            py_obj = tuple(py_obj)
        elif isinstance(py_obj, str):
            py_obj = tuple(py_obj.split('::'))  # map keys

        if isinstance(py_obj, tuple) and len(py_obj) == 2:
            value = tuple(cls.type_args[i].from_python_object(py_obj[i]) for i in [0, 1])
            return cls(value)
        else:
            struct = Struct.from_nested_type(cls)
            return cls.from_python_object(struct.normalize_python_object(py_obj))

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

    def to_python_object(self, lazy_diff=False) -> Union[dict, tuple]:
        struct = Struct.from_nested_type(type(self))
        flat_values = struct.get_flat_values(self.items)
        if isinstance(flat_values, dict):
            return {name: arg.to_python_object(lazy_diff=lazy_diff) for name, arg in flat_values.items()}
        else:
            return tuple(arg.to_python_object(lazy_diff=lazy_diff) for arg in flat_values)

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'PairType':
        value = tuple(item.merge_lazy_diff(lazy_diff) for item in self)
        return type(self)(value)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        for item in self:
            item.aggregate_lazy_diff(lazy_diff, mode=mode)

    def attach_lazy_storage(self, lazy_storage: LazyStorage, action: str):
        for item in self:
            item.attach_lazy_storage(lazy_storage, action=action)

    def __getitem__(self, key: Union[int, str]) -> MichelsonType:
        if isinstance(key, int) and 0 <= key <= 1:
            return self.items[key]
        else:
            struct = Struct.from_nested_type(type(self))
            return struct.get_value(self.items, key)
