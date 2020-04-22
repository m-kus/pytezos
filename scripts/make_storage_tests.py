from tests.templates import storage_test_case
from os.path import dirname, join, exists, basename
from os import mkdir
from glob import glob


def make_storage_tests():
    proj_dir = dirname(dirname(__file__))
    cases_dir = join(proj_dir, 'tests', 'storage', 'cases')
    if not exists(cases_dir):
        mkdir(cases_dir)

    for filename in glob(join(proj_dir, 'tests', 'storage/**/*.json')):
        case = basename(filename).replace(".json", '')
        body = storage_test_case.format(
            case=case,
            path=join(*filename.split('/')[-3:])
        )
        with open(join(cases_dir, f'test_{case}.py'), 'w+') as f:
            f.write(body)


if __name__ == '__main__':
    make_storage_tests()
