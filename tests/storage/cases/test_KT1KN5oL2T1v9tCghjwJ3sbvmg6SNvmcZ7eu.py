from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline, micheline_to_michelson


class StorageTestKT1KN5oL2T1v9tCghjwJ3sbvmg6SNvmcZ7eu(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.contract = get_data('storage/carthagenet/KT1KN5oL2T1v9tCghjwJ3sbvmg6SNvmcZ7eu.json')

    def test_storage_encoding_KT1KN5oL2T1v9tCghjwJ3sbvmg6SNvmcZ7eu(self):
        type_expr = self.contract['script']['code'][1]
        val_expr = self.contract['script']['storage']
        schema = build_schema(type_expr)
        decoded = decode_micheline(val_expr, type_expr, schema)
        actual = encode_micheline(decoded, schema)
        self.assertEqual(val_expr, actual)

    def test_storage_schema_KT1KN5oL2T1v9tCghjwJ3sbvmg6SNvmcZ7eu(self):
        _ = build_schema(self.contract['script']['code'][0])

    def test_storage_format_KT1KN5oL2T1v9tCghjwJ3sbvmg6SNvmcZ7eu(self):
        _ = micheline_to_michelson(self.contract['script']['code'])
        _ = micheline_to_michelson(self.contract['script']['storage'])
