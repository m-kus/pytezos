from random import SystemRandom

from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.michelson.parse import michelson_to_micheline
from pytezos.michelson.types.base import MichelsonType
from pytezos.crypto.key import Key

rnd = SystemRandom()


def get_random_key():
    curve = rnd.choice([b'ed', b'sp', b'p2'])
    return Key.generate(export=False, curve=curve)


class MichelsonTestCase(SandboxedNodeTestCase):

    def test_map_order(self):
        self.bake_block()

        random_keys = [
            (i, get_random_key())
            for i in range(100)
        ]
        payload = {
            key.public_key(): i
            for i, key in random_keys
        }

        ty_expr = michelson_to_micheline('map key int')
        ty = MichelsonType.match(ty_expr)
        val_expr = ty.from_python_object(payload).to_micheline_value()

        self.client.shell.head.helpers.scripts.typecheck_data.post(dict(
            data=val_expr,
            type=ty_expr
        ))
