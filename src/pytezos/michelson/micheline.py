from functools import wraps
from pprint import pformat
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Type, TypeVar, Union, cast, overload

from typing_extensions import Literal

from pytezos.michelson.forge import unforge_address, unforge_chain_id, unforge_micheline, unforge_public_key, unforge_signature
from pytezos.michelson.format import micheline_to_michelson


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
            raise MichelsonRuntimeError(*e.args) from e
    return wrapper


def try_catch(prim):
    def _catch(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                raise MichelsonRuntimeError(prim, *e.args) from e
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
    handler = handlers[(prim, len(args))]  # type: ignore
    return handler(args)


def parse_micheline_literal(val_expr, handlers: Dict[str, Callable]):
    assert isinstance(val_expr, dict), f'expected dict, got {pformat(val_expr)}'
    try:
        core_type, value = next((k, v) for k, v in val_expr.items() if k[0] != '_' and k != 'annots')
    except StopIteration as e:
        raise Exception(f'Can\'t parse literal `{val_expr}`') from e
    expected = ' or '.join(map(lambda x: f'`{x}`', handlers))
    if core_type not in handlers:
        raise Exception(f'Expected one of {expected}, got {core_type}')
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
        super().__init_subclass__(**kwargs)  # type: ignore
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

                # FIXME: We need entrypoint to be an argument
                if prim == 'RUN':
                    if annots:
                        args = [{'string': annots[0][1:]}] + args  # type: ignore
                        annots = []
                    else:
                        args = [{'string': 'default'}] + args  # type: ignore

                args_len = len(args)
                if (prim, args_len) not in Micheline.classes:
                    args_len = None  # type: ignore
                assert (prim, args_len) in Micheline.classes, f'unregistered primitive {prim} ({args_len} args)'
                cls = Micheline.classes[prim, args_len]
                try:
                    return cls.create_type(args=list(map(Micheline.match, args)), annots=annots)
                except Exception as e:
                    raise MichelsonRuntimeError(cls.prim, *e.args) from e
            else:
                literal = parse_micheline_literal(expr, {
                    'int': int,
                    'string': str,
                    'bytes': bytes.fromhex,
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
        return cast(Type['MichelsonPrimitive'], res)  # type: ignore

    @classmethod
    def assert_type_equal(cls, other: Type['Micheline'], path='', message=''):
        comment = f' [{message}]' if message else ''
        assert cls.prim == other.prim, f'expected {other.prim}, got {cls.prim} at `{path}`{comment}'
        assert len(cls.args) == len(other.args), \
            f'expected {len(other.args)} args, got {len(cls.args)} at `{path}`{comment}'
        for i, arg in enumerate(other.args):
            cls.args[i].assert_type_equal(arg, path=f'{path}/{i}', message=message)
        assert cls.literal == other.literal, \
            f'expected {other.literal}, got {cls.literal} at `{path}`{comment}'  # type: ignore

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
    def execute(cls, stack, stdout, context) -> 'Micheline':
        assert False, f'`execute` has to be explicitly defined'


MichelineT = TypeVar('MichelineT', bound=Micheline)


class MichelineSequence(Micheline):

    def __init__(self, items: List[Micheline]):
        super(MichelineSequence, self).__init__()
        self.items = items

    @classmethod
    def as_micheline_expr(cls) -> list:  # type: ignore
        return [arg.as_micheline_expr() for arg in cls.args]

    @classmethod
    def execute(cls, stack, stdout, context) -> Micheline:
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
        if not isinstance(cls.literal, int):
            raise TypeError(f'Expected int, got {cls.literal}')  # type: ignore
        return cls.literal

    @classmethod
    def get_string(cls) -> str:
        if not isinstance(cls.literal, str):
            raise TypeError(f'Expected str, got {cls.literal}')  # type: ignore
        return cls.literal

    @classmethod
    def get_bytes(cls) -> bytes:
        if not isinstance(cls.literal, bytes):
            raise TypeError(f'Expected bytes, got {cls.literal}')  # type: ignore
        return cls.literal


def validate_sections(sequence: Type[MichelineSequence], sections: Sequence[str]) -> None:
    if len(sequence.args) != len(sections):
        raise Exception(f'expected {len(sections)} sections, got {len(sequence.args)}')
    sequence_sections = {arg.prim for arg in sequence.args}
    if sequence_sections != set(sections):
        raise Exception(f'Unknown sections {sequence_sections}, expected: {sections}')


@overload
def get_script_section(sequence: Type[MichelineSequence], cls: None, name: str, required: Literal[True])\
        -> MichelineT:
    ...


@overload
def get_script_section(sequence: Type[MichelineSequence], cls: None, name: str, required: Literal[False])\
        -> Optional[MichelineT]:
    ...


@overload
def get_script_section(sequence: Type[MichelineSequence], cls: Type[MichelineT], name: None, required: Literal[True])\
        -> MichelineT:
    ...


@overload
def get_script_section(sequence: Type[MichelineSequence], cls: Type[MichelineT], name: None, required: Literal[False])\
        -> Optional[MichelineT]:
    ...


def get_script_section(sequence, cls=None, name=None, required=False):
    try:
        if cls:
            return next(arg for arg in sequence.args if issubclass(arg, cls))
        elif name:
            return next(arg for arg in sequence['code'] if arg['prim'] == name)
        else:
            raise Exception('Either `cls` or `name` must be specified')
    except StopIteration:
        if required:
            raise
    return None
