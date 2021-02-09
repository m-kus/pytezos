from unittest import TestCase

from pytezos.michelson.types import TimestampType
from pytezos.michelson.parse import MichelsonParser


class TestParsing(TestCase):

    def test_wrapped_expr(self):
        p = MichelsonParser()
        p.parse('(Pair 1 2)')

    def test_unpair_single_annot(self):
        p = MichelsonParser()
        p.parse('UNPAIR @left')

    def test_timestamp_with_millis(self):
        res = TimestampType.from_micheline_value({'string': '2021-01-06T14:57:27.821Z'})
        self.assertEqual(1609945047, int(res))
