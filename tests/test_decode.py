from unittest import TestCase
from parameterized import parameterized

from pytezos.michelson.converter import michelson_to_micheline
from pytezos.michelson.contract import ContractStorage, ContractParameter
from pytezos.michelson.grammar import MichelsonParser
from pytezos.repl.parser import parse_expression

storage_data = [(
    """Pair (Pair "tz1YPSCGWXwBdTncK2aCctSZAXWvGsGwVJqU" True) 
            (Pair (Pair None { Elt (Pair "tz1YPSCGWXwBdTncK2aCctSZAXWvGsGwVJqU" 0) 0 }) 
                  (Pair {} {}))""",
    """
    storage (pair (pair %admin (address %admin) (bool %paused))
          (pair %assets
             (pair (option %hook
                      (pair (lambda %hook
                               unit
                               (contract
                                  (pair (pair (list %batch
                                                 (pair (pair (nat %amount) (option %from_ address))
                                                       (pair (option %to_ address) (nat %token_id))))
                                              (address %fa2))
                                        (address %operator))))
                            (pair %permissions_descriptor
                               (pair (pair (option %custom (pair (option %config_api address) (string %tag)))
                                           (or %operator
                                              (unit %operator_transfer_denied)
                                              (unit %operator_transfer_permitted)))
                                     (pair (or %receiver
                                              (or (unit %optional_owner_hook) (unit %owner_no_op))
                                              (unit %required_owner_hook))
                                           (or %self (unit %self_transfer_denied) (unit %self_transfer_permitted))))
                               (or %sender
                                  (or (unit %optional_owner_hook) (unit %owner_no_op))
                                  (unit %required_owner_hook)))))
                   (big_map %ledger (pair address nat) nat))
             (pair (big_map %operators
                      (pair address address)
                      (or (or (unit %all_operator_tokens) (set %all_operator_tokens_except nat))
                          (set %some_operator_tokens nat)))
                   (big_map %tokens
                      nat
                      (pair (pair %metadata
                               (pair (pair (nat %decimals) (map %extras string string))
                                     (pair (string %name) (string %symbol)))
                               (nat %token_id))
                            (nat %total_supply))))))
    """
)]


parameter_data = [(
    """
    Right (Left (Right (Left (Pair "Proposal 003 - Blend Fee Structure"
                            { Elt "url1"
                                   (Pair
                                     0x82ef44771f292a7e3e763730d9561a6f87d5cc0ab509123d8b6bd9705318c3c4
                                     "https://forum.stakerdao.com/uploads/short-url/22zZKdcC7SfoyCwGibMTvFCOuW9.pdf") }))))
    """,
    """
    or
  (or
    (or (pair %voteForProposal (nat :proposalId) (pair (key :votePk) (signature :voteSig)))
        (pair %getBalance (address :owner) (contract nat)))
    (or (pair %getTotalSupply unit (contract nat)) (bytes %fund)))
  (or
    (or
      (or (set %newCouncil key_hash)
          (pair %transfer (address :from) (pair (address :to) (nat :value))))
      (or (pair %newProposal (string :description) (map :newPolicy string (pair bytes string)))
          (unit %freeze)))
    (or (pair %withdraw (address :to) (mutez :amount))
        (lambda :successor %setSuccessor
          (or
            (or (pair (nat :proposalId) (pair (key :votePk) (signature :voteSig)))
                (pair (address :owner) (contract nat)))
            (or (pair unit (contract nat)) bytes))
          operation)))
    """
)]


class TestComparable(TestCase):

    @parameterized.expand(storage_data)
    def test_storage_decode(self, val_expr, type_expr):
        storage = ContractStorage(michelson_to_micheline(type_expr))
        source = michelson_to_micheline(val_expr)
        decoded = storage.decode(source)
        encoded = storage.encode(decoded)
        self.assertEqual(source, encoded)

    @parameterized.expand(parameter_data)
    def test_parameter_decode(self, val_expr, type_expr):
        parameter = ContractParameter(michelson_to_micheline(type_expr))
        source = michelson_to_micheline(val_expr)
        decoded = parameter.decode(source)
        encoded = parameter.encode(decoded, entrypoint='default')
        self.assertEqual(source, encoded['value'])

    def test_wrapped_expr(self):
        p = MichelsonParser()
        p.parse('(Pair 1 2)')

    def test_unpair_single_annot(self):
        p = MichelsonParser()
        p.parse('UNPAIR @left')

    def test_root_option(self):
        storage = ContractStorage(michelson_to_micheline("storage (option string)"))
        self.assertEqual({"prim": "None"}, storage.encode(None))
        self.assertEqual({"prim": "Some", "args": [{"string": ""}]}, storage.encode(""))

    def test_timestamp_with_millis(self):
        res = parse_expression({'string': '2021-01-06T14:57:27.821Z'}, {'prim': 'timestamp'})
        self.assertEqual(1609945047, res)
