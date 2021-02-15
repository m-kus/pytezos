from typing import Tuple, List, Optional, Any, cast

from pytezos.michelson.micheline import MichelsonRuntimeError
from pytezos.michelson.parse import MichelsonParser
from pytezos.context.impl import ExecutionContext
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.program import MichelsonProgram
from pytezos.michelson.types import OperationType


class Interpreter:
    """ Michelson interpreter reimplemented in Python.
    Based on the following reference: https://tezos.gitlab.io/michelson-reference/
    """

    def __init__(self, debug=True):
        self.stack = MichelsonStack()
        self.context = ExecutionContext()
        self.parser = MichelsonParser(extra_primitives=[])
        self.debug = debug

    @staticmethod
    def run_code(parameter, storage, script, entrypoint='default', output_mode='readable',
                 amount=None, chain_id=None, source=None, sender=None, balance=None, block_id=None, **kwargs) \
            -> Tuple[List[dict], Any, List[dict], List[str], Optional[Exception]]:
        context = ExecutionContext(
            amount=amount,
            chain_id=chain_id,
            source=source,
            sender=sender,
            balance=balance,
            block_id=block_id,
            script=dict(code=script),
            **kwargs
        )
        stack = MichelsonStack()
        stdout = []
        try:
            program = MichelsonProgram.load(context, with_code=True)
            res = program.instantiate(
                entrypoint=entrypoint,
                parameter=parameter,
                storage=storage
            )
            res.begin(stack, stdout, context)
            res.execute(stack, stdout, context)
            operations, storage, lazy_diff, _ = res.end(stack, stdout, output_mode=output_mode)
            return operations, storage, lazy_diff, stdout, None
        except MichelsonRuntimeError as e:
            stdout.append(e.format_stdout())
            return [], None, [], stdout, e

    @staticmethod
    def run_view(entrypoint, parameter, storage, context: ExecutionContext) \
            -> Tuple[Any, List[str], Optional[Exception]]:
        ctx = ExecutionContext(
            shell=context.shell,
            key=context.key,
            block_id=context.block_id,
            script=context.script,
            address=context.address
        )
        stack = MichelsonStack()
        stdout = []
        try:
            program = MichelsonProgram.load(ctx, with_code=True)
            res = program.instantiate(
                entrypoint=entrypoint,
                parameter=parameter,
                storage=storage
            )
            res.begin(stack, stdout, context)
            res.execute(stack, stdout, context)
            _, _, _, pair = res.end(stack, stdout)
            operations = cast(List[OperationType], list(pair.items[0]))
            assert len(operations) == 1, f'multiple internal operations, not sure which one to pick'
            return operations[0].to_python_object(), stdout, None
        except MichelsonRuntimeError as e:
            stdout.append(e.format_stdout())
            return None, stdout, e
