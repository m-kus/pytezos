from pytezos.types.base import MichelsonType, undefined


class PairType(MichelsonType, prim='pair', args_len=None):

    @classmethod
    def construct_type(cls, field_name, type_name, args):
        if len(args) == 2:
            pass
        elif len(args) > 2:  # comb
            args = [args[0], cls.construct_type(None, None, args[1:])]
        else:
            assert False, f'unexpected number of args: {len(args)}'
        return cls(value=undefined(), field_name=field_name, type_name=type_name, args=args)

    def assert_value_defined(self):
        assert isinstance(self.value, tuple), f'value is undefined'
        assert len(self.value) == 2, f'expected 2 args, got {len(self.value)}'
        for i, arg in enumerate(self.value):
            assert isinstance(arg, type(self.args[i])),  \
                f'expected {type(self.args[i]).__name__}, got {type(arg).__name__}'

    def parse_micheline_value(self, val_expr):
        if isinstance(val_expr, dict):
            prim, args = val_expr.get('prim'), val_expr.get('args', [])
            assert prim == 'Pair', f'expected Pair, got {prim}'
        elif isinstance(val_expr, list):
            args = val_expr
        else:
            assert False, f'either dict(prim) or list expected, got {type(val_expr).__name__}'

        if len(args) == 2:
            value = [self.args[i].parse_micheline_value(arg)
                     for i, arg in enumerate(args)]
        elif len(args) > 2:
            value = [self.args[0].parse_micheline_value(args[0]),
                     self.args[1].parse_micheline_value(args[1:])]
        else:
            assert False, f'at least two args expected, got {len(args)}'
        return self.spawn(tuple(value))

    def iter_comb(self):
        self.assert_value_defined()
        left, right = self.value
        yield left
        if isinstance(right, PairType) and right.field_name is None and right.type_name is None:
            yield from right.iter_comb()
        else:
            yield right

    def to_micheline_value(self, mode='readable'):
        args = [arg.to_micheline_value(mode=mode) for arg in self.iter_comb()]
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

    def enumerate_args(self, path='') -> list:
        flat_args = []
        for i, arg in enumerate(self.args):
            if isinstance(arg, PairType) and arg.field_name is None and arg.type_name is None:
                flat_args.extend(arg.enumerate_args(path + str(i)))
            else:
                flat_args.append((path + str(i), arg))
        return flat_args

    def get_schema(self):  # TODO: cache it
        flat_args = self.enumerate_args()
        reserved_names = set()
        names = {}
        for i, (path, arg) in enumerate(flat_args):
            name = arg.field_name or arg.type_name
            if name is not None and name not in reserved_names:
                reserved_names.add(name)
                names[path] = name
            else:
                names[path] = f'{arg.prim}_{i}'

        if reserved_names:
            return names, {name: path for path, name in names.items()}
        else:
            return None, {i: path for i, path in enumerate(names)}

    def iter_values(self, path=''):
        self.assert_value_defined()
        for i, arg in enumerate(self.value):
            if isinstance(arg, PairType) and arg.field_name is None and arg.type_name is None:
                yield from arg.iter_values(path + str(i))
            elif isinstance(arg, MichelsonType):
                yield path + str(i), arg
            else:
                assert arg is None, f'unexpected arg {arg}'

    def parse_python_object(self, py_obj):
        if isinstance(py_obj, str):
            py_obj = tuple(py_obj.split('::'))  # map keys
        elif isinstance(py_obj, list):
            py_obj = tuple(py_obj)

        if isinstance(py_obj, tuple) and len(py_obj) == 2:
            value = tuple(self.args[i].parse_python_object(item) for i, item in enumerate(py_obj))
            return self.spawn(value)
        else:
            names, paths = self.get_schema()
            if names:
                assert isinstance(py_obj, dict), f'expected dict, got {type(py_obj).__name__}'
                values = {paths[name]: value for name, value in py_obj.items()}
            else:
                assert isinstance(py_obj, tuple), f'expected tuple, got {type(py_obj).__name__})'
                values = {paths[i]: value for i, value in enumerate(py_obj)}

            def wrap_tuple(path=''):
                return tuple(
                    values[subpath] if subpath in values else wrap_tuple(subpath)
                    for subpath in [path + '0', path + '1']
                )

            assert len(paths) == len(values), f'expected {len(paths)} items, got {len(values)}'
            return self.parse_python_object(wrap_tuple())

    def to_python_object(self):
        names, _ = self.get_schema()
        flat_values = [arg.to_python_object() for arg in self.iter_values()]
        if names:
            return {names[path]: arg for path, arg in flat_values}
        else:
            return tuple(arg for _, arg in flat_values)
