from unittest import TestCase, skip

from pytezos import pytezos


class TestInjection(TestCase):

    @skip
    def test_one(self):
        counter = pytezos.using('florencenet').contract('KT1ECSt8FzxAtHxoxi4xN1JwkKUbBe4TS9kz')
        res = counter.increment(1).send(min_confirmations=3)
