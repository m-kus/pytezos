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
    """Result of running contract in interpreter"""

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
    ) -> None:
        self.stack = MichelsonStack()
        self.context = ExecutionContext()
        self.context.debug = debug
        self.parser = MichelsonParser(debug=debug, extra_primitives=extra_primitives)

    def execute(self, code: str) -> InterpreterResult:
        """Execute some code preserving current context and stack

        :param code: Michelson code
        """
        result = InterpreterResult(stdout=[])
        stack_backup = deepcopy(self.stack)
        context_backup = deepcopy(self.context)

        try:
            code_section = CodeSection.match(michelson_to_micheline(code))
            instructions = code_section.args[0].execute(self.stack, result.stdout, self.context)
            result.instructions = MichelineSequence([instructions])
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
        """Reset interpreter's stack and context"""
        self.stack = MichelsonStack()
        self.context = ExecutionContext()

    @staticmethod
    def run_code(
        parameter,
        storage,
        script: str,
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
        """Execute contract in interpreter

        :param parameter: parameter expression
        :param storage: storage expression
        :param script: contract's Michelson code
        :param entrypoint: contract entrypoint
        :param output_mode: one of readable/optimized/legacy_optimized
        :param amount: patch AMOUNT
        :param chain_id: patch CHAIN_ID
        :param source: patch SOURCE
        :param sender: patch SENDER
        :param balance: patch BALANCE
        :param block_id: set block ID
        """
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
        entrypoint: str,
        parameter,
        storage,
        context: ExecutionContext,
    ) -> Tuple[Any, Any, List[str], Optional[Exception]]:
        """Execute view of contract loaded in context

        :param entrypoint: contract entrypoint
        :param parameter: parameter section
        :param storage: storage section
        :param context: execution context
        :returns: [operations, storage, stdout, error]
        """
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
            storage = pair.items[1]
            return [op.to_python_object() for op in operations], storage.to_python_object(), stdout, None
        except MichelsonRuntimeError as e:
            stdout.append(e.format_stdout())
            return None, None, stdout, e

    @staticmethod
    def run_tzt(
        script: str,
        amount=None,
        chain_id=None,
        source=None,
        sender=None,
        balance=None,
        block_id=None,
        **kwargs,
    ) -> None:
        """Execute TZT test suite code

        :param script: test contract's Michelson code
        :param amount: patch AMOUNT
        :param chain_id: patch CHAIN_ID
        :param source: patch SOURCE
        :param sender: patch SENDER
        :param balance: patch BALANCE
        :param block_id: set block ID
        """
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
