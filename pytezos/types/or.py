from pytezos.types.base import MichelsonType, parse_micheline_value


class OrType(MichelsonType, prim='or', args_len=2):

    def assert_value_defined(self):
        assert isinstance(self.value, list), f'value is undefined'
        defined = [isinstance(arg, type(self.args[i])) for i, arg in enumerate(self.value)]
        assert len(defined) == 1, f'expected single path defined, got {len(defined)}'

    def parse_micheline_value(self, val_expr):
        value = parse_micheline_value(val_expr, {
            ('Left', 1): lambda x: (self.args[0].parse_micheline_value(x), None),
            ('Right', 1): lambda x: (None, self.args[1].parse_micheline_value(x))
        })
        return self.spawn(value)

    def to_micheline_value(self, mode='optimized'):
        self.assert_value_defined()
        for i, prim in enumerate(['Left', 'Right']):
            if isinstance(self.value[i], MichelsonType):
                return {'prim': prim, 'args': [self.value[i].to_micheline_type(mode=mode)]}
        assert False

    def get_flat_args(self, path='') -> list:
        flat_args = []
        for i, arg in enumerate(self.args):
            if isinstance(arg, OrType):
                flat_args.extend(arg.get_flat_args(path + str(i)))
            else:
                flat_args.append((path + str(i), arg))
        return flat_args

    def get_flat_value(self, path='') -> list:
        self.assert_value_defined()
        flat_value = []
        for i, arg in enumerate(self.value):
            if isinstance(arg, OrType):
                flat_value.extend(arg.get_flat_value(path + str(i)))
            elif isinstance(arg, MichelsonType):
                arg.assert_value_defined()
                flat_value.append((path + str(i), arg.value))
            else:
                assert arg in None, f'unexpected arg {arg}'
                flat_value.append((path + str(i), None))
        return flat_value

    def get_schema(self):  # TODO: cache it
        flat_args = self.get_flat_args()
        reserved_names = set()
        entry_points = {}
        or_paths = {}
        for i, (path, arg) in enumerate(flat_args):
            if arg.field_name is not None and arg.field_name not in reserved_names:
                reserved_names.add(arg.field_name)
                entry_points[path] = arg.field_name
            else:
                entry_points[path] = f'{arg.prim}_{i}'
            or_paths[entry_points[path]] = path
        return entry_points, or_paths

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, dict), f'expected dict, got {type(py_obj).__name__}'
        assert len(py_obj) == 1, f'single key expected, got {len(py_obj)}'
        key = next(py_obj)
        _, or_paths = self.get_schema()

        if key in or_paths:
            def wrap_python_object(obj, path):
                return {int(path[0]): wrap_python_object(obj, path[1:])} if path else obj
            key = int(or_paths[key][0])
            py_obj = wrap_python_object(py_obj, or_paths[key][1:])

        if key == 0:
            value = (self.args[0].parse_python_object(py_obj[key]), None)
        elif key == 1:
            value = (None, self.args[1].parse_python_object(py_obj[key]))
        else:
            assert False, f'either known entry point or 0/1 expected, got {key}'
        return self.spawn(value)

    def to_python_object(self):
        entry_points, _ = self.get_schema()
        flat_value = self.get_flat_value()
        path, arg = next((path, arg) for path, arg in flat_value if arg is not None)
        return {entry_points[path]: arg.to_python_object()}
