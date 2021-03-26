from typing import Any, Dict, List, Optional, Type, Union, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline, MichelsonRuntimeError
from pytezos.michelson.types import OrType
from pytezos.michelson.types.adt import wrap_parameters
from pytezos.michelson.types.base import MichelsonType, parse_name
from pytezos.michelson.types.core import Unit


class ParameterSection(Micheline, prim='parameter', args_len=1):
    args: List[Type[MichelsonType]]  # type: ignore
    root_name: str

    def __init__(self, item: MichelsonType):
        super().__init__()
        self.item = item

    def __repr__(self):
        return repr(self.item)

    @staticmethod
    def match(type_expr) -> Type['ParameterSection']:
        try:
            cls = Micheline.match(type_expr)
            if not issubclass(cls, ParameterSection):
                cls = ParameterSection.create_type(args=[cls])
        except Exception as e:
            raise MichelsonRuntimeError('parameter', *e.args) from e
        return cls

    @classmethod
    def create_type(cls,
                    args: List[Union[Type['Micheline'], Any]],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['ParameterSection']:
        root_name = parse_name(annots, prefix='%')  # type: ignore
        root_type = args[0]
        if issubclass(root_type, OrType):
            if not root_name:
                root_name = root_type.field_name  # type: ignore
            if not root_name:
                flat_args = root_type.get_flat_args(entrypoints=True)  # type: ignore
                assert isinstance(flat_args, dict), f'expected a named type, got {flat_args}'
                root_name = 'root' if 'default' in flat_args else 'default'
        else:
            assert args[0].field_name is None, f'only top-or can be annotated, got ({args[0].prim} %{args[0].field_name})'  # type: ignore
            if not root_name:
                root_name = 'default'
        res = type(cls.__name__, (cls,), dict(args=args, root_name=root_name, **kwargs))
        return cast(Type['ParameterSection'], res)

    @classmethod
    def execute(cls, stack, stdout: List[str], context: AbstractContext):
        context.set_parameter_expr(cls.as_micheline_expr())
        stdout.append(f'parameter: updated')

    @classmethod
    def list_entrypoints(cls) -> Dict[str, Type[MichelsonType]]:
        entrypoints = dict()
        root_type = cls.args[0]
        if issubclass(root_type, OrType):
            flat_args = root_type.get_flat_args(entrypoints=True)
            assert isinstance(flat_args, dict), f'expected dict of named entrypoints'
            for name, arg in flat_args.items():
                entrypoints[name] = arg.get_anon_type()
        entrypoints[cls.root_name] = root_type
        return entrypoints

    @classmethod
    def from_parameters(cls, parameters: Dict[str, Any]) -> 'ParameterSection':
        if len(parameters) == 0:
            parameters = {'entrypoint': 'default', 'value': {'prim': 'Unit'}}
        assert isinstance(parameters, dict) and parameters.keys() == {'entrypoint', 'value'}, \
            f'expected {{entrypoint, value}}, got {parameters}'
        entrypoint = parameters['entrypoint']
        if entrypoint == cls.root_name:
            res = cls.from_micheline_value(parameters['value'])
            return cast(ParameterSection, res)
        else:
            root_type = cls.args[0]
            assert issubclass(root_type, OrType), f'expected `{cls.root_name}`, got `{entrypoint}`'
            _, key_to_path, _ = root_type.get_type_layout(entrypoints=True)
            assert entrypoint in key_to_path, f'unexpected entrypoint `{entrypoint}`'  # type: ignore
            val_expr = wrap_parameters(parameters['value'], key_to_path[entrypoint])  # type: ignore
            item = root_type.from_micheline_value(val_expr)
            return cls(item)

    def to_parameters(self, mode='readable') -> Dict[str, Any]:
        entrypoint, item = self.root_name, self.item
        if isinstance(self.item, OrType):
            flat_values = self.item.get_flat_values(entrypoints=True)
            assert isinstance(flat_values, dict) and len(flat_values) == 1, f'expected named type'
            entrypoint, item = next(iter(flat_values.items()))
        return {'entrypoint': entrypoint,
                'value': item.to_micheline_value(mode=mode)}

    @classmethod
    def generate_pydoc(cls) -> str:
        definitions = []  # type: ignore
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
        if isinstance(py_obj, str):
            entrypoint = py_obj
            py_obj = {entrypoint: Unit}
        else:
            assert isinstance(py_obj, dict) and len(py_obj) == 1, \
                f'expected dict with a single key, got {type(py_obj).__name__} `{py_obj}`'
            entrypoint = next(iter(py_obj))
        if entrypoint == cls.root_name:
            item = cls.args[0].from_python_object(py_obj[entrypoint])
        else:
            assert issubclass(cls.args[0], OrType), f'expected `{cls.root_name}`, got `{entrypoint}`'
            item = cls.args[0].from_python_object(py_obj)
        return cls(item)

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        return self.item.to_micheline_value(mode=mode, lazy_diff=lazy_diff)

    def to_python_object(self, try_unpack=False, lazy_diff=False) -> dict:
        py_obj = self.item.to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff)
        if issubclass(self.args[0], OrType):
            return py_obj
        else:
            return {self.root_name: py_obj}

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'ParameterSection':
        item = self.item.merge_lazy_diff(lazy_diff)
        return type(self)(item)

    def attach_context(self, context: AbstractContext):
        self.item.attach_context(context, big_map_copy=True)

    def aggregate_lazy_diff(self, mode='readable') -> List[dict]:
        lazy_diff = []  # type: ignore
        self.item.aggregate_lazy_diff(lazy_diff, mode=mode)
        return lazy_diff

    def __getitem__(self, key):
        assert hasattr(self.item, '__getitem__'), f'index access is not implemented for {self.item.prim}'
        return self.item[key]
