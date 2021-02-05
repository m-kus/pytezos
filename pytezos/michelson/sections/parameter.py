from typing import List, Type, cast, Dict, Any

from pytezos.michelson.types import *
from pytezos.michelson.micheline import Micheline
from pytezos.context.execution import ExecutionContext
from pytezos.michelson.types.adt import ADT


class ParameterSection(Micheline, prim='parameter', args_len=1):
    args: List[Type[MichelsonType]]

    def __init__(self, item: MichelsonType):
        super(Micheline, self).__init__()
        self.item = item

    def __repr__(self):
        return repr(self.item)

    @staticmethod
    def match(type_expr) -> Type['ParameterSection']:
        cls = Micheline.match(type_expr)
        if not issubclass(cls, ParameterSection):
            cls = ParameterSection.create_type(args=[cls])
        return cls

    @classmethod
    def execute(cls, stack, stdout: List[str], context: ExecutionContext):
        context.set_parameter_expr(cls.as_micheline_expr())
        stdout.append(f'parameter: updated')

    @classmethod
    def list_entrypoints(cls) -> Dict[str, Type[MichelsonType]]:
        entrypoints = dict()
        if cls.args[0].prim == 'or':
            flat_args = ADT.get_flat_args(cls.args[0], force_recurse=True, fields_only=True)
            if isinstance(flat_args, dict):
                for name, arg in flat_args.items():
                    entrypoints[name] = arg.get_anon_type()
        root_name = 'root' if 'default' in entrypoints else 'default'
        assert root_name not in entrypoints
        entrypoints[root_name] = cls.args[0]
        return entrypoints

    @classmethod
    def from_parameters(cls, parameters: Dict[str, Any]) -> 'ParameterSection':
        if not parameters:
            parameters = {'entrypoint': 'default', 'value': {'prim': 'Unit'}}
        assert isinstance(parameters, dict) and parameters.keys() == {'entrypoint', 'value'}, \
            f'expected {{entrypoint, value}}, got {parameters}'
        entrypoint = parameters['entrypoint']
        if cls.args[0].prim == 'or':
            struct = ADT.from_nested_type(cls.args[0], force_recurse=True)
            if struct.has_path(entrypoint):
                val_expr = struct.normalize_micheline_value(entrypoint, parameters['value'])
                item = cls.args[0].from_micheline_value(val_expr)
                return cls(item)
        assert entrypoint in ['default', 'root'], f'unexpected entrypoint {entrypoint}'
        res = cls.from_micheline_value(parameters['value'])
        return cast(ParameterSection, res)

    def to_parameters(self, mode='readable') -> Dict[str, Any]:
        entrypoint, item = 'default', self.item
        if isinstance(self.item, OrType):
            struct = ADT.from_nested_type(self.args[0], force_recurse=True)
            if struct.is_named():
                flat_values = struct.get_flat_values(self.item.items,
                                                     ignore_annots=True,
                                                     allow_nones=True,
                                                     fields_only=True)
                assert isinstance(flat_values, dict) and len(flat_values) == 1
                entrypoint, item = next(iter(flat_values.items()))
        return {'entrypoint': entrypoint,
                'value': item.to_micheline_value(mode=mode)}

    @classmethod
    def generate_pydoc(cls) -> str:
        definitions = []
        res = cls.args[0].generate_pydoc(definitions, cls.prim)
        if res != f'${cls.prim}':
            definitions.insert(0, (cls.prim, res))
        return '\n'.join(f'${var}:\n\t{doc}\n' for var, doc in definitions)

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'ParameterSection':
        item = cls.args[0].from_micheline_value(val_expr)
        return cls(item)

    @classmethod
    def from_python_object(cls, py_obj) -> 'ParameterSection':
        item = cls.args[0].from_python_object(py_obj)
        return cls(item)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return self.item.to_micheline_value(mode=mode, lazy_diff=lazy_diff)

    def to_python_object(self, try_unpack=False, lazy_diff=False):
        return self.item.to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff)

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'ParameterSection':
        item = self.item.merge_lazy_diff(lazy_diff)
        return type(self)(item)

    def attach_context(self, context: ExecutionContext):
        self.item.attach_context(context, big_map_copy=True)

    def aggregate_lazy_diff(self, mode='readable') -> List[dict]:
        lazy_diff = []
        self.item.aggregate_lazy_diff(lazy_diff, mode=mode)
        return lazy_diff

    def __getitem__(self, key):
        assert hasattr(self.item, '__getitem__'), f'index access is not implemented for {self.item.prim}'
        return self.item[key]
