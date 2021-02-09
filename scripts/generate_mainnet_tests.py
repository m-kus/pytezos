from os.path import join, dirname, isdir, basename, splitext, exists
from glob import glob

base_dir = join(dirname(dirname(__file__)), 'tests', 'mainnet')


def read_template(name):
    with open(join(base_dir, f'{name}.py')) as f:
        return f.read()


contract_test_case_template = read_template('test_contract_template')
operation_test_case_template = read_template('test_operation_template')


def generate_contract_test_case(folder):
    cid = folder[3:9].lower() if folder.startswith('KT1') else folder
    with open(join(base_dir, folder, f'test_{cid}.py'), 'w+') as f:
        res = contract_test_case_template \
            .replace('{folder}', '') \
            .replace('_template', f'_{cid}') \
            .replace('Template', cid.upper())
        f.write(res)


def generate_operation_test_case(folder, entrypoint):
    cid = folder[3:9].lower() if folder.startswith('KT1') else folder
    with open(join(base_dir, folder, f'test_{cid}_{entrypoint}.py'), 'w+') as f:
        res = operation_test_case_template \
            .replace('{folder}', '') \
            .replace('{entrypoint}', entrypoint) \
            .replace('_template', f'_{cid}') \
            .replace('Template', cid.upper())
        f.write(res)


def write_init_file(folder):
    path = join(base_dir, folder, '__init__.py')
    if not exists(path):
        with open(path, 'w+') as f:
            f.write('')


if __name__ == '__main__':
    for case_dir in glob(join(base_dir, '*')):
        if isdir(case_dir):
            folder = basename(case_dir)
            write_init_file(folder)
            generate_contract_test_case(folder)
            for file in glob(join(case_dir, '*.json')):
                filename, _ = splitext(basename(file))
                if not filename.startswith('__'):
                    generate_operation_test_case(folder, filename)
