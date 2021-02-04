from typing import Optional, Tuple, Generator, List, Type

from pytezos.michelson.types.base import MichelsonType
from pytezos.michelson.micheline import parse_micheline_value, Micheline, MichelineSequence
from pytezos.context.execution import ExecutionContext


class EltLiteral(Micheline, prim='Elt', args_len=2):
    pass


class MapType(MichelsonType, prim='map', args_len=2):

    def __init__(self, items: List[Tuple[MichelsonType, MichelsonType]]):
        super(MapType, self).__init__()
        self.items = items

    def __repr__(self):
        elements = [f'{repr(k)}: {repr(v)}' for k, v in self.items]
        return f'{{{", ".join(elements)}}}'

    def __len__(self):
        return len(self.items)

    def __iter__(self) -> Generator[Tuple[MichelsonType, MichelsonType], None, None]:
        yield from iter(self.items)

    @staticmethod
    def empty(key_type: Type[MichelsonType], val_type: Type[MichelsonType]) -> 'MapType':
        cls = MapType.create_type(args=[key_type, val_type])
        return cls(items=[])

    @staticmethod
    def from_items(items: List[Tuple[MichelsonType, MichelsonType]]) -> 'MapType':
        assert len(items) > 0, 'cannot instantiate from empty list'
        key_type, val_type = type(items[0][0]), type(items[0][1])
        for key, val in items[1:]:
            key_type.assert_type_equal(type(key))
            val_type.assert_type_equal(type(val))
        cls = MapType.create_type(args=[key_type, val_type])
        cls.check_constraints(items)
        return cls(items=items)

    @classmethod
    def check_constraints(cls, items: List[Tuple[MichelsonType, MichelsonType]]):
        keys = list(map(lambda x: x[0], items))
        assert len(set(keys)) == len(keys), f'duplicate keys found'
        assert keys == list(sorted(keys)), f'keys are unsorted'

    @classmethod
    def generate_pydoc(cls, definitions: List[Tuple[str, str]], inferred_name=None):
        name = cls.field_name or cls.type_name or inferred_name
        arg_names = [f'{name}_key', f'{name}_value'] if name else [None, None]
        key, val = [arg.generate_pydoc(definitions, inferred_name=arg_names[i]) for i, arg in enumerate(cls.args)]
        return f'{{ {key}: {val}, ... }}'

    @classmethod
    def dummy(cls, context: ExecutionContext) -> 'MapType':
        return cls([])

    @classmethod
    def parse_micheline_value(cls, val_expr) -> List[Tuple[MichelsonType, MichelsonType]]:
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'

        def parse_elt(elt_expr) -> Tuple[MichelsonType, MichelsonType]:
            return parse_micheline_value(elt_expr, {
                ('Elt', 2): lambda x: tuple(cls.args[i].from_micheline_value(arg) for i, arg in enumerate(x))
            })

        items = list(map(parse_elt, val_expr))
        cls.check_constraints(items)
        return items

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'MapType':
        return cls(cls.parse_micheline_value(val_expr))

    @classmethod
    def parse_python_object(cls, py_obj) -> List[Tuple[MichelsonType, MichelsonType]]:
        assert isinstance(py_obj, dict), f'expected dict, got {type(py_obj).__name__}'
        items = [
            (cls.args[0].from_python_object(k), cls.args[1].from_python_object(v))
            for k, v in py_obj.items()
        ]
        return list(sorted(items, key=lambda x: x[0]))

    @classmethod
    def from_python_object(cls, py_obj) -> 'MapType':
        return cls(cls.parse_python_object(py_obj))

    def to_literal(self) -> Type[Micheline]:
        return MichelineSequence.create_type(args=[
            EltLiteral.create_type(args=[k.to_literal(), v.to_literal()])
            for k, v in self.items
        ])

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return [
            {'prim': 'Elt', 'args': [x.to_micheline_value(mode=mode, lazy_diff=lazy_diff) for x in elt]}
            for elt in self
        ]

    def to_python_object(self, try_unpack=False, lazy_diff=False) -> dict:
        return {
            k.to_python_object(try_unpack=try_unpack):
                v.to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff) if v else None
            for k, v in self
        }

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'MapType':
        value = [(key, val.merge_lazy_diff(lazy_diff)) for key, val in self]
        return type(self)(value)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        for _, val in self:
            val.aggregate_lazy_diff(lazy_diff, mode=mode)

    def attach_context(self, context: ExecutionContext, big_map_copy=False):
        for _, val in self:
            val.attach_context(context, big_map_copy=big_map_copy)

    def get(self, key: MichelsonType, dup=True) -> Optional[MichelsonType]:
        self.args[0].assert_type_equal(type(key))
        if dup:
            assert self.args[1].is_duplicable(), f'use GET_AND_UPDATE instead'
        return next((item[1] for item in self if item[0] == key), None)

    def contains(self, key: MichelsonType):
        return self.get(key, dup=False) is not None

    def update(self, key: MichelsonType, val: Optional[MichelsonType]) -> Tuple[Optional[MichelsonType], MichelsonType]:
        prev_val = self.get(key, dup=False)
        if prev_val is not None:
            if val is not None:
                items = [(k, v if k != key else val) for k, v in self]
            else:  # remove
                items = [(k, v) for k, v in self if k != key]
        else:
            if val is not None:
                items = list(sorted(self.items + [(key, val)], key=lambda x: x[0]))
            else:  # do nothing
                items = self.items
        return prev_val, type(self)(items)

    def __contains__(self, key_obj):
        key = self.args[0].from_python_object(key_obj)
        return self.contains(key)

    def __getitem__(self, key_obj) -> MichelsonType:
        key = self.args[0].from_python_object(key_obj)
        val = self.get(key)
        assert val is not None, f'not found: {key_obj}'
        return val
