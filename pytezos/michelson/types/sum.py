from typing import Generator, Tuple, Optional, List, Union, Type
from pprint import pformat

from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.micheline import parse_micheline_value
from pytezos.context.execution import ExecutionContext
from pytezos.michelson.types.adt import ADT


class OrType(MichelsonType, prim='or', args_len=2):

    def __init__(self, items: Tuple[Optional[MichelsonType], ...]):
        super(OrType, self).__init__()
        self.items = items

    def __repr__(self):
        return pformat(tuple(map(repr, self.items)))

    def __iter__(self) -> Generator[Optional[MichelsonType], None, None]:
        yield from self.items

    def __eq__(self, other):
        raise NotImplementedError

    def __hash__(self):
        return hash(self.items)

    def is_left(self) -> bool:
        return self.items[0] is not None

    def resolve(self) -> MichelsonType:
        return next(item for item in self if item is not None)

    @staticmethod
    def from_left(left: MichelsonType, right_type: Type[MichelsonType]):
        cls = OrType.create_type(args=[type(left), right_type])
        return cls((left, None))

    @staticmethod
    def from_right(right: MichelsonType, left_type: Type[MichelsonType]):
        cls = OrType.create_type(args=[left_type, type(right)])
        return cls((None, right))

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None):
        name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
        flat_args = ADT.get_flat_args(cls, ignore_annots=True, force_named=True)
        assert isinstance(flat_args, dict)
        variants = [
            (name, arg.generate_pydoc(definitions, inferred_name=name))
            for name, arg in flat_args.items()
        ]
        doc = ' ||\n\t'.join(f'{{ "{entry_point}": {arg_doc} }}' for entry_point, arg_doc in variants)
        definitions.insert(0, (name, doc))
        return f'${name}'

    @classmethod
    def dummy(cls, context: ExecutionContext):
        assert False, 'forbidden'

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'OrType':
        value = parse_micheline_value(val_expr, {
            ('Left', 1): lambda x: (cls.args[0].from_micheline_value(x[0]), None),
            ('Right', 1): lambda x: (None, cls.args[1].from_micheline_value(x[0]))
        })
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'OrType':
        if isinstance(py_obj, tuple):
            assert len(py_obj) == 2, f'expected 2 args, got {len(py_obj)}'
            assert len([x for x in py_obj if x is None]) == 1, f'only single variant allowed'
            value = tuple(
                item if item is None else cls.args[i].from_python_object(item)
                for i, item in enumerate(py_obj)
            )
            return cls(value)
        elif isinstance(py_obj, dict):
            struct = ADT.from_nested_type(cls, ignore_annots=True, force_named=True)
            return cls.from_python_object(struct.normalize_python_object(py_obj))
        else:
            assert False, f'expected tuple or dict, got {type(py_obj).__name__}'

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        for i, prim in enumerate(['Left', 'Right']):
            if isinstance(self.items[i], MichelsonType):
                return {'prim': prim, 'args': [self.items[i].to_micheline_type(mode=mode, lazy_diff=lazy_diff)]}
        assert False, f'unexpected value {self.items}'

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        struct = ADT.from_nested_type(type(self), ignore_annots=True, force_named=True)
        flat_values = struct.get_flat_values(self.items, ignore_annots=True, allow_nones=True)
        assert isinstance(flat_values, dict) and len(flat_values) == 1
        return {
            name: value.to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff)
            for name, value in flat_values.items()
        }

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'OrType':
        value = tuple(item.merge_lazy_diff(lazy_diff) if item else None for item in self)
        return type(self)(value)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        for item in self:
            if item is not None:
                item.aggregate_lazy_diff(lazy_diff, mode=mode)

    def attach_context(self, context: ExecutionContext, big_map_copy=False):
        for item in self:
            if item is not None:
                item.attach_context(context, big_map_copy=big_map_copy)

    def __getitem__(self, key: Union[int, str]):
        if isinstance(key, int) and 0 <= key <= 1:
            return self.items[key]
        else:
            struct = ADT.from_nested_type(type(self), ignore_annots=True, force_named=True)
            return struct.get_value(self.items, key, ignore_annots=True, allow_nones=True)
