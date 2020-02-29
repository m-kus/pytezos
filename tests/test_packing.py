from unittest import TestCase
from parameterized import parameterized

from pytezos.michelson.pack import get_key_hash


class TestPacking(TestCase):

    @parameterized.expand([
        ({"bytes": "000018896fcfc6690baefa9aedc6d759f9bf05727e8c"},
         {"prim": "address"},
         "expru2YV8AanTTUSV4K21P7X4DzbuWQFVk7NewDuP1A5uamffiiFA3"),
        ({"string": "tz1MsmYzmqxHs9trE1qQugZxxcLPqAXdQaX9"},
         {"prim": "address"},
         "expru2YV8AanTTUSV4K21P7X4DzbuWQFVk7NewDuP1A5uamffiiFA3"),
        ({"string": "Game one!"},
         {"prim": "string"},
         "exprtiRSZkLKYRess9GZ3ryb4cVQD36WLo2oysZBFxKTZ2jXqcHWGj"),
        ({"int": "505506"},
         {"prim": "int"},
         "exprufzwVGdAX7zG91UpiAkR2yVxEDE75tHD5YgSBmYMUx22teZTCM")
    ])
    def test_get_key_hash(self, val_expr, type_expr, expected):
        self.assertEqual(expected, get_key_hash(val_expr, type_expr))
