from pprint import pprint
from collections import namedtuple

from pytezos.michelson.forge import prim_tags
from pytezos.michelson.micheline import Schema, collapse_micheline, build_maps, parse_micheline, \
    parse_json, make_micheline, michelson_to_micheline
from pytezos.michelson.formatter import micheline_to_michelson
from pytezos.michelson.docstring import generate_docstring

BigMapSchema = namedtuple('BigMapSchema', ['bin_to_id', 'id_to_bin'])


class MichelineSchemaError(ValueError):
    pass


def build_schema(code) -> Schema:
    """
    Creates internal structures necessary for decoding/encoding micheline:
    `metadata` -> micheline tree with collapsed `pair`, `or`, and `option` nodes
    `bin_types` -> maps binary path to primitive
    `bin_names` -> binary path to key name mapping
    `json_to_bin` -> json path to binary path mapping
    :param code: parameter or storage section of smart contract source code (in micheline)
    :return: Schema
    """
    try:
        metadata = collapse_micheline(code)
        return Schema(metadata, *build_maps(metadata))
    except (KeyError, ValueError, TypeError) as e:
        pprint(code, compact=True)
        raise MichelineSchemaError(f'Failed to build schema', e.args)


def decode_micheline(val_expr, type_expr, schema: Schema, root='0'):
    """
    Converts Micheline data into Python object
    :param val_expr: Micheline value expression
    :param type_expr: Michelson type expression for the entire type
    :param schema: schema built for particular contract/section
    :param root: which binary node to take as root, used to decode BigMap values/diffs
    :return: Object
    """
    try:
        return parse_micheline(val_expr, type_expr, schema, root)
    except (KeyError, IndexError, TypeError) as e:
        print(generate_docstring(schema, 'schema'))
        pprint(val_expr, compact=True)
        raise MichelineSchemaError(f'Failed to decode micheline expression', e.args)


def encode_micheline(data, schema: Schema, root='0', binary=False):
    """
    Converts Python object into Micheline expression
    :param data: Python object
    :param schema: schema built for particular contract/section
    :param root: which binary node to take as root, used to encode BigMap values
    :param binary: Encode keys and addresses in bytes rather than strings, default is False
    :return: Micheline expression
    """
    try:
        bin_values = parse_json(data, schema, root)
        return make_micheline(bin_values, schema.bin_types, root, binary)
    except (KeyError, IndexError, TypeError) as e:
        print(generate_docstring(schema, 'schema'))
        pprint(data, compact=True)
        raise MichelineSchemaError(f'Failed to encode micheline expression', e.args)


def convert(source, schema: Schema = None, output='micheline', inline=False):
    """
    Convert data between different representations (DO NOT USE FOR STORAGE/PARAMETER, can be ambiguous)
    :param source: Data, can be one of Michelson (string), Micheline expression, object
    :param schema: Needed if decoding/encoding objects (optional)
    :param output: Output format, one of 'micheline' (default), 'michelson', 'object'
    :param inline: Used for michelson output, whether to omit line breaks
    """
    if isinstance(source, str):
        try:
            source = michelson_to_micheline(source)
        except ValueError:
            assert schema
            source = encode_micheline(source, schema)
    elif not is_micheline(source):
        assert schema
        source = encode_micheline(source, schema)

    if output == 'michelson':
        return micheline_to_michelson(source, inline)
    elif output == 'object':
        assert False, f'not supported'
    elif output == 'micheline':
        return source
    else:
        assert False, output


def build_big_map_schema(data, schema: Schema) -> BigMapSchema:
    bin_to_id = dict()
    id_to_bin = dict()

    def scan_big_map_ids(node, path):
        if len(path) == 0:
            assert node.get('int'), (node, path)
            yield int(node['int'])
        elif isinstance(node, list):
            for item in node:
                yield from scan_big_map_ids(item, path)
        else:
            assert node.get('args'), (node, path)
            yield from scan_big_map_ids(node['args'][int(path[0])], path[1:])

    for bin_path, prim in schema.bin_types.items():
        if prim == 'big_map':
            for big_map_id in scan_big_map_ids(data, bin_path[1:]):
                bin_to_id[bin_path], id_to_bin[big_map_id] = big_map_id, bin_path

    return BigMapSchema(bin_to_id, id_to_bin)


def is_micheline(value):
    if isinstance(value, list):
        def get_prim(x):
            return x.get('prim') if isinstance(x, dict) else None
        return set(map(get_prim, value)) == {'parameter', 'storage', 'code'}
    elif isinstance(value, dict):
        primitives = list(prim_tags.keys())
        return any(map(lambda x: x in value, ['prim', 'args', 'annots', *primitives]))
    else:
        return False
