import json
from os.path import dirname
from os.path import join
from unittest import TestCase

from parameterized import parameterized  # type: ignore

from pytezos import pytezos
from pytezos.operation.group import OperationGroup


class TestOperationForging(TestCase):
    @parameterized.expand(
        [
            ("ooFdR2Anyv7pHaehM2rK5DaUWaVv3wUkyR5mkm9u7Wd8jtQaXA9",),
            ("onewnQxJgwk384Bk6fuLmq7rFM5AePy2xLV1v475H4nog9Y9Haz",),
            ("onpsXDeuWpVH9oNd9XHDvUZMwekVrNS9rsdbp9f3LDbimLqZDrw",),
        ]
    )
    def test_operation_hash_is_correct(self, opg_hash):
        with open(join(dirname(__file__), 'data', f'{opg_hash}.json')) as f:
            data = json.loads(f.read())

        group = OperationGroup(
            context=pytezos.using('mumbainet').context,
            contents=data['contents'],
            chain_id=data['chain_id'],
            protocol=data['protocol'],
            branch=data['branch'],
            signature=data['signature'],
        )
        res = group.hash()
        self.assertEqual(opg_hash, res)
