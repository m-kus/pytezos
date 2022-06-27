from unittest import TestCase

from parameterized import parameterized

from pytezos import pytezos


class FailingNoopCase(TestCase):
    @parameterized.expand(
        [
            (
                'bootstrap1',
                'msg1',
                'BMFCHw1mv3A71KpTuGD3MoFnkHk9wvTYjUzuR9QqiUumKGFG6pM',
                'edsigu61KJzuwsQrPdWW7mj1RK1C9VjLn5cA1wDjmhGtxq4EPiTLpwztTj1H8iWR3VDFdAP2ggKdZbtnVW2K6KqTPVXAvEnGsG4',
            ),
        ]
    )
    def test_sign_verify_message(self, alias, message, block, expected):
        client = pytezos.using(key=alias)
        sig = client.sign_message(message, block=block)
        self.assertEqual(expected, sig)
        pytezos.check_message(message, public_key=client.key.public_key(), signature=expected, block=block)
