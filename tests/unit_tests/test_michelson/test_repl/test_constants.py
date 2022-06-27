from unittest import TestCase

from pytezos.contract.interface import ContractInterface, ExecutionContext

source = """
parameter (constant "exprvKFFbc7SnPjkPZgyhaHewQhmrouNjNae3DpsQ8KuADn9i2WuJ8") ;
storage (constant "expruu5BTdW7ajqJ9XPTF3kgcV78pRiaBW3Gq31mgp3WSYjjUBYxre") ;
code { DROP;
       PUSH int (constant "exprtrpoeDzM3su4bwEdzXewTxXjXbiCBu2bxtMKWk5k2eW2Rqod86");
       NIL operation ; PAIR }
"""


class GlobalConstantsTestCase(TestCase):

    def test_resolve_code(self):
        context = ExecutionContext()
        context.register_global_constant({'prim': 'int'})
        context.register_global_constant({'prim': 'unit'})
        context.register_global_constant({'int': '12345'})
        ci = ContractInterface.from_michelson(source, context)
        res = ci.call().interpret()
        self.assertEqual(12345, res.storage)
