from typing import List, Type, cast, Dict, Tuple, Any, Union, Optional

from pytezos.michelson.micheline import MichelsonPrimitive
from pytezos.michelson.types.base import MichelsonType


def format_stdout(prim: str, inputs: list, outputs: list):
    return f'{prim} / {" : ".join(map(repr, inputs))} => {" : ".join(map(repr, outputs))}'


def dispatch_types(*args, mapping: Dict[Tuple[Type[MichelsonType], ...], Tuple[Any, ...]]):
    key = tuple(type(arg) for arg in args)
    assert key in mapping, f'unexpected arguments {", ".join(map(lambda x: x.__name__, key))}'
    return mapping[key]


class MichelsonInstruction(MichelsonPrimitive):
    args: List[Union[Type['MichelsonInstruction'], Any]] = []
    field_names: List[str] = []

    @staticmethod
    def match(expr) -> Type['MichelsonInstruction']:
        return cast(Type['MichelsonInstruction'], MichelsonPrimitive.match(expr))

    @classmethod
    def create_type(cls,
                    args: List[Type['MichelsonPrimitive']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonInstruction']:
        field_names = [a[1:] for a in annots if a.startswith('%')] if annots else []
        assert len(field_names) == len(annots), f'only field annotations allowed'
        res = type(cls.__name__, (cls,), dict(args=args,
                                              field_names=field_names,
                                              **kwargs))
        return cast(Type['MichelsonInstruction'], res)

    @classmethod
    def as_micheline_expr(cls) -> dict:
        args = [arg.as_micheline_expr() if issubclass(arg, MichelsonPrimitive) else arg
                for arg in cls.args]
        annots = [f'%{name}' for name in cls.field_names]
        expr = dict(prim=cls.prim, annots=annots, args=args)
        return {k: v for k, v in expr.items() if v}
