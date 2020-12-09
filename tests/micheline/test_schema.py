from unittest import TestCase
from tests import get_data
from pprint import pprint

from pytezos.micheline.schema import build_schema


class TestMichelineSchema(TestCase):

    def test_schema(self):
        src = get_data(path='contracts/KT199ibictE9LbQn1kWkhowdiZti6F9mFZQg/code_KT199i.json')
        schema = build_schema(src[0])
        pprint(schema)
