from pprint import pformat
from functools import wraps
from typing import Tuple, Dict, Callable, List, Optional, Type, cast, Any, Union

from pytezos.michelson.format import micheline_to_michelson
from pytezos.michelson.forge import unforge_chain_id, unforge_address, unforge_public_key, unforge_signature, \
    unforge_micheline
from pytezos.michelson.tags import prim_tags


class MichelsonRuntimeError(Exception):

    def format_stdout(self):
        offset, instruction = next((
            (len(self.args) - i, arg)
            for i, arg in enumerate(reversed(self.args))
            if str(arg).isupper()
        ), (0, 'ERROR'))
        message = ' -> '.join(self.args[offset:])
        return f'{instruction}: {message}'


def catch(prim, func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if not e.args:
                e.args = (type(e).__name__,)
            if prim:
                e.args = (prim, *e.args)
            raise MichelsonRuntimeError(*e.args)
    return wrapper


def try_catch(prim):
    def _catch(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                raise MichelsonRuntimeError(prim, *e.args)
        return wrapper
    return _catch


class ErrorTrace(type):

    def __new__(mcs, name, bases, attrs, **kwargs):
        wrapped_attrs = {}
        for attr_name, attr in attrs.items():
            prim = kwargs.get('prim')
            if type(attr) in [classmethod, staticmethod] and not attr_name.startswith('_'):
                attr = type(attr)(catch(prim, attr.__func__))
            elif callable(attr) and not attr_name.startswith('_'):
                attr = catch(prim, attr)
            wrapped_attrs[attr_name] = attr
        return type.__new__(mcs, name, bases, wrapped_attrs, **kwargs)


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


def get_script_section(script, section_name):
    assert isinstance(script, dict), f'expected dict, got {script}'
    assert isinstance(script['code'], list), f'expected list, got {script.get("code")}'
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


class Micheline(metaclass=ErrorTrace):
    prim: Optional[str] = None
    args: List[Type['Micheline']] = []
    literal: Optional[Union[int, str, bytes]] = None
    classes: Dict[Tuple[str, Optional[int]], Type['Micheline']] = {}

    @classmethod
    def __init_subclass__(cls, prim: Optional[str] = None, args_len: Optional[int] = 0, **kwargs):
        super().__init_subclass__(**kwargs)
        if prim is not None:
            assert (prim, args_len) not in cls.classes, f'duplicate key {prim} ({args_len} args)'
            cls.classes[(prim, args_len)] = cls
            cls.prim = prim

    def __str__(self):
        assert False, '__str__ has to be explicitly defined'

    def __repr__(self):
        assert False, '__repr__ has to be explicitly defined'

    @staticmethod
    def match(expr) -> Type['Micheline']:
        if isinstance(expr, list):
            args = [Micheline.match(arg) for arg in expr]
            return MichelineSequence.create_type(args=args)
        elif isinstance(expr, dict):
            if expr.get('prim'):
                prim, args, annots = parse_micheline_prim(expr)
                args_len = len(args)
                if (prim, args_len) not in Micheline.classes:
                    args_len = None
                assert (prim, args_len) in Micheline.classes, f'unregistered primitive {prim} ({args_len} args)'
                cls = Micheline.classes[prim, args_len]
                try:
                    return cls.create_type(args=list(map(Micheline.match, args)), annots=annots)
                except Exception as e:
                    raise MichelsonRuntimeError(cls.prim, *e.args)
            else:
                literal = parse_micheline_literal(expr, {
                    'int': int,
                    'string': str,
                    'bytes': lambda x: bytes.fromhex(x)
                })
                return MichelineLiteral.create(literal=literal)
        else:
            raise MichelsonRuntimeError(f'malformed expression `{expr}`')

    @classmethod
    def create_type(cls,
                    args: List[Type['Micheline']],
                    annots: Optional[list] = None,
                    **kwargs) -> Type['Micheline']:
        res = type(cls.__name__, (cls,), dict(args=args, **kwargs))
        return cast(Type['MichelsonPrimitive'], res)

    @classmethod
    def assert_type_equal(cls, other: Type['Micheline'], path='', message=''):
        comment = f' [{message}]' if message else ''
        assert cls.prim == other.prim, f'expected {other.prim}, got {cls.prim} at `{path}`{comment}'
        assert len(cls.args) == len(other.args), \
            f'expected {len(other.args)} args, got {len(cls.args)} at `{path}`{comment}'
        for i, arg in enumerate(other.args):
            cls.args[i].assert_type_equal(arg, path=f'{path}/{i}', message=message)
        assert cls.literal == other.literal, \
            f'expected {other.literal}, got {cls.literal} at `{path}`{comment}'

    @classmethod
    def assert_type_in(cls, *others: Type['Micheline'], message=''):
        comment = f' [{message}]' if message else ''
        expected = [ty.prim for ty in others]
        assert any(issubclass(cls, ty) for ty in others), f'expected one of {expected}, got {cls.prim}{comment}'

    @classmethod
    def as_micheline_expr(cls) -> dict:
        args = [arg.as_micheline_expr() for arg in cls.args]
        expr = dict(prim=cls.prim, args=args)
        return {k: v for k, v in expr.items() if v}

    @classmethod
    def execute(cls, stack, stdout, context):
        assert False, f'`execute` has to be explicitly defined'


class MichelineSequence(Micheline):

    def __init__(self, items: List[Micheline]):
        super(MichelineSequence, self).__init__()
        self.items = items

    @classmethod
    def as_micheline_expr(cls) -> list:
        return [arg.as_micheline_expr() for arg in cls.args]

    @classmethod
    def execute(cls, stack, stdout, context):
        return cls([arg.execute(stack, stdout, context) for arg in cls.args])


class MichelineLiteral(Micheline):

    @classmethod
    def create(cls, literal: Union[int, str, bytes]):
        return cls.create_type(args=[], annots=[], literal=literal)

    @classmethod
    def as_micheline_expr(cls) -> dict:
        if isinstance(cls.literal, int):
            return {'int': str(cls.literal)}
        elif isinstance(cls.literal, str):
            return {'string': cls.literal}
        elif isinstance(cls.literal, bytes):
            return {'bytes': cls.literal.hex()}
        else:
            assert False, f'unexpected value `{cls.literal}`'

    @classmethod
    def get_int(cls) -> int:
        assert isinstance(cls.literal, int), f'expected int, got {cls.literal}'
        return cls.literal

    @classmethod
    def get_string(cls) -> str:
        assert isinstance(cls.literal, str), f'expected string, got {cls.literal}'
        return cls.literal

    @classmethod
    def get_bytes(cls) -> bytes:
        assert isinstance(cls.literal, bytes), f'expected bytes, got {cls.literal}'
        return cls.literal
