from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import cast
from typing import overload

from pytezos.context.abstract import AbstractContext
from pytezos.michelson.instructions.base import MichelsonInstruction
from pytezos.michelson.instructions.base import format_stdout
from pytezos.michelson.instructions.tzt import StackEltInstruction
from pytezos.michelson.micheline import Micheline
from pytezos.michelson.micheline import MichelineSequence
from pytezos.michelson.micheline import get_script_section
from pytezos.michelson.micheline import try_catch
from pytezos.michelson.micheline import validate_sections
from pytezos.michelson.sections.code import CodeSection
from pytezos.michelson.sections.parameter import ParameterSection
from pytezos.michelson.sections.storage import StorageSection
from pytezos.michelson.sections.tzt import InputSection
from pytezos.michelson.sections.tzt import OutputSection
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import ListType
from pytezos.michelson.types import OperationType
from pytezos.michelson.types import PairType


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
        cls = type(
            MichelsonProgram.__name__,
            (MichelsonProgram,),
            dict(
                parameter=ParameterSection.match(context.get_parameter_expr()),
                storage=StorageSection.match(context.get_storage_expr()),
                code=CodeSection.match(context.get_code_expr() if with_code else []),
            ),
        )
        return cast(Type['MichelsonProgram'], cls)

    @staticmethod
    def create(sequence: Type[MichelineSequence]) -> Type['MichelsonProgram']:
        validate_sections(sequence, ('parameter', 'storage', 'code'))
        cls = type(
            MichelsonProgram.__name__,
            (MichelsonProgram,),
            dict(
                parameter=get_script_section(sequence, cls=ParameterSection, required=True),  # type: ignore
                storage=get_script_section(sequence, cls=StorageSection, required=True),  # type: ignore
                code=get_script_section(sequence, cls=CodeSection, required=True),  # type: ignore
            ),
        )
        return cast(Type['MichelsonProgram'], cls)

    @staticmethod
    def match(expr) -> Type['MichelsonProgram']:
        seq = cast(Type[MichelineSequence], MichelineSequence.match(expr))
        if not issubclass(seq, MichelineSequence):
            raise Exception(f'Expected sequence, got {seq.prim}')
        return MichelsonProgram.create(seq)

    @classmethod
    def as_micheline_expr(cls):
        return [
            cls.parameter.as_micheline_expr(),
            cls.storage.as_micheline_expr(),
            cls.code.as_micheline_expr(),
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
    def end(self, stack: MichelsonStack, stdout: List[str], output_mode='readable') -> Tuple[List[dict], Any, List[dict], PairType]:
        res = cast(PairType, stack.pop1())
        if len(stack):
            raise Exception(f'Stack is not empty: {repr(stack)}')
        res.assert_type_equal(
            PairType.create_type(
                args=[ListType.create_type(args=[OperationType]), self.storage.args[0]],
            ),
            message='list of operations + resulting storage',
        )
        operations = [op.content for op in res.items[0]]  # type: ignore
        lazy_diff = []  # type: ignore
        storage = res.items[1].aggregate_lazy_diff(lazy_diff).to_micheline_value(mode=output_mode)
        stdout.append(format_stdout(f'END %{self.entrypoint}', [res], []))
        return operations, storage, lazy_diff, res


class TztMichelsonProgram:
    code: Type[CodeSection]
    input: Type[InputSection]
    output: Type[OutputSection]

    @staticmethod
    def load(context: AbstractContext, with_code=False):
        cls = type(
            TztMichelsonProgram.__name__,
            (TztMichelsonProgram,),
            dict(
                input=InputSection.match(context.get_input_expr()),
                output=OutputSection.match(context.get_output_expr()),
                code=CodeSection.match(context.get_code_expr() if with_code else []),
            ),
        )
        return cast(Type['TztMichelsonProgram'], cls)

    @staticmethod
    def create(sequence: Type[MichelineSequence]) -> Type['TztMichelsonProgram']:
        validate_sections(sequence, ('input', 'output', 'code'))
        cls = type(
            TztMichelsonProgram.__name__,
            (TztMichelsonProgram,),
            dict(
                input=get_script_section(sequence, cls=InputSection, required=True),  # type: ignore
                output=get_script_section(sequence, cls=OutputSection, required=True),  # type: ignore
                code=get_script_section(sequence, cls=CodeSection, required=True),  # type: ignore
            ),
        )
        return cast(Type['TztMichelsonProgram'], cls)

    @staticmethod
    def match(expr) -> Type['TztMichelsonProgram']:
        seq = cast(Type[MichelineSequence], MichelineSequence.match(expr))
        if not issubclass(seq, MichelineSequence):
            raise Exception(f'expected sequence, got {seq.prim}')
        return TztMichelsonProgram.create(seq)

    @classmethod
    def as_micheline_expr(cls):
        # TODO: Serialize all sections
        return [
            cls.code.as_micheline_expr(),
            cls.input.as_micheline_expr(),
            cls.output.as_micheline_expr(),
        ]

    @classmethod
    def instantiate(cls) -> 'TztMichelsonProgram':
        return cls()

    def fill_context(self, context: AbstractContext) -> None:
        raise NotImplementedError

    def begin(self, stack: MichelsonStack, stdout: List[str], context: AbstractContext):  # pylint: disable=no-self-use
        for item in self.input.args[0].args[::-1]:
            cast(StackEltInstruction, item).push(stack, stdout, context)

    def execute(self, stack: MichelsonStack, stdout: List[str], context: AbstractContext) -> MichelsonInstruction:
        return self.code.args[0].execute(stack, stdout, context)

    def end(self, stack: MichelsonStack, stdout: List[str]) -> None:
        for item in self.output.args[0].args:
            cast(StackEltInstruction, item).pull(stack, stdout)

        if len(stack):
            raise Exception('Stack is not empty after processing `output` section')
