import yaml
from copy import deepcopy
from pprint import pformat

from pytezos.michelson.grammar import MichelsonParser, MichelsonParserError
from pytezos.michelson.converter import michelson_to_micheline, micheline_to_michelson
from pytezos.repl.control import do_interpret, MichelsonRuntimeError
from pytezos.repl.helpers import *
from pytezos.repl.arithmetic import *
from pytezos.repl.structures import *
from pytezos.repl.blockchain import *


def get_content(obj: dict):
    content = obj.get('_content')
    if content:
        return format_content(content)
    return {}


def format_stack_item(item: StackItem):
    row = {}
    if isinstance(item, Operation):
        row['value'] = yaml.dump(get_content(item.val_expr)).rstrip('\n')
    elif isinstance(item, List) and item.val_type() == Operation:
        row['value'] = yaml.dump([get_content(x) for x in item.val_expr]).rstrip('\n')
    else:
        row['value'] = micheline_to_michelson(item.val_expr)

    row['type'] = micheline_to_michelson(item.type_expr)
    if item.name is not None:
        row['name'] = f'@{item.name}'

    return row


def format_diff(diff: dict):
    if diff['action'] == 'alloc':
        return {'big_map': diff['big_map'],
                'action': diff['action'],
                'key': micheline_to_michelson(diff['key_type']),
                'value': micheline_to_michelson(diff['value_type'])}
    elif diff['action'] == 'update':
        return {'big_map': diff['big_map'],
                'action': diff['action'],
                'key': micheline_to_michelson(diff['key']),
                'value': micheline_to_michelson(diff['value']) if diff.get('value') else 'null'}
    elif diff['action'] == 'copy':
        return {'destination_big_map': diff['big_map'],
                'action': diff['action'],
                'value': diff['source_big_map']}
    elif diff['action'] == 'remove':
        return {'big_map': diff['big_map'],
                'action': diff['action']}
    else:
        assert False, diff['action']


def format_content(content):
    if content['kind'] == 'transaction':
        return {'kind': content['kind'],
                'target': content['destination'],
                'amount': content['amount'],
                'entrypoint': content['parameters']['entrypoint'],
                'parameters': micheline_to_michelson(content['parameters']['value'])}
    elif content['kind'] == 'origination':
        res = {'kind': content['kind'],
               'target': content['originated_contract'],
               'amount': content['balance'],
               'storage': micheline_to_michelson(content['script']['storage']),
               'code': micheline_to_michelson(content['script']['code'])}
        if content.get('delegate'):
            res['delegate'] = content['delegate']
        return res
    elif content['kind'] == 'delegation':
        return {'kind': content['kind'],
                'target': content['delegate']}
    else:
        assert False, content['kind']


def format_stdout(items):
    newline = True
    depth = 0
    res = []

    def break_line():
        nonlocal newline
        nonlocal res
        if not newline:
            res.append('\n')
            newline = True

    for item in items:
        if item['action'] == 'begin':
            break_line()
            if item['prim'] not in ['parameter', 'storage', 'code', 'STORAGE', 'DUMP']:
                res.extend(['  ' * depth, item['prim'], ':'])
                depth += 1
                newline = False
        elif item['action'] == 'end':
            depth -= 1
            break_line()
        elif item['action'] in ['message', 'event']:
            res.append('  ' * depth if newline else ' ')
            res.extend([item['text'], ';'])
            newline = False
        else:
            assert False, item['action']

    res = ''.join(res).strip('\n')
    if '\n' not in res and all(map(lambda x: x['action'] != 'message', items)):
        return ''

    return res


def format_result(result):
    if result is None:
        return None
    kind = result['kind']
    if kind == 'message':
        return result
    elif kind == 'big_map_diff':
        return {'value': list(map(format_diff, result['big_map_diff'])), **result}
    elif kind == 'code':
        return {'value': micheline_to_michelson(result['code']), **result}
    elif kind == 'stack':
        return {'value': list(map(format_stack_item, result['stack'])), **result}
    elif kind == 'output':
        operations = [format_content(x.get('_content')) for x in result['operations'].val_expr]
        storage = [format_stack_item(result['storage'])]
        big_map_diff = list(map(format_diff, result['big_map_diff']))
        return {'value': (operations, storage, big_map_diff), **result}
    else:
        assert False, kind


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
                res = {'kind': 'stack', 'stack': self.ctx.dump(count=1)}

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
                print('RESULT: ' + pformat(int_res['result']))

        return int_res
