from traceback import format_exception
from typing import Any, Dict, List, Optional, Tuple, cast

from ipykernel.kernelbase import Kernel  # type: ignore
from tabulate import tabulate

from michelson_kernel import __version__
from michelson_kernel.docs import docs
from pytezos import MichelsonType, micheline_to_michelson
from pytezos.michelson.instructions import BigMapDiffInstruction, CommitInstruction
from pytezos.michelson.instructions.base import MichelsonInstruction
from pytezos.michelson.micheline import MichelineSequence, MichelsonRuntimeError
from pytezos.michelson.parse import MichelsonParserError
from pytezos.michelson.repl import Interpreter
from pytezos.michelson.stack import MichelsonStack
from pytezos.michelson.tags import prim_tags
from pytezos.michelson.types import OperationType, PairType

static_macros = [
    'CMPEQ',
    'CMPNEQ',
    'CMPLT',
    'CMPGT',
    'CMPLE',
    'CMPGE',
    'IFEQ',
    'IFNEQ',
    'IFLT',
    'IFGT',
    'IFLE',
    'IFGE',
    'IFCMPEQ',
    'IFCMPNEQ',
    'IFCMPLT',
    'IFCMPGT',
    'IFCMPLE',
    'IFCMPGE',
    'FAIL',
    'ASSERT_EQ',
    'ASSERT_NEQ',
    'ASSERT_LT',
    'ASSERT_GT',
    'ASSERT_LE',
    'ASSERT_GE',
    'ASSERT_CMPEQ',
    'ASSERT_CMPNEQ',
    'ASSERT_CMPLT',
    'ASSERT_CMPGT',
    'ASSERT_CMPLE',
    'ASSERT_CMPGE',
    'ASSERT_NONE',
    'ASSERT_SOME',
    'ASSERT_LEFT',
    'ASSERT_RIGHT',
    'UNPAIR',
    'IF_SOME',
    'SET_CAR',
    'SET_CDR',
    'MAP_CAR',
    'MAP_CDR',
]


def parse_token(line: str, cursor_pos: int) -> Tuple[str, int, int]:

    begin_pos = next((i + 1 for i in range(cursor_pos - 1, 0, -1) if line[i] in ' ;({\n'), 0)
    end_pos = next((i for i in range(cursor_pos, len(line)) if line[i] in ' ;){\n'), len(line))
    return line[begin_pos:end_pos], begin_pos, end_pos


def preformat_operations_table(items: List[OperationType]) -> List[Dict[str, Any]]:
    return [
        {
            'type': item.prim,
            **item.content,
        }
        for item in items
    ]


def preformat_storage_table(item) -> List[Dict[str, Any]]:
    return [
        {
            'type': item.prim,
            'value': item.to_python_object(),
        }
    ]


def preformat_stack_table(items: List[MichelsonInstruction]) -> List[Dict[str, Any]]:
    return [
        {
            'index': i,
            'type': item.prim,
            # FIXME:
            'value': item.to_python_object(),  # type: ignore
        }
        for i, item in enumerate(items)
    ]


def html_table(table: List[Dict[str, Any]], header: str) -> str:
    def pre(s):
        return f'<pre style="text-align: left;">{s}</pre>'

    def pre_dict(d):
        return {k: pre(v) for k, v in d.items()}

    result = f'<h4>{header}</h4>'
    result += tabulate(list(map(pre_dict, table)), tablefmt='html', headers="keys")
    # NOTE: Tabulate escapes our <pre> tags
    result = result.replace('&lt;', '<').replace('&gt;', '>')
    return result


def plain_table(table: List[Dict[str, Any]], header: str) -> str:
    result = f'{header}\n'
    return result + tabulate(table, tablefmt='simple', headers='keys')


def preformat_lazy_diff_table(lazy_diff: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    table = []
    for diff in lazy_diff:
        _id = diff['id']
        diff = diff['diff']
        if diff['action'] == 'alloc':
            table.append(
                {
                    'id': _id,
                    'action': 'alloc',
                    'key': '',
                    'value': '',
                }
            )
        for update in diff['updates']:
            table.append(
                {
                    'id': _id,
                    'action': 'update',
                    'key': micheline_to_michelson(update['key']),
                    'value': micheline_to_michelson(update['value']),
                }
            )
    return table


class MichelsonKernel(Kernel):
    implementation = 'IMichelson'
    implementation_version = __version__
    language_info = {
        'name': 'Michelson',
        'mimetype': 'text/x-michelson',
        'file_extension': '.tz',
        'codemirror_mode': 'michelson',
    }
    banner = 'Michelson (Tezos VM language)'
    help_links = [
        'https://michelson.nomadic-labs.com/',
        'https://tezos.gitlab.io/whitedoc/michelson.html',
    ]

    def __init__(self, **kwargs):
        super(MichelsonKernel, self).__init__(**kwargs)
        self.interpreter = Interpreter()

    def _stdout(self, text: str) -> None:
        self.send_response(
            self.iopub_socket,
            'stream',
            {
                'name': 'stdout',
                'text': text,
            },
        )

    def _find_stack_items(self, instructions: MichelineSequence, stack: MichelsonStack) -> Optional[List[MichelsonInstruction]]:
        for operation in instructions.items[::-1]:
            items = getattr(operation, 'items', None)
            if isinstance(items, MichelineSequence):
                stack_items = self._find_stack_items(instructions, stack)
                if stack_items:
                    return stack_items
            if not isinstance(operation, MichelsonInstruction):
                continue
            if operation.stack_items_added:
                return cast(List[MichelsonInstruction], stack.items[-operation.stack_items_added :])
        return None

    def _find_lazy_diff(self, instructions: MichelineSequence) -> Optional[List[Dict[str, str]]]:
        for instruction in instructions.items[::-1]:
            if isinstance(instruction, CommitInstruction) and instruction.lazy_diff:
                return instruction.lazy_diff
            elif isinstance(instruction, BigMapDiffInstruction) and instruction.lazy_diff:
                return instruction.lazy_diff
        return None

    def _find_contract_result(self, instructions: MichelineSequence) -> Optional[PairType]:
        for instruction in instructions.items[::-1]:
            if isinstance(instruction, CommitInstruction):
                return instruction.result
        return None

    def _send_success_response(self, instructions: MichelineSequence, stack: MichelsonStack) -> Dict[str, Any]:
        plain, html = '', ''

        contract_result = self._find_contract_result(instructions)
        if contract_result:
            header = 'Operations'
            table = preformat_operations_table(cast(List[OperationType], contract_result.items[0]))
            plain += plain_table(table, header)
            html += html_table(table, header)

            header = 'Storage'
            table = preformat_storage_table(contract_result.items[1])
            plain += plain_table(table, header)
            html += html_table(table, header)

        modified_items = self._find_stack_items(instructions, stack)
        if modified_items is not None and not contract_result:
            header = 'Stack updates'
            table = preformat_stack_table(modified_items)
            plain += plain_table(table, header)
            html += html_table(table, header)

        lazy_diff = self._find_lazy_diff(instructions)
        if lazy_diff:
            header = 'BigMap diff'
            lazy_diff_table = preformat_lazy_diff_table(lazy_diff)
            plain += plain_table(lazy_diff_table, header)
            html += html_table(lazy_diff_table, header)

        result = {
            'data': {
                'text/plain': plain,
                'text/html': html,
            },
            'metadata': {},
            'execution_count': self.execution_count,
        }

        self.send_response(
            self.iopub_socket,
            'execute_result',
            result,
        )
        return result

    def _send_fail_response(self, error: Exception) -> Dict[str, Any]:
        if isinstance(error, (MichelsonParserError, MichelsonRuntimeError)):
            traceback = [error.format_stdout()]
        else:
            traceback = format_exception(error.__class__, error, None)
        result = {
            'status': 'error',
            'ename': error.__class__.__name__,
            'evalue': str(error),
            'traceback': traceback,
        }
        self.send_response(
            self.iopub_socket,
            'stream',
            {
                'name': 'stderr',
                'text': '\n'.join(traceback),
            },
        )
        return result

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):

        interpreter_result = self.interpreter.execute(code)

        if not silent and interpreter_result.stdout:
            self._stdout('\n'.join(interpreter_result.stdout))

        if not interpreter_result.error:
            if not silent:
                return self._send_success_response(interpreter_result.instructions, interpreter_result.stack)
        else:
            return self._send_fail_response(interpreter_result.error)
        return {}

    def do_complete(self, code, cursor_pos):
        token, begin_pos, end_pos = parse_token(code, cursor_pos)

        suggests = []
        for word_set in [prim_tags, static_macros]:
            for word in word_set:
                if word.startswith(token):
                    suggests.append(word)

        if suggests:
            res = {
                'matches': suggests,
                'cursor_start': begin_pos,
                'cursor_end': end_pos,
            }
        else:
            res = {
                'matches': [],
                'cursor_start': cursor_pos,
                'cursor_end': cursor_pos,
            }

        res['status'] = 'ok'
        return res

    def do_inspect(self, code, cursor_pos, detail_level=0):
        token, _, _ = parse_token(code, cursor_pos)
        docstring = docs.get(token)
        if docstring:
            res = {'found': True, 'data': {'text/plain': docstring}}
        else:
            res = {'found': False}

        res['status'] = 'ok'
        return res
