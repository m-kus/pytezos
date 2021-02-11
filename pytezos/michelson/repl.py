from typing import Tuple, List, Optional, Any

from pytezos.michelson.micheline import MichelsonRuntimeError, get_script_section
from pytezos.michelson.parse import MichelsonParser
from pytezos.context.impl import ExecutionContext
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.program import MichelsonProgram


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
            **kwargs
        )
        context.set_parameter_expr(get_script_section(dict(code=script), 'parameter'))
        context.set_storage_expr(get_script_section(dict(code=script), 'storage'))
        context.set_code_expr(get_script_section(dict(code=script), 'code'))
        stack = MichelsonStack()
        stdout = []
        try:
            program = MichelsonProgram.match(script)
            res = program.instantiate(
                entrypoint=entrypoint,
                parameter=parameter,
                storage=storage
            )
            res.begin(stack, stdout, context)
            res.execute(stack, stdout, context)
            operations, storage, lazy_diff = res.end(stack, stdout, output_mode=output_mode)
            return operations, storage, lazy_diff, stdout, None
        except MichelsonRuntimeError as e:
            stdout.append(e.format_stdout())
            return [], None, [], stdout, e
