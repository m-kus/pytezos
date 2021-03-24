from typing import Any, Dict, List, Optional, Tuple, Type, Union, cast

from pytezos.context.abstract import AbstractContext  # type: ignore
from pytezos.michelson.micheline import Micheline
from pytezos.michelson.stack import MichelsonStack


class Wildcard:

    @staticmethod
    def n(count: int) -> List['Wildcard']:
        return [Wildcard() for _ in range(count)]

    def __repr__(self):
        return '*'


def format_stdout(prim: str, inputs: list, outputs: list, arg=None):
    arg = f' {arg}' if arg else ''
    pop = " : ".join(map(repr, inputs)) if inputs else '_'
    push = " : ".join(map(repr, outputs)) if outputs else '_'
    return f'{prim}{arg} / {pop} => {push}'


def dispatch_types(*args: Type[Micheline],
                   mapping: Dict[Tuple[Type[Micheline], ...], Tuple[Any, ...]]):
    key = tuple(arg.prim for arg in args)
    mapping = {tuple(arg.prim for arg in k): v for k, v in mapping.items()}  # type: ignore
    assert key in mapping, f'unexpected types `{" * ".join(key)}`'  # type: ignore
    return mapping[key]  # type: ignore


class MichelsonInstruction(Micheline):
    args: List[Union[Type['MichelsonInstruction'], Any]] = []
    field_names: List[str] = []
    var_names: List[str] = []

    def __init__(self, stack_items_added: int = 0) -> None:
        self.stack_items_added = stack_items_added

    @staticmethod
    def match(expr) -> Type['MichelsonInstruction']:
        return cast(Type['MichelsonInstruction'], Micheline.match(expr))

    @classmethod
    def create_type(cls,
                    args: List[Type['Micheline']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonInstruction']:
        if annots:
            field_names = [a[1:] for a in annots if a.startswith('%')]
            var_names = [a[1:] for a in annots if a.startswith('@')]
        else:
            field_names, var_names = [], []
        res = type(cls.__name__, (cls,), dict(args=args,
                                              field_names=field_names,
                                              var_names=var_names,
                                              **kwargs))
        return cast(Type['MichelsonInstruction'], res)

    @classmethod
    def as_micheline_expr(cls) -> dict:
        annots = []
        if cls.var_names is not None:
            annots.extend([f'@{x}' for x in cls.var_names])
        if cls.field_names is not None:
            annots.extend([f'%{x}' for x in cls.field_names])
        args = [arg.as_micheline_expr() for arg in cls.args]
        expr = dict(prim=cls.prim, annots=annots, args=args)
        return {k: v for k, v in expr.items() if v}

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        raise NotImplementedError
