from copy import deepcopy
from pprint import pformat

from pytezos.michelson.grammar import MichelsonParser, MichelsonParserError
from pytezos.michelson.converter import michelson_to_micheline, micheline_to_michelson
from pytezos.repl.control import do_interpret, MichelsonRuntimeError
from pytezos.repl.helpers import *
from pytezos.repl.arithmetic import *
from pytezos.repl.structures import *
from pytezos.repl.blockchain import *


def format_stack_item(item: StackItem):
    row = {
        'value': micheline_to_michelson(item.val_expr),
        'type': micheline_to_michelson(item.type_expr)
    }
    if item.name is not None:
        row['name'] = item.name
    return row


def format_stdout(items):
    res = ''.join(items).lstrip('\n')
    return res if any(map(lambda x: x in res, ['\n', 'PRINT'])) else ''


def format_result(result):
    if result is None:
        return None
    elif isinstance(result, StackItem):
        return [format_stack_item(result)]
    elif isinstance(result, list):
        if len(result) > 0 and isinstance(result[0], StackItem):
            return list(map(format_stack_item, result))
    return result


def format_stderr(error):
    ename = type(error).__name__
    if isinstance(error, MichelsonRuntimeError):
        evalue, traceback = error.message, 'at ' + ' -> '.join(error.trace)
    elif isinstance(error, MichelsonParserError):
        evalue, traceback = error.message, f'at line {error.line}, pos {error.pos}'
    else:
        evalue, traceback = pformat(error.args, compact=True), ''
    return {'name': ename,
            'value': evalue,
            'trace': traceback}


class Interpreter:

    def __init__(self, debug=True):
        self.ctx = Context()
        self.parser = MichelsonParser(extra_primitives=helpers_prim)
        self.debug = debug

    def execute(self, code):
        int_res = {'success': False}

        try:
            code_expr = michelson_to_micheline(code, parser=self.parser)
        except MichelsonParserError as e:
            if self.debug:
                raise e
            int_res['stderr'] = format_stderr(e)
            return int_res

        backup = deepcopy(self.ctx)

        try:
            res = do_interpret(self.ctx, code_expr)
            if res is None and self.ctx.pushed:
                res = self.ctx.dump(count=1)

            int_res['result'] = format_result(res)
            int_res['stdout'] = format_stdout(self.ctx.stdout)
            int_res['success'] = True
            self.ctx.reset()
        except MichelsonRuntimeError as e:
            int_res['stderr'] = format_stderr(e)
            int_res['stdout'] = format_stdout(self.ctx.stdout)
            self.ctx = backup

            if self.debug:
                if int_res.get('stdout'):
                    print(int_res['stdout'])
                raise e

        if self.debug:
            if int_res.get('stdout'):
                print(int_res['stdout'])
            if int_res.get('result'):
                print('RETURN: ' + pformat(int_res['result']))

        return int_res
