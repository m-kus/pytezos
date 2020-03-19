from os.path import dirname, join
from unittest import TestCase

from pytezos import pytezos, ContractInterface
from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.contract import micheline_to_michelson

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
        cls.i = Interpreter()
        cls.mac = ContractInterface.create_from(join(dirname(__file__), 'mac.tz'))
        cls.maxDiff = None

    def test_pause(self):
        res = self.mac.pause(True).result(
            storage=initial_storage,
            source=pytezos.key.public_key_hash())
        self.assertTrue(res.storage['admin']['paused'])

    def test_is_operator_callback(self):
        param = {
            'callback': 'KT1V4jijVy1HfVWde6HBVD1cCygZDtFJK4Xz',
            'operator': {
                'operator': pytezos.key.public_key_hash(),
                'owner': pytezos.key.public_key_hash(),
                'tokens': {'all_tokens': None}
            }
        }
        parameter = micheline_to_michelson(
            self.mac.contract.parameter.encode(param, entrypoint='is_operator')['value'])
        storage = micheline_to_michelson(
            self.mac.contract.storage.encode(initial_storage))

        self.i.execute(f'INCLUDE "{join(dirname(__file__), "mac.tz")}"')
        res = self.i.execute(f'RUN %is_operator ({parameter}) ({storage})')

        self.assertTrue(res['success'])
        self.assertIsNotNone(res['result'].get('operations'))
        self.assertEqual(1, len(res['result']['operations']))

        content = res['result']['operations'][0].content
        print(micheline_to_michelson(content['parameters']['value']))
