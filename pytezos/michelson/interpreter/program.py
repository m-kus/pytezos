from typing import Type, cast

from pytezos.michelson.sections.parameter import ParameterSection
from pytezos.michelson.sections.storage import StorageSection
from pytezos.michelson.sections.code import CodeSection
from pytezos.michelson.micheline import MichelsonSequence


class MichelsonProgram:
    parameter: Type[ParameterSection]
    storage: Type[StorageSection]
    code: Type[CodeSection]

    @staticmethod
    def match(sequence: Type[MichelsonSequence]) -> Type['MichelsonProgram']:
        assert len(sequence.args) == 3, f'expected 3 sections, got {len(sequence.args)}'
        assert {arg.prim for arg in sequence.args} == {'parameter', 'storage', 'code'}, f'unexpected sections'
        parameter = next(arg for arg in sequence.args if issubclass(arg, ParameterSection))
        storage = next(arg for arg in sequence.args if issubclass(arg, StorageSection))
        code = next(arg for arg in sequence.args if issubclass(arg, CodeSection))
        cls = type(MichelsonProgram.__name__, (), dict(parameter=parameter, storage=storage, code=code))
        return cast(Type['MichelsonProgram'], cls)

    @classmethod
    def as_micheline_expr(cls):
        return [
            cls.parameter.as_micheline_expr(),
            cls.storage.as_micheline_expr(),
            cls.code.as_micheline_expr()
        ]
