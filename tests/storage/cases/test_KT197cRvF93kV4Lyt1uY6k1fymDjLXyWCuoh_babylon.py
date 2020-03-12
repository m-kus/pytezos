from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline, micheline_to_michelson


class StorageTestKT197cRvF93kV4Lyt1uY6k1fymDjLXyWCuoh_babylon(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.contract = get_data('storage/mainnet/KT197cRvF93kV4Lyt1uY6k1fymDjLXyWCuoh_babylon.json')

    def test_storage_encoding_KT197cRvF93kV4Lyt1uY6k1fymDjLXyWCuoh_babylon(self):
        type_expr = self.contract['script']['code'][1]
        val_expr = self.contract['script']['storage']
        schema = build_schema(type_expr)
        decoded = decode_micheline(val_expr, type_expr, schema)
        actual = encode_micheline(decoded, schema)
        self.assertEqual(val_expr, actual)

    def test_storage_schema_KT197cRvF93kV4Lyt1uY6k1fymDjLXyWCuoh_babylon(self):
        _ = build_schema(self.contract['script']['code'][0])

    def test_storage_format_KT197cRvF93kV4Lyt1uY6k1fymDjLXyWCuoh_babylon(self):
        _ = micheline_to_michelson(self.contract['script']['code'])
        _ = micheline_to_michelson(self.contract['script']['storage'])
