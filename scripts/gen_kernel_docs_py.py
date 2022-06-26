from os.path import dirname, join
from pprint import pprint

import requests
import yaml

target_path = join(dirname(dirname(__file__)), 'src', 'michelson_kernel', 'docs.py')
meta_url = 'https://gitlab.com/tezos/michelson-reference/-/raw/master/michelson_reference/michelson-meta.yaml'
sema_url = 'https://gitlab.com/tezos/michelson-reference/-/raw/master/michelson_reference/michelson.json'
extra = {'RENAME': '', 'CAST': '', 'TOP': '', 'EXPAND': ''}


def format_entry(title, concl, descr):
    res = [title]
    if isinstance(concl, list):
        for x in concl:
            res.append(x['conclusion'][7:])
    if descr:
        res.append(descr.replace('`', ''))
    else:
        return None
    return '\n'.join(res)


def generate():
    meta_src = requests.get(meta_url).text
    meta = yaml.load(meta_src, Loader=yaml.SafeLoader)
    sema = requests.get(sema_url).json()
    docs = extra.copy()

    for section in ['instructions', 'types']:
        args_key = {'instructions': 'op_args', 'types': 'ty_args'}[section]
        for primitive, body in meta[section].items():

            docs[primitive] = format_entry(
                title=sema[section].get(primitive, {}).get(args_key, ''),
                concl=sema[section].get(primitive, {}).get('ty', ''),
                descr=body.get('documentation_short'),
            )

    with open(target_path, 'w+') as f:
        f.write('docs = ')
        pprint(docs, stream=f, indent=4, width=120)


if __name__ == '__main__':
    generate()
