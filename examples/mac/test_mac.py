from os.path import dirname, join
from unittest import TestCase

from pytezos import pytezos, ContractInterface

initial_storage = {
    'admin': {
        'admin': pytezos.key.public_key_hash(),
        'paused': False
    },
    'assets': {
        'hook': {
            'hook': '{ UNIT ; FAILWITH }',
            'permissions_descriptor': {
                'custom': {
                    'config_api': None,
                    'tag': 'none'
                },
                'operator': 'operator_transfer_permitted',
                'receiver': 'optional_owner_hook',
                'self': 'self_transfer_permitted',
                'sender': 'optional_owner_hook'
            }
        },
        'ledger': {},
        'operators': {},
        'tokens': {}
    }
}


class TestMac(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mac = ContractInterface.create_from(join(dirname(__file__), 'mac.tz'))
        cls.maxDiff = None

    def test_pause(self):
        res = self.mac.pause(True).interpret(
            storage=initial_storage,
            source=pytezos.key.public_key_hash(),
            sender=pytezos.key.public_key_hash())
        self.assertTrue(res.storage['admin']['paused'])

    def test_is_operator_callback(self):
        res = self.mac.is_operator(callback='KT1V4jijVy1HfVWde6HBVD1cCygZDtFJK4Xz',  # does not matter
                                   operator={
                                       'operator': pytezos.key.public_key_hash(),
                                       'owner': pytezos.key.public_key_hash(),
                                       'tokens': {'all_tokens': None}
                                   }) \
            .interpret(storage=initial_storage)
        self.assertEqual(1, len(res.operations))
