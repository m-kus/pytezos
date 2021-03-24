from copy import deepcopy
from typing import Any, List, Optional, Tuple, cast

from attr import dataclass

from pytezos.context.impl import ExecutionContext
from pytezos.michelson.micheline import MichelineSequence, MichelsonRuntimeError
from pytezos.michelson.parse import MichelsonParser, MichelsonParserError, michelson_to_micheline
from pytezos.michelson.program import MichelsonProgram, TztMichelsonProgram
from pytezos.michelson.sections import CodeSection
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.types import OperationType


@dataclass(kw_only=True)
class InterpreterResult:
    operations = None
    storage = None
    lazy_diff = None
    stdout: List[str]
    error: Optional[Exception] = None
    instructions: Optional[MichelineSequence] = None
    stack: Optional[MichelsonStack] = None


class Interpreter:
    """Michelson interpreter reimplemented in Python.
    Based on the following reference: https://tezos.gitlab.io/michelson-reference/
    """

    def __init__(
        self,
        extra_primitives: Optional[List[str]] = None,
        debug: bool = False,
    ):
        self.stack = MichelsonStack()
        self.context = ExecutionContext()
        self.context.debug = debug
        self.parser = MichelsonParser(debug=debug, extra_primitives=extra_primitives)

    def execute(self, code: str) -> InterpreterResult:
        """Execute some code preserving current context and stack"""
        result = InterpreterResult(stdout=[])
        stack_backup = deepcopy(self.stack)
        context_backup = deepcopy(self.context)

        try:
            code_section = CodeSection.match(michelson_to_micheline(code))
            instructions = code_section.args[0].execute(self.stack, result.stdout, self.context)
            result.instructions = cast(MichelineSequence, instructions)
            result.stack = self.stack
        except (MichelsonParserError, MichelsonRuntimeError) as e:
            if self.context.debug:
                raise

            self.stack = stack_backup
            self.context = context_backup
            result.stdout.append(e.format_stdout())
            result.error = e

        return result

    def reset(self) -> None:
        self.stack = MichelsonStack()
        self.context = ExecutionContext()

    @staticmethod
    def run_code(
        parameter,
        storage,
        script,
        entrypoint='default',
        output_mode='readable',
        amount=None,
        chain_id=None,
        source=None,
        sender=None,
        balance=None,
        block_id=None,
        **kwargs,
    ) -> Tuple[List[dict], Any, List[dict], List[str], Optional[Exception]]:
        context = ExecutionContext(
            amount=amount,
            chain_id=chain_id,
            source=source,
            sender=sender,
            balance=balance,
            block_id=block_id,
            script=dict(code=script),
            **kwargs,
        )
        stack = MichelsonStack()
        stdout = []  # type: ignore
        try:
            program = MichelsonProgram.load(context, with_code=True)
            res = program.instantiate(
                entrypoint=entrypoint,
                parameter=parameter,
                storage=storage,
            )
            res.begin(stack, stdout, context)
            res.execute(stack, stdout, context)
            operations, storage, lazy_diff, _ = res.end(stack, stdout, output_mode=output_mode)
            return operations, storage, lazy_diff, stdout, None
        except MichelsonRuntimeError as e:
            stdout.append(e.format_stdout())
            return [], None, [], stdout, e

    @staticmethod
    def run_view(
        entrypoint,
        parameter,
        storage,
        context: ExecutionContext,
    ) -> Tuple[Any, List[str], Optional[Exception]]:
        ctx = ExecutionContext(
            shell=context.shell,
            key=context.key,
            block_id=context.block_id,
            script=context.script,
            address=context.address,
        )
        stack = MichelsonStack()
        stdout = []  # type: ignore
        try:
            program = MichelsonProgram.load(ctx, with_code=True)
            res = program.instantiate(entrypoint=entrypoint, parameter=parameter, storage=storage)
            res.begin(stack, stdout, context)
            res.execute(stack, stdout, context)
            _, _, _, pair = res.end(stack, stdout)
            operations = cast(List[OperationType], list(pair.items[0]))
            if not len(operations) == 1:
                raise Exception('Multiple internal operations, not sure which one to pick')
            return operations[0].to_python_object(), stdout, None
        except MichelsonRuntimeError as e:
            stdout.append(e.format_stdout())
            return None, stdout, e

    @staticmethod
    def run_tzt(
        script,
        amount=None,
        chain_id=None,
        source=None,
        sender=None,
        balance=None,
        block_id=None,
        **kwargs,
    ) -> None:
        context = ExecutionContext(
            amount=amount,
            chain_id=chain_id,
            source=source,
            sender=sender,
            balance=balance,
            block_id=block_id,
            script=dict(code=script),
            tzt=True,
            **kwargs,
        )
        stack = MichelsonStack()
        stdout: List[str] = []

        program = TztMichelsonProgram.load(context, with_code=True)
        res = program.instantiate()
        res.fill_context(script, context)
        res.register_bigmaps(stack, stdout, context)
        res.begin(stack, stdout, context)
        res.execute(stack, stdout, context)
        res.end(stack, stdout, context)
