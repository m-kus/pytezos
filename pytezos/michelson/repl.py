from typing import Tuple, List, Optional

from pytezos.michelson.micheline import MichelsonError, get_script_section
from pytezos.michelson.parse import MichelsonParser
from pytezos.context.repl import REPLContext
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.program import MichelsonProgram
from pytezos.michelson.types import OperationType
from pytezos.michelson.sections.storage import StorageSection


# def format_diff(diff: dict):
#     if diff['action'] == 'alloc':
#         return {'big_map': diff['big_map'],
#                 'action': diff['action'],
#                 'key': micheline_to_michelson(diff['key_type']),
#                 'value': micheline_to_michelson(diff['value_type'])}
#     elif diff['action'] == 'update':
#         return {'big_map': diff['big_map'],
#                 'action': diff['action'],
#                 'key': micheline_to_michelson(diff['key']),
#                 'value': micheline_to_michelson(diff['value']) if diff.get('value') else 'null'}
#     elif diff['action'] == 'copy':
#         return {'destination_big_map': diff['big_map'],
#                 'action': diff['action'],
#                 'value': diff['source_big_map']}
#     elif diff['action'] == 'remove':
#         return {'big_map': diff['big_map'],
#                 'action': diff['action']}
#     else:
#         assert False, diff['action']
#
#
# def format_content(content):
#     if content['kind'] == 'transaction':
#         return {'kind': content['kind'],
#                 'target': content['destination'],
#                 'amount': content['amount'],
#                 'entrypoint': content['parameters']['entrypoint'],
#                 'parameters': micheline_to_michelson(content['parameters']['value'])}
#     elif content['kind'] == 'origination':
#         res = {'kind': content['kind'],
#                'target': content['originated_contract'],
#                'amount': content['balance'],
#                'storage': micheline_to_michelson(content['script']['storage']),
#                'code': micheline_to_michelson(content['script']['code'])}
#         if content.get('delegate'):
#             res['delegate'] = content['delegate']
#         return res
#     elif content['kind'] == 'delegation':
#         return {'kind': content['kind'],
#                 'target': content['delegate']}
#     else:
#         assert False, content['kind']
#
#
# def format_result(result):
#     if result is None:
#         return None
#     kind = result['kind']
#     if kind == 'message':
#         return result
#     elif kind == 'big_map_diff':
#         return {'value': list(map(format_diff, result['big_map_diff'])), **result}
#     elif kind == 'code':
#         return {'value': micheline_to_michelson(result['code']), **result}
#     elif kind == 'stack':
#         return {'value': list(map(format_stack_item, result['stack'])), **result}
#     elif kind == 'output':
#         operations = [format_content(x.get('_content')) for x in result['operations'].val_expr]
#         storage = [format_stack_item(result['storage'])]
#         big_map_diff = list(map(format_diff, result['big_map_diff']))
#         return {'value': (operations, storage, big_map_diff), **result}
#     else:
#         assert False, kind
#
#
# def format_stderr(error):
#     ename = type(error).__name__
#     if isinstance(error, MichelsonRuntimeError):
#         evalue, traceback = error.message, 'at ' + ' -> '.join(error.trace)
#     elif isinstance(error, MichelsonParserError):
#         evalue, traceback = error.message, f'at line {error.line}, pos {error.pos}'
#     else:
#         evalue, traceback = pformat(error.args, compact=True), ''
#     return {'name': ename,
#             'value': evalue,
#             'trace': traceback}


class Interpreter:
    """ Michelson interpreter reimplemented in Python.
    Based on the following reference: https://tezos.gitlab.io/michelson-reference/
    """

    def __init__(self, debug=True):
        self.stack = MichelsonStack()
        self.context = REPLContext()
        self.parser = MichelsonParser(extra_primitives=[])
        self.debug = debug

    @staticmethod
    def run_code(parameter, storage, script, entrypoint='default',
                 amount=None, chain_id=None, source=None, sender=None, balance=None, block_id=None) \
            -> Tuple[List[OperationType], Optional[StorageSection], List[str], Optional[Exception]]:
        stack = MichelsonStack()
        stdout = []
        context = REPLContext(
            amount=amount,
            chain_id=chain_id,
            source=source,
            sender=sender,
            balance=balance,
            block_id=block_id
        )
        context.set_parameter_expr(get_script_section(dict(code=script), 'parameter'))
        context.set_storage_expr(get_script_section(dict(code=script), 'storage'))
        context.set_code_expr(get_script_section(dict(code=script), 'code'))

        try:
            program = MichelsonProgram.match(script)
            res = program.instantiate(
                entrypoint=entrypoint,
                parameter=parameter,
                storage=storage
            )
            res.begin(stack, stdout)
            res.execute(stack, stdout, context)
            operations, storage = res.end(stack, stdout)
            return operations, storage, stdout, None
        except MichelsonError as e:
            stdout.append(e.format_stderr())
            return [], None, stdout, e

    #
    # def execute(self, code):
    #     """ Execute Michelson instructions (note that stack is not cleared after execution).
    #
    #     :param code: Michelson source (any valid Michelson expression or special helpers)
    #     :returns: {"success": True|False, "stdout": "", "stderr": {}, "result": {"value": "", ...}}
    #     """
    #     int_res = {'success': False}
    #     stdout = []
    #
    #     try:
    #         code_expr = michelson_to_micheline(code, parser=self.parser)
    #         code_ast = MichelsonPrimitive.match(code_expr)
    #     except (MichelsonParserError, AssertionError) as e:
    #         if self.debug:
    #             raise e
    #         int_res['stderr'] = format_stderr(e)
    #         return int_res
    #
    #     backup = deepcopy(self.stack)
    #     try:
    #         res = code_ast.execute(self.stack, stdout, self.context)
    #         if res is None and self.ctx.pushed:
    #             res = {'kind': 'stack', 'stack': self.ctx.dump(count=1)}
    #
    #         int_res['result'] = format_result(res)
    #         int_res['stdout'] = format_stdout(stdout)
    #         int_res['success'] = True
    #         self.context.reset()
    #     except AssertionError as e:
    #         int_res['stderr'] = format_stderr(e)
    #         int_res['stdout'] = format_stdout(self.ctx.stdout)
    #         self.stack = backup
    #
    #         if self.debug:
    #             if int_res.get('stdout'):
    #                 print(int_res['stdout'])
    #             raise e
    #
    #     if self.debug:
    #         if int_res.get('stdout'):
    #             print(int_res['stdout'])
    #         if int_res.get('result'):
    #             print('RESULT: ' + pformat(int_res['result']))
    #
    #     return int_res
