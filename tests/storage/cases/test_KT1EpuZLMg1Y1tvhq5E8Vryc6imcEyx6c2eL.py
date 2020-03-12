from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline, micheline_to_michelson


class StorageTestKT1EpuZLMg1Y1tvhq5E8Vryc6imcEyx6c2eL(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.contract = get_data('storage/carthagenet/KT1EpuZLMg1Y1tvhq5E8Vryc6imcEyx6c2eL.json')

    def test_storage_encoding_KT1EpuZLMg1Y1tvhq5E8Vryc6imcEyx6c2eL(self):
        type_expr = self.contract['script']['code'][1]
        val_expr = self.contract['script']['storage']
        schema = build_schema(type_expr)
        decoded = decode_micheline(val_expr, type_expr, schema)
        actual = encode_micheline(decoded, schema)
        self.assertEqual(val_expr, actual)

    def test_storage_schema_KT1EpuZLMg1Y1tvhq5E8Vryc6imcEyx6c2eL(self):
        _ = build_schema(self.contract['script']['code'][0])

    def test_storage_format_KT1EpuZLMg1Y1tvhq5E8Vryc6imcEyx6c2eL(self):
        _ = micheline_to_michelson(self.contract['script']['code'])
        _ = micheline_to_michelson(self.contract['script']['storage'])
