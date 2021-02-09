from typing import Generator, Tuple, Optional, List, Union, Type

from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.micheline import parse_micheline_value, Micheline
from pytezos.context.abstract import AbstractContext
from pytezos.michelson.types.adt import ADT, Nested
from pytezos.michelson.types.core import Unit, UnitType
from pytezos.michelson.types.option import Null, OptionType


def format_tuple(length: int, idx: int, val: str) -> str:
    values = [val if i == idx else None for i in range(length)]
    return f'({", ".join(values)})'


class LeftLiteral(Micheline, prim='Left', args_len=1):
    pass


class RightLiteral(Micheline, prim='Right', args_len=1):
    pass


class OrType(MichelsonType, prim='or', args_len=2):

    def __init__(self, items: Tuple[Optional[MichelsonType], ...]):
        super(OrType, self).__init__()
        self.items = items

    def __repr__(self):
        return f'({" + ".join(map(repr, self.items))})'

    def __iter__(self) -> Generator[Optional[MichelsonType], None, None]:
        yield from self.items

    def __eq__(self, other: 'OrType'):
        return all(
            item == other.items[i]
            for i, item in enumerate(self.items)
        )

    def __lt__(self, other: 'OrType'):
        if self.is_left() and other.is_right():
            return True
        elif self.is_left() and other.is_left():
            return self.items[0] < other.items[0]
        elif self.is_right() and other.is_right():
            return self.items[1] < other.items[1]
        else:
            return False

    def __hash__(self):
        return hash(self.items)

    def is_left(self) -> bool:
        return isinstance(self.items[0], MichelsonType)

    def is_right(self) -> bool:
        return isinstance(self.items[1], MichelsonType)

    def resolve(self) -> MichelsonType:
        return next(item for item in self if isinstance(item, MichelsonType))

    @staticmethod
    def from_left(left: MichelsonType, right_type: Type[MichelsonType]):
        cls = OrType.create_type(args=[type(left), right_type])
        return cls((left, None))

    @staticmethod
    def from_right(right: MichelsonType, left_type: Type[MichelsonType]):
        cls = OrType.create_type(args=[left_type, type(right)])
        return cls((None, right))

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None, comparable=False):
        name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
        flat_args = ADT.get_flat_args(cls, ignore_annots=True, force_named=True, force_unnamed=comparable)
        if isinstance(flat_args, dict):
            variants = [(name, arg.generate_pydoc(definitions, inferred_name=name))
                        for name, arg in flat_args.items()]
            doc = ' ||\n\t'.join(f'{{ "{entrypoint}": {arg_doc} }}' for entrypoint, arg_doc in variants)
        else:
            variants = [arg.generate_pydoc(definitions, inferred_name=name, comparable=comparable)
                        for arg in flat_args]
            doc = ' ||\n\t'.join(format_tuple(len(variants), i, arg_doc) for i, arg_doc in enumerate(variants))
        definitions.insert(0, (name, doc))
        return f'${name}'

    @classmethod
    def dummy(cls, context: AbstractContext):
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
        if isinstance(py_obj, list):
            py_obj = tuple(py_obj)

        if isinstance(py_obj, tuple) or isinstance(py_obj, dict):
            struct = ADT.from_nested_type(cls, ignore_annots=True, force_named=True)
            return cls.from_python_object(struct.normalize_python_object(py_obj))
        elif isinstance(py_obj, Nested):
            value = tuple(None if py_obj[i] is None else cls.args[i].from_python_object(py_obj[i]) for i in [0, 1])
            return cls(value)
        else:
            assert False, f'expected list, tuple, or dict, got {type(py_obj).__name__}'

    def to_literal(self) -> Type[Micheline]:
        if self.is_left():
            return LeftLiteral.create_type(args=[self.items[0].to_literal()])
        else:
            return RightLiteral.create_type(args=[self.items[1].to_literal()])

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        for i, prim in enumerate(['Left', 'Right']):
            if isinstance(self.items[i], MichelsonType):
                return {'prim': prim, 'args': [self.items[i].to_micheline_value(mode=mode, lazy_diff=lazy_diff)]}
        assert False, f'unexpected value {self.items}'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False) -> Union[tuple, dict]:
        if comparable:
            values = []
            for item in self.items:
                if isinstance(item, OptionType) and item.is_none():
                    values.append(Null)
                elif isinstance(item, UnitType):
                    values.append(Unit)
                elif isinstance(item, MichelsonType):
                    values.append(
                        item.to_python_object(
                            try_unpack=try_unpack,
                            lazy_diff=lazy_diff,
                            comparable=comparable))
                else:
                    values.append(None)
            return tuple(values)
        else:
            struct = ADT.from_nested_type(type(self), ignore_annots=True, force_named=True)
            flat_values = struct.get_flat_values(self.items, ignore_annots=True, allow_nones=True)
            assert isinstance(flat_values, dict) and len(flat_values) == 1
            return {
                name: value.to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff)
                for name, value in flat_values.items()
            }

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'OrType':
        items = tuple(item.merge_lazy_diff(lazy_diff) if isinstance(item, MichelsonType) else item
                      for item in self.items)
        return type(self)(items)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        items = tuple(item.aggregate_lazy_diff(lazy_diff, mode=mode) if isinstance(item, MichelsonType) else item
                      for item in self.items)
        return type(self)(items)

    def attach_context(self, context: AbstractContext, big_map_copy=False):
        for item in self:
            if isinstance(item, MichelsonType):
                item.attach_context(context, big_map_copy=big_map_copy)

    def __getitem__(self, key: Union[int, str]):
        struct = ADT.from_nested_type(type(self), ignore_annots=True, force_named=True)
        return struct.get_value(self.items, key, ignore_annots=True, allow_nones=True)
