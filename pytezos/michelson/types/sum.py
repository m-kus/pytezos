from typing import Generator, List, Optional, Tuple, Type, Union, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline, parse_micheline_value
from pytezos.michelson.types.adt import ADTMixin, Nested, wrap_or
from pytezos.michelson.types.base import MichelsonType, Undefined, undefined
from pytezos.michelson.types.core import Unit, UnitType


class LeftLiteral(Micheline, prim='Left', args_len=1):
    pass


class RightLiteral(Micheline, prim='Right', args_len=1):
    pass


class OrType(MichelsonType, ADTMixin, prim='or', args_len=2):
    is_enum: bool

    def __init__(self, items: Tuple[Union[undefined, MichelsonType], ...]):
        super(OrType, self).__init__()
        self.items = items

    def __repr__(self):
        return f'({" + ".join(map(repr, self.items))})'

    def __iter__(self) -> Generator[Optional[MichelsonType], None, None]:
        yield from self.items  # type: ignore

    def __eq__(self, other: 'OrType'):  # type: ignore
        return all(
            item == other.items[i]
            for i, item in enumerate(self.items)
        )

    def __lt__(self, other: 'OrType'):  # type: ignore
        if self.is_left() and other.is_right():
            return True
        elif self.is_left() and other.is_left():
            return self.items[0] < other.items[0]  # type: ignore
        elif self.is_right() and other.is_right():
            return self.items[1] < other.items[1]  # type: ignore
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
        return cls((left, Undefined))

    @staticmethod
    def from_right(right: MichelsonType, left_type: Type[MichelsonType]):
        cls = OrType.create_type(args=[left_type, type(right)])
        return cls((Undefined, right))

    @classmethod
    def iter_type_args(cls, entrypoints=False, path='') -> Generator[Tuple[str, Type[MichelsonType]], None, None]:
        for i, arg in enumerate(cls.args):
            if issubclass(arg, OrType):
                if entrypoints and arg.field_name:
                    yield path + str(i), arg
                yield from arg.iter_type_args(entrypoints=entrypoints, path=path + str(i))  # type: ignore
            elif entrypoints is False or arg.field_name:
                yield path + str(i), arg

    @classmethod
    def create_type(cls,
                    args: List[Type['Micheline']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['OrType']:
        def all_units(arguments: List[Type['Micheline']]):
            for arg in arguments:
                if issubclass(arg, OrType):
                    if not all_units(arg.args):
                        return False
                elif not issubclass(arg, UnitType):
                    return False
            return True

        is_enum = all_units(args)
        res = super(OrType, cls).create_type(args=args, annots=annots, is_enum=is_enum, **kwargs)
        return cast(Type['OrType'], res)

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None, comparable=False):
        name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
        flat_args = cls.get_flat_args(infer_names=True)
        assert isinstance(flat_args, dict), f'sum type has to be named (in the scope of PyTezos)'
        if cls.is_enum:
            doc = ' || '.join(flat_args.keys())
        else:
            variants = [(entrypoint, arg.generate_pydoc(definitions, inferred_name=entrypoint))
                        for entrypoint, arg in flat_args.items()]
            if comparable:
                doc = ' ||\n\t'.join(f'( "{entrypoint}", {arg_doc} )' for entrypoint, arg_doc in variants)
            else:
                doc = ' ||\n\t'.join(f'{{ "{entrypoint}": {arg_doc} }}' for entrypoint, arg_doc in variants)
        definitions.insert(0, (name, doc))
        return f'${name}'

    @classmethod
    def dummy(cls, context: AbstractContext):
        return cls((cls.args[0].dummy(context), Undefined))

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'OrType':
        value = parse_micheline_value(val_expr, {
            ('Left', 1): lambda x: (cls.args[0].from_micheline_value(x[0]), Undefined),
            ('Right', 1): lambda x: (Undefined, cls.args[1].from_micheline_value(x[0]))
        })
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'OrType':
        if isinstance(py_obj, list):
            py_obj = tuple(py_obj)
        elif isinstance(py_obj, str):
            assert cls.is_enum, 'string values allowed for enums only'
            py_obj = {py_obj: Unit}
        elif isinstance(py_obj, tuple):
            assert len(py_obj) == 2, f'expected `(entrypoint, value)`, got {py_obj}'
            py_obj = {py_obj[0]: py_obj[1]}

        if isinstance(py_obj, dict):
            assert len(py_obj) == 1, f'single key expected, got {len(py_obj)}'
            entrypoint = next(iter(py_obj))
            _, key_to_path, _ = cls.get_type_layout(infer_names=True)
            assert key_to_path, f'sum type has to be named (in the scope of PyTezos)'
            return cls.from_python_object(wrap_or(py_obj[entrypoint], key_to_path[entrypoint]))
        elif isinstance(py_obj, Nested):
            value = tuple(Undefined if py_obj[i] is Undefined
                          else cls.args[i].from_python_object(py_obj[i])
                          for i in [0, 1])
            return cls(value)
        else:
            assert False, f'expected list, tuple, or dict, got `{py_obj}`'

    def iter_values(self, path='') -> Generator[Tuple[str, MichelsonType], None, None]:
        for i, arg in enumerate(self.items):
            if isinstance(arg, OrType):
                yield from arg.iter_values(path + str(i))
            elif isinstance(arg, MichelsonType):
                yield path + str(i), arg
            else:
                assert arg == Undefined, f'expected Michelson type or undefined, got {arg}'

    def to_literal(self) -> Type[Micheline]:
        if self.is_left():
            return LeftLiteral.create_type(args=[self.items[0].to_literal()])  # type: ignore
        else:
            return RightLiteral.create_type(args=[self.items[1].to_literal()])  # type: ignore

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        for i, prim in enumerate(['Left', 'Right']):
            if isinstance(self.items[i], MichelsonType):
                return {'prim': prim, 'args': [self.items[i].to_micheline_value(mode=mode, lazy_diff=lazy_diff)]}
        assert False, f'unexpected value {self.items}'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False) -> Union[tuple, dict]:
        flat_values = self.get_flat_values(infer_names=True)
        assert isinstance(flat_values, dict) and len(flat_values) == 1, \
            f'sum type has to be named (in the scope of PyTezos)'
        entrypoint = next(iter(flat_values))
        if self.is_enum:
            return entrypoint  # type: ignore
        else:
            py_obj = flat_values[entrypoint].to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff)
            return (entrypoint, py_obj) if comparable else {entrypoint: py_obj}

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'OrType':
        items = tuple(item.merge_lazy_diff(lazy_diff) if isinstance(item, MichelsonType) else item
                      for item in self.items)
        return type(self)(items)  # type: ignore

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        items = tuple(item.aggregate_lazy_diff(lazy_diff, mode=mode) if isinstance(item, MichelsonType) else item
                      for item in self.items)
        return type(self)(items)  # type: ignore

    def attach_context(self, context: AbstractContext, big_map_copy=False):
        for item in self:
            if isinstance(item, MichelsonType):
                item.attach_context(context, big_map_copy=big_map_copy)

    def __getitem__(self, key: Union[int, str]) -> MichelsonType:
        return self.get_value(key, infer_names=True)
