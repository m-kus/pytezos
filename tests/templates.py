michelson_coding_test_case = """from unittest import TestCase

from tests import get_data
from pytezos.michelson.micheline import micheline_to_michelson, michelson_to_micheline


class MichelsonCodingTest{case}(TestCase):
    
    def setUp(self):
        self.maxDiff = None
"""


test_michelson_parse = """
    def test_michelson_parse_{case}(self):
        expected = get_data(
            path='{json_path}')
        actual = michelson_to_micheline(get_data(
            path='{tz_path}'))
        self.assertEqual(expected, actual)
"""


test_michelson_format = """
    def test_michelson_format_{case}(self):
        expected = get_data(
            path='{tz_path}')
        actual = micheline_to_michelson(get_data(
            path='{json_path}'), 
            inline=True)
        self.assertEqual(expected, actual)
"""


test_michelson_inverse = """
    def test_michelson_inverse_{case}(self):
        expected = get_data(
            path='{json_path}')
        actual = michelson_to_micheline(micheline_to_michelson(expected))
        self.assertEqual(expected, actual)
"""


micheline_coding_test_case = """from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, encode_micheline, decode_micheline


class MichelineCodingTest{case}(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        code = get_data(
            path='{json_path}')
        cls.schema = dict(
            parameter=build_schema(code[0]),
            storage=build_schema(code[1])
        )
"""


test_micheline_inverse = """
    def test_micheline_inverse_{case}(self):
        expected = get_data(
            path='{json_path}')
        decoded = decode_micheline(expected, self.schema['{section}'])
        actual = encode_micheline(decoded, self.schema['{section}'])
        self.assertEqual(expected, actual)
"""


operation_forging_test_case = """from unittest import TestCase

from tests import get_data
from pytezos.operation.forge import forge_operation_group


class OperationForgingTest{case}(TestCase):

    def setUp(self):
        self.maxDiff = None
        
    def test_forge_{case}(self):
        expected = get_data(
            path='{hex_path}')
        actual = forge_operation_group(get_data(
            path='{json_path}'))
        self.assertEqual(expected, actual)
"""


big_map_test_case = """from unittest import TestCase

from tests import get_data
from pytezos.michelson.contract import ContractStorage


class BigMapCodingTest{case}(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_big_map_{case}(self):    
        section = get_data(
            path='{code_path}')
        storage = ContractStorage(section)
            
        big_map_diff = get_data(
            path='{diff_path}')
        expected = [
            dict(key=item['key'], value=item.get('value'))
            for item in big_map_diff
        ]
        
        big_map = storage.big_map_diff_decode(expected)
        actual = storage.big_map_diff_encode(big_map)
        self.assertEqual(expected, actual)
"""

opcode_test_case = """from unittest import TestCase

from tests import abspath

from pytezos.instructions.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.instructions.parser import parse_expression


class OpcodeTest{case}(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_{case}(self):
        res = self.i.execute(f'INCLUDE "{{abspath("{filename}")}}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN {parameter} {storage}')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('{expected}')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
"""

big_map_diff_test_case = """from unittest import TestCase

from tests import abspath

from pytezos.instructions.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.instructions.parser import parse_expression


class OpcodeTest{case}(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)

    def test_opcode_{case}(self):
        res = self.i.execute(f'INCLUDE "{{abspath("{filename}")}}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN {parameter} {storage}')
        self.assertTrue(res['success'])
        
        exp_val_expr = michelson_to_micheline('{expected}')
        exp_val = parse_expression(exp_val_expr, res['result']['storage'].type_expr)
        self.assertEqual(exp_val, res['result']['storage']._val)
        
        big_map_diff = {big_map_diff}
        self.assertCountEqual(big_map_diff, res['result']['big_map_diff'])
"""

success_test_case = """from unittest import TestCase

from tests import abspath

from pytezos.instructions.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.instructions.parser import parse_expression


class OpcodeTest{case}(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=False)  # disable exceptions

    def test_opcode_{case}(self):
        res = self.i.execute(f'INCLUDE "{{abspath("{filename}")}}"')
        self.assertTrue(res['success'])

        res = self.i.execute('RUN {parameter} {storage}')
        self.assertEqual({expected}, res['success'])
"""

storage_test_case = """from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline, micheline_to_michelson


class StorageTest{case}(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.contract = get_data('{path}')

    def test_storage_encoding_{case}(self):
        type_expr = self.contract['script']['code'][1]
        val_expr = self.contract['script']['storage']
        schema = build_schema(type_expr)
        decoded = decode_micheline(val_expr, type_expr, schema)
        actual = encode_micheline(decoded, schema)
        self.assertEqual(val_expr, actual)

    def test_storage_schema_{case}(self):
        _ = build_schema(self.contract['script']['code'][0])

    def test_storage_format_{case}(self):
        _ = micheline_to_michelson(self.contract['script']['code'])
        _ = micheline_to_michelson(self.contract['script']['storage'])
"""