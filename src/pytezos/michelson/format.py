import json
from datetime import datetime

from pytezos.logging import logger

line_size = 100


def format_timestamp(timestamp: int) -> str:
    """ Format unix timestamp.

    :param timestamp: Unix timestamp (seconds)
    """
    dt = datetime.utcfromtimestamp(timestamp)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


class MichelsonFormatterError(ValueError):
    pass


def is_framed(node):
    if node['prim'] in {'Pair', 'Left', 'Right', 'Some', 'pair', 'or', 'option', 'map', 'big_map', 'list', 'set',
                        'contract', 'lambda', 'ticket', 'sapling_state', 'sapling_transaction'}:
        return True
    elif node['prim'] in {'key', 'unit', 'signature', 'operation', 'int', 'nat', 'string', 'bytes', 'mutez', 'bool',
                          'key_hash', 'timestamp', 'address', 'bls12_381_g1', 'bls12_381_g2', 'bls12_381_fr',
                          'chain_id', 'never'}:
        return 'annots' in node
    return False


def is_complex(node):
    return node['prim'] == 'LAMBDA' \
           or node['prim'].startswith('IF')


def is_inline(node):
    return node['prim'] == 'PUSH'


def is_script(node):
    return all(map(
        lambda x: isinstance(x, dict) and x.get('prim') in ['parameter', 'storage', 'code'],
        node))


def format_node(node, indent='', inline=False, is_root=False, wrapped=False):
    if isinstance(node, list):
        is_script_root = is_root and is_script(node)
        seq_indent = indent if is_script_root else indent + ' ' * 2
        items = list(map(lambda x: format_node(x, seq_indent, inline, wrapped=True), node))
        if items:
            length = len(indent) + sum(map(len, items)) + 4
            space = '' if is_script_root else ' '
            if inline or length < line_size:
                seq = f'{space}; '.join(items)
            else:
                seq = f'{space};\n{seq_indent}'.join(items)
            return seq if is_script_root else f'{{ {seq} }}'
        else:
            return '{}'

    elif isinstance(node, dict):
        if node.get('prim'):
            expr = ' '.join([node['prim']] + node.get('annots', []))
            args = node.get('args', [])

            if is_complex(node):
                arg_indent = indent + ' ' * 2
                items = list(map(lambda x: format_node(x, arg_indent, inline), args))
                length = len(indent) + len(expr) + sum(map(len, items)) + len(items) + 1
                if inline or length < line_size:
                    expr = f'{expr} {" ".join(items)}'
                else:
                    expr = f'\n{arg_indent}'.join([expr] + items)

            elif len(args) == 1:
                arg_indent = indent + ' ' * (len(expr) + 1)
                expr = f'{expr} {format_node(args[0], arg_indent, inline)}'

            elif len(args) > 1:
                arg_indent = indent + ' ' * 2
                alt_indent = indent + ' ' * (len(expr) + 2)
                for arg in args:
                    item = format_node(arg, arg_indent, inline)
                    length = len(indent) + len(expr) + len(item) + 1
                    if inline or is_inline(node) or length < line_size:
                        arg_indent = alt_indent
                        expr = f'{expr} {item}'
                    else:
                        expr = f'{expr}\n{arg_indent}{item}'

            if is_framed(node) and not is_root and not wrapped:
                return f'({expr})'
            else:
                return expr
        else:
            core_type, value = next((k, v) for k, v in node.items() if k[0] != '_' and k != 'annots')
            if core_type == 'int':
                return value
            elif core_type == 'bytes':
                return f'0x{value}'
            elif core_type == 'string':
                return json.dumps(value)
            else:
                assert False, f'unexpected core node {node}'
    else:
        assert False, f'unexpected node {node}'


def micheline_to_michelson(data, inline=False, wrap=False) -> str:
    """ Converts micheline expression into formatted Michelson source.

    :param data: Micheline expression
    :param inline: produce single line, used for tezos-client arguments (False by default)
    :param wrap: ensure expression is wrapped in brackets
    """
    try:
        res = format_node(data, inline=inline, is_root=True)
        if wrap and any(map(res.startswith, ['Left', 'Right', 'Some', 'Pair'])):
            return f'({res})'
        else:
            return res
    except (KeyError, IndexError, TypeError) as e:
        logger.info(data, compact=True)
        raise MichelsonFormatterError(e.args)
