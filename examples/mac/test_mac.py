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
            'hook': """
                { DROP ;
                  PUSH address "KT1V4jijVy1HfVWde6HBVD1cCygZDtFJK4Xz" ; 
                  CONTRACT (pair
                             (pair
                               (list %batch (pair (pair (nat %amount) (option %from_ address))
                                                  (pair (option %to_ address) (nat %token_id))))
                               (address %fa2))
                             (address %operator)) ;
                  IF_NONE { FAIL } {} }
            """,
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
        self.assertTrue(res.context['admin']['paused'])

    def test_is_operator_callback(self):
        res = self.mac.is_operator(callback='KT1V4jijVy1HfVWde6HBVD1cCygZDtFJK4Xz',  # does not matter
                                   operator={
                                       'operator': pytezos.key.public_key_hash(),
                                       'owner': pytezos.key.public_key_hash(),
                                       'tokens': {'all_tokens': None}
                                   }) \
            .interpret(storage=initial_storage)
        self.assertEqual(1, len(res.operations))

    def test_transfer(self):
        initial_storage_balance = initial_storage.copy()
        initial_storage_balance['assets']['ledger'] = {
            (pytezos.key.public_key_hash(), 0): 42000
        }

        res = self.mac.transfer([
            dict(amount=1000,
                 from_=pytezos.key.public_key_hash(),
                 to_='tz1abavrqYNzpcDPiQURyCt1THti8J27W6mR',
                 token_id=0)]) \
            .interpret(storage=initial_storage_balance)
        self.assertDictEqual({
            (pytezos.key.public_key_hash(), 0): 41000,
            ('tz1abavrqYNzpcDPiQURyCt1THti8J27W6mR', 0): 1000
        }, res.big_map_diff['assets/ledger'])
