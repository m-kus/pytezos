from pytezos.types.base import MichelsonType, parse_micheline_value


class MapType(MichelsonType, prim='map', args_len=2):

    def assert_value_defined(self):
        assert isinstance(self.value, list), f'value is undefined'
        for elt in self.value:
            for i, arg in enumerate(elt):
                assert isinstance(arg, type(self.args[0])), \
                    f'invalid type: expected {type(self.args[0]).__name__}, got {type(arg).__name__}'

    def parse_micheline_elt(self, val_expr):
        return parse_micheline_value(val_expr, {
            ('Elt', 2): lambda x: [self.args[i].parse_micheline_value(arg) for i, arg in enumerate(x)]
        })

    def parse_micheline_value(self, val_expr):
        assert isinstance(val_expr, list), f'expected list, got {type(val_expr).__name__}'
        value = list(map(self.parse_micheline_elt, val_expr))
        keys = list(map(lambda x: x[0], value))
        assert len(set(keys)) == len(keys), f'duplicate keys found'
        assert keys == list(sorted(keys)), f'keys are unsorted'
        self.spawn(value)

    def to_micheline_value(self, mode='readable'):
        self.assert_value_defined()
        return [
            {'prim': 'Elt',
             'args': list(map(lambda x: x.to_micheline_value(mode=mode), elt))}
            for elt in self.value
        ]

    def parse_python_object(self, py_obj):
        assert isinstance(py_obj, dict), f'expected dict, got {type(py_obj).__name__}'
        value = [
            [self.args[i].parse_python_object(arg) for i, arg in enumerate(elt)]
            for elt in py_obj.items()
        ]
        value = list(sorted(value, key=lambda x: x[0]))
        self.spawn(value)

    def to_python_object(self):
        self.assert_value_defined()
        return {k.to_python_object(): v.to_python_object() for k, v in self.value}

    def generate_pydoc(self, definitions: list, imposed_name=None):
        name = self.field_name or self.type_name or imposed_name
        arg_names = [f'{name}_key', f'{name}_value'] if name else [None, None]
        key, val = [arg.generate_pydoc(definitions, imposed_name=arg_names[i]) for i, arg in enumerate(self.args)]
        return f'{{ {key}: {val}, ... }}'
