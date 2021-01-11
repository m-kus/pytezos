from os.path import dirname

from pytezos.micheline.types import get_name
from pytezos.micheline.formatter import micheline_to_michelson

core_types = ['string', 'int', 'bool']
domain_types = {
    'nat': 'int  /* Natural number */',
    'unit': 'Unit || None /* Void */',
    'bytes': 'string  /* Hex string */ ||\n\tbytes  /* Python byte string */',
    'timestamp': 'int  /* Unix time in seconds */ ||\n\tstring  /* Formatted datetime `%Y-%m-%dT%H:%M:%SZ` */',
    'mutez': 'int  /* Amount in `utz` (10^-6) */ ||\n\tDecimal  /* Amount in `tz` */',
    'contract': 'string  /* Base58 encoded `KT` address with optional entrypoint */',
    'address': 'string  /* Base58 encoded `tz` or `KT` address */',
    'key': 'string  /* Base58 encoded public key */',
    'key_hash': 'string  /* Base58 encoded public key hash */',
    'signature': 'string  /* Base58 encoded signature */',
    'lambda': 'string  /* Michelson source code */',
    'chain_id': 'string  /* Base58 encoded chain ID */'
}


def generate_pydoc(schema: dict, title, root_path='/') -> str:
    """ Describes an according PyObject for a Micheline type (of arbitrary complexity).

    :param schema: type schema
    :param title: pydoc title
    :param root_path: type path to the root element (default is '/')
    :returns: formatted text
    """
    pydoc = list()
    known_types = set()

    def parse_node(type_path, is_element=False, is_entry=False, michelson_field=None):
        node = schema[type_path]

        def get_type_name():
            if type_path == root_path:
                return f'${title}'
            elif node.get('name'):
                return f'{node["name"]}'
            else:
                parent_node = schema[dirname(type_path)]
                parent_name = parent_node.get('name', parent_node['prim'])
                postfix = '_item' if is_element else schema[type_path].get('idx', 0)
                return f'${parent_name}_{postfix}'

        if node['prim'] == 'union':
            assert len(node.get('names')) == len(node['args']), f'union has to be named'
            variants = [
                f'{{ "{node["names"][i]}": {parse_node(arg_path, is_entry=True)} }}'
                for i, arg_path in enumerate(node['args'])
            ]
            doc = ' || \n\t'.join(variants)
            res = get_type_name()
            pydoc.insert(0, f'{res}:\n\t{doc}\n')
            return res

        elif node['prim'] == 'enum':
            assert len(node.get('names')) == len(node['args']), f'enum has to be named'
            res = ' || '.join(map(lambda x: f'"{x}"', node['names']))

        elif node['prim'] == 'tuple':
            args = map(parse_node, node['args'])
            if len(node.get('names')) == len(node['args']):
                lines = [f'  "{node["names"][i]}": {arg}' for i, arg in enumerate(args)]
                doc = '\t{\n\t' + ',\n\t'.join(lines) + '\n\t}'
                res = get_type_name()
                pydoc.insert(0, f'{res}:\n{doc}\n')
                return res
            else:
                res = f'[ {" , ".join(args)} ]'

        elif node['prim'] in {'set', 'list'}:
            value = parse_node(node['args'][0], is_element=True)
            res = f'[ {value} , ... ]'

        elif node['prim'] in {'map', 'big_map'}:
            key = parse_node(node['args'][0])
            val = parse_node(node['args'][1], is_element=True)
            res = f'{{ {key} : {val} , ... }}'
            if node['prim'] == 'big_map':
                res += '  /* big_map */'

        elif node['prim'] == 'option':
            value = parse_node(node['args'][0])
            res = f'None || {value}'

        elif node['prim'] in {'contract', 'lambda'}:
            type_name = get_type_name()
            if michelson_field in node:
                field = micheline_to_michelson(node[michelson_field])
                if len(field) < 10:
                    res = field
                else:
                    res = f'{type_name}_{michelson_field}'
                    pydoc.insert(0, f'{res}:\n{field}\n')
                return res
            else:
                param = parse_node(type_path, michelson_field='param')
                if node['prim'] == 'lambda':
                    ret = parse_node(type_path, michelson_field='ret')
                    res = f'lambda ({param} -> {ret})'
                else:
                    res = f'contract ({param})'
                known_types.add(node['prim'])

        else:
            res = node['prim']
            if res not in core_types:
                res = f'${res}'

            if is_entry:
                comment = get_name(schema[type_path], prefixes=[':', '%'])
                if comment:
                    res = f'{res}  /* {comment} */'

            if node['prim'] not in core_types:
                if type_path == root_path:
                    res = domain_types.get(node["prim"], "undefined")
                else:
                    known_types.add(node['prim'])

        if type_path == root_path:
            pydoc.insert(0, f'${title}:\n\t{res}\n')
        return res

    parse_node(root_path)
    for prim in known_types:
        pydoc.append(f'${prim}:\n\t{domain_types.get(prim, "undefined")}\n')
    return '\n'.join(pydoc)
