from os.path import basename

from pytezos.michelson.micheline import Schema, is_optional

core_types = ['string', 'int', 'bool']
domain_types = {
    'nat': 'int  /* Natural number */',
    'unit': 'None /* Void */',
    'bytes': 'string  /* Hex string */ ||\n\tbytes  /* Python byte string */',
    'timestamp': 'int  /* Unix time in seconds */ ||\n\tstring  /* Formatted datetime `%Y-%m-%dT%H:%M:%SZ` */',
    'mutez': 'int  /* Amount in `utz` (10^-6) */ ||\n\tDecimal  /* Amount in `tz` */',
    'contract': 'string  /* Base58 encoded `KT` address */',
    'address': 'string  /* Base58 encoded `tz` or `KT` address */',
    'key': 'string  /* Base58 encoded public key */',
    'key_hash': 'string  /* Base58 encoded public key hash */',
    'signature': 'string  /* Base58 encoded signature */',
    'lambda': 'string  /* Michelson source code */'
}


def generate_docstring(schema: Schema, title, root='0'):
    docstring = list()
    known_types = set()

    def get_node(bin_path):
        return schema.metadata[bin_path]

    def get_name(bin_path):
        name = schema.bin_names.get(bin_path)
        if not name:
            name = next((basename(k) for k, v in schema.json_to_bin.items() if v == bin_path), bin_path)
        return name

    def get_type(bin_path):
        default = get_name(bin_path[:-1]) + '_item'
        return schema.metadata[bin_path].get('typename', default)

    def get_comment(bin_path):
        node = schema.metadata[bin_path]
        return node.get('typename', node.get('fieldname'))

    def decode_node(bin_path, is_element=False, is_entry=False):
        node = get_node(bin_path)
        bin_type = schema.bin_types[bin_path]

        def get_struct_name():
            if bin_path == root:
                struct_name = title
            elif is_element:
                struct_name = get_type(bin_path)
            else:
                struct_name = get_name(bin_path)
            return f'${struct_name}'

        if bin_type == 'router':
            entries = {get_name(x): decode_node(x, is_entry=True) for x in node['args']}
            doc = ' || \n\t'.join(map(lambda x: '{ ' + f'"{x[0]}": {x[1]}' + ' }', entries.items()))
            res = get_struct_name()
            docstring.insert(0, f'{res}:\n\t{doc}\n')
            return res

        elif bin_type == 'enum':
            res = ' || '.join(map(lambda x: f'"{get_name(x)}"', node['args']))

        elif bin_type == 'namedtuple':
            items = map(lambda x: (get_name(x), decode_node(x)), node['args'])
            lines = map(lambda x: f'  "{x[0]}": {x[1]}', items)
            doc = '\t{\n\t' + ',\n\t'.join(lines) + '\n\t}'
            res = get_struct_name()
            docstring.insert(0, f'{res}:\n{doc}\n')
            return res

        elif bin_type == 'tuple':
            values = map(decode_node, node['args'])
            res = f'[ {" , ".join(values)} ]'

        elif bin_type in {'keypair', 'pair'}:
            values = map(decode_node, node['args'])
            res = f'( {" , ".join(values)} )'

        elif bin_type in {'set', 'list'}:
            value = decode_node(node['args'][0], is_element=True)
            res = f'[ {value} , ... ]'

        elif bin_type in {'map', 'big_map'}:
            item = (decode_node(node['args'][0]), decode_node(node['args'][1], is_element=True))
            res = '{ ' + f'{item[0]} : {item[1]} , ...' + ' }'
            if bin_type == 'big_map':
                res += '  /* big_map */'

        else:
            res = node['prim']
            if res not in core_types:
                res = f'${res}'

            if is_entry:
                comment = get_comment(bin_path)
                if comment:
                    res = f'{res}  /* {comment} */'

            if node['prim'] in ['contract', 'lambda']:
                parameter = schema.metadata[bin_path]['parameter']
                res = f'{res} ({parameter})'

            if is_optional(schema, bin_path):
                res = f'None || {res}'

            if node['prim'] not in core_types:
                if bin_path == root:
                    res = domain_types[node["prim"]]
                else:
                    assert node['prim'] in domain_types, f'not a domain type {node["prim"]}'
                    known_types.add(node['prim'])

        if bin_path == root:
            docstring.insert(0, f'${title}:\n\t{res}\n')

        return res

    decode_node(root)

    for prim in known_types:
        docstring.append(f'${prim}:\n\t{domain_types[prim]}\n')

    return '\n'.join(docstring)
