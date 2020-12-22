from typing import Generator, Tuple

from pytezos.types.base import MichelsonType, parse_micheline_value


class OrType(MichelsonType, prim='or', args_len=2):

    def assert_value_defined(self):
        assert isinstance(self.value, tuple), f'value is undefined'
        assert len(self.value) == 2, f'expected 2 args, got {len(self.value)}'
        defined = [isinstance(arg, type(self.args[i])) for i, arg in enumerate(self.value)]
        assert len(defined) == 1, f'expected single variant defined, got {len(defined)}'

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_value(val_expr, {
            ('Left', 1): lambda x: (self.args[0].parse_micheline_value(x), None),
            ('Right', 1): lambda x: (None, self.args[1].parse_micheline_value(x))
        })
        return self.spawn(value)

    def to_micheline_value(self, mode='readable'):
        self.assert_value_defined()
        for i, prim in enumerate(['Left', 'Right']):
            if isinstance(self.value[i], MichelsonType):
                return {'prim': prim, 'args': [self.value[i].to_micheline_type(mode=mode)]}
        assert False

    def iter_args(self, path='') -> Generator:
        for i, arg in enumerate(self.args):
            if isinstance(arg, OrType):
                yield from arg.iter_args(path + str(i))
            else:
                yield path + str(i), arg

    def iter_values(self, path='') -> Generator:
        self.assert_value_defined()
        for i, arg in enumerate(self.value):
            if isinstance(arg, OrType):
                yield from arg.iter_values(path + str(i))
            elif isinstance(arg, MichelsonType):
                yield path + str(i), arg
            else:
                assert arg is None, f'unexpected arg {arg}'

    def get_schema(self):  # TODO: cache it
        flat_args = list(self.iter_args())
        reserved_names = set()
        entry_points = {}
        paths = {}
        for i, (path, arg) in enumerate(flat_args):
            if arg.field_name is not None and arg.field_name not in reserved_names:
                reserved_names.add(arg.field_name)
                entry_points[path] = arg.field_name
            else:
                entry_points[path] = f'{arg.prim}_{i}'
            paths[entry_points[path]] = path
        return flat_args, entry_points, paths

    def parse_python_object(self, py_obj):
        if isinstance(py_obj, tuple):
            assert len(py_obj) == 2, f'expected 2 args, got {len(py_obj)}'
            assert len([x for x in py_obj if x is None]) == 1, f'only single variant allowed'
            value = tuple(
                item if item is None else self.args[i].parse_python_object(item)
                for i, item in enumerate(py_obj)
            )
            return self.spawn(value)
        elif isinstance(py_obj, dict):
            assert len(py_obj) == 1, f'single key expected, got {len(py_obj)}'
            _, _, paths = self.get_schema()
            entry_point = next(py_obj)
            assert entry_point in paths, f'unknown entrypoint {entry_point}'

            def wrap_tuple(obj, path):
                if len(path) == 0:
                    return obj
                elif path[0] == '0':
                    return wrap_tuple(obj, path[1:]), None
                elif path[1] == '1':
                    return None, wrap_tuple(obj, path[1:])
                else:
                    assert False, path

            return self.parse_python_object(wrap_tuple(py_obj, paths[entry_point]))
        else:
            assert False, f'expected tuple or dict, got {type(py_obj).__name__}'

    def to_python_object(self):
        _, entry_points, _ = self.get_schema()
        path, value = next(self.iter_values())
        assert path in entry_points, f'unknown entry point: {path}'
        return {entry_points[path]: value.to_python_object()}

    def generate_pydoc(self, definitions: list, imposed_name=None):
        flat_args, entry_points, _ = self.get_schema()
        variants = [
            (entry_points[path], arg.generate_pydoc(definitions, imposed_name=entry_points[path]))
            for path, arg in flat_args
        ]
        doc = ' ||\n\t'.join(f'{{ "{entry_point}": {arg_doc} }}' for entry_point, arg_doc in variants)
        name = self.field_name or self.type_name or imposed_name or f'{self.prim}_{len(definitions)}'
        definitions.insert(0, (name, doc))
        return f'${name}'
