from typing import Generator, List, Optional, Tuple, Type, Union, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline
from pytezos.michelson.types.adt import ADTMixin, Nested, wrap_pair
from pytezos.michelson.types.base import MichelsonType


class PairLiteral(Micheline, prim='Pair', args_len=None):
    pass


class PairType(MichelsonType, ADTMixin, prim='pair', args_len=None):

    def __init__(self, items: Tuple[MichelsonType, ...]):
        super(PairType, self).__init__()
        self.items = items

    def __eq__(self, other: 'PairType'):  # type: ignore
        return all(
            item == other.items[i]
            for i, item in enumerate(self.items)
        )

    def __lt__(self, other: 'PairType'):  # type: ignore
        for i, item in enumerate(self.items):
            if item > other.items[i]:
                return False
        return True

    def __hash__(self):
        return hash(self.items)

    def __repr__(self):
        return f'({" * ".join(map(repr, self.items))})'

    def __iter__(self) -> Generator[MichelsonType, None, None]:
        yield from iter(self.items)

    @classmethod
    def init(cls, items: List[MichelsonType]) -> 'PairType':
        if len(items) > 2:
            right_cls = cast(Type['PairType'], cls.args[1])
            items = items[0], right_cls.init(items[1:])  # type: ignore
        else:
            items = tuple(items)  # type: ignore
        return cls(items)  # type: ignore

    @staticmethod
    def from_comb(items: List[MichelsonType]) -> 'PairType':
        cls = PairType.create_type(args=[type(item) for item in items])
        return cls.init(items)

    @classmethod
    def create_type(cls,
                    args: List[Type['Micheline']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['PairType']:
        if len(args) > 2:  # comb
            args = [args[0], PairType.create_type(args=args[1:])]
        else:
            assert len(args) == 2, f'unexpected number of args: {len(args)}'
        type_class = super(PairType, cls).create_type(args=args, annots=annots)
        return cast(Type['PairType'], type_class)

    @classmethod
    def iter_type_args(cls, entrypoints=False, path='') -> Generator[Tuple[str, Type[MichelsonType]], None, None]:
        for i, arg in enumerate(cls.args):
            if issubclass(arg, PairType) and not (arg.field_name or arg.type_name):
                yield from arg.iter_type_args(path=path + str(i))  # type: ignore
            else:
                yield path + str(i), arg

    @classmethod
    def generate_pydoc(cls, definitions: list, inferred_name=None, comparable=False):
        name = cls.field_name or cls.type_name or inferred_name or f'{cls.prim}_{len(definitions)}'
        flat_args = cls.get_flat_args(force_tuple=comparable)
        if isinstance(flat_args, dict):
            fields = [
                (name, arg.generate_pydoc(definitions, inferred_name=name))
                for name, arg in flat_args.items()
            ]
            doc = '{\n' + ',\n'.join(f'\t  "{name}": {arg_doc}' for name, arg_doc in fields) + '\n\t}'
        else:
            items = [
                arg.generate_pydoc(definitions, inferred_name=f'{arg.prim}_{i}')
                for i, arg in enumerate(flat_args)
            ]
            if all(arg.prim in ['pair', 'or'] or not arg.args for arg in flat_args):
                return f'( {", ".join(items)} )'
            else:
                doc = '(\n' + ',\n'.join(f'\t  {arg_doc}' for arg_doc in items) + '\n\t)'
        definitions.insert(0, (name, doc))
        return f'${name}'

    @classmethod
    def dummy(cls, context: AbstractContext) -> 'PairType':
        return cls(tuple(arg.dummy(context) for arg in cls.args))

    @classmethod
    def from_micheline_value(cls, val_expr) -> 'PairType':
        if isinstance(val_expr, dict):
            prim, args = val_expr.get('prim'), val_expr.get('args', [])
            assert prim == 'Pair', f'expected Pair, got {prim}'
        elif isinstance(val_expr, list):
            args = val_expr
        else:
            assert False, f'either dict(prim) or list expected, got {type(val_expr).__name__}'

        if len(args) == 2:
            value = tuple(cls.args[i].from_micheline_value(arg) for i, arg in enumerate(args))
        elif len(args) > 2:
            value = cls.args[0].from_micheline_value(args[0]), cls.args[1].from_micheline_value(args[1:])
        else:
            assert False, f'at least two args expected, got {len(args)}'
        return cls(value)

    @classmethod
    def from_python_object(cls, py_obj) -> 'PairType':
        if isinstance(py_obj, list):
            py_obj = tuple(py_obj)

        if isinstance(py_obj, tuple) or isinstance(py_obj, dict):
            path_to_key, key_to_path, idx_to_path = cls.get_type_layout()
            if isinstance(py_obj, tuple):
                py_obj = {idx_to_path[i]: value for i, value in enumerate(py_obj)}
            else:
                assert key_to_path, f'expected named type'
                py_obj = {key_to_path[key]: value for key, value in py_obj.items()}
            try:
                return cls.from_python_object(wrap_pair(py_obj))
            except KeyError as e:
                if not isinstance(path_to_key, dict):
                    path_to_key = {v: f'{k}th' for k, v in idx_to_path.items()}
                field = path_to_key.get(e.args[0], 'some')
                raise KeyError(f'Missing {field} field')
        elif isinstance(py_obj, Nested):
            value = tuple(cls.args[i].from_python_object(py_obj[i]) for i in [0, 1])
            return cls(value)
        else:
            assert False, f'expected list, tuple, or dict, got {type(py_obj).__name__}'

    def iter_values(self, path='') -> Generator[Tuple[str, MichelsonType], None, None]:
        for i, item in enumerate(self.items):
            if isinstance(item, PairType) and not (item.field_name or item.type_name):
                yield from item.iter_values(path + str(i))
            else:
                yield path + str(i), item

    def iter_comb(self, include_nodes=False) -> Generator[MichelsonType, None, None]:
        if include_nodes:
            yield self
        for i, item in enumerate(self):
            if i == 1 and isinstance(item, PairType) and not (item.field_name or item.type_name):
                yield from item.iter_comb(include_nodes=include_nodes)
            else:
                yield item

    def access_comb(self, idx: int) -> MichelsonType:
        return next(item for i, item in enumerate(self.iter_comb(include_nodes=True)) if i == idx)

    def update_comb(self, idx: int, element: MichelsonType) -> 'PairType':
        if idx % 2 == 1:
            leaves = [element if 2 * i + 1 == idx else item for i, item in enumerate(self.iter_comb())]
        else:
            leaves = [item for i, item in enumerate(self.iter_comb()) if 2 * i + 1 < idx]
            if isinstance(element, PairType):
                leaves.extend(element.iter_comb())
            else:
                leaves.append(element)
        return type(self).from_comb(leaves)

    def to_literal(self) -> Type[Micheline]:
        return PairLiteral.create_type(args=[item.to_literal() for item in self.items])

    def to_micheline_value(self, mode='readable', lazy_diff=False):
        if mode == 'legacy_optimized':
            items = self.items
        else:
            items = list(self.iter_comb())
        args = [arg.to_micheline_value(mode=mode, lazy_diff=lazy_diff) for arg in items]
        if mode in ['readable', 'legacy_optimized']:
            return {'prim': 'Pair', 'args': args}
        elif mode == 'optimized':
            if len(args) == 2:
                return {'prim': 'Pair', 'args': args}
            elif len(args) == 3:
                return {'prim': 'Pair', 'args': [args[0], {'prim': 'Pair', 'args': args[1:]}]}
            elif len(args) >= 4:
                return args
            else:
                assert False, f'unexpected number of args {len(args)}'
        else:
            assert False, f'unsupported mode {mode}'

    def to_python_object(self, try_unpack=False, lazy_diff=False, comparable=False) -> Union[dict, tuple]:
        flat_values = self.get_flat_values(force_tuple=comparable)
        if isinstance(flat_values, dict):
            return {
                name: arg.to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff)
                for name, arg in flat_values.items()
            }
        return tuple(
            arg.to_python_object(try_unpack=try_unpack, lazy_diff=lazy_diff, comparable=comparable)
            for arg in flat_values
        )

    def merge_lazy_diff(self, lazy_diff: List[dict]) -> 'PairType':
        items = tuple(item.merge_lazy_diff(lazy_diff) for item in self)
        return type(self)(items)

    def aggregate_lazy_diff(self, lazy_diff: List[dict], mode='readable'):
        items = tuple(item.aggregate_lazy_diff(lazy_diff, mode=mode) for item in self)
        return type(self)(items)

    def attach_context(self, context: AbstractContext, big_map_copy=False):
        for item in self:
            item.attach_context(context, big_map_copy=big_map_copy)

    def __getitem__(self, key: Union[int, str]) -> MichelsonType:
        return self.get_value(key)
