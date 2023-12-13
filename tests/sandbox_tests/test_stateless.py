from random import SystemRandom

from pytezos import ContractInterface
from pytezos.crypto.key import Key
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.types.base import MichelsonType
from pytezos.sandbox.node import SandboxedNodeTestCase

rnd = SystemRandom()


def get_random_key():
    curve = rnd.choice([b'ed', b'sp', b'p2'])
    return Key.generate(export=False, curve=curve)


class TestStateless(SandboxedNodeTestCase):
    def test_now(self):
        code = """
        parameter unit;
        storage timestamp;
        code { DROP ;
               NOW ;
               NIL operation ;
               PAIR }
        """
        contract = ContractInterface.from_michelson(code).using(shell=self.client.shell)
        now = self.client.now()
        res = contract.default().run_code()
        self.assertEqual(now, res.storage)

    def test_lazy_storage_diff(self):
        code = """
        { parameter string ;
          storage (big_map string nat) ;
          code { UNPAIR ;
                 SWAP ;
                 PUSH nat 1 ;
                 SOME ;
                 DIG 2 ;
                 UPDATE ;
                 NIL operation ;
                 PAIR } }
        """
        contract = ContractInterface.from_michelson(code).using(shell=self.client.shell)
        res = contract.default('hello').run_code()
        self.assertEqual({'hello': 1}, res.storage)
        self.assertEqual(1, len(res.lazy_diff))
        res1 = contract.default('hello').interpret()
        self.assertEqual({'hello': 1}, res1.storage)

    def test_map_order(self):
        self.bake_block()

        random_keys = [(i, get_random_key()) for i in range(100)]
        payload = {key.public_key(): i for i, key in random_keys}

        ty_expr = michelson_to_micheline('map key int')
        ty = MichelsonType.match(ty_expr)
        val_expr = ty.from_python_object(payload).to_micheline_value()

        self.client.shell.head.helpers.scripts.typecheck_data.post(
            {
                'data': val_expr,
                'type': ty_expr,
            }
        )
