from typing import Type, List, Tuple, cast

from pytezos.michelson.sections.parameter import ParameterSection
from pytezos.michelson.micheline import MichelsonSequence
from pytezos.michelson.sections.storage import StorageSection
from pytezos.michelson.sections.code import CodeSection
from pytezos.context.base import NodeContext
from pytezos.michelson.types import PairType, OperationType, ListType
from pytezos.michelson.interpreter.stack import MichelsonStack
from pytezos.michelson.instructions.base import format_stdout, MichelsonInstruction


class MichelsonProgram:
    parameter: Type[ParameterSection]
    storage: Type[StorageSection]
    code: Type[CodeSection]

    def __init__(self, parameter: ParameterSection, storage: StorageSection):
        self.parameter_value = parameter
        self.storage_value = storage

    @staticmethod
    def load(context: NodeContext, with_code=False):
        parameter = ParameterSection.match(context.get_parameter_expr())
        storage = StorageSection.match(context.get_storage_expr())
        code = CodeSection.match(context.get_code_expr() if with_code else [])
        cls = type(MichelsonProgram.__name__, (), dict(parameter=parameter, storage=storage, code=code))
        return cast(Type['MichelsonProgram'], cls)

    @staticmethod
    def create(sequence: Type[MichelsonSequence]) -> Type['MichelsonProgram']:
        assert len(sequence.args) == 3, f'expected 3 sections, got {len(sequence.args)}'
        assert {arg.prim for arg in sequence.args} == {'parameter', 'storage', 'code'}, f'unexpected sections'
        parameter = next(arg for arg in sequence.args if issubclass(arg, ParameterSection))
        storage = next(arg for arg in sequence.args if issubclass(arg, StorageSection))
        code = next(arg for arg in sequence.args if issubclass(arg, CodeSection))
        cls = type(MichelsonProgram.__name__, (), dict(parameter=parameter, storage=storage, code=code))
        return cast(Type['MichelsonProgram'], cls)

    @staticmethod
    def match(expr) -> Type['MichelsonProgram']:
        seq = cast(Type[MichelsonSequence], MichelsonSequence.match(expr))
        return MichelsonProgram.create(seq)

    @classmethod
    def as_micheline_expr(cls):
        return [
            cls.parameter.as_micheline_expr(),
            cls.storage.as_micheline_expr(),
            cls.code.as_micheline_expr()
        ]

    @classmethod
    def from_micheline_value(cls, entrypoint: str, parameter, storage) -> 'MichelsonProgram':
        parameter_value = cls.parameter.from_parameters(dict(entrypoint=entrypoint, value=parameter))
        storage_value = cls.storage.from_micheline_value(storage)
        return cls(parameter_value, storage_value)

    def begin(self, stack: MichelsonStack, stdout: List[str]):
        res = PairType.from_comb_leaves([self.parameter_value.item, self.storage_value.item])
        stack.push(res)
        stdout.append(format_stdout('begin', [], [res]))

    def execute(self, stack: MichelsonStack, stdout: List[str], context: NodeContext) -> MichelsonInstruction:
        return self.code.execute(stack, stdout, context)

    def commit(self, stack: MichelsonStack, stdout: List[str]) -> Tuple[List[OperationType], StorageSection]:
        res = cast(PairType, stack.pop1())
        assert len(stack) == 0, f'stack is not empty: {repr(stack)}'
        assert isinstance(res, PairType), f'expected pair, got {res.prim}'
        operations, storage_value = res.items
        operations.assert_equal_types(ListType.create_type([OperationType]))
        storage_value.assert_equal_types(self.storage.args[0])
        stdout.append(format_stdout('commit', [res], []))
        return list(operations), StorageSection(storage_value)
