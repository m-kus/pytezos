import logging
from unittest import TestCase, skip

from pytezos import pytezos

logging.basicConfig(level=logging.INFO)


class TestInjection(TestCase):

    @skip
    def test_one(self):
        counter = pytezos.using('florencenet').contract('KT1ECSt8FzxAtHxoxi4xN1JwkKUbBe4TS9kz')
        res = counter.increment(1).send(min_confirmations=3)

    @skip
    def test_batch(self):
        operations = [
            pytezos.transaction(destination=pytezos.key.public_key_hash(), amount=1)
            for _ in range(41)
        ]
        res = pytezos.bulk(*operations).send(ttl=60, min_confirmations=1)
