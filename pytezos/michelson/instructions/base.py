from typing import List, Optional, Type, cast, Dict, Tuple, Any, Union

from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.micheline import MichelsonPrimitive
from pytezos.michelson.types.base import MichelsonType
from pytezos.context.base import NodeContext


def format_stdout(prim: str, inputs: list, outputs: list):
    return f'{prim} / {" : ".join(map(repr, inputs))} => {" : ".join(map(repr, outputs))}'


def dispatch_types(*args, mapping: Dict[Tuple[Type[MichelsonType], ...], Tuple[Any, ...]]):
    key = tuple(type(arg) for arg in args)
    assert key in mapping, f'unexpected arguments {", ".join(map(lambda x: x.__name__, key))}'
    return mapping[key]


class MichelsonInstruction(MichelsonPrimitive):
    args: List[Union[Type['MichelsonInstruction'], Any]] = []
    field_names: List[str] = []
    context: Optional[NodeContext] = None

    @staticmethod
    def match(expr) -> Type['MichelsonInstruction']:
        return cast(Type['MichelsonInstruction'], MichelsonPrimitive.match(expr))

    @classmethod
    def create_type(cls, args: List[Type['MichelsonPrimitive']],
                    params: Optional[list] = None,
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonInstruction']:
        field_names = [a[1:] for a in annots if a.startswith('%')] if annots else []
        assert len(field_names) == len(annots), f'only field annotations allowed'
        res = type(cls.__name__, (cls,), dict(args=args,
                                              params=params,
                                              field_names=field_names,
                                              **kwargs))
        return cast(Type['MichelsonInstruction'], res)

    @classmethod
    def attach_context(cls, context: NodeContext):
        cls.context = context

    @classmethod
    def as_micheline_expr(cls) -> dict:
        args = [arg.as_micheline_expr() for arg in cls.args]
        annots = [f'%{name}' for name in cls.field_names]
        expr = dict(prim=cls.prim, annots=annots, args=args)
        return {k: v for k, v in expr.items() if v}

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str]):
        raise NotImplementedError
