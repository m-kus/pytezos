from tests.templates import opcode_test_case
from os.path import dirname, join, exists, relpath
from os import mkdir
#
#
# def make_packing_tests():
#     proj_dir = dirname(dirname(__file__))
#     cases_dir = join(proj_dir, 'tests', 'opcodes', 'cases')
#     if not exists(cases_dir):
#         mkdir(cases_dir)
#
#     for i, (filename, storage, parameter, expected) in enumerate(parameterized_data):
#         case = filename.replace(".tz", f'_{i}')
#         body = opcode_test_case.format(
#             case=case,
#             filename=join('opcodes', 'contracts', filename),
#             parameter=wrap(parameter),
#             storage=wrap(storage),
#             expected=wrap(expected)
#         )
#         with open(join(cases_dir, f'test_{case}.py'), 'w+') as f:
#             f.write(body)
#
#
# if __name__ == '__main__':
#     make_opcode_tests()
