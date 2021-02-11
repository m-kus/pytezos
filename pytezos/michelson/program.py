from typing import Type, List, Tuple, cast, Any

from pytezos.michelson.sections.parameter import ParameterSection
from pytezos.michelson.micheline import MichelineSequence, try_catch
from pytezos.michelson.sections.storage import StorageSection
from pytezos.michelson.sections.code import CodeSection
from pytezos.context.abstract import AbstractContext
from pytezos.michelson.types import PairType, OperationType, ListType
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.instructions.base import format_stdout, MichelsonInstruction


class MichelsonProgram:
    parameter: Type[ParameterSection]
    storage: Type[StorageSection]
    code: Type[CodeSection]

    def __init__(self, entrypoint: str, parameter: ParameterSection, storage: StorageSection):
        self.entrypoint = entrypoint
        self.parameter_value = parameter
        self.storage_value = storage

    @staticmethod
    def load(context: AbstractContext, with_code=False):
        parameter = ParameterSection.match(context.get_parameter_expr())
        storage = StorageSection.match(context.get_storage_expr())
        code = CodeSection.match(context.get_code_expr() if with_code else [])
        cls = type(MichelsonProgram.__name__, (MichelsonProgram,), dict(parameter=parameter,
                                                                        storage=storage,
                                                                        code=code))
        return cast(Type['MichelsonProgram'], cls)

    @staticmethod
    def create(sequence: Type[MichelineSequence]) -> Type['MichelsonProgram']:
        assert len(sequence.args) == 3, f'expected 3 sections, got {len(sequence.args)}'
        assert {arg.prim for arg in sequence.args} == {'parameter', 'storage', 'code'}, f'unexpected sections'
        parameter = next(arg for arg in sequence.args if issubclass(arg, ParameterSection))
        storage = next(arg for arg in sequence.args if issubclass(arg, StorageSection))
        code = next(arg for arg in sequence.args if issubclass(arg, CodeSection))
        cls = type(MichelsonProgram.__name__, (MichelsonProgram,), dict(parameter=parameter,
                                                                        storage=storage,
                                                                        code=code))
        return cast(Type['MichelsonProgram'], cls)

    @staticmethod
    def match(expr) -> Type['MichelsonProgram']:
        seq = cast(Type[MichelineSequence], MichelineSequence.match(expr))
        assert issubclass(seq, MichelineSequence), f'expected sequence, got {seq.prim}'
        return MichelsonProgram.create(seq)

    @classmethod
    def as_micheline_expr(cls):
        return [
            cls.parameter.as_micheline_expr(),
            cls.storage.as_micheline_expr(),
            cls.code.as_micheline_expr()
        ]

    @classmethod
    def instantiate(cls, entrypoint: str, parameter, storage) -> 'MichelsonProgram':
        parameter_value = cls.parameter.from_parameters(dict(entrypoint=entrypoint, value=parameter))
        storage_value = cls.storage.from_micheline_value(storage)
        return cls(entrypoint, parameter_value, storage_value)

    @try_catch('BEGIN')
    def begin(self, stack: MichelsonStack, stdout: List[str], context: AbstractContext):
        self.parameter_value.attach_context(context)
        self.storage_value.attach_context(context)
        res = PairType.from_comb([self.parameter_value.item, self.storage_value.item])
        stack.push(res)
        stdout.append(format_stdout(f'BEGIN %{self.entrypoint}', [], [res]))

    def execute(self, stack: MichelsonStack, stdout: List[str], context: AbstractContext) -> MichelsonInstruction:
        return self.code.args[0].execute(stack, stdout, context)

    @try_catch('END')
    def end(self, stack: MichelsonStack, stdout: List[str], output_mode='readable') -> Tuple[List[dict], Any, List[dict]]:
        res = cast(PairType, stack.pop1())
        assert len(stack) == 0, f'stack is not empty: {repr(stack)}'
        res.assert_type_equal(PairType.create_type(args=[
            ListType.create_type([OperationType]),
            self.storage.args[0]
        ]), message='list of operations + resulting storage')
        operations = [op.to_python_object() for op in res.items[0]]
        lazy_diff = []
        storage = res.items[1].aggregate_lazy_diff(lazy_diff).to_micheline_value(mode=output_mode)
        stdout.append(format_stdout(f'END %{self.entrypoint}', [res], []))
        return operations, storage, lazy_diff
