from typing import Optional, Tuple, Generator, List

from pytezos.types.base import MichelsonType, parse_micheline_value


class MapType(MichelsonType, prim='map', args_len=2):

    @classmethod
    def construct_value(cls, value: List[Tuple[MichelsonType, MichelsonType]]) -> 'MapType':
        assert len(value) > 0, f'cannot instantiate from empty list'
        type_args = [item.get_type() for item in value[0]]
        assert len(type_args) == 2, f'expected two args, got {len(type_args)}'
        assert type_args[0].is_comparable(), f'{type_args[0].prim} is not a comparable type'
        # TODO: assert homogeneous
        return cls(value=value, type_args=type_args)

    def assert_value_defined(self):
        assert isinstance(self.value, list), f'expected list, got {type(self.value).__name__}'

    def assert_item_defined(self, idx: int, arg: MichelsonType):
        assert isinstance(arg, type(self.type_args[idx])), \
            f'expected {type(self.type_args[idx]).__name__}, got {type(arg).__name__}'

    def assert_elt_defined(self, item: Tuple[MichelsonType, MichelsonType]):
        assert isinstance(item, tuple), f'expected list, got {type(item).__name__}'
        assert len(item) == 2, f'expected 2 args, got {len(item)}'
        for i, arg in enumerate(item):
            self.assert_item_defined(i, arg)

    def __len__(self):
        self.assert_value_defined()
        return len(self.value)

    def __iter__(self) -> Generator[Tuple[MichelsonType, MichelsonType], None, None]:
        self.assert_value_defined()
        for item in self.value:
            self.assert_elt_defined(item)
            yield item

    def get(self, key: MichelsonType, check_dup=True) -> Optional[MichelsonType]:
        self.assert_value_defined()
        self.assert_item_defined(0, key)
        if check_dup:
            assert self.type_args[1].is_duplicable(), f'use get and update instead'
        return next((item[1] for item in self if item[0] == key), None)

    def contains(self, key: MichelsonType):
        return self.get(key, check_dup=False) is not None

    def update(self, key: MichelsonType, val: Optional[MichelsonType]) -> Tuple[Optional[MichelsonType], MichelsonType]:
        self.assert_item_defined(1, val)
        prev_val = self.get(key)
        if prev_val is not None:
            if val is not None:
                value = [(k, v if k != key else val) for k, v in self]
            else:  # remove
                value = [(k, v) for k, v in self if k != key]
        else:
            if val is not None:
                value = list(sorted(self.value + [(key, val)], key=lambda x: x[0]))
            else:
                value = self.value
        return prev_val, self.spawn(value)

    def parse_micheline_elt(self, val_expr) -> Tuple[MichelsonType, MichelsonType]:
        return parse_micheline_value(val_expr, {
            ('Elt', 2): lambda x: tuple(self.type_args[i].parse_micheline_value(arg) for i, arg in enumerate(x))
        })

    def parse_micheline_value(self, val_expr):
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'
        value = list(map(self.parse_micheline_elt, val_expr))
        keys = list(map(lambda x: x[0], value))
        assert len(set(keys)) == len(keys), f'duplicate keys found'
        assert keys == list(sorted(keys)), f'keys are unsorted'
        return self.spawn(value)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return [
            {'prim': 'Elt', 'args': [x.to_micheline_value(mode=mode, lazy_diff=lazy_diff) for x in elt]}
            for elt in self
        ]

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, dict), f'expected dict, got {type(py_obj).__name__}'
        value = [
            [self.type_args[i].parse_python_object(arg) for i, arg in enumerate(elt)]
            for elt in py_obj.items()
        ]
        value = list(sorted(value, key=lambda x: x[0]))
        return self.spawn(value)

    def to_python_object(self, lazy_diff=False):
        return {k.to_python_object(): v.to_python_object(lazy_diff=lazy_diff) for k, v in self}

    def generate_pydoc(self, definitions: list, inferred_name=None):
        name = self.field_name or self.type_name or inferred_name
        arg_names = [f'{name}_key', f'{name}_value'] if name else [None, None]
        key, val = [arg.generate_pydoc(definitions, inferred_name=arg_names[i]) for i, arg in enumerate(self.type_args)]
        return f'{{ {key}: {val}, ... }}'

    def __contains__(self, key_obj):
        key = self.type_args[0].parse_python_object(key_obj)
        return self.contains(key)

    def __getitem__(self, key_obj) -> MichelsonType:
        self.assert_value_defined()
        key = self.type_args[1].parse_python_object(key_obj)
        val = self.get(key)
        assert val is not None, f'not found: {key_obj}'
        return val
