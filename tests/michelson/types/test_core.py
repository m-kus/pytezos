from unittest import TestCase

from pytezos.types import MichelsonType

parameter = {"prim":"parameter","args":[{"prim":"or","args":[{"prim":"or","args":[{"prim":"pair","args":[{"prim":"address","annots":["%participant"]},{"prim":"pair","args":[{"prim":"pair","args":[{"prim":"bytes","annots":["%hashed_secret"]},{"prim":"timestamp","annots":["%refund_time"]}]},{"prim":"mutez","annots":["%payoff"]}],"annots":["%settings"]}],"annots":[":initiate","%initiate"]},{"prim":"bytes","annots":[":hashed_secret","%add"]}],"annots":["%fund"]},{"prim":"or","args":[{"prim":"bytes","annots":[":secret","%redeem"]},{"prim":"bytes","annots":[":hashed_secret","%refund"]}],"annots":["%withdraw"]}]}]}
storage = {"prim":"storage","args":[{"prim":"pair","args":[{"prim":"big_map","args":[{"prim":"bytes"},{"prim":"pair","args":[{"prim":"pair","args":[{"prim":"address","annots":["%initiator"]},{"prim":"address","annots":["%participant"]}],"annots":["%recipients"]},{"prim":"pair","args":[{"prim":"pair","args":[{"prim":"mutez","annots":["%amount"]},{"prim":"timestamp","annots":["%refund_time"]}]},{"prim":"mutez","annots":["%payoff"]}],"annots":["%settings"]}]}]},{"prim":"unit"}]}]}


class TestMichelsonTypesCore(TestCase):

    def test_adt(self):
        param_type = MichelsonType.from_micheline_type(parameter)
        storage_type = MichelsonType.from_micheline_type(storage)
        self.assertTrue(True)
