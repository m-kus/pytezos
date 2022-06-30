import json
from collections import defaultdict
from os.path import dirname
from os.path import join
from typing import Dict

from pytezos import pytezos

no_descr = '¯\\_(ツ)_/¯'


def parse_describe_output(data, root='/'):
    info = defaultdict(dict)  # type: Dict[str, dict]

    def parse_node(node, path):
        assert isinstance(node, dict), node
        if 'static' in node:
            for k, v in node['static'].items():
                if k.endswith('service'):
                    info[path][v['meth']] = {
                        'descr': v.get('description', no_descr),
                        'args': [
                            {
                                'name': arg['name'],
                                'descr': arg.get('description', no_descr),
                            }
                            for arg in v.get('query', [])
                        ],
                        'ret': v['output']['json_schema'].get('type', 'object').capitalize(),
                    }
                elif k == 'subdirs':
                    if 'dynamic_dispatch' in v:
                        arg = v['dynamic_dispatch']['arg']
                        info[path]['item'] = {
                            'name': arg['name'],
                            'descr': arg.get('descr', no_descr),
                        }
                        parse_node(v['dynamic_dispatch']['tree'], join(path, '{}'))
                    if 'suffixes' in v:
                        info[path]['props'] = list(map(lambda x: x['name'], v['suffixes']))
                        for suffix in v['suffixes']:
                            parse_node(suffix['tree'], join(path, suffix['name']))
                else:
                    raise AssertionError()
        elif 'dynamic' in node:
            pass
        else:
            raise AssertionError(node)

    parse_node(data, root)
    return info


if __name__ == '__main__':
    shell_docs = parse_describe_output(pytezos.shell.describe(recurse=True))
    chain_docs = parse_describe_output(
        pytezos.shell.describe.chains.main.mempool(recurse=True),
        root='/chains/{}/mempool',
    )
    block_docs = parse_describe_output(
        pytezos.shell.describe.chains.main.blocks.head(recurse=True),
        root='/chains/{}/blocks/{}',
    )
    context_docs = parse_describe_output(
        pytezos.shell.describe.chains.main.blocks.head.context.raw.json(recurse=True),
        root='/chains/{}/blocks/{}/context/raw/json',
    )
    docs = json.dumps({**shell_docs, **chain_docs, **block_docs, **context_docs}, indent=2)
    output_path = join(dirname(dirname(__file__)), 'src/pytezos/rpc/docs.py')
    with open(output_path, 'w+') as f:
        f.write(f'rpc_docs = {docs}\n')
