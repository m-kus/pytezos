from typing import List, Type, cast, Dict, Tuple, Any, Union, Optional

from pytezos.context.execution import ExecutionContext
from pytezos.michelson.micheline import MichelsonPrimitive
from pytezos.michelson.interpreter.stack import MichelsonStack


def format_stdout(prim: str, inputs: list, outputs: list):
    pop = " : ".join(map(repr, inputs)) if inputs else '_'
    push = " : ".join(map(repr, outputs)) if outputs else '_'
    return f'{prim} / {pop} => {push}'


def dispatch_types(*args: Type[MichelsonPrimitive],
                   mapping: Dict[Tuple[Type[MichelsonPrimitive], ...], Tuple[Any, ...]]):
    key = tuple(arg.prim for arg in args)
    mapping = {tuple(arg.prim for arg in k): v for k, v in mapping.items()}
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

    @classmethod
    def execute(cls, stack: 'MichelsonStack', stdout: List[str], context: ExecutionContext):
        raise NotImplementedError
