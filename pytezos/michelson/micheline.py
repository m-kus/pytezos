from pprint import pformat
from typing import Tuple, Dict, Callable, List, Optional, Type, cast, Any, Union

from pytezos import micheline_to_michelson, unforge_micheline
from pytezos.michelson.forge import unforge_chain_id, unforge_address, unforge_public_key, unforge_signature
from pytezos.michelson.instructions.base import MichelsonInstruction
from pytezos.michelson.tags import prim_tags
from pytezos.context.base import NodeContext
from pytezos.michelson.interpreter.stack import MichelsonStack


def is_micheline(value) -> bool:
    """ Check if value is a Micheline expression (using heuristics, so not 100% accurate).
    :param value: Object
    :rtype: bool
    """
    if isinstance(value, list):
        def get_prim(x):
            return x.get('prim') if isinstance(x, dict) else None
        return set(map(get_prim, value)) == {'parameter', 'storage', 'code'}
    elif isinstance(value, dict):
        primitives = list(prim_tags.keys())
        return any(map(lambda x: x in value, ['prim', 'args', 'annots', *primitives]))
    else:
        return False


def is_prim_expr(type_expr) -> bool:
    return isinstance(type_expr, dict) \
            and isinstance(type_expr.get('prim'), str) \
            and type_expr['prim'] == type_expr['prim'].lower()


def get_script_section(script, section_name):
    assert isinstance(script, dict)
    assert isinstance(script['code'], list)
    return next(section for section in script['code'] if section['prim'] == section_name)


def parse_micheline_prim(prim_expr) -> Tuple[str, list, list]:
    assert isinstance(prim_expr, dict), f'expected dict, got {pformat(prim_expr)} (instr_expr)'
    prim = prim_expr.get('prim')
    assert prim is not None, f'prim field is absent'
    args = prim_expr.get('args', [])
    assert isinstance(args, list), f'{prim}: expected list of args, got {pformat(args)} (args)'
    annots = prim_expr.get('annots', [])
    assert isinstance(annots, list), f'{prim}: expected list of annots, got {pformat(annots)} (annots)'
    return prim, args, annots


def parse_micheline_value(val_expr, handlers: Dict[Tuple[str, int], Callable]):
    assert isinstance(val_expr, dict), f'expected dict, got {pformat(val_expr)} (val_expr)'
    prim, args = val_expr.get('prim'), val_expr.get('args', [])
    expected = ' or '.join(map(lambda x: f'{x[0]} ({x[1]} args)', handlers))
    assert (prim, len(args)) in handlers, f'expected {expected}, got {prim} ({len(args)} args)'
    handler = handlers[(prim, len(args))]
    return handler(args)


def parse_micheline_literal(val_expr, handlers: Dict[str, Callable]):
    assert isinstance(val_expr, dict), f'expected dict, got {pformat(val_expr)}'
    core_type, value = next((k, v) for k, v in val_expr.items() if k[0] != '_' and k != 'annots')
    expected = ' or '.join(map(lambda x: f'`{x}`', handlers))
    assert core_type in handlers, f'expected one of {expected}, got {core_type}'
    handler = handlers[core_type]
    return handler(value)


def micheline_value_to_python_object(val_expr):
    if isinstance(val_expr, dict):
        if len(val_expr) == 1:
            prim = next(iter(val_expr))
            if prim == 'string':
                return val_expr[prim]
            elif prim == 'int':
                return int(val_expr[prim])
            elif prim == 'bytes':
                return blind_unpack(bytes.fromhex(val_expr[prim]))
            elif prim == 'bool':
                return True if val_expr[prim] == 'True' else False
        elif val_expr.get('prim'):
            prim = val_expr['prim']
            if prim == 'Pair':
                return tuple(micheline_value_to_python_object(x) for x in val_expr['args'])
    return micheline_to_michelson(val_expr)


def blind_unpack(data: bytes):
    try:
        return unforge_chain_id(data)
    except ValueError:
        pass
    try:
        return unforge_address(data)
    except (ValueError, KeyError):
        pass
    try:
        return unforge_public_key(data)
    except (ValueError, KeyError):
        pass
    try:
        return unforge_signature(data)
    except ValueError:
        pass

    if len(data) > 0 and data.startswith(b'\x05'):
        try:
            res = unforge_micheline(data[1:])
            return micheline_value_to_python_object(res)
        except (ValueError, AssertionError):
            pass

    try:
        return data.decode()
    except ValueError:
        pass

    return data


class MichelsonPrimitive:
    prim: str
    args: List[Union[Type['MichelsonPrimitive'], Any]] = []
    classes: Dict[Tuple[str, Optional[int]], Type['MichelsonPrimitive']] = {}

    @classmethod
    def __init_subclass__(cls, prim: Optional[str] = None, args_len: Optional[int] = 0, **kwargs):
        super().__init_subclass__(**kwargs)
        assert prim, f'undefined primitive'
        assert (prim, args_len) not in cls.classes, f'duplicate key {prim} ({args_len} args)'
        cls.classes[(prim, args_len)] = cls
        cls.prim = prim

    def __str__(self):
        assert False, 'has to be explicitly defined'

    def __repr__(self):
        assert False, 'has to be explicitly defined'

    @staticmethod
    def match(expr) -> Type['MichelsonPrimitive']:
        if isinstance(expr, list):
            args = [MichelsonPrimitive.match(arg) for arg in expr]
            return MichelsonSequence.create_type(args=args)
        else:
            prim, args, annots = parse_micheline_prim(expr)
            args_len = len(args)
            assert (prim, args_len) in MichelsonPrimitive.classes, f'unregistered primitive {prim} ({args_len} args)'
            cls, args_len = MichelsonPrimitive.classes[prim, args_len]
            args = [MichelsonPrimitive.match(arg) if is_prim_expr(arg) else arg for arg in args]
            return cls.create_type(args, annots)

    @classmethod
    def create_type(cls,
                    args: List[Union[Type['MichelsonPrimitive'], Any]],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['MichelsonPrimitive']:
        res = type(cls.__name__, (cls,), dict(args=args, **kwargs))
        return cast(Type['MichelsonPrimitive'], res)

    @classmethod
    def as_micheline_expr(cls) -> dict:
        args = [arg.as_micheline_expr() if issubclass(arg, MichelsonPrimitive) else arg
                for arg in cls.args]
        expr = dict(prim=cls.prim, args=args)
        return {k: v for k, v in expr.items() if v}

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        assert False, 'forbidden'


class MichelsonSequence(MichelsonInstruction, args_len=None):

    def __init__(self, items: List[MichelsonInstruction]):
        super(MichelsonSequence, self).__init__()
        self.items = items

    @classmethod
    def execute(cls, stack: MichelsonStack, stdout: List[str], context: NodeContext):
        items = [arg.execute(stack, stdout, context=context) if issubclass(arg, MichelsonInstruction) else arg
                 for arg in cls.args]
        return cls(items)

    @classmethod
    def as_micheline_expr(cls) -> list:
        return [arg.as_micheline_expr() for arg in cls.args]
