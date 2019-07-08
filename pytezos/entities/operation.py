from binascii import hexlify

from pytezos.crypto import Key, blake2b_32
from pytezos.encoding import base58_decode, base58_encode

"""

Block operations (list of lists)
|
|--- endorsements / validation pass #0
|
|--- votes / validation pass #1
|
|--- anonymous / validation pass #2
|
|--- managers / validation pass #3

Operation
|
|--- operation content #0
     |
     |--- internal operation #0.0
     |
     |--- <...>
|
|--- <...>

"""


class Contents:

    def __init__(self, content):
        self._content = content

    @classmethod
    def endorsement(cls, level: int):
        """
        Endorse a block
        :param level: Endorsed level
        :return: Operation content
        """
        return Contents({
            'kind': 'endorsement',
            'level': level
        })

    @classmethod
    def seed_nonce_revelation(cls, level: int, nonce):
        """
        Reveal the nonce committed in the previous cycle.
        More info https://tezos.stackexchange.com/questions/567/what-are-nonce-revelations
        :param level: When nonce hash was committed
        :param nonce: Hex string
        :return: Operation content
        """
        return Contents({
            'kind': 'seed_nonce_revelation',
            'level': level,
            'nonce': nonce
        })

    @classmethod
    def double_endorsement_evidence(cls, op1: dict, op2: dict):
        """
        Provide evidence of double endorsement (endorsing two different blocks at the same block height).
        :param op1: Inline endorsement {
            "branch": $block_hash,
            "operations": {
                "kind": "endorsement",
                "level": integer ∈ [-2^31-2, 2^31+2]
            },
            "signature"?: $Signature
        }
        :param op2: Inline endorsement
        :return: Operation content
        """
        return Contents({
            'kind': 'double_endorsement_evidence',
            'op1': op1,
            'op2': op2
        })

    @classmethod
    def double_baking_evidence(cls, bh1, bh2):
        """
        Provide evidence of double baking (two different blocks at the same height).
        :param bh1: First block hash
        :param bh2: Second block hash
        :return: Operation content
        """
        return Contents({
            'kind': 'double_baking_evidence',
            'bh1': bh1,
            'bh2': bh2
        })

    @classmethod
    def activate_account(cls, pkh, activation_code):
        """
        Activate recommended allocations for contributions to the TF fundraiser.
        More info https://activate.tezos.com/
        :param pkh: Public key hash
        :param activation_code: Secret code from pdf
        :return: Operation content
        """
        return Contents({
            'kind': 'activate_account',
            'pkh': pkh,
            'secret': activation_code
        })

    @classmethod
    def proposals(cls, proposals: list, source=None, period=None):
        """
        Submit and/or upvote proposals to amend the protocol.
        Can only be submitted during a proposal period.
        More info https://tezos.gitlab.io/master/whitedoc/voting.html
        :param proposals: List of proposal hashes
        :param source: Public key hash (of the signatory), leave none for autocomplete
        :param period: Number of the current voting period, leave none for autocomplete
        :return: Operation content
        """
        return Contents({
            'kind': 'proposals',
            'source': source,
            'period': period,
            'proposals': proposals
        })

    @classmethod
    def ballot(cls, proposal, ballot, source=None, period=None):
        """
        Vote for a proposal in a given voting period.
        Can only be submitted during Testing_vote or Promotion_vote periods, and only once per period.
        More info https://tezos.gitlab.io/master/whitedoc/voting.html
        :param proposal: Hash of the proposal
        :param ballot: 'Yay', 'Nay' or 'Pass'
        :param source: Public key hash (of the signatory), leave none for autocomplete
        :param period: Number of the current voting period, leave none for autocomplete
        :return:
        """
        return Contents({
            'kind': 'ballot',
            'source': source,
            'period': period,
            'proposal': proposal,
            'ballot': ballot
        })

    @classmethod
    def reveal(cls, public_key, source=None, counter=None, fee=None, gas_limit=None, storage_limit=None):
        """
        Reveal the public key associated with a tz address.
        :param public_key: Public key to reveal, Base58 encoded
        :param source:
        :param counter: Current contract counter, leave none for autocomplete
        (More info https://tezos.stackexchange.com/questions/632/how-counter-grows)
        :param fee: Leave none for autocomplete
        :param gas_limit: Leave none for autocomplete
        :param storage_limit: Leave none for autocomplete
        :return:
        """
        return Contents({
            'kind': 'reveal',
            'source': source,
            'fee': fee,
            'counter': counter,
            'gas_limit': gas_limit,
            'storage_limit': storage_limit,
            'public_key': public_key
        })

    @classmethod
    def transaction(cls, destination, amount: int, parameters=None,
                    source=None, counter=None, fee=None, gas_limit=None, storage_limit=None):
        """
        Transfer tezzies to an account (implicit or originated).
        If the receiver is an originated account (KT1…), then optional parameters may be passed.
        :param source:
        :param destination:
        :param amount:
        :param counter:
        :param parameters:
        :param fee:
        :param gas_limit:
        :param storage_limit:
        :return: Operation content
        """
        return Contents({
            'kind': 'transaction',
            'source': source,
            'fee': fee,
            'counter': counter,
            'gas_limit': gas_limit,
            'storage_limit': storage_limit,
            'amount': amount,
            'destination': destination,
            'parameters': parameters
        })

    @classmethod
    def origination(cls, script=None, source=None, counter=None, fee=None, gas_limit=None, storage_limit=None):
        """

        :param script:
        :param source:
        :param counter:
        :param fee:
        :param gas_limit:
        :param storage_limit:
        :return:
        """
        return Contents({
            'kind': 'transaction',
            'source': source,
            'fee': fee,
            'counter': counter,
            'gas_limit': gas_limit,
            'storage_limit': storage_limit,
            'manager_pubkey': source,  #
            'balance': 0,
            'script': script
        })

    @classmethod
    def delegation(cls, delegate, source=None, counter=None, fee=None, gas_limit=None, storage_limit=None):
        """

        :param delegate:
        :param source:
        :param counter:
        :param fee:
        :param gas_limit:
        :param storage_limit:
        :return:
        """
        return Contents({
            'kind': 'delegation',
            'source': source,
            'fee': fee,
            'counter': counter,
            'gas_limit': gas_limit,
            'storage_limit': storage_limit,
            'delegate': delegate
        })


    def __repr__(self):
        return str(self._op)

    def watermark(self):
        content = self.get('contents')[0]
        kind = content['kind']
        if kind in ['endorsement', 'seed_nonce_revelation']:
            return '02' + self.get_chain_watermark()
        if kind in ['transaction', 'origination', 'delegation', 'reveal', 'ballot', 'proposals', 'activate_account']:
            return '03'
        raise NotImplementedError(kind)

    def source(self):
        content = self.get('contents')[0]
        kind = content['kind']
        if kind in ['endorsement']:
            return content['metadata']['delegate']
        if kind == 'activate_account':
            return content['pkh']
        if kind in ['transaction', 'origination', 'delegation', 'reveal', 'ballot', 'proposals']:
            return content['source']
        raise NotImplementedError(f'Operation `{kind}` is anonymous.')

    def protocol(self):
        try:
            protocol = self.get('protocol')
        except KeyError:
            branch = self.get("branch")
            protocol = self._node.get(f'chains/main/blocks/{branch}/header').get('protocol')
        return protocol

    def unsigned_data(self) -> dict:
        operation = self()
        return {
            'branch': operation['branch'],
            'contents': [
                {k: v for k, v in c.items() if k != 'metadata'}
                for c in operation['contents']
            ]
        }

    def signed_data(self) -> dict:
        return {
            'protocol': self.protocol(),
            'signature': self.get('signature'),
            **self.unsigned_data()
        }

    def unsigned_bytes(self):
        return self.watermark() + self.forge()

    def signed_bytes(self):
        signature_bytes = hexlify(base58_decode(self.get('signature'))).decode()
        return self.forge() + signature_bytes

    def calculate_hash(self):
        hash_digest = blake2b_32(self.signed_bytes()).digest()
        return base58_encode(hash_digest, b'o').decode()

    def forge(self):
        return self._node.post(
            path='chains/main/blocks/head/helpers/forge/operations',
            json=self.unsigned_data(),
            cache=True
        )

    def sign(self, key):
        if isinstance(key, str):
            key = Key.from_key(key)
        if not isinstance(key, Key):
            raise ValueError('Base58 encoded secret key or Key instance required.')

        self._data['signature'] = key.sign(self.unsigned_bytes(), generic=True)
        return self._data['signature']

    def preapply(self, branch=None):
        operation = self.signed_data()
        if branch is None:
            branch = operation['branch']

        data = self._node.post(
            path=f'chains/main/blocks/{branch}/helpers/preapply/operations',
            json=[operation],
            cache=True
        )
        self._data['contents'] = data[0]['contents']
        return data

    def verify_signature(self):
        pk = self.get_public_key(self.source())
        Key.from_key(pk).verify(self.get('signature'), self.unsigned_bytes())

    def contents(self, kind=None):
        return filter_contents(self(), kind)
