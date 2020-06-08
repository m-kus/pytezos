from unittest import TestCase

from pytezos import ContractInterface
from pytezos.michelson.contract import ContractStorage
from pytezos.michelson.converter import michelson_to_micheline

code = """
parameter (or
            (pair %set_data (key_hash %delegate)
                            (pair
                              (option %data (pair
                                             (pair
                                               (pair (bytes %bakerName)
                                                     (bool %openForDelegation))
                                               (bytes %bakerOffchainRegistryUrl))
                                             (pair
                                               (pair (nat %split)
                                                     (list %bakerPaysFromAccounts address))
                                               (pair
                                                 (pair
                                                   (pair (nat %minDelegation)
                                                         (bool %subtractPayoutsLessThanMin))
                                                   (pair (int %payoutDelay)
                                                         (pair (nat %payoutFrequency)
                                                               (int %minPayout))))
                                                 (pair
                                                   (pair
                                                     (bool %bakerChargesTransactionFee)
                                                     (nat %paymentConfigMask))
                                                   (pair (nat %overDelegationThreshold)
                                                         (bool %subtractRewardsFromUninvitedDelegation)))))))
                              (option %reporterAccount address)))
            (or (pair %set_fees (mutez %signup_fee) (mutez %update_fee))
                (contract %withdraw unit)));
storage (pair
          (big_map key_hash
                   (pair
                     (pair
                       (option %data (pair
                                      (pair
                                        (pair (bytes %bakerName)
                                              (bool %openForDelegation))
                                        (bytes %bakerOffchainRegistryUrl))
                                      (pair
                                        (pair (nat %split)
                                              (list %bakerPaysFromAccounts address))
                                        (pair
                                          (pair
                                            (pair (nat %minDelegation)
                                                  (bool %subtractPayoutsLessThanMin))
                                            (pair (int %payoutDelay)
                                                  (pair (nat %payoutFrequency)
                                                        (int %minPayout))))
                                          (pair
                                            (pair (bool %bakerChargesTransactionFee)
                                                  (nat %paymentConfigMask))
                                            (pair (nat %overDelegationThreshold)
                                                  (bool %subtractRewardsFromUninvitedDelegation)))))))
                       (option %reporterAccount address))
                     (timestamp %last_update)))
          (pair (address %owner) (pair (mutez %signup_fee) (mutez %update_fee))));
code { { { DUP ; CAR ; DIP { CDR } } } ;
       IF_LEFT
         { DUP ;
           CDR ;
           CAR ;
           { IF_NONE
               {}
               { CAR ;
                 DUP ;
                 CAR ;
                 CAR ;
                 SIZE ;
                 PUSH nat 61 ;
                 { { COMPARE ; GT } ; IF {} { { UNIT ; FAILWITH } } } ;
                 CDR ;
                 SIZE ;
                 PUSH nat 81 ;
                 { { COMPARE ; GT } ; IF {} { { UNIT ; FAILWITH } } } } } ;
           { { DUP ; CAR ; DIP { CDR } } } ;
           { DIP 2 { DUP } ; DIG 3 } ;
           CAR ;
           { DIP { DUP } ; SWAP } ;
           GET @from_storage ;
           IF_NONE
             { DUP ;
               IMPLICIT_ACCOUNT ;
               ADDRESS ;
               SENDER ;
               { { COMPARE ; EQ } ; IF {} { { UNIT ; FAILWITH } } } ;
               { DIP 2 { DUP } ; DIG 3 } ;
               { CDR ; CDR ; CAR %signup_fee } ;
               AMOUNT ;
               { { COMPARE ; EQ } ; IF {} { { UNIT ; FAILWITH } } } }
             { { CAR ; CDR %reporterAccount } ;
               IF_NONE { PUSH bool False } { SENDER ; COMPARE ; EQ } ;
               DIP { DUP ; IMPLICIT_ACCOUNT ; ADDRESS ; SENDER ; COMPARE ; EQ } ;
               OR ;
               { IF {} { { UNIT ; FAILWITH } } } ;
               { DIP 2 { DUP } ; DIG 3 } ;
               { CDR ; CDR ; CDR %update_fee } ;
               AMOUNT ;
               { { COMPARE ; EQ } ; IF {} { { UNIT ; FAILWITH } } } } ;
           DIP { NOW ; SWAP ; PAIR ; SOME ; DIP { { { DUP ; CAR ; DIP { CDR } } } } } ;
           UPDATE ;
           PAIR ;
           NIL operation ;
           PAIR }
         { { DIP { DUP } ; SWAP } ;
           { CDR ; CAR %owner } ;
           SENDER ;
           { { COMPARE ; EQ } ; IF {} { { UNIT ; FAILWITH } } } ;
           AMOUNT ;
           PUSH mutez 0 ;
           { { COMPARE ; EQ } ; IF {} { { UNIT ; FAILWITH } } } ;
           IF_LEFT
             { SWAP ;
               { DUP ; DIP { CDR @%% ; { CAR @%% ; PAIR %@ % } } ; CAR @%% ; PAIR %@ %@ } ;
               NIL operation ;
               PAIR }
             { BALANCE ; UNIT ; TRANSFER_TOKENS ; NIL operation ; SWAP ; CONS ; PAIR } } }
"""
storage = "Pair 17 (Pair 0x0000176e8f231f39c20a1cbd1ce3cee7806abf52914e (Pair 1500000 500000))"

key_pair_storage = """
storage (pair (nat %total) 
              (map %chapters (pair string nat) 
                             (big_map %balances (address nat) 
                                                nat)))
"""


class TestBmdQuery(TestCase):

    def test_bmd_path(self):
        ci = ContractInterface.create_from(code)
        ci.contract.storage.big_map_init(michelson_to_micheline(storage))
        query = ci.contract.storage.big_map_query('big_map_0/tz1bHzftcTKZMTZgLLtnrXydCm6UEqf4ivca')
        self.assertEqual(
            {'big_map_id': 17, 'script_expr': 'expruGu4fvT7wyJYm2Rdz7jssqBZyoSmi3kub6Us3guARnzR9HBQCe'}, query)

    def test_bmd_decode_bin_path_0(self):
        cs = ContractStorage(michelson_to_micheline("storage (big_map address nat)"))
        cs.big_map_init({'int': 42})
        res = cs.big_map_diff_decode([{
            'action': 'update',
            'big_map': '42',
            'key': {'string': 'tz1irF8HUsQp2dLhKNMhteG1qALNU9g3pfdN'},
            'value': {'int': '100500'}
        }])
        self.assertDictEqual({'tz1irF8HUsQp2dLhKNMhteG1qALNU9g3pfdN': 100500}, res)

    def test_bmd_nested_tuples(self):
        cs = ContractStorage(michelson_to_micheline(key_pair_storage))
        cs.big_map_init(michelson_to_micheline("""
            Pair 100 { Elt (Pair "main" 0) 42 }
        """))