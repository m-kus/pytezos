import json
import logging
from pytezos import pytezos

from pytezos.sandbox.node import SandboxedNodeTestCase
from pytezos.sandbox.parameters import FLORENCE



class TransactionCounterTestCase(SandboxedNodeTestCase):
    PROTOCOL = FLORENCE

    def test_endorsement(self):
        ed = pytezos.endorsement(1).fill().sign()
        ed_payload = ed.json_payload()

        eds = pytezos.endorsement_with_slot(
            endorsement={
                'branch': ed_payload['branch'],
                'operations': {
                    'kind': 'endorsement',
                    'level': int(ed_payload['contents'][0]['level'])
                },
                'signature': ed_payload['signature'],
            },
            slot=1,
        )
        eds = eds.fill().sign()
        eds.forge(True)
        eds.inject()