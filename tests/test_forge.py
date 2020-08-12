from unittest import TestCase

from pytezos.operation.forge import forge_operation_group


class TestForging(TestCase):

    def test_regr_local_remote_diff(self):
        opg = {'branch': 'BKpLvH3E3bUa5Z2nb3RkH2p6EKLfymvxUAEgtRJnu4m9UX1TWUb',
               'contents': [{'amount': '0',
                             'counter': '446245',
                             'destination': 'KT1VYUxhLoSvouozCaDGL1XcswnagNfwr3yi',
                             'fee': '104274',
                             'gas_limit': '1040000',
                             'kind': 'transaction',
                             'parameters': {'entrypoint': 'default',
                                            'value': {'prim': 'Unit'}},
                             'source': 'tz1grSQDByRpnVs7sPtaprNZRp531ZKz6Jmm',
                             'storage_limit': '60000'}],
               'protocol': 'PsCARTHAGazKbHtnKfLzQg3kms52kSRpgnDY982a9oYsSXRLQEb',
               'signature': None}
        local = forge_operation_group(opg).hex()
        remote = "0dc397b7865779d87bd47d406e8b4eee84498f22ab01dff124433c7f057af5ae6c00e8b36c80efb51ec85a1456" \
                 "2426049aa182a3ce38d2ae06a59e1b80bd3fe0d4030001e5ebf2dcc7dcc9d13c2c45cd76823dd604740c7f0000"

        self.assertEqual(remote, local)
