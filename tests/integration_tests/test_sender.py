from unittest import TestCase, skip

from pytezos import ContractInterface

code = """
parameter unit;
storage address;
code { DROP ;
       SENDER ;
       NIL operation ;
       PAIR }
"""
initial = 'tz1h3rQ8wBxFd8L9B3d7Jhaawu6Z568XU3xY'
source = 'KT1WhouvVKZFH94VXj9pa8v4szvfrBwXoBUj'
sender = 'tz1irF8HUsQp2dLhKNMhteG1qALNU9g3pfdN'


class SenderContractTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ci = ContractInterface.from_michelson(code).using('mainnet')

    def test_sender(self):
        res = self.ci.default().run_code(storage=initial, source=source, sender=sender)
        self.assertEqual(sender, res.storage)

    def test_no_source(self):
        res = self.ci.default().run_code(storage=initial, sender=sender)
        self.assertEqual(sender, res.storage)

    def test_no_sender(self):
        res = self.ci.default().run_code(storage=initial, source=source)
        self.assertEqual(source, res.storage)
